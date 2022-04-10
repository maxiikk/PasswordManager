from Encryptor import AES_Encryption
from tkinter import *
import os.path
import pyperclip as clip
from tkinter import ttk
import random
import struct

master = Tk()
master.title("Password Generator")
master.geometry("580x270")
menu = Menu(master)
master.config(menu = menu, bg='#bdbdbd')
master.resizable(width=False, height=False)
curlang = IntVar()
curlang.set(0)
mypassword = StringVar()
passwordentered = IntVar()
setpassopen = IntVar() #to check if a setpassword() window is already open
passwarningopen = IntVar()
cipher = StringVar()
def setpasswarning():
    passerror = Toplevel(master)
    passerrorlabel = StringVar()
    passerror.config(bg='#bdbdbd')
    passerror.geometry("300x100")
    passwarningopen.set(1)
    def warnclose():
        passwarningopen.set(0)
        passerror.destroy()
    passerror.protocol("WM_DELETE_WINDOW", warnclose)
    passerror.resizable(width=False, height=False)
    if curlang.get() == 0:
        passerrorlabel.set("Set a password first!")
        passerror.title("Password Error")
    elif curlang.get() == 1:
        passerrorlabel.set("Сперва назначьте пароль!")
        passerror.title("Ошибка пароля")
    elif curlang.get() == 2:
        passerrorlabel.set("Βάλτε κωδικό πρώτα!")
        passerror.title("Σφάλμα Κωδικού")
    blanklabel = Label(passerror, text = " ", bg='#bdbdbd').grid(row = 0)
    errlabel = Label(passerror, text = passerrorlabel.get(), bg='#bdbdbd', font=("Courier", 16, "bold")).grid(row = 1)
def setpassword():
    setapass = Toplevel(master)
    e = Entry(setapass)
    e2 = Entry(setapass)
    setpasslabel = StringVar()
    confirmpasslabel = StringVar()
    setpassbuttonlabel = StringVar()
    setapass.config(bg='#bdbdbd')
    def passclose():
        setpassopen.set(0)
        setapass.destroy()
    setapass.protocol("WM_DELETE_WINDOW", passclose)
    setapass.resizable(width=False, height=False)
    setpassopen.set(1)
    warninglabel = StringVar()
    warninglabel.set("")
    def complete():
        if len(e.get()) != 0 and len(e2.get()) != 0: #check if the password entry is empty
            if e.get() == e2.get():
                wrongpass = 0
                mypassword.set(e.get()) #get the password entry's contents
                if os.path.isfile("Encrypted Password Storage.txt"):
                    file = open("Encrypted Password Storage.txt", "r")
                    todecnextline = 0
                    for line in file:
                        if "Encrypted Password:" in line:
                            todecnextline = 1
                        else:
                            if todecnextline == 1:
                                try:
                                    l = decrypt2(str(line), 0)
                                    todecnextline = 0
                                except:
                                    wrongpass = 1
                if wrongpass == 1:
                    if curlang.get() == 0:
                        warninglabel.set("Wrong Password!")
                    elif curlang.get() == 1:
                        warninglabel.set("Неправильный пароль!")
                    elif curlang.get() == 2:
                        warninglabel.set("Λάθος κωδικός!")
                elif wrongpass == 0:
                    passwordentered.set(1) #to confirm later that the password has been entered
                    setpassopen.set(0) #confirm that the process is done and the window will be closed after this command
                    setapass.destroy()
            else:
                if curlang.get() == 0:
                    warninglabel.set("The two passwords are not equal!")
                elif curlang.get() == 1:
                    warninglabel.set("Пароли не совпадают!")
                elif curlang.get() == 2:
                    warninglabel.set("Οι δύο κωδικοί είναι διαφορετικοί!")
        else:
            if curlang.get() == 0:
                warninglabel.set("Password fields shouldn't be empty!")
            elif curlang.get() == 1:
                warninglabel.set("Пароли не могут быть пустыми!")
            elif curlang.get() == 2:
                warninglabel.set("Οι κωδικοί δεν μπορούν να είναι άδειοι!")
    if curlang.get() == 0:
        setpasslabel.set("Set a password:")
        setpassbuttonlabel.set("Set password")
        setapass.title("Set A Password First!")
        confirmpasslabel.set("Confirm Password:")
        setapass.geometry("550x110")
    elif curlang.get() == 1:
        setpasslabel.set("Назначьте пароль:")
        setpassbuttonlabel.set("Назначить пароль")
        setapass.title("Назначьте Пароль Сперва!")
        confirmpasslabel.set("Введите еще раз:")
        setapass.geometry("560x110")
    elif curlang.get() == 2:
        setpasslabel.set("Βάλτε κωδικό:")
        setpassbuttonlabel.set("ΟΚ")
        setapass.title("Βάλτε Κωδικό Πρώτα!")
        confirmpasslabel.set("Άλλη μια φορά:")
        setapass.geometry("570x110")
    blanklabel = Label(setapass, text = " ", bg='#bdbdbd').grid(row = 0)
    warnlabel = Label(setapass, textvariable = warninglabel, bg='#bdbdbd', fg = "red").grid(row = 3, stick = W)
    label = Label(setapass, text = setpasslabel.get(), bg='#bdbdbd', font=("Sans Serif", 10, "bold")).grid(row = 1, stick = W)
    label = Label(setapass, text = confirmpasslabel.get(), bg='#bdbdbd', font=("Sans Serif", 10, "bold")).grid(row = 2, stick = W)
    e.grid(row = 1, column = 1, stick = W)
    e2.grid(row = 2, column = 1, stick = W)
    e2.config(show="*")
    e.config(show="*")
    blanklabel = Label(setapass, text = "    ", bg='#bdbdbd').grid(row = 1, column = 2, stick = W)
    setpass = Button(setapass, text = setpassbuttonlabel.get(), command = complete, width = 15, bg='lightgrey', borderwidth = 5, font=("Serif", 11)).grid(row = 2, column = 3, stick = W)


def openpasses():
    savedpassespage = Toplevel(master)
    savedpassespage.config(bg='#bdbdbd')
    savedpassespage.resizable(width=False, height=False)
    passesl2 = Text(savedpassespage, height = 25, width = 55, font=("Courier", 10, "bold"), bg='lightgrey')
    passesl2.grid(row = 1)
    if passwordentered.get() != 1 and setpassopen.get() != 1:
       setpassword()
    def areyousure():
        areyousure = Toplevel(master)
        areyousure.config(bg='#bdbdbd')
        areyousure.resizable(width=False, height=False)
        label = Label(areyousure, text = "   ", bg='#bdbdbd').grid(row = 0, column = 0, stick = W)
        label = Label(areyousure, text = "   ", bg='#bdbdbd').grid(row = 1, column = 0, stick = W)
        yesbuttonlabel = StringVar()
        nobuttonlabel = StringVar()
        if curlang.get() == 0:
            areyousure.title("Are you sure?")
            label = Label(areyousure, text = "Are you sure that you want to save the file?", bg='#bdbdbd').grid(row = 0, column = 1, stick = W)
            yesbuttonlabel.set("Yes")
            nobuttonlabel.set("NO")
        elif curlang.get() == 1:
            areyousure.title("Вы уверены?")
            label = Label(areyousure, text = "Вы уверены что хотите сохранить файл?", bg='#bdbdbd').grid(row = 0, column = 1, stick = W)
            yesbuttonlabel.set("Да")
            nobuttonlabel.set("НЕТ")
        elif curlang.get() == 2:
            areyousure.title("Είστε σίγουροι?")
            label = Label(areyousure, text = "Είστε σίγουροι ότι θέλετε να αποθηκεύσετε το αρχείο?", bg='#bdbdbd').grid(row = 0, column = 1, stick = W)
            yesbuttonlabel.set("Ναι")
            nobuttonlabel.set("ΟΧΙ")
        yes = Button(areyousure, text = yesbuttonlabel.get(), command = lambda: savepassesfile(areyousure), width = 15, bg='lightgrey', borderwidth = 5).grid(row = 2, column = 2, stick = W)
        no = Button(areyousure, text = nobuttonlabel.get(), command = areyousure.destroy, width = 15, bg='lightgrey', borderwidth = 5).grid(row = 2, column = 0, stick = W)
    def savepassesfile(areyousure):
        areyousure.destroy()
        if passwordentered.get() == 1:
            if os.path.isfile("Encrypted Password Storage.txt"):
                sfile = open("Encrypted Password Storage.txt", "r+")
                sfile.truncate(0)
                passes = str(passesl2.get("1.0", "end"))
                for line in passes.splitlines():
                    if curlang.get() == 0:
                        if "Password: " in line:
                            k = line.replace("Password: ", "")
                            k = k.replace('\n', "")
                            sfile.write("\nEncrypted Password:\n")
                            cipher = AES_Encryption(key=mypassword.get(), iv = 'dsfgsjklcvb45eso')
                            encpass2 = cipher.encrypt(k)
                            encpass2 = str(encpass2)
                            l = ""
                            o = 0
                            for b in encpass2:
                                if o != 0 and o != 1 and o != (len(encpass2)-1):
                                    l += b
                                o += 1
                            encpass2 = l
                            sfile.write(l + "\n")
                        elif "Name: " in line:
                            sfile.write('\n' + str(line))
                    elif curlang.get() == 1:
                        if "Пароль: " in line:
                            k = line.replace("Пароль: ", "")
                            k = k.replace('\n', "")
                            sfile.write("\nEncrypted Password:\n")
                            cipher = AES_Encryption(key=mypassword.get(), iv = 'dsfgsjklcvb45eso')
                            encpass2 = cipher.encrypt(k)
                            encpass2 = str(encpass2)
                            l = ""
                            o = 0
                            for b in encpass2:
                                if o != 0 and o != 1 and o != (len(encpass2)-1):
                                    l += b
                                o += 1
                                encpass2 = l
                            sfile.write(l + "\n")
                        elif "Название Пароля: " in line:
                            sfile.write('\n' + str(line.replace("Название Пароля", "Name")))
                    elif curlang.get() == 2:
                        if "Κωδικός: " in line:
                            k = line.replace("Κωδικός: ", "")
                            k = k.replace('\n', "")
                            sfile.write("\nEncrypted Password:\n")
                            cipher = AES_Encryption(key=mypassword.get(), iv = 'dsfgsjklcvb45eso')
                            encpass2 = cipher.encrypt(k)
                            encpass2 = str(encpass2)
                            l = ""
                            o = 0
                            for b in encpass2:
                                if o != 0 and o != 1 and o != (len(encpass2)-1):
                                    l += b
                                o += 1
                            encpass2 = l
                            sfile.write(l + "\n")
                        elif "Όνομα Κωδικού: " in line:
                            sfile.write('\n' + str(line.replace("Όνομα Κωδικού", "Name")))
            sfile.close()
        elif passwordentered.get() != 1 and setpassopen.get() != 1:
            if passwarningopen.get() == 0:
                setpasswarning()
            setpassword()
        elif passwordentered.get() != 1 and setpassopen.get() == 1: #its better to show the warning more times than the set password window to avoid setting a wrong password
            if passwarningopen.get() == 0:
                setpasswarning()
    def refreshpasses():
        passesl2.delete('1.0', "end")
        if curlang.get() == 0:
            passesl2.insert(INSERT, "You can add new passwords by writing them the same way as the program-saved ones but using latin letters only for the name and password\n-------------------------------------------------------\n")
        elif curlang.get() == 1:
            passesl2.insert(INSERT, "Вы можете добавить новые пароли добавляя их таким же образом как и пароли сохранненые программой но исключительно латиницей в имени и в пароле\n-------------------------------------------------------\n")
        elif curlang.get() == 2:
            passesl2.insert(INSERT, "Μπορείτε να βάλετε τους δικούς σας κωδικούς γράφοντας τους με τον ίδιο τρόπο όπως το κάνει το πρόγραμμα και μόνο με λατινικούς χαρακτήρες το όνομα και τον κωδικό \n-------------------------------------------------------\n")
        if os.path.isfile("Encrypted Password Storage.txt"):
            file = open("Encrypted Password Storage.txt", "r")
            todecnextline = 0
            for line in file:
                if "Encrypted Password:" in line:
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
                        try:
                            l = decrypt2(str(line), 0)
                            todecnextline = 0
                            passesl2.insert(INSERT, str(l) + '\n')
                        except:
                            if curlang.get() == 0:
                                passesl2.insert(INSERT, "Error while decrypting password, check the entered password and the format of the passwords in the password storage file!")
                            elif curlang.get() == 1:
                                passesl2.insert(INSERT, "Произошла ошибка при расшифровки пароля, проверьте введенный пароль и формат паролей в файле со сохраннеными паролями!")
                            elif curlang.get() == 2:
                                passesl2.insert(INSERT, "Σφαλμα στην αποκρυπτογράφηση του κωδικού, ελέγξτε τον κωδικό σας και την μορφή με την οποία εμφανίζονται οι κωδικοί στο αρχείο με τους κρυπτογραφημένους κωδικούς!")
                            todecnextline = 0
                    else:
                        passesl2.insert(INSERT, '\n')
            file.close()
        else:
            if curlang.get() == 0:
                passesl2.insert(INSERT, "Encrypted Password Storage.txt not found!\nYou may not have created a password yet or the file may have been deleted!")
            elif curlang.get() == 1:
                passesl2.insert(INSERT, "Encrypted Password Storage.txt Не найден!\nВозможно, вы еще не сохраняли пароли или же файл был удален!")
            elif curlang.get() == 2:
                passesl2.insert(INSERT, "Encrypted Password Storage.txt Δεν βρέθηκε!\nΊσως να μην έχετε αποθηκεύσει κωδικούς ακόμη ή το αρχείο να εχεί διαγραφεί!")
    savepassesbuttonlabel = StringVar()
    refreshbuttonlabel = StringVar()
    if curlang.get() == 0:
        refreshbuttonlabel.set("Refresh")
        savepassesbuttonlabel.set("Save")
        savedpassespage.title("Saved Passwords")
        passesl = Label(savedpassespage, text = "Saved Passwords:", bg='#bdbdbd').grid(row = 0, column = 0)
    elif curlang.get() == 1:
        refreshbuttonlabel.set("Перезагрузить")
        savepassesbuttonlabel.set("Сохранить")
        savedpassespage.title("Сохраненные Пароли")
        passesl = Label(savedpassespage, text = "Сохраненные Пароли:", bg='#bdbdbd').grid(row = 0, column = 0)
    elif curlang.get() == 2:
        refreshbuttonlabel.set("Επαναφόρτωση")
        savepassesbuttonlabel.set("Αποθήκευση")
        savedpassespage.title("Αποθηκευμένοι Κωδικοί")
        passesl = Label(savedpassespage, text = "Αποθηκευμένοι Κωδικοί:", bg='#bdbdbd').grid(row = 0, column = 0)
    refreshbutton = Button(savedpassespage, textvariable = refreshbuttonlabel, bg='lightgrey', command = refreshpasses, borderwidth = 5, font=("Sans Serif", 9, "bold")).grid(row = 0, column = 1)
    savepassesbutton = Button(savedpassespage, textvariable = savepassesbuttonlabel, bg='lightgrey', command = areyousure, borderwidth = 5, font=("Sans Serif", 9, "bold")).grid(row = 2, column = 0)
    refreshpasses()

def openimp():
    impage = Toplevel(master)
    impage.config(bg='#bdbdbd')
    impage.resizable(width = False, height = False)
    if curlang.get() == 0:
        impage.title("Important Note")
        l10 = Label (impage, text = "IMPORTANT!!!!", font=("Courier", 18, "bold"), bg='#bdbdbd').grid(row = 0)
        l10 = Label (impage, text = "\n\nBackup the file to decrypt the passwords in the future!!!\nFile name:\nEncrypted Password Storage.txt", font=("Courier", 12, "bold"), bg='#bdbdbd').grid(row = 1)
    elif curlang.get() == 1:
        impage.title("Важная Записка")
        l10 = Label (impage, text = "ВАЖНО!!!!", font=("Courier", 18, "bold"), bg='#bdbdbd').grid(row = 0)
        l10 = Label (impage, text = "\n\nСохраните этот файл чтобы расшифровать пароли в будущем!!!\nНазвание Файла:\nEncrypted Password Storage.txt", font=("Courier", 12, "bold"), bg='#bdbdbd').grid(row = 1)
    elif curlang.get() == 2:
        impage.title("Σημαντική Παρατήρηση")
        l10 = Label (impage, text = "ΣΗΜΑΝΤΙΚΟ!!!!", font=("Courier", 18, "bold"), bg='#bdbdbd').grid(row = 0)
        l10 = Label (impage, text = "\n\nΑποθηκεύστε σε ασφαλή μέρος το παρακάτω αρχείο για την αποκρυπτογράφηση των κωδικών σας στο μέλλον!!!\nΌνομα Αρχείου:\nEncrypted Password Storage.txt", font=("Courier", 12, "bold"), bg='#bdbdbd').grid(row = 1)
    
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
passwrd = Menu(menu, tearoff = 0)
changepasswordlabel = StringVar()
aboutuscaslabel = StringVar()
langlabel = StringVar()
savedpasslabel = StringVar()
aboutuslabel = StringVar()
importantlabel = StringVar()
viewsavedlabel = StringVar()
hidepassvar = IntVar()
passstrength = StringVar()
recentrating = StringVar()
recentrating.set(0)
def setenglish():
    curlang.set(0)
    master.title("Password Generator")
    master.geometry("580x270")
    yourpasswordislabel.set("Your Password is: ")
    passwordnamelabel.set('Password Name')
    passwordlengthlabel.set('Length')
    decryptbutton.set("Decrypt")
    generatebutton.set("[Generate]")
    clearbuttonlabel.set("Clear")
    copybutton.set("Copy")
    savebutton.set("Save")
    if hidepassvar.get() == 0:
        hidepassbuttonlabel.set("Hide")
    else:
        hidepassbuttonlabel.set("Show")
    symbolscheck.set("Symbols")
    numberscheck.set("Numbers")
    uppercheck.set("UpperCase Letters")
    lowercheck.set("LowerCase Letters")
    encryptedpasslabel.set("Encrypted: ")
    decryptedpasslabel.set("Decrypted: ")
    yourencpasswordlabel.set("Your Password in encrypted format:")
    about.entryconfigure(0, label = "Important Note")
    about.entryconfigure(1, label = "About us")
    savedpasses.entryconfigure(0, label = "Saved Passwords")
    passwrd.entryconfigure(0, label = "Change Password")
    aboutuscaslabel.set("About us")
    passstrength.set("Strength: \n" + recentrating.get())
    langlabel.set("Language")
    savedpasslabel.set("Saved Passwords")
    aboutuslabel.set("About us")
    importantlabel.set("Important Note")
    viewsavedlabel.set("View Saved Passwords")

def setrussian():
    curlang.set(1)
    master.title("Генератор Паролей")
    master.geometry("660x270")
    yourpasswordislabel.set("Пароль: ")
    passwordnamelabel.set('Название Пароля')
    passwordlengthlabel.set('Размер Пароля')
    clearbuttonlabel.set("Очистить")
    decryptbutton.set("Расшифровать")
    generatebutton.set("[Сгенерировать]")
    about.entryconfigure(0, label = "Важная Записка")
    about.entryconfigure(1, label = "О нас")
    savedpasses.entryconfigure(0, label = "Просмотр Сохраненных Паролей")
    passwrd.entryconfigure(0, label = "Поменять Пароль")
    copybutton.set("Скопировать")
    savebutton.set("Сохранить")
    symbolscheck.set("Символы")
    if hidepassvar.get() == 0:
        hidepassbuttonlabel.set("Скрыть")
    else:
        hidepassbuttonlabel.set("Показать")
    numberscheck.set("Цифры")
    uppercheck.set("Большие Буквы")
    lowercheck.set("Маленькие Буквы")
    encryptedpasslabel.set("Зашифрованно: ")
    passstrength.set("Прочность: \n" + recentrating.get())
    decryptedpasslabel.set("Расшифрованно: ")
    yourencpasswordlabel.set("Пароль в зашифрованном виде:")
    aboutuscaslabel.set("О нас")
    langlabel.set("Язык")
    savedpasslabel.set("Сохранненые Пароли")
    aboutuslabel.set("О нас")
    importantlabel.set("Важная Записка")
    viewsavedlabel.set("Посмотреть Сохранненые Пароли")

def setgreek():
    curlang.set(2)
    master.title("Γεννήτρια Κωδικών Πρόσβασης")
    master.geometry("630x270")
    yourpasswordislabel.set("Κωδικός Πρόσβασης: ")
    passwordnamelabel.set('Όνομα Κωδικού')
    passwordlengthlabel.set('Μέγεθος')
    decryptbutton.set("Αποκρυπτογράφηση")
    passstrength.set("Αντοχή: \n" + recentrating.get())
    generatebutton.set("[Δημιουργία]")
    copybutton.set("Αντιγραφή")
    savebutton.set("Αποθήκευση")
    if hidepassvar.get() == 0:
        hidepassbuttonlabel.set("Απόκρυψη")
    else:
        hidepassbuttonlabel.set("Εμφάνιση")
    clearbuttonlabel.set("Καθαρισμός")
    symbolscheck.set("Σύμβολα")
    numberscheck.set("Αριθμοί")
    uppercheck.set("Κεφαλαία Γράμματα")
    lowercheck.set("Μικρά Γράμματα")
    about.entryconfigure(0, label = "Σημαντική Παρατήρηση")
    about.entryconfigure(1, label = "Ποιοί είμαστε")
    savedpasses.entryconfigure(0, label = "Αποθηκεύμενοι Κωδικοί")
    passwrd.entryconfigure(0, label = "Αλλαγή Κωδικού")
    encryptedpasslabel.set("Κρυπτογραφημένος: ")
    decryptedpasslabel.set("Αποκρυπτογραφημένος: ")
    yourencpasswordlabel.set("Κρυπτογραφημένος Κωδικός:")
    aboutuscaslabel.set("Ποιοί Είμαστε")
    langlabel.set("Γλώσσα")
    savedpasslabel.set("Αποθηκευμένοι Κωδικοί")
    aboutuslabel.set("Ποιοί Είμαστε")
    importantlabel.set("Σημαντική Παρατήρηση")
    viewsavedlabel.set("Άνοιγμα Αποθηκευμένων Κωδικών")

aboutuscaslabel.set("About us")
changepasswordlabel.set("Change Password")
langlabel.set("Language")
savedpasslabel.set("Saved Passwords")
aboutuslabel.set("About us")
importantlabel.set("Important Note")
viewsavedlabel.set("View Saved Passwords")
menu.add_cascade(label = "About us", menu = about)
menu.add_cascade(label = "Password", menu = passwrd)
passwrd.add_command(label = changepasswordlabel.get(), command = setpassword)
menu.add_cascade(label = "Language", menu = lang)
lang.add_command(label = 'English', command = setenglish)
lang.add_command(label = 'Русский', command = setrussian)
lang.add_command(label = 'Ελληνικά', command = setgreek)
savedpasses = Menu(menu, tearoff = 0)
menu.add_cascade(label = "Saved Passwords", menu = savedpasses)
savedpasses.add_command(label=viewsavedlabel.get(), command = openpasses)
about.add_command(label=importantlabel.get(), command = openimp)
about.add_command(label=aboutuslabel.get(), command = openab)
decpass = StringVar()
encpass = StringVar()
yourpasswordislabel = StringVar()
yourpasswordislabel.set("Your Password is: ")
l2 = Label(master, textvariable = yourpasswordislabel, bg='#bdbdbd').grid(row = 4, column = 0, stick = E)
passstrength.set("Strength: \n0")
l00 = Label(master, textvariable = passstrength, bg= '#bdbdbd').grid(row = 4, column = 5, stick = W)
yourencpasswordlabel = StringVar()
yourencpasswordlabel.set("Your Password in encrypted format:")
l3 = Label(master, textvariable = yourencpasswordlabel, anchor = 'w', bg='#bdbdbd').grid(row = 5, column = 0, ipadx = 1, stick = E)
blank = Label(master, text = " ", anchor=W, bg='#bdbdbd').grid(row = 3, column = 2, ipadx = 1, stick = W)
decryptedpasslabel = StringVar()
decryptedpasslabel.set("Decrypted: ")
l5 = Label(master, textvariable = decryptedpasslabel, bg='#bdbdbd').grid(row = 9, column = 0, ipadx = 1, stick = E)
encryptedpasslabel = StringVar()
encryptedpasslabel.set("Encrypted: ")
l10 = Label(master, textvariable = encryptedpasslabel, bg='#bdbdbd').grid(row = 6, column = 0, ipadx = 1, stick = E)
e3 = Text(master, width = 20, borderwidth = 2, bg='lightgrey', height = 2) #Encrypted Password Entry
e3.grid(row = 6, column = 1, stick = W)
e4 = Text(master, width = 20, borderwidth = 2, bg='lightgrey', height = 2) #Your Password is Entry
e4.grid(row= 4, column = 1, stick = W)
e5 = Text(master, width = 20, borderwidth = 2, bg='lightgrey', height = 2) #Decrypted Password Entry
e5.grid(row= 9, column = 1, stick = W)
e6 = Text(master, width = 20, borderwidth = 2, bg='lightgrey', height = 2) #Password in encrypted format entry
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
                rating -= (passtorate.count('i') + passtorate.count('1'))
        elif 'l' in passtorate:
            rating -= (passtorate.count('i')+ passtorate.count('l'))
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
    recentrating.set(str(rating))
    return int(rating)

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
    e4.insert(INSERT, l)
    ratingvar = ratepass(str(l))
    if curlang.get() == 0:
        passstrength.set("Strength: \n" + str(ratingvar))
    elif curlang.get() == 1:
        passstrength.set("Прочность: \n" + str(ratingvar))
    elif curlang.get() == 2:
        passstrength.set("Αντοχή: \n" + str(ratingvar))
    cipher = AES_Encryption(key=mypassword.get(), iv = 'dsfghjklcvb45eso')
    encpass2 = cipher.encrypt(l)
    encpass2 = str(encpass2)
    l = ""
    o = 0
    for b in encpass2:
        if o != 0 and o != 1 and o != (len(encpass2)-1):
            l += b
        o += 1
    encpass.set(l)
    e6.insert(INSERT, l)
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
    todec = todec.encode().decode('unicode_escape').encode("raw_unicode_escape")
    def remove_bytes(buffer, start, end):
        fmt = '%ds %dx %ds' % (start, end-start, len(buffer)-end)
        return b''.join(struct.unpack(fmt, buffer))
    todec = remove_bytes(todec, (len(todec)-1), (len(todec)))
    cipher = AES_Encryption(key=mypassword.get(), iv = 'dsfgsjklcvb45eso')
    decr = cipher.decrypt(todec)
    decr = str(decr)
    if mode == 1:
        e5.delete('1.0',"end")
        e5.insert(INSERT, str(decr))
    else:
        return str(decr)

def copy2 (passtocopy):
    clip.copy(str(passtocopy))

def copy4 (passtocopy):
    clip.copy(str(passtocopy))

def copy6 (passtocopy):
    clip.copy(str(passtocopy))


def hidepassword():
    if hidepassvar.get() == 0:
        e4.config(bg = "black")
        e5.config(bg = "black")
        if curlang.get() == 0:
            hidepassbuttonlabel.set("Show")
        elif curlang.get() == 1:
            hidepassbuttonlabel.set("Показать")
        elif curlang.get() == 2:
            hidepassbuttonlabel.set("Εμφάνιση")
        hidepassvar.set(1)
    else:
        e4.config(bg = "lightgrey")
        e5.config(bg = "lightgrey")
        if curlang.get() == 0:
            hidepassbuttonlabel.set("Hide")
        elif curlang.get() == 1:
            hidepassbuttonlabel.set("Скрыть")
        elif curlang.get() == 2:
            hidepassbuttonlabel.set("Απόκρυψη")
        hidepassvar.set(0)
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
    if b != 0 and e2.get() != "0" and passwordentered.get() == 1:
        e4.delete('1.0', "end")
        e6.delete('1.0', "end")
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
    if passwordentered.get() != 1 and setpassopen.get() != 1:
        if passwarningopen.get() == 0:
            setpasswarning()
        setpassword()
    elif passwordentered.get() != 1 and setpassopen.get() == 1:
        if passwarningopen.get() == 0:
            setpasswarning()

def clearencpass ():
    e3.delete('1.0', "end")

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
clearbuttonlabel = StringVar() #>>
clearbuttonlabel.set("Clear") #>>
hidepassbuttonlabel = StringVar()
hidepassbuttonlabel.set("Hide")
hidepassbutton = Button(master, textvariable = hidepassbuttonlabel, command = hidepassword, bg='lightgrey', borderwidth = 5).grid(row = 4, column = 4, ipadx = 1, stick = W)
clearbutton = Button (master, textvariable = clearbuttonlabel, command = clearencpass, bg='lightgrey', borderwidth = 5).grid(row = 6, column = 4, ipadx = 1, stick = W)
b2 = Button(master , textvariable = savebutton, command = lambda: savetofile(str(e1.get()), str(encpass.get())), bg='lightgrey', borderwidth = 5).grid(row = 5, column = 3, ipadx = 1, stick = W)
b5 = Button(master , textvariable = copybutton, command = lambda: copy6(str(encpass.get())), bg='lightgrey', borderwidth = 5).grid(row = 5, column = 4, ipadx = 1, stick = W)
b3 = Button(master, textvariable = decryptbutton, command = lambda: decrypt2(e3.get("1.0","end"), 1), bg='lightgrey', borderwidth = 5).grid(row = 6, column = 3, ipadx = 1, stick = W)
b4 = Button(master, textvariable = copybutton, command = lambda: copy2(str(e5.get("1.0","end"))), bg='lightgrey', borderwidth = 5).grid(row = 9, column = 3, ipadx = 1, stick = W)
b6 = Button(master, textvariable = copybutton, command = lambda: copy4(str(e4.get("1.0","end"))), bg='lightgrey', borderwidth = 5).grid(row = 4, column = 3, ipadx = 1, stick = W)
b1 = Button(master, textvariable = generatebutton, command = dothis, bg='lightgrey', borderwidth = 5, font=("Serif", 10, "bold")).grid(row=1, column=3, ipadx = 1, stick = W)
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
setpassword()
mainloop()
"""
--------------------------------------------------
Borrowed Code from: 

https://stackoverflow.com/questions/18563018/how-to-remove-a-range-of-bytes-from-a-bytes-object-in-python

--------------------------------------------------

In development by inf2021221 & inf2021198 & inf2021119 for our university project at IONIO 
University of Informatics

Link to the Github project:
    https://github.com/maxiikk/PasswordGenerator

Last edit made at 10/4/2022 18:16
Version: 1.1
"""
