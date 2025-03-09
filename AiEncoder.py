# Developed in Python 3.8 but is compatable with later versions
# Encode your text to send for your weekly 5 points

# Simply write your 5 points out, copy and paste it into the text field and press the 'Encode Text' button.
# Then just copy the newly encoded text and use that to send to OPM/OSD or to whoever. 
# DON'T FORGET TO ENCRPYT AND NOT ALLOW FORWARDING AS WELL IN THE EMAIL.

#The best type of compliance is malicious compliance
import random
import tkinter as tk
import pyperclip

random_Invisible_Unicode = ['​','؜'] #zero width
random_Invisible_Cap_Alphabet = ['󠁁','󠁂','󠁃','󠁄','󠁆','󠁇','󠁈','󠁉','󠁊','󠁋','󠁌','󠁌','󠁍','󠁍','󠁏','󠁐','󠁑','󠁒','󠁓','󠁔','󠁕','󠁖','󠁗','󠁘','󠁙','󠁚']
random_Invisible_smol_Alphabet = ['󠁡','󠁢','󠁣','󠁤','󠁥','󠁦','󠁧','󠁨','󠁩','󠁪','󠁫','󠁬','󠁭','󠁮','󠁯','󠁰','󠁱','󠁲','󠁳','󠁴','󠁵','󠁶','󠁷','󠁸','󠁹','󠁺']
visible_Cap_Character_Dict = [['A','Α'],
                          ['B','В'],
                          ['C','С'],
                          ['D','Đ'],
                          ['E', 'Ε'],
                          ['F',],
                          ['G',],
                          ['H',],
                          ['I',''],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [],
                          []
                          ]
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
output = tk.Text(root, state='normal')
entry = tk.Entry(root, width=50)
# entry.grid(row=0, column=1)

def grabRandomFromList(id_number):
    if(id(random_Invisible_Unicode) == id_number):
        return random_Invisible_Unicode[random.randint(1,100) % len(random_Invisible_Unicode)]
    if(id(random_Invisible_Cap_Alphabet) == id_number):
        return random_Invisible_Cap_Alphabet[random.randint(1,100) % len(random_Invisible_Cap_Alphabet)]
    if(id(random_Invisible_smol_Alphabet) == id_number):
        return random_Invisible_smol_Alphabet[random.randint(1,100) % len(random_Invisible_smol_Alphabet)]
    return "ERROR"

def encodeOutput():
    entrystring = entry.get()
    textField.config(state='normal')
    textField.delete('1.0',tk.END)
    output.delete('1.0',tk.END)
    # entry.delete(0, tk.END)
    encodedOutput = ''
    for character in entrystring:
        for i in range(random.randint(min_Insert_Value_Between_Characters,max_Insert_Value_Between_Characters)):
            # if random.randint(1,100) % current_List_Count == 
            # encodedOutput += random_Invisible_Unicode[random.randint(1,100) % len(random_Invisible_Unicode)]
            encodedOutput += grabRandomFromList(current_List_List[random.randint(1,100) % len(current_List_List)])
        if character == 'A':
            encodedOutput +='Α'
        elif character == 'B':
            encodedOutput +='В'
        elif character == 'C':
            encodedOutput +='С'
        elif character == 'D':
            encodedOutput +='Đ'
        elif character == 'E':
            encodedOutput +='Ε'
        elif character == 'F':
            encodedOutput +='Ḟ'
        elif character == 'G':
            encodedOutput +='G' #normal latin character
        elif character == 'H':
            encodedOutput +='Η'
        elif character == 'I':
            encodedOutput +='Ι'
        elif character == 'J':
            encodedOutput +='Ј'
        elif character == 'K':
            encodedOutput +='Κ'
        elif character == 'L':
            encodedOutput +='L' #normal latin character
        elif character == 'M':
            encodedOutput +='Μ'
        elif character == 'N':
            encodedOutput +='Ν'
        elif character == 'O':
            encodedOutput +='Ο'
        elif character == 'P':
            encodedOutput +='Ρ'
        elif character == 'Q':
            encodedOutput +='Q' #normal latin character
        elif character == 'R':
            encodedOutput +='Ɍ'
        elif character == 'S':
            encodedOutput +='Ѕ'
        elif character == 'T':
            encodedOutput +='Τ'
        elif character == 'U':
            encodedOutput +='Ų'
        elif character == 'V':
            encodedOutput +='Ѵ'
        elif character == 'W':
            encodedOutput +='Ш'
        elif character == 'X':
            encodedOutput +='Χ'
        elif character == 'Y':
            encodedOutput +='Υ'
        elif character == 'Z':
            encodedOutput +='Ζ'
        elif character == 'a':
            encodedOutput +='ɑ'
        elif character == 'b':
            encodedOutput +='ƅ'
        elif character == 'c':
            encodedOutput +='с'
        elif character == 'd':
            encodedOutput +='ď'
        elif character == 'e':
            encodedOutput +='е'
        elif character == 'f':
            encodedOutput +='f' #normal latin character
        elif character == 'g':
            encodedOutput +='ɡ'
        elif character == 'h':
            encodedOutput +='һ'
        elif character == 'i':
            encodedOutput +='ί'
        elif character == 'j':
            encodedOutput +='ϳ'
        elif character == 'k':
            encodedOutput +='ҟ'
        elif character == 'l':
            encodedOutput +='ḷ'
        elif character == 'm':
            encodedOutput +='ՠ'
        elif character == 'n':
            encodedOutput +='п'
        elif character == 'o':
            encodedOutput +='ο'
        elif character == 'p':
            encodedOutput +='р'
        elif character == 'q':
            encodedOutput +='ɋ'
        elif character == 'r':
            encodedOutput +='r' #normal latin character
        elif character == 's':
            encodedOutput +='ѕ'
        elif character == 't':
            encodedOutput +='t' #normal latin character
        elif character == 'u':
            encodedOutput +='џ'
        elif character == 'v':
            encodedOutput +='ν'
        elif character == 'w':
            encodedOutput +='ɯ'
        elif character == 'x':
            encodedOutput +='х'
        elif character == 'y':
            encodedOutput +='у'
        elif character == 'z':
            encodedOutput +='ẓ'
        else:
            encodedOutput += character
        # encodedOutput += character
    # entry.insert(0, encodedOutput)
    textField.insert('1.0',encodedOutput)
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