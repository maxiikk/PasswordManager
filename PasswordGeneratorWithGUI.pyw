from tkinter import *
import os.path
from cryptography.fernet import Fernet
import random
master = Tk()
master.title("Password Generator")
lol = StringVar()
decpass = StringVar()
key = Fernet.generate_key()
fernet = Fernet(key)
encpass = StringVar()
l2 = Label(master, text = "Your Password is: ").grid(row = 4, column = 0)
l3 = Label(master, text = "Your password in encrypted format: ").grid(row = 5, column = 0)
l5 = Label(master, text = "Decrypted: ").grid(row = 7, column = 0)
l6 = Label(master, textvariable = decpass).grid(row = 7, column = 1)
l4 = Label(master, textvariable = encpass).grid(row = 5, column = 1)
e3 = Entry(master)
e3.grid(row = 6, column = 0)
l1 = Label(master, textvariable = lol).grid(row= 4, column = 1)
def generate(o, symbsbase):
    password = []
    w = ""
    b = 0
    for i in range (0, o):
        a = random.randint(0, len(symbsbase)-1)
        password.append(symbsbase[a])
    for i in range (0, len(password)):
        w += password[i]
        b += 1
        if b%100 == 0:
            w += "\n"
    lol.set(w)
    encpass2 = fernet.encrypt(w.encode())
    encpass2 = str(encpass2)
    l = ""
    o = 0
    for b in encpass2:
        if o != 0 and o != 1 and o != (len(encpass2)-1):
            if o != 0 and o%100 == 0:
                l += "\n"
            l += b
        o += 1
    encpass2 = l
    encpass.set(encpass2)
    

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
    file = open("Ecnrypted Password Storage.txt", "a")
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
            if o != 0 and o%100 == 0:
                l += "\n"
            l += b
        o += 1
    decpass.set(str(l))

def decrypt1():
    decrypt2(e3.get())

def dothisbitch():
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
        gen(var1.get(), var2.get(), var3.get(), var4.get())
    
Label(master, text='Password Name').grid(row=0)
Label(master, text='Length').grid(row=1)
e1 = Entry(master)
def savetofile1 ():
    savetofile(str(e1.get()), str(encpass.get()))
e2 = Entry(master)
e1.grid(row=0, column = 1)
e2.grid(row=1, column = 1)
b2 = Button(master , text = 'Save', command = savetofile1).grid(row = 5, column = 2)
b3 = Button(master, text = 'Decrypt', command = decrypt1).grid(row = 6, column = 2)
b1 = Button(master, text ='Enter', command = dothisbitch).grid(row=1, column=2)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
Checkbutton(master, text='Symbols', variable=var1).grid(row=2)
Checkbutton(master, text='Numbers', variable=var2).grid(row=2, column = 1)
Checkbutton(master, text='UpperCase Letters', variable=var3).grid(row=2, column = 2)
Checkbutton(master, text='LowerCase Letters', variable=var4).grid(row=2, column = 3)
mainloop()


"""
--------------------------------------------------
Borrowed Code from: 

None

--------------------------------------------------

In development by inf2021221 & inf2021198 for our university project at IONIO 
University of Informatics

Link to the Github project:
    https://github.com/maxiikk/PasswordGenerator

Last edit made at 8/3/2022 23:48
"""
