from tkinter import *
import os.path
import pyperclip as clip
from tkinter import ttk 
from cryptography.fernet import Fernet
import random
master = Tk()
master.title("Password Generator")
master.geometry("500x280")
menu = Menu(master)
master.config(menu = menu, bg='#bdbdbd')
master.resizable(width=False, height=False)
def openkey():
    savedkeypage = Toplevel(master)
    savedkeypage.title("Decryption Key")
    keyl = Label(savedkeypage, text = "Decryption Key:").grid(row = 0, column = 0)
    keyl2 = Text(savedkeypage, height = 5, width = 45, font=("Courier", 10, "bold"))
    keyl2.grid(row = 1)
    savedkeypage.resizable(width=False, height=False)
    if os.path.isfile("deckey.txt"):
        skey = open("deckey.txt", "r").read()
        keyl2.insert(INSERT, "Key: " + str(skey))
        keyl2.insert(END, "\n\n\nTHE KEY IS NEEDED FOR DECRYPTION!")
    else:
        keyl2.insert(INSERT, "deckey.txt not found!")
def openpasses():
    savedpassespage = Toplevel(master)
    savedpassespage.title("Saved Passwords")
    passesl = Label(savedpassespage, text = "Saved Passwords:").grid(row = 0, column = 0)
    passesl2 = Text(savedpassespage, height = 25, width = 55, font=("Courier", 10, "bold"))
    passesl2.grid(row = 1)
    savedpassespage.resizable(width=False, height=False)
    if os.path.isfile("Encrypted Password Storage.txt"):
        passes = open("Encrypted Password Storage.txt", "r").read()
        passesl2.insert(INSERT, "=======================================================\n||Copy a password and decrypt it in the main window. ||\n=======================================================")
        passesl2.insert(INSERT, str(passes))
    else:
        passesl2.insert(INSERT, "Encrypted Password Storage.txt not found!\nYou may not have created a password yet!")
def openimp():
    impage = Toplevel(master)
    impage.title("Important Note")
    l10 = Label (impage, text = "IMPORTANT!!!!", font=("Courier", 18, "bold")).grid(row = 0)
    l10 = Label (impage, text = "\nAfter launching the program there will be generated a key-file \nthats used to decrypt the passwords from the encrypted password storage!!!\nBackup these two files to decrypt the passwords in the future!!!\nFile names:\ndeckey.txt\n&\nEncrypted Password Storage.txt\n\nThe key-file is automatically used by the program\nafter the program is launched from the same folder!", font=("Courier", 12, "bold")).grid(row = 1)
def openab():
    abpage = Toplevel(master)
    abpage.title("About us")
    l11 = Label(abpage, text="Made by inf2021221 & inf2021198 & inf2021119 for a \npython project at IONIO University of Informatics\n2021-2022", font=("Courier", 13, "italic")).grid(row = 0)
about = Menu(menu)
menu.add_cascade(label = 'About us', menu = about)
savedkey = Menu(menu)
menu.add_cascade(label = 'Key', menu = savedkey)
savedkey.add_command(label = 'View Key', command = openkey)
savedpasses = Menu(menu)
menu.add_cascade(label = 'Saved Passwords', menu = savedpasses)
savedpasses.add_command(label='View Saved Passwords', command = openpasses)
about.add_command(label='Important Note', command = openimp)
about.add_command(label='About us', command = openab)
decpass = StringVar()
if os.path.isfile("deckey.txt"):
    key = open("deckey.txt", "rb").read()
else:
    key = Fernet.generate_key()
    key2 = str(key)
    l = ""
    o = 0
    for b in key2:
        if o != 0 and o != 1 and o != (len(key2)-1):
            l += b
        o += 1
    savepass = open("deckey.txt", "a")
    savepass.write(str(l))
    savepass.close()
fernet = Fernet(key)
encpass = StringVar()
l2 = Label(master, text = "Your Password is: ", bg='#bdbdbd').grid(row = 4, column = 0, stick = W)
l3 = Label(master, text = "Your password in encrypted format: ", anchor = 'w', bg='#bdbdbd').grid(row = 5, column = 0, ipadx = 1, stick = W)
blank = Label(master, text = " ", anchor=W, bg='#bdbdbd').grid(row = 3, column = 2, ipadx = 1, stick = W)
l5 = Label(master, text = "Decrypted: ", bg='#bdbdbd').grid(row = 9, column = 0, ipadx = 1, stick = W)
l10 = Label(master, text = "Encrypted: ", bg='#bdbdbd').grid(row = 6, column = 0, ipadx = 1, stick = W)
e3 = Entry(master, width = 20, borderwidth = 2, bg='lightgrey')
e3.grid(row = 6, column = 1, stick = W)
e4 = Entry(master, width = 20, borderwidth = 2, bg='lightgrey')
e4.grid(row= 4, column = 1, stick = W)
e5 = Entry(master, width = 20, borderwidth = 2, bg='lightgrey')
e5.grid(row= 9, column = 1, stick = W)
e6 = Entry(master, width = 20, borderwidth = 2, bg='lightgrey')
e6.grid(row= 5, column = 1, stick = W)
def generate(o, symbsbase):
    password = []
    w = ""
    l = ""
    b = 0
    for i in range (0, o):
        a = random.randint(0, len(symbsbase)-1)
        password.append(symbsbase[a])
    for i in range (0, len(password)):
        w += password[i]
        l += password[i]
        b += 1
        if b%50 == 0:
            w += "\n"
    e4.insert(1, l)
    encpass2 = fernet.encrypt(l.encode())
    encpass2 = str(encpass2)
    l = ""
    o = 0
    for b in encpass2:
        if o != 0 and o != 1 and o != (len(encpass2)-1):
            if o != 0 and o%50 == 0:
                l += "\n"
            l += b
        o += 1
    encpass2 = l
    encpass.set(encpass2)
    e6.insert(1, encpass2)
    encpass2 = ""
    

def gen(s, n, u, l):
    symbs = []
    sym = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', '=', '?']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbslower = ['a', 'b' , 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    symbsupper = ['A', 'B' , 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if s == 1:
        for i in range (0, len(sym)):
            symbs.append(sym[i])
    if n == 1:
        for i in range (0, len(nums)):
            symbs.append(nums[i])
    if u == 1:
        for i in range(0, len(symbsupper)):
            symbs.append(symbsupper[i])
    if l == 1:
        for i in range (0, len(symbslower)):
            symbs.append(symbslower[i])
    generate(int(e2.get()), symbs)

def savetofile(passname, passtosave):
    file = open("Encrypted Password Storage.txt", "a")
    l = ""
    for b in passtosave:
        if b != '\n':
            l += b
    file.write("\nName: " + passname + "\nEncrypted Password: " + str(l))
    file.write("\n")
    file.close()

def decrypt2(todec):

    todec = bytes(todec, 'utf-8')
    decr = fernet.decrypt(todec)
    decr = str(decr)
    l = ""
    o = 0
    for b in decr:
        if o != 0 and o != 1 and o != (len(decr)-1):
            if o != 0 and o%50 == 0:
                l += "\n"
            l += b
        o += 1
    e5.delete("0","end")
    e5.insert(0, str(l))

def decrypt1():
    decrypt2(e3.get())

def copy2 (passtocopy):
    clip.copy(str(passtocopy))

def copy1 ():
    copy2(str(e5.get()))

def copy4 (passtocopy):
    clip.copy(str(passtocopy))

def copy3 ():
    copy4(str(e4.get()))

def copy6 (passtocopy):
    clip.copy(str(passtocopy))

def copy5 ():
    l = ""
    p = str(encpass.get())
    for b in p:
        if b != '\n':
            l += b
    copy6(l)


def dothis():
    b = 0
    if var1.get() == 1:
        b += 1
    if var2.get() == 1:
        b += 1
    if var3.get() == 1:
        b += 1
    if var4.get() == 1:
        b += 1
    if b != 0:
        e4.delete("0", "end")
        e6.delete("0", "end")
        gen(var1.get(), var2.get(), var3.get(), var4.get())
    
Label(master, text='Password Name', bg='#bdbdbd').grid(row=0, ipadx = 1, stick = W)
Label(master, text='Length', bg='#bdbdbd').grid(row=1, ipadx = 1, stick = W)
e1 = Entry(master, bg='lightgrey')
e1.insert(0, "Test")
def savetofile1 ():
    savetofile(str(e1.get()), str(encpass.get()))
e2 = Entry(master, bg='lightgrey')
e2.insert(0, "8")
e1.grid(row=0, column = 1, ipadx = 1, stick = W)
e2.grid(row=1, column = 1, ipadx = 1, stick = W)
b2 = Button(master , text = 'Save', command = savetofile1, bg='white', borderwidth = 5).grid(row = 5, column = 3, ipadx = 1, stick = W)
b5 = Button(master , text = 'Copy', command = copy5, bg='white', borderwidth = 5).grid(row = 5, column = 4, ipadx = 1, stick = W)
b3 = Button(master, text = 'Decrypt', command = decrypt1, bg='white', borderwidth = 5).grid(row = 6, column = 3, ipadx = 1, stick = W)
b4 = Button(master, text = 'Copy', command = copy1, bg='white', borderwidth = 5).grid(row = 9, column = 3, ipadx = 1, stick = W)
b6 = Button(master, text = 'Copy', command = copy3, bg='white', borderwidth = 5).grid(row = 4, column = 3, ipadx = 1, stick = W)
b1 = Button(master, text ='[Generate]', command = dothis, bg='white', borderwidth = 5).grid(row=1, column=3, ipadx = 1, stick = W)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var1.set(1)
var2.set(1)
var3.set(1)
var4.set(1)
Checkbutton(master, text='Symbols', variable=var1, anchor = 'w', bg='#bdbdbd').grid(row=3, column = 1, ipadx = 1, stick = W)
Checkbutton(master, text='Numbers', variable=var2, anchor = 'w', bg='#bdbdbd').grid(row=3, column = 0, ipadx = 1, stick = W)
Checkbutton(master, text='UpperCase Letters', variable=var3, anchor = 'w', bg='#bdbdbd').grid(row=2, column = 0, ipadx = 1, stick = W)
Checkbutton(master, text='LowerCase Letters', variable=var4, anchor = 'w', bg='#bdbdbd').grid(row=2, column = 1, ipadx = 1, stick = W)
mainloop()
"""
--------------------------------------------------
Borrowed Code from: 

None

--------------------------------------------------

In development by inf2021221 & inf2021198 & inf2021119 for our university project at IONIO 
University of Informatics

Link to the Github project:
    https://github.com/maxiikk/PasswordGenerator

Last edit made at 22/3/2022 23:18
"""
