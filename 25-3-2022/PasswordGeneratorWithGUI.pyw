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
curlang = IntVar()
curlang.set(0)

def openkey():
    savedkeypage = Toplevel(master)
    savedkeypage.config(bg='#bdbdbd')
    if curlang.get() == 0:
        savedkeypage.title("Decryption Key")
        keyl = Label(savedkeypage, text = "Decryption Key:", bg='#bdbdbd').grid(row = 0, column = 0)
    elif curlang.get() == 1:
        savedkeypage.title("Ключ Расшифровки")
        keyl = Label(savedkeypage, text = "Ключ Расшифровки:", bg='#bdbdbd').grid(row = 0, column = 0)
    elif curlang.get() == 2:
        savedkeypage.title("Κλειδί Αποκρυπτογράφησης")
        keyl = Label(savedkeypage, text = "Κλειδί Αποκρυπτογράφησης:", bg='#bdbdbd').grid(row = 0, column = 0)
    keyl2 = Text(savedkeypage, height = 5, width = 45, font=("Courier", 10, "bold"), bg='lightgrey')
    keyl2.grid(row = 1)
    savedkeypage.resizable(width=False, height=False)
    if os.path.isfile("deckey.txt"):
        skey = open("deckey.txt", "r").read()
        if curlang.get() == 0:
            keyl2.insert(INSERT, "Key: " + str(skey))
            keyl2.insert(END, "\n\n\nTHE KEY IS NEEDED FOR DECRYPTION!")
        elif curlang.get() == 1:
            keyl2.insert(INSERT, "Ключ: " + str(skey))
            keyl2.insert(END, "\n\n\nКЛЮЧ НУЖЕН ДЛЯ РАСШИФРОВКИ!")
        elif curlang.get() == 2:
            keyl2.insert(INSERT, "Κλειδί: " + str(skey))
            keyl2.insert(END, "\n\n\nΤΟ ΚΛΕΙΔΙ ΕΙΝΑΙ ΓΙΑ ΤΗΝ ΑΠΟΚΡΥΠΤΟΓΡΑΦΗΣΗ!")
    else:
        if curlang.get() == 0:
            keyl2.insert(INSERT, "deckey.txt not found!")
        elif curlang.get() == 1:
            keyl2.insert(INSERT, "deckey.txt Не Найден!")
        elif curlang.get() == 2:
            keyl2.insert(INSERT, "deckey.txt Δεν βρέθηκε!")
def openpasses():
    savedpassespage = Toplevel(master)
    savedpassespage.config(bg='#bdbdbd')
    savedpassespage.resizable(width=False, height=False)
    if curlang.get() == 0:
        savedpassespage.title("Saved Passwords")
        passesl = Label(savedpassespage, text = "Saved Passwords:", bg='#bdbdbd').grid(row = 0, column = 0)
    elif curlang.get() == 1:
        savedpassespage.title("Сохраненные Пароли")
        passesl = Label(savedpassespage, text = "Сохраненные Пароли:", bg='#bdbdbd').grid(row = 0, column = 0)
    elif curlang.get() == 2:
        savedpassespage.title("Αποθηκευμένοι Κωδικοί")
        passesl = Label(savedpassespage, text = "Αποθηκευμένοι Κωδικοί:", bg='#bdbdbd').grid(row = 0, column = 0)
    passesl2 = Text(savedpassespage, height = 25, width = 55, font=("Courier", 10, "bold"), bg='lightgrey')
    passesl2.grid(row = 1)
    if os.path.isfile("Encrypted Password Storage.txt"):
        file = open("Encrypted Password Storage.txt", "r")
        todecnextline = 0
        for line in file:
            if line == "Encrypted Password:\n":
                todecnextline = 1
                if curlang.get() == 0:
                    passesl2.insert(INSERT, "Password: ")
                elif curlang.get() == 1:
                    passesl2.insert(INSERT, "Пароль: ")
                elif curlang.get() == 2:
                    passesl2.insert(INSERT, "Κωδικός: ")
            elif "Name:" in line:
                if curlang.get() == 0:
                    passesl2.insert(INSERT, line)
                elif curlang.get() == 1:
                    passesl2.insert(INSERT, line.replace('Name:', 'Название Пароля:'))
                elif curlang.get() == 2:
                    passesl2.insert(INSERT, line.replace('Name:', 'Όνομα Κωδικού:'))
            else:
                if todecnextline == 1:
                    l = decrypt2(str(line), 0)
                    todecnextline = 0
                    passesl2.insert(INSERT, str(l) + '\n')
                else:
                    passesl2.insert(INSERT, str(line))
    else:
        if curlang.get() == 0:
            passesl2.insert(INSERT, "Encrypted Password Storage.txt not found!\nYou may not have created a password yet!")
        elif curlang.get() == 1:
            passesl2.insert(INSERT, "Encrypted Password Storage.txt Не найден!\nВозможно, вы еще не сохраняли пароли!")
        elif curlang.get() == 2:
            passesl2.insert(INSERT, "Encrypted Password Storage.txt Δεν βρέθηκε!\nΊσως να μην έχετε αποθηκεύσει κωδικούς ακόμη!")
        
def openimp():
    impage = Toplevel(master)
    impage.config(bg='#bdbdbd')
    impage.resizable(width = False, height = False)
    
    if curlang.get() == 0:
        impage.title("Important Note")
        l10 = Label (impage, text = "IMPORTANT!!!!", font=("Courier", 18, "bold"), bg='#bdbdbd').grid(row = 0)
        l10 = Label (impage, text = "\nAfter launching the program there will be generated a key-file \nthats used to decrypt the passwords from the encrypted password storage!!!\nBackup these two files to decrypt the passwords in the future!!!\nFile names:\ndeckey.txt\n&\nEncrypted Password Storage.txt\n\nThe key-file is automatically used by the program\nafter the program is launched from the same folder!", font=("Courier", 12, "bold"), bg='#bdbdbd').grid(row = 1)
    elif curlang.get() == 1:
        impage.title("Важная Записка")
        l10 = Label (impage, text = "ВАЖНО!!!!", font=("Courier", 18, "bold"), bg='#bdbdbd').grid(row = 0)
        l10 = Label (impage, text = "\nПосле запуска программы в папке появится файл-ключ\nкоторый нужен для расшифровки паролей из сохранненых паролей!!!\nСохраните эти два файла чтобы расшифровать пароли в будущем!!!\nНазвания Файлов:\ndeckey.txt\n&\nEncrypted Password Storage.txt\n\nФайл-ключ будет автоматически использован\nиз папки из которой была запущена программа!", font=("Courier", 12, "bold"), bg='#bdbdbd').grid(row = 1)
    elif curlang.get() == 2:
        impage.title("Σημαντική Παρατήρηση")
        l10 = Label (impage, text = "ΣΗΜΑΝΤΙΚΟ!!!!", font=("Courier", 18, "bold"), bg='#bdbdbd').grid(row = 0)
        l10 = Label (impage, text = "\nΜετά την εκτέλεση του προγράμματος θα δημιουργηθεί αρχείο-κλειδί\nτο οποίο είναι απαραίτητο για την αποκρυπτογράφηση των κωδικών!!!\nΑποθηκεύστε σε ασφαλή μέρος τα παρακάτω αρχεία για την αποκρυπτογράφηση στο μέλλον!!!\nΟνόματα Αρχείων:\ndeckey.txt\n&\nEncrypted Password Storage.txt\n\nΤο αρχείο-κλειδί χρησιμοποιείται αυτόματα απο το πρόγραμμα\nόταν το πρόγραμμα εκτελείται από τον ίδιο φάκελο με το κλειδί!", font=("Courier", 12, "bold"), bg='#bdbdbd').grid(row = 1)
    
def openab():
    abpage = Toplevel(master)
    abpage.geometry("520x150")
    abpage.config(bg='#bdbdbd')
    abpage.resizable(width = False, height = False)
    if curlang.get() == 0:
        abpage.title("About us")
        l11 = Label(abpage, text="Made by inf2021221 & inf2021198 & inf2021119 for a \npython project at IONIO University of Informatics\n2021-2022", font=("Courier", 13, "italic"), bg='#bdbdbd').grid(row = 0)
    elif curlang.get() == 1:
        abpage.title("О нас")
        abpage.geometry("760x150")
        l11 = Label(abpage, text="Эта программа создана совместно с inf2021221 & inf2021198 & inf2021119 ради \nпроекта по программированию в Ионическом Университете Информатики\n2021-2022", font=("Courier", 13, "italic"), bg='#bdbdbd').grid(row = 0)
    elif curlang.get() == 2:
        abpage.title("Ποιοί Είμαστε")
        abpage.geometry("800x150")
        l11 = Label(abpage, text="Προγραμματισμένο ομαδικά από τους inf2021221 & inf2021198 & inf2021119 για μια \nεργασία προγραμματισμού στο τμήμα πληροφορηκής του Ιονίου Πανεπιστημίου\n2021-2022", font=("Courier", 13, "italic"), bg='#bdbdbd').grid(row = 0)
about = Menu(menu, tearoff = 0)
lang = Menu(menu, tearoff = 0)
aboutuscaslabel = StringVar()
langlabel = StringVar()
keylabel = StringVar()
savedpasslabel = StringVar()
aboutuslabel = StringVar()
importantlabel = StringVar()
viewsavedlabel = StringVar()
viewkeylabel = StringVar()
def setenglish():
    curlang.set(0)
    master.title("Password Generator")
    master.geometry("500x280")
    yourpasswordislabel.set("Your Password is: ")
    passwordnamelabel.set('Password Name')
    passwordlengthlabel.set('Length')
    decryptbutton.set("Decrypt")
    generatebutton.set("[Generate]")
    clearbuttonlabel.set("Clear")
    copybutton.set("Copy")
    savebutton.set("Save")
    symbolscheck.set("Symbols")
    numberscheck.set("Numbers")
    uppercheck.set("UpperCase Letters")
    lowercheck.set("LowerCase Letters")
    encryptedpasslabel.set("Encrypted: ")
    decryptedpasslabel.set("Decrypted: ")
    yourencpasswordlabel.set("Your Password in encrypted format:")
    aboutuscaslabel.set("About us")
    langlabel.set("Language")
    keylabel.set("Key")
    savedpasslabel.set("Saved Passwords")
    aboutuslabel.set("About us")
    importantlabel.set("Important Note")
    viewsavedlabel.set("View Saved Passwords")
    viewkeylabel.set("View Key")
def setrussian():
    curlang.set(1)
    master.title("Генератор Паролей")
    master.geometry("550x280")
    yourpasswordislabel.set("Пароль: ")
    passwordnamelabel.set('Название Пароля')
    passwordlengthlabel.set('Размер Пароля')
    clearbuttonlabel.set("Очистить")
    decryptbutton.set("Расшифровать")
    generatebutton.set("[Сгенерировать]")
    about.entryconfigure(0, label = "Важная Записка")
    about.entryconfigure(1, label = "О нас")
    savedkey.entryconfigure(0, label = "Просмотр Ключа")
    savedpasses.entryconfigure(0, label = "Просмотр Сохраненных Паролей")
    copybutton.set("Скопировать")
    savebutton.set("Сохранить")
    symbolscheck.set("Символы")
    numberscheck.set("Цифры")
    uppercheck.set("Большие Буквы")
    lowercheck.set("Маленькие Буквы")
    encryptedpasslabel.set("Зашифрованно: ")
    decryptedpasslabel.set("Расшифрованно: ")
    yourencpasswordlabel.set("Пароль в зашифрованном виде:")
    aboutuscaslabel.set("О нас")
    langlabel.set("Язык")
    keylabel.set("Ключ")
    savedpasslabel.set("Сохранненые Пароли")
    aboutuslabel.set("О нас")
    importantlabel.set("Важная Записка")
    viewsavedlabel.set("Посмотреть Сохранненые Пароли")
    viewkeylabel.set("Посмотреть Ключ")
def setgreek():
    curlang.set(2)
    master.title("Γεννήτρια Κωδικών Πρόσβασης")
    master.geometry("570x280")
    yourpasswordislabel.set("Κωδικός Πρόσβασης: ")
    passwordnamelabel.set('Όνομα Κωδικού')
    passwordlengthlabel.set('Μέγεθος')
    decryptbutton.set("Αποκρυπτογράφηση")
    generatebutton.set("[Δημιουργία]")
    copybutton.set("Αντιγραφή")
    savebutton.set("Αποθήκευση")
    clearbuttonlabel.set("Καθαρισμός")
    symbolscheck.set("Σύμβολα")
    numberscheck.set("Αριθμοί")
    uppercheck.set("Κεφαλαία Γράμματα")
    lowercheck.set("Μικρά Γράμματα")
    about.entryconfigure(0, label = "Σημαντική Παρατήρηση")
    about.entryconfigure(1, label = "Ποιοί είμαστε")
    savedkey.entryconfigure(0, label = "Κλειδί")
    savedpasses.entryconfigure(0, label = "Αποθηκεύμενοι Κωδικοί")
    encryptedpasslabel.set("Κρυπτογραφημένος: ")
    decryptedpasslabel.set("Αποκρυπτογραφημένος: ")
    yourencpasswordlabel.set("Κρυπτογραφημένος Κωδικός:")
    aboutuscaslabel.set("Ποιοί Είμαστε")
    langlabel.set("Γλώσσα")
    keylabel.set("Κλειδί")
    savedpasslabel.set("Αποθηκευμένοι Κωδικοί")
    aboutuslabel.set("Ποιοί Είμαστε")
    importantlabel.set("Σημαντική Παρατήρηση")
    viewsavedlabel.set("Άνοιγμα Αποθηκευμένων Κωδικών")
    viewkeylabel.set("Άνοιγμα Κλειδιού")
aboutuscaslabel.set("About us")
langlabel.set("Language")
keylabel.set("Key")
savedpasslabel.set("Saved Passwords")
aboutuslabel.set("About us")
importantlabel.set("Important Note")
viewsavedlabel.set("View Saved Passwords")
viewkeylabel.set("View Key")
menu.add_cascade(label = aboutuscaslabel.get(), menu = about)
menu.add_cascade(label = langlabel.get(), menu = lang)
lang.add_command(label = 'English', command = setenglish)
lang.add_command(label = 'Русский', command = setrussian)
lang.add_command(label = 'Ελληνικά', command = setgreek)
savedkey = Menu(menu, tearoff = 0)
menu.add_cascade(label = keylabel.get(), menu = savedkey)
savedkey.add_command(label = viewkeylabel.get(), command = openkey)
savedpasses = Menu(menu, tearoff = 0)
menu.add_cascade(label = savedpasslabel.get(), menu = savedpasses)
savedpasses.add_command(label=viewsavedlabel.get(), command = openpasses)
about.add_command(label=importantlabel.get(), command = openimp)
about.add_command(label=aboutuslabel.get(), command = openab)
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
yourpasswordislabel = StringVar()
yourpasswordislabel.set("Your Password is: ")
l2 = Label(master, textvariable = yourpasswordislabel, bg='#bdbdbd').grid(row = 4, column = 0, stick = W)
passstrength = IntVar()
l00 = Label(master, textvariable = passstrength, bg= '#bdbdbd').grid(row = 4, column = 4, stick = W)
yourencpasswordlabel = StringVar()
yourencpasswordlabel.set("Your Password in encrypted format:")
l3 = Label(master, textvariable = yourencpasswordlabel, anchor = 'w', bg='#bdbdbd').grid(row = 5, column = 0, ipadx = 1, stick = W)
blank = Label(master, text = " ", anchor=W, bg='#bdbdbd').grid(row = 3, column = 2, ipadx = 1, stick = W)
decryptedpasslabel = StringVar()
decryptedpasslabel.set("Decrypted: ")
l5 = Label(master, textvariable = decryptedpasslabel, bg='#bdbdbd').grid(row = 9, column = 0, ipadx = 1, stick = W)
encryptedpasslabel = StringVar()
encryptedpasslabel.set("Encrypted: ")
l10 = Label(master, textvariable = encryptedpasslabel, bg='#bdbdbd').grid(row = 6, column = 0, ipadx = 1, stick = W)
e3 = Entry(master, width = 20, borderwidth = 2, bg='lightgrey') #Encrypted Password Entry
e3.grid(row = 6, column = 1, stick = W)
e4 = Entry(master, width = 20, borderwidth = 2, bg='lightgrey') #Your Password is Entry
e4.grid(row= 4, column = 1, stick = W)
e5 = Entry(master, width = 20, borderwidth = 2, bg='lightgrey') #Decrypted Password Entry
e5.grid(row= 9, column = 1, stick = W)
e6 = Entry(master, width = 20, borderwidth = 2, bg='lightgrey') #Password in encrypted format entry
e6.grid(row= 5, column = 1, stick = W)
def ratepass(passtorate):
    rating = 0
    for a in passtorate:
        if passtorate.count(a) == 1:
            if len(passtorate) > 40:
                rating += 10
            elif len(passtorate) > 10:
                rating += 7
            else:
                rating += 5
        elif passtorate.count(a) == 2:
            if len(passtorate) > 40:
                rating += 7
            elif len(passtorate) > 10:
                rating += 5
            else:
                rating += 4
        elif passtorate.count(a) == 3:
            if len(passtorate) > 100:
                rating += 10
            elif len(passtorate) > 50:
                rating += 5
            else:
                rating += 3
        else:
            rating += 1 + len(passtorate)/5
    if 'i' in passtorate:
        if 'I' in passtorate:
            if '1' in passtorate:
                if 'l' in passtorate:
                    rating -= (passtorate.count('i') + passtorate.count('I') + passtorate.count('1') + passtorate.count('l'))
                else:
                    rating -= (passtorate.count('i') + passtorate.count('I') + passtorate.count('1'))
            elif 'l' in passtorate:
                rating -= (passtorate.count('i') + passtorate.count('I') + passtorate.count('l'))
            else:
                rating -= (passtorate.count('i') + passtorate.count('I'))
        elif '1' in passtorate:
            if 'l' in passtorate:
                rating -= (passtorate.count('i') + passtorate.count('1') + passtorate.count('l'))
            else:
                rating -= (passtorate.count('i') + passtorate.count('1'))*2
        elif 'l' in passtorate:
            rating -= (passtorate.count('i')+ passtorate.count('l'))*2
    elif 'I' in passtorate:
        if '1' in passtorate:
            if 'l' in passtorate:
                rating -= (passtorate.count('I') + passtorate.count('1') + passtorate.count('l'))
            else:
                rating -= (passtorate.count('I') + passtorate.count('1'))
        elif 'l' in passtorate:
            rating -= (passtorate.count('I') + passtorate.count('l'))
    elif '1' in passtorate:
        if 'l' in passtorate:
            rating -= (passtorate.count('1') + passtorate.count('l'))
    if 'o' in passtorate:
        if 'O' in passtorate:
            if '0' in passtorate:
                rating -= (passtorate.count('o') + passtorate.count('0') + passtorate.count('O'))
            else:
                rating -= (passtorate.count('o') + passtorate.count('O'))
        elif '0' in passtorate:
            rating -= (passtorate.count('o') + passtorate.count('0'))
    elif 'O' in passtorate:
        if '0' in passtorate:
            rating -= (passtorate.count('O') + passtorate.count('0'))
    if 's' in passtorate:
        if 'S' in passtorate:
            rating -= (passtorate.count('s') + passtorate.count('S'))
    if 'v' in passtorate:
        if 'V' in passtorate:
            rating -= (passtorate.count('v') + passtorate.count('V'))
    if 't' in passtorate:
        if 'T' in passtorate:
            rating -= (passtorate.count('t') + passtorate.count('T'))
    if 'x' in passtorate:
        if 'X' in passtorate:
            rating -= (passtorate.count('x') + passtorate.count('X'))
    if 'j' in passtorate:
        if 'i' in passtorate:
            rating -= (passtorate.count('j') + passtorate.count('i'))
    if 'w' in passtorate:
        if 'W' in passtorate:
            rating -= (passtorate.count('w') + passtorate.count('W'))
    if 'y' in passtorate:
        if 'Y' in passtorate:
            rating -= (passtorate.count('Y') + passtorate.count('y'))
    if 'O' in passtorate:
        if 'Q' in passtorate:
            rating -= (passtorate.count('Q') + passtorate.count('O'))
    rating += len(passtorate)
    if len(passtorate) == 1 or len(passtorate) == 2 or len(passtorate) == 3:
        rating = len(passtorate) * len(passtorate)
    return rating
def generate(o, symbsbase):
    password = []
    w = ""
    l = ""
    b = 0
    for i in range (0, o):
        a = random.randint(0, len(symbsbase)-1)
        password.append(symbsbase[a])
    for i in range (0, len(password)):
        l += password[i]
    e4.insert(1, l)
    ratingvar = ratepass(str(l))
    passstrength.set(ratingvar)
    encpass2 = fernet.encrypt(l.encode())
    encpass2 = str(encpass2)
    l = ""
    o = 0
    for b in encpass2:
        if o != 0 and o != 1 and o != (len(encpass2)-1):
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
    if len(passtosave) != 0:
        file = open("Encrypted Password Storage.txt", "a")
        file.write("\nName: " + passname + "\nEncrypted Password:\n" + str(passtosave))
        file.write("\n")
        file.close()

def decrypt2(todec, mode):

    todec = bytes(todec, 'utf-8')
    decr = fernet.decrypt(todec)
    decr = str(decr)
    l = ""
    o = 0
    for b in decr:
        if o != 0 and o != 1 and o != (len(decr)-1):
            l += b
        o += 1
    if mode == 1:
        e5.delete("0","end")
        e5.insert(0, str(l))
    else:
        return str(l)

def copy2 (passtocopy):
    clip.copy(str(passtocopy))

def copy4 (passtocopy):
    clip.copy(str(passtocopy))

def copy6 (passtocopy):
    clip.copy(str(passtocopy))


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
    if b != 0 and e2.get() != "0":
        e4.delete("0", "end")
        e6.delete("0", "end")
        gen(var1.get(), var2.get(), var3.get(), var4.get())
    if b == 0 and e2.get() == "0":
        selerror3 = Toplevel(master)
        selerror3.config(bg='#bdbdbd')
        if curlang.get() == 0:
            selerror3.title("Selection And Length Error")
            labelwarning = Label(selerror3, text = "Select at least one thing to include in your password and set a proper length!", font=("Courier", 14, "bold"), bg='#bdbdbd').grid(row = 0, column = 0)
        elif curlang.get() == 1:
            selerror3.title("Недопустимый Размер и Выбранные Символы")
            labelwarning = Label(selerror3, text = "Выберите хотя бы что-нибудь из символов и назначьте размер пароля больше 0!", font=("Courier", 14, "bold"), bg='#bdbdbd').grid(row = 0, column = 0)
        elif curlang.get() == 2:
            selerror3.title("Λάθος μέγεθος και επιλόγη συμβόλων")
            labelwarning = Label(selerror3, text = "Επιλεξτε τουλάχιστον μια από τις επιλογές συμβόλων και καθορίστε μέγεθος μεγαλύτερο του μηδενός!", font=("Courier", 14, "bold"), bg='#bdbdbd').grid(row = 0, column = 0)
    else:
        if b == 0:
            if curlang.get() == 0:
                selerror1 = Toplevel(master)
                selerror1.config(bg='#bdbdbd')
                selerror1.title("Selection Error")
                labelwarning = Label(selerror1, text = "Select at least one thing to include in your password!", font=("Courier", 14, "bold"), bg='#bdbdbd').grid(row = 0, column = 0)
            elif curlang.get() == 1:
                selerror1 = Toplevel(master)
                selerror1.config(bg='#bdbdbd')
                selerror1.title("Недопустимое Количество Выбранных Символов")
                labelwarning = Label(selerror1, text = "Выберите хотя бы один из символов для пароля!", font=("Courier", 14, "bold"), bg='#bdbdbd').grid(row = 0, column = 0)
            elif curlang.get() == 2:
                selerror1 = Toplevel(master)
                selerror1.config(bg='#bdbdbd')
                selerror1.title("Μη επαρκής αριθμός επιλογών συμβόλων")
                labelwarning = Label(selerror1, text = "Επιλέξτε τουλάχιστον ένα από τα σύμβολα για τον κωδικό σας!", font=("Courier", 14, "bold"), bg='#bdbdbd').grid(row = 0, column = 0)
        elif e2.get() == "0":
            if curlang.get() == 0:
                selerror2 = Toplevel(master)
                selerror2.config(bg='#bdbdbd')
                selerror2.title("Length Error")
                labelwarning = Label(selerror2, text = "Length cant be 0!", font=("Courier", 14, "bold"), bg='#bdbdbd').grid(row = 0, column = 0)
            elif curlang.get() == 1:
                selerror2 = Toplevel(master)
                selerror2.config(bg='#bdbdbd')
                selerror2.title("Недопустимый Размер Пароля")
                labelwarning = Label(selerror2, text = "Размер пароля не может быть 0!", font=("Courier", 14, "bold"), bg='#bdbdbd').grid(row = 0, column = 0)
            elif curlang.get() == 2:
                selerror2 = Toplevel(master)
                selerror2.config(bg='#bdbdbd')
                selerror2.title("Σφάλμα Μεγέθους")
                labelwarning = Label(selerror2, text = "Το μέγεθος δεν μπορεί να είναι 0!", font=("Courier", 14, "bold"), bg='#bdbdbd').grid(row = 0, column = 0)
def clearencpass ():
    e3.delete("0", "end")
passwordnamelabel = StringVar()
passwordnamelabel.set('Password Name')
Label(master, textvariable = passwordnamelabel, bg='#bdbdbd').grid(row=0, ipadx = 1, stick = W)
passwordlengthlabel = StringVar()
passwordlengthlabel.set('Length')
Label(master, textvariable = passwordlengthlabel, bg='#bdbdbd').grid(row=1, ipadx = 1, stick = W)
e1 = Entry(master, bg='lightgrey') #Entry for the password name
e1.insert(0, "Test")
e2 = Entry(master, bg='lightgrey') #Entry for the password length
e2.insert(0, "8")
e1.grid(row=0, column = 1, ipadx = 1, stick = W) #Setting the locations of the entries
e2.grid(row=1, column = 1, ipadx = 1, stick = W) #>>
savebutton = StringVar() #Text variable for the names of the buttons to switch between languages >>
savebutton.set("Save") #Setting to english by default >>>
copybutton = StringVar() #>>
copybutton.set("Copy") #>>>
generatebutton = StringVar() #>>
generatebutton.set("[Generate]") #>>>
decryptbutton = StringVar() #>>
decryptbutton.set("Decrypt") #>>>
clearbuttonlabel = StringVar()
clearbuttonlabel.set("Clear")
clearbutton = Button (master, textvariable = clearbuttonlabel, command = clearencpass, bg='white', borderwidth = 5).grid(row = 6, column = 4, ipadx = 1, stick = W)
b2 = Button(master , textvariable = savebutton, command = lambda: savetofile(str(e1.get()), str(encpass.get())), bg='white', borderwidth = 5).grid(row = 5, column = 3, ipadx = 1, stick = W)
b5 = Button(master , textvariable = copybutton, command = lambda: copy6(str(encpass.get())), bg='white', borderwidth = 5).grid(row = 5, column = 4, ipadx = 1, stick = W)
b3 = Button(master, textvariable = decryptbutton, command = lambda: decrypt2(e3.get(), 1), bg='white', borderwidth = 5).grid(row = 6, column = 3, ipadx = 1, stick = W)
b4 = Button(master, textvariable = copybutton, command = lambda: copy2(str(e5.get())), bg='white', borderwidth = 5).grid(row = 9, column = 3, ipadx = 1, stick = W)
b6 = Button(master, textvariable = copybutton, command = lambda: copy4(str(e4.get())), bg='white', borderwidth = 5).grid(row = 4, column = 3, ipadx = 1, stick = W)
b1 = Button(master, textvariable = generatebutton, command = dothis, bg='white', borderwidth = 5).grid(row=1, column=3, ipadx = 1, stick = W)
var1 = IntVar() #Symbols CheckBox Variable
var2 = IntVar() #Numbers CheckBox Variable
var3 = IntVar() #UpperCase Letters CheckBox Variable
var4 = IntVar() #LowerCase Letters CheckBox Variable
var1.set(1) #Setting all the checkboxes to checked by default >>
var2.set(1) #>>
var3.set(1) #>>
var4.set(1) #>>
symbolscheck = StringVar() #Text Variable for the checkboxes names for switching between languages >>
numberscheck = StringVar() #>>
uppercheck = StringVar() #>>
lowercheck = StringVar() #>>
symbolscheck.set("Symbols") #Setting the text to english version by default >>
numberscheck.set("Numbers") #>>
uppercheck.set("UpperCase Letters") #>>
lowercheck.set("LowerCase Letters") #>>
Checkbutton(master, textvariable =symbolscheck, variable=var1, anchor = 'w', bg='#bdbdbd').grid(row=3, column = 1, ipadx = 1, stick = W)
Checkbutton(master, textvariable=numberscheck, variable=var2, anchor = 'w', bg='#bdbdbd').grid(row=3, column = 0, ipadx = 1, stick = W)
Checkbutton(master, textvariable=uppercheck, variable=var3, anchor = 'w', bg='#bdbdbd').grid(row=2, column = 0, ipadx = 1, stick = W)
Checkbutton(master, textvariable=lowercheck, variable=var4, anchor = 'w', bg='#bdbdbd').grid(row=2, column = 1, ipadx = 1, stick = W)
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

Last edit made at 25/3/2022 21:09
"""
