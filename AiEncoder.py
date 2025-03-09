# Developed in Python 3.8 but is compatable with later versions
# Encode your text to send for your weekly 5 points

# Simply write your 5 points out, copy and paste it into the text field and press the 'Encode Text' button.
# Then just copy the newly encoded text and use that to send to OPM/OSD or to whoever. 
# DON'T FORGET TO ENCRPYT AND NOT ALLOW FORWARDING AS WELL IN THE EMAIL.

#The best type of compliance is malicious compliance
import random
import tkinter as tk
import pyperclip

#Randomly selected stuff
random_Invisible_Unicode = ['​','؜'] #zero width
random_Invisible_Cap_Alphabet = ['󠁁','󠁂','󠁃','󠁄','󠁆','󠁇','󠁈','󠁉','󠁊','󠁋','󠁌','󠁌','󠁍','󠁍','󠁏','󠁐','󠁑','󠁒','󠁓','󠁔','󠁕','󠁖','󠁗','󠁘','󠁙','󠁚']
random_Invisible_smol_Alphabet = ['󠁡','󠁢','󠁣','󠁤','󠁥','󠁦','󠁧','󠁨','󠁩','󠁪','󠁫','󠁬','󠁭','󠁮','󠁯','󠁰','󠁱','󠁲','󠁳','󠁴','󠁵','󠁶','󠁷','󠁸','󠁹','󠁺']

#visible to user
visible_Cap_Character_Dict = {'A': 'Α',
                              'B': 'В',
                              'C': 'С',
                              'D': 'Đ',
                              'E': 'Ε',
                              'F': 'Ḟ',
                              'G': 'G', #normal latin character
                              'H': 'Η',
                              'I': 'Ι',
                              'J': 'Ј',
                              'K': 'Κ',
                              'L': 'L', #normal latin character
                              'M': 'Μ',
                              'N': 'Ν',
                              'O': 'Ο',
                              'P': 'Ρ',
                              'Q': 'Q', #normal latin character
                              'R': 'Ɍ',
                              'S': 'Ѕ',
                              'T': 'Τ',
                              'U': 'Ų',
                              'V': 'Ѵ',
                              'W': 'Ш',
                              'X': 'Χ',
                              'Y': 'Υ',
                              'Z': 'Ζ'}
visible_smol_Character_Dict = {'a':'ɑ',
                               'b':'ƅ',
                               'c':'с',
                               'd':'ď',
                               'e':'е',
                               'f':'f', #normal latin character
                               'g':'ɡ', 
                               'h':'һ',
                               'i':'ί',
                               'j':'ϳ',
                               'k':'ҟ',
                               'l':'ḷ', 
                               'm':'ՠ',
                               'n':'п',
                               'o':'ο',
                               'p':'р',
                               'q':'ɋ', 
                               'r':'r', #normal latin character
                               's':'ѕ',
                               't':'t', #normal latin character
                               'u':'џ',
                               'v':'ν',
                               'w':'ɯ',
                               'x':'х',
                               'y':'у',
                               'z':'ẓ',
                               }

# how many of the random invisible characters added between each visible character. 
# The higher the number the more characters it takes up.
min_Insert_Value_Between_Characters = 2
max_Insert_Value_Between_Characters = 10
current_List_List = [id(random_Invisible_Cap_Alphabet),
                     id(random_Invisible_smol_Alphabet),
                     id(random_Invisible_Unicode)]

#create tkinter stuff
root = tk.Tk()
root.geometry('650x480')
root.title("Encode Your Text")


label= tk.Label(root, text="Paste text here: ")
# label.grid(row=0,column=0)


textField = tk.Text(root, state='disabled')
# textField.grid(row=1, columnspan=3)
# output is held in memory for copying to clipboard. This text isn't displayed
output = tk.Text(root, state='normal')

entry = tk.Entry(root, width=50)
# entry.grid(row=0, column=1)

def grabRandomFromList(id_number):
    """
    Returns:
        random unicode character based on whatever list
    """
    if(id(random_Invisible_Unicode) == id_number):
        return random_Invisible_Unicode[random.randint(1,100) % len(random_Invisible_Unicode)]
    if(id(random_Invisible_Cap_Alphabet) == id_number):
        return random_Invisible_Cap_Alphabet[random.randint(1,100) % len(random_Invisible_Cap_Alphabet)]
    if(id(random_Invisible_smol_Alphabet) == id_number):
        return random_Invisible_smol_Alphabet[random.randint(1,100) % len(random_Invisible_smol_Alphabet)]
    return "ERROR"

def encodeOutput():
    """
    Grabs what user typed in textField and encodes it.
    
    Returns:
        sets value of textfield and copies encodedOutput to pastebin with pyperclip
    """
    entrystring = entry.get()
    textField.config(state='normal')
    textField.delete('1.0',tk.END)
    output.delete('1.0',tk.END)
    # entry.delete(0, tk.END)
    encodedOutput = '‭'
    for character in entrystring:
        for i in range(random.randint(min_Insert_Value_Between_Characters,max_Insert_Value_Between_Characters)):
            encodedOutput += grabRandomFromList(current_List_List[random.randint(1,100) % len(current_List_List)])
        if character in visible_Cap_Character_Dict.keys():
            encodedOutput += visible_Cap_Character_Dict[character]
        elif character in visible_smol_Character_Dict.keys():
            encodedOutput += visible_smol_Character_Dict[character]
        else:
            encodedOutput += character
    
    textField.insert('1.0',"Encoded text below may look like there are no spaces but there are.\n")
    textField.insert(tk.END,encodedOutput)
    textField.insert(tk.END,"\n\nCOPIED TO CLIPBOARD")
    textField.config(state='disabled')

    output.insert('1.0',encodedOutput)
    copy_text()

encodeButton = tk.Button(root, text="Encode Text", command=encodeOutput)
# button.grid(row=0, column=2)

def copy_text():
    pyperclip.copy(output.get('1.0', tk.END))
copyButton = tk.Button(root,text="COPY TO CLIPBOARD", command=copy_text)

label.pack()
entry.pack()
encodeButton.pack()
textField.pack()
copyButton.pack()

root.mainloop()