from Encryptor import AES_Encryption
from tkinter import *
import os.path
import pyperclip as clip
from tkinter import ttk
import random
import struct #struct is used for the decrypt function

master = Tk() #creating the main window
appwidth = 580
appheight = 290
screenwidth = master.winfo_screenwidth()
screenheight = master.winfo_screenheight()
xx = int((screenwidth/2) - (appwidth/2))
yy = int((screenheight/2) - (appheight/2))
master.title("Password Generator") #main window title
master.geometry(f"{appwidth}x{appheight}+{xx}+{yy}") #defining main window's size
menu = Menu(master) #defining main window's menu
master.config(menu = menu, bg='#bdbdbd') #changing main window's background and assigning the menu we creating to the menu of the main window
master.resizable(width=False, height=False) #making the main window non-resizable so it doesnt get ugly upon changing it's size
curlang = IntVar() #variable to track the current language of the program
curlang.set(0) #setting by default to 0 which is for English
mypassword = StringVar() #variable for the user's password
passwordentered = IntVar() #variable to track if a password has been entered successfully
setpassopen = IntVar() #to check if the setpassword() is already active to avoid many same windows
passwarningopen = IntVar() #to check if the setpasswarning() function is already active
usingsimilarchars = IntVar()
usingsimilarchars.set(1)
usingambiguoussymbs = IntVar()
usingambiguoussymbs.set(1)
cipher = StringVar() #Variable for the cipher
mainframe = Frame(master, bg='#bdbdbd')
mainframe.grid(row = 0, stick = W)
secframe = Frame(master, bg='#bdbdbd')
secframe.grid(row = 1)

def decrypt(todec, password): 
    todec = todec.encode().decode('unicode_escape').encode("raw_unicode_escape")
    def remove_bytes(buffer, start, end): 
        fmt = '%ds %dx %ds' % (start, end-start, len(buffer)-end)
        return b''.join(struct.unpack(fmt, buffer))
    todec = remove_bytes(todec, (len(todec)-1), (len(todec)))
    cipher = AES_Encryption(key=password, iv = 'dsfgsjklcvb45eso')
    decr = cipher.decrypt(todec)
    decr = str(decr)
    return decr
def encrypt2 (k, password):
    cipher = AES_Encryption(key=password, iv = 'dsfgsjklcvb45eso') #create the cipher for the encryption
    enc = cipher.encrypt(k) #encrypt with the password
    enc = str(enc) #convert from bytes to string
    l = "" #temporary variable to contain the encrypted password for the '' to be removed
    o = 0 #temporary variable used to track the position in the string
    for b in enc: #process for removing the '' from the string for a more friendly look
        if o != 0 and o != 1 and o != (len(enc)-1):
            l += b
        o += 1
    return l
def encrypt (k):
    cipher = AES_Encryption(key=mypassword.get(), iv = 'dsfgsjklcvb45eso') #create the cipher for the encryption
    enc = cipher.encrypt(k) #encrypt with the password
    enc = str(enc) #convert from bytes to string
    l = "" #temporary variable to contain the encrypted password for the '' to be removed
    o = 0 #temporary variable used to track the position in the string
    for b in enc: #process for removing the '' from the string for a more friendly look
        if o != 0 and o != 1 and o != (len(enc)-1):
            l += b
        o += 1
    return l
def setpasswarning():
    passerror = Toplevel(master) #defining a new window with the name passerror >>
    passerrorlabel = StringVar() #label to show warnings related to the entered password
    passerror.config(bg='#bdbdbd') #>>
    passerror.geometry("300x100") #>>
    passwarningopen.set(1) #setting the variable to 1 to confirm later that the window is already open
    def warnclose(): #close button function
        passwarningopen.set(0) #setting the passerror window tracking variable to 0/closed
        passerror.destroy() #closing the passerror window
    passerror.protocol("WM_DELETE_WINDOW", warnclose) #redefining window's close button function
    passerror.resizable(width=False, height=False) #>>
    if curlang.get() == 0: #localization for the shown labels
        passerrorlabel.set("Set a password first!")
        passerror.title("Password Error")
    elif curlang.get() == 1:
        passerrorlabel.set("Сперва назначьте пароль!")
        passerror.title("Ошибка пароля")
    elif curlang.get() == 2:
        passerrorlabel.set("Βάλτε κωδικό πρώτα!")
        passerror.title("Σφάλμα Κωδικού")
    blanklabel = Label(passerror, text = " ", bg='#bdbdbd').grid(row = 0)
    errlabel = Label(passerror, text = passerrorlabel.get(), bg='#bdbdbd', font=("Courier", 16, "bold")).grid(row = 1) #label for the warning
def setpassword (mode = 0):
    setapass = Toplevel(master) #Creating new window with the name setapass >>
    setpasslabel = StringVar() #variable used for localization of the window's labels >>>
    confirmpasslabel = StringVar() #>>>
    setpassbuttonlabel = StringVar() #>>>
    setapass.config(bg='#bdbdbd') #>>
    mainframe = Frame(setapass, bg='#bdbdbd')
    mainframe.grid(row = 0)
    e = Entry(mainframe) #creating entry e for the first password field
    e2 = Entry(mainframe) #creating entry e2 for the second password field
    def passclose(): #redefining window's close button function
        setpassopen.set(0) #setting to 0/closed
        setapass.destroy() #closing the window
    setapass.protocol("WM_DELETE_WINDOW", passclose) #redifining close button's function
    setapass.resizable(width=False, height=False) #>>
    setpassopen.set(1) #setting to 1/open
    warninglabel = StringVar() #variable for the warning label
    warninglabel.set("") #default warning - no warning
    changepassmode = IntVar()
    changepassmode.set(mode)
    def complete():
        if len(e.get()) != 0 and len(e2.get()) != 0: #check if the password entry is empty
            if e.get() == e2.get(): #if the two password fields are equal
                wrongpass = 0
                mypassword.set(e.get()) #get the password entry's contents
                if changepassmode.get() == 0:
                    if os.path.isfile("Encrypted Password Storage.txt"): #checking if the password entered can decrypt the saved passwords in case there are any saved passwords
                        file = open("Encrypted Password Storage.txt", "r")
                        todecnextline = 0 #variable to determine which line to decrypt
                        for line in file:
                            if "Encrypted Password:" in line:
                                todecnextline = 1 #if the password field is in the next field the variable is set to 1 to decrypt the next line that contains the password
                            else:
                                if todecnextline == 1:
                                    try:
                                        l = decrypt2(str(line), mode = 0)
                                        todecnextline = 0
                                    except:
                                        wrongpass = 1 #if decryption fails then the entered password does not match the password that the saved passwords are encrypted with
                if wrongpass == 1: #if the decryption fails, show a warning
                    if curlang.get() == 0:
                        warninglabel.set("Wrong Password!")
                    elif curlang.get() == 1:
                        warninglabel.set("Неправильный пароль!")
                    elif curlang.get() == 2:
                        warninglabel.set("Λάθος κωδικός!")
                elif wrongpass == 0:
                    passwordentered.set(1) #to confirm later that the password has been entered
                    e1.focus_set()
                    setpassopen.set(0) #confirm that the process is done and the window will be closed after this command
                    setapass.destroy() #closing window after successful password entry
            else: #if the two password fields are not equal then show a warning in the correct language
                if curlang.get() == 0:
                    warninglabel.set("The two passwords are not equal!")
                elif curlang.get() == 1:
                    warninglabel.set("Пароли не совпадают!")
                elif curlang.get() == 2:
                    warninglabel.set("Οι δύο κωδικοί είναι διαφορετικοί!")
        else: #if the password fields are empty then show a warning
            if curlang.get() == 0:
                warninglabel.set("Password fields shouldn't be empty!")
            elif curlang.get() == 1:
                warninglabel.set("Пароли не могут быть пустыми!")
            elif curlang.get() == 2:
                warninglabel.set("Οι κωδικοί δεν μπορούν να είναι άδειοι!")
    if curlang.get() == 0: #localization of the shown labels
        setpasslabel.set("Set a password:")
        setpassbuttonlabel.set("Set password")
        setapass.title("Set A Password First!")
        confirmpasslabel.set("Confirm Password:")
        setapass.geometry(f'{550}x{110}+{int(xx-200)}+{int(yy-143)}')
    elif curlang.get() == 1:
        setpasslabel.set("Назначьте пароль:")
        setpassbuttonlabel.set("Назначить пароль")
        setapass.title("Назначьте Пароль Сперва!")
        confirmpasslabel.set("Введите еще раз:")
        setapass.geometry(f'{560}x{110}+{int(xx-200)}+{int(yy-143)}')
    elif curlang.get() == 2:
        setpasslabel.set("Βάλτε κωδικό:")
        setpassbuttonlabel.set("ΟΚ")
        setapass.title("Βάλτε Κωδικό Πρώτα!")
        confirmpasslabel.set("Άλλη μια φορά:")
        setapass.geometry(f'{570}x{110}+{int(xx-200)}+{int(yy-143)}')
    blanklabel = Label(mainframe, text = " ", bg='#bdbdbd').grid(row = 0) #used for the UI >>>>
    warnlabel = Label(setapass, textvariable = warninglabel, bg='#bdbdbd', fg = "red").grid(row = 3, stick = W)
    label = Label(mainframe, text = setpasslabel.get(), bg='#bdbdbd', font=("Sans Serif", 10, "bold")).grid(row = 1, stick = W)
    label = Label(mainframe, text = confirmpasslabel.get(), bg='#bdbdbd', font=("Sans Serif", 10, "bold")).grid(row = 2, stick = W)
    e.grid(row = 1, column = 1, stick = W) #setting the location of the first password field
    e2.grid(row = 2, column = 1, stick = W) #setting the location of the second password field
    e2.config(show="*") #hide entered password >
    e.config(show="*") #>
    blanklabel = Label(mainframe, text = "    ", bg='#bdbdbd').grid(row = 1, column = 2, stick = W) #>>>>
    setpass = Button(mainframe, text = setpassbuttonlabel.get(), command = complete, width = 15, bg='lightgrey', borderwidth = 5, font=("Arial", 10, "bold")).grid(row = 2, column = 3, stick = W) #"Set Password" button definition
    e.bind("<Return>", lambda event: e2.focus_set())
    e2.bind("<Return>", lambda event: complete())
    setapass.focus_set()
    e.focus_set()
def successwin(text, filename = "", geom = "250x100"):
    success = Toplevel(master)
    success.title("SUCCESS!")
    success.resizable(width = False, height = False)
    success.geometry(f'{geom}+{int(xx+215)}+{int(yy+36)}')
    success.config(bg='#bdbdbd')
    Label(success, text = "        ", bg='#bdbdbd').grid(row = 0)
    Label(success, text = ("          " + text +"!   "), fg = "green", font = ("bold", 14), bg='#bdbdbd').grid(row = 1)
    if filename != "":
        Button(success, text = " Open ", command = lambda: opennote(filename), width = 10, height = 1).grid(row = 1, column = 1, stick = W)
    Label(success, text = "        ", bg='#bdbdbd').grid(row = 2)

def failedwin():
    failed = Toplevel(master)
    failed.title("FAILED!")
    failed.resizable(width = False, height = False)
    failed.config(bg='#bdbdbd')
    failed.geometry(f'{200}x{50}+{int(xx+215)}+{int(yy+87)}')
    Label(failed, text = "        ", bg='#bdbdbd').grid(row = 0)
    Label(failed, text = "           FAILED!", fg = "red", font = ("bold", 14), bg='#bdbdbd').grid(row = 1)
    Label(failed, text = "        ", bg='#bdbdbd').grid(row = 2)

passeslistopen = IntVar()
def openpasses():
    passeswindow = Toplevel(master)
    passeswindow.title("Passwords")
    passeswindow.resizable(height = False, width = False)
    passeswindow.config(bg='#bdbdbd')
    passeswindow.geometry(f'{760}x{605}+{int(xx+215)}+{int(yy+170)}')
    def passesclose(): 
        passeslistopen.set(0) 
        passeswindow.destroy() 
    passeswindow.protocol("WM_DELETE_WINDOW", passesclose)
    passeslistopen.set(1)
    mainframe = Frame(passeswindow)
    mainframe.grid(row=1, column = 1, stick = N)
    mainframe.config(bg='#bdbdbd')
    secframe = Frame(mainframe)
    secframe.config(bg='#bdbdbd')
    secframe.grid(row = 0, column = 0, stick = N)
    firstframe = Frame(passeswindow)
    firstframe.config(bg='#bdbdbd')
    firstframe.grid(row = 1, column = 0)
    canvas = Canvas(firstframe, bg='#bdbdbd', width = 600, height = 600)
    canvas.grid(row=0, column=0, sticky="news")
    scrollbar = Scrollbar(firstframe, orient='vertical', command=canvas.yview)
    scrollbar.grid(row=0, column=99, sticky = NS)
    canvas['yscrollcommand'] = scrollbar.set
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
    frame_buttons = Frame(canvas, bg='#bdbdbd')
    canvas.create_window((0, 0), window=frame_buttons, anchor='nw')
    def scrolllistbox(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    passeswindow.bind("<MouseWheel>", scrolllistbox)
    def savename(k, j):
        mainfile = open("Encrypted Password Storage.txt", "r+")
        lines = mainfile.readlines()
        mainfile.close()
        done = 0
        i = -1
        index = 0
        print(k)
        todecnextline = 0
        for line in lines:
            i += 1
            if "Name:" in line:
                todecnextline = 1
            else:
                if todecnextline == 1:
                    try: #using "try" to avoid crashing upon failed decryption attempt
                        l = decrypt2(str(line), 0)
                        index += 1
                        print(l)
                        todecnextline = 0
                        if index == j:
                            lines[i] = line.replace(line, encrypt(k) + "\n")
                            print(decrypt2(lines[i]))
                            done = 1
                            break
                    except: #show a decryption error in case of a failed decryption
                        failedwin()
                        return
        if done == 1:
            mainfile = open("Encrypted Password Storage.txt", "w+")
            mainfile.truncate(0)
            for line in lines:
                mainfile.write(line)
            mainfile.close()
            successwin("Saved!")
    def savepass(k, j):
        mainfile = open("Encrypted Password Storage.txt", "r+")
        lines = mainfile.readlines()
        mainfile.close()
        done = 0
        i = -1
        index = 0
        print(k)
        todecnextline = 0
        for line in lines:
            i += 1
            if "Encrypted Password:" in line: #detecting the start of the password definition and setting the variable to 1 to decrypt the next line
                todecnextline = 1
            else:
                if todecnextline == 1:
                    try: #using "try" to avoid crashing upon failed decryption attempt
                        l = decrypt2(str(line))
                        index += 1
                        print(l)
                        todecnextline = 0
                        if index == j:
                            lines[i] = line.replace(line, encrypt(k) + "\n")
                            print(decrypt2(lines[i]))
                            done = 1
                            break
                    except: #show a decryption error in case of a failed decryption
                        failedwin()
                        return
        if done == 1:
            mainfile = open("Encrypted Password Storage.txt", "w+")
            mainfile.truncate(0)
            for line in lines:
                mainfile.write(line)
            mainfile.close()
            successwin("Saved!")
    def copypass(k):
        copy2(k.replace("\n", ""))
    def refreshpasses():
        firstframe = Frame(passeswindow)
        firstframe.config(bg='#bdbdbd')
        firstframe.grid(row = 1, column = 0)
        canvas = Canvas(firstframe, bg='#bdbdbd', width = 600, height = 600)
        canvas.grid(row=0, column=0, sticky="news")
        scrollbar = Scrollbar(firstframe, orient='vertical', command=canvas.yview)
        scrollbar.grid(row=0, column=99, sticky = NS)
        canvas['yscrollcommand'] = scrollbar.set
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
        frame_buttons = Frame(canvas, bg='#bdbdbd')
        canvas.create_window((0, 0), window=frame_buttons, anchor='nw')
        def scrolllistbox(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        passeswindow.bind("<MouseWheel>", scrolllistbox)
        i = 0
        todecnextlinename = 0
        todecnextlinepass = 0
        passesamount = 0
        namesamount = 0
        savepassbuttonlabel = StringVar()
        savenamebuttonlabel = StringVar()
        copypassbuttonlabel = StringVar()
        showpassbuttonlabel = StringVar()
        hidepassbuttonlabel = StringVar()
        if curlang.get() == 0:
            savepassbuttonlabel.set("Save Pass")
            savenamebuttonlabel.set("Save Name")
            copypassbuttonlabel.set("Copy")
            showpassbuttonlabel.set("Show")
            hidepassbuttonlabel.set("Hide")
        elif curlang.get() == 1:
            savepassbuttonlabel.set("Сохранить Пар.")
            savenamebuttonlabel.set("Сохранить Имя")
            copypassbuttonlabel.set("Копировать")
            showpassbuttonlabel.set("Показать")
            hidepassbuttonlabel.set("Скрыть")
        elif curlang.get() == 2:
            savepassbuttonlabel.set("Αποθήκευση Κωδ.")
            savenamebuttonlabel.set("Αποθήκευση Ονόμ.")
            copypassbuttonlabel.set("Αντιγραφή")
            showpassbuttonlabel.set("Εμφάνιση")
            hidepassbuttonlabel.set("Κρύψιμο")
        if passwordentered.get() == 1:
            mainfile = open("Encrypted Password Storage.txt", "r+")
            lines = mainfile.readlines()
            mainfile.close()
            for line in lines:
                if "Encrypted Password:" in line: #detecting the start of the password definition and setting the variable to 1 to decrypt the next line
                    todecnextlinepass = 1
                    if curlang.get() == 0: #localization of the shown text in the Text Box with the decrypted passwords
                        Label(frame_buttons, text = "Password: ", bg='#bdbdbd').grid(row = i+1, column = 0, stick = E)
                    elif curlang.get() == 1:
                        Label(frame_buttons, text = "Пароль: ", bg='#bdbdbd').grid(row = i+1, column = 0, stick = E)
                    elif curlang.get() == 2:
                        Label(frame_buttons, text = "Κωδικός: ", bg='#bdbdbd').grid(row = i+1, column = 0, stick = E)
                    Label(frame_buttons, text = "", bg='#bdbdbd').grid(row = i+2, column = 0)
                elif "Name:" in line:
                    todecnextlinename = 1
                    if curlang.get() == 0: #localization of the shown text in the Text Box with the decrypted passwords
                        Label(frame_buttons, text = "Name: ", bg='#bdbdbd').grid(row = i, column = 0, stick = E)
                    elif curlang.get() == 1:
                        Label(frame_buttons, text = "Название Пароля: ", bg='#bdbdbd').grid(row = i, column = 0, stick = E)
                    elif curlang.get() == 2:
                        Label(frame_buttons, text = "Όνομα Κωδικού: ", bg='#bdbdbd').grid(row = i, column = 0, stick = E)
                else:
                    if todecnextlinepass == 1 or todecnextlinename == 1:
                        try: #using "try" to avoid crashing upon failed decryption attempt
                            l = decrypt2(str(line), 0)
                            if todecnextlinename == 1:
                                todecnextlinename = 0
                                namesamount+=1
                                temptext = Text(frame_buttons, height = 1, width = 20)
                                temptext.insert(INSERT, str(l))
                                temptext.grid(row = i, column = 1)
                                def savenameinit(k, p):
                                    savename(k.get("1.0", "end"), p)
                                Button(frame_buttons, text = savenamebuttonlabel.get(), width = 15, command = lambda p = namesamount, k = temptext: savenameinit(k, p)).grid(row = i, column = 2)
                            elif todecnextlinepass == 1:
                                passesamount+=1
                                todecnextlinepass = 0
                                temptext = Entry(frame_buttons, width = 27)
                                temptext.insert(INSERT, str(l))
                                temptext.grid(row = i+1, column = 1)
                                temptext.config(show="*")
                                def savepassinit(k, p):
                                    savepass(k.get(), p)
                                def copypassinit(k):
                                    copypass(k.get())
                                showpassvar = IntVar()
                                def showpass(k, var):
                                    if var.get() == 0:
                                        k.config(show="")
                                        var.set(1)
                                    else:
                                        k.config(show="*")
                                        var.set(0)
                                Button(frame_buttons, text = savepassbuttonlabel.get(), width = 15, command = lambda p = passesamount, k = temptext: savepassinit(k, p)).grid(row = i+1, column = 2)
                                Button(frame_buttons, text = copypassbuttonlabel.get(), width = 15, command = lambda k = temptext: copypassinit(k)).grid(row = i+1, column = 3)
                                showbutton = Button(frame_buttons, text = showpassbuttonlabel.get(), width = 15, command = lambda k = temptext, var = showpassvar: showpass(k, var)).grid(row = i+1, column = 4)
                                i += 3
                        except: #show a decryption error in case of a failed decryption
                            failedwin()
                            return
        else:
            if passwarningopen.get() != 1:
                setpasswarning()
    refreshpasses()
    
    def areyousure(): #function to confirm user's actions
        areyousure = Toplevel(master)
        areyousure.config(bg='#bdbdbd')
        areyousure.resizable(width=False, height=False)
        label = Label(areyousure, text = "   ", bg='#bdbdbd').grid(row = 0, column = 0, stick = W)
        label = Label(areyousure, text = "   ", bg='#bdbdbd').grid(row = 1, column = 0, stick = W)
        yesbuttonlabel = StringVar()
        nobuttonlabel = StringVar()
        def finish():
            savepassesfile()
            areyousure.destroy()
        if curlang.get() == 0: #localization of the shown labels and buttons
            areyousure.title("Are you sure?")
            label = Label(areyousure, text = "Are you sure that you want to save the file?", bg='#bdbdbd').grid(row = 0, column = 1, stick = W)
            yesbuttonlabel.set("Yes")
            nobuttonlabel.set("NO")
        elif curlang.get() == 1: #localization of the shown labels and buttons
            areyousure.title("Вы уверены?")
            label = Label(areyousure, text = "Вы уверены что хотите сохранить файл?", bg='#bdbdbd').grid(row = 0, column = 1, stick = W)
            yesbuttonlabel.set("Да")
            nobuttonlabel.set("НЕТ")
        elif curlang.get() == 2: #localization of the shown labels and buttons
            areyousure.title("Είστε σίγουροι?")
            label = Label(areyousure, text = "Είστε σίγουροι ότι θέλετε να αποθηκεύσετε το αρχείο?", bg='#bdbdbd').grid(row = 0, column = 1, stick = W)
            yesbuttonlabel.set("Ναι")
            nobuttonlabel.set("ΟΧΙ")
        yes = Button(areyousure, text = yesbuttonlabel.get(), command = finish, width = 15, bg='lightgrey', borderwidth = 5).grid(row = 2, column = 2, stick = W) #defining the "Yes" button and it's properties and location
        no = Button(areyousure, text = nobuttonlabel.get(), command = areyousure.destroy, width = 15, bg='lightgrey', borderwidth = 5).grid(row = 2, column = 0, stick = W) #defining the "No" button and it's properties and location
    
    def changepassword():
        refreshpasses()
        setapass = Toplevel(master) #Creating new window with the name setapass >>
        setpasslabel = StringVar() #variable used for localization of the window's labels >>>
        confirmpasslabel = StringVar() #>>>
        setpassbuttonlabel = StringVar() #>>>
        setapass.config(bg='#bdbdbd') #>>
        def passclose(): #redefining window's close button function
            setpassopen.set(0) #setting to 0/closed
            setapass.destroy() #closing the window
        setapass.protocol("WM_DELETE_WINDOW", passclose) #redifining close button's function
        setapass.resizable(width=False, height=False) #>>
        setpassopen.set(1) #setting to 1/open
        warninglabel = StringVar() #variable for the warning label
        warninglabel.set("") #default warning - no warning
        mainframe = Frame(setapass, bg='#bdbdbd')
        mainframe.grid(row = 0)
        e = Entry(mainframe) #creating entry e for the first password field
        e2 = Entry(mainframe) #creating entry e2 for the second password field
        def areyousure2(): #function to confirm user's actions
            areyousure = Toplevel(master)
            areyousure.config(bg='#bdbdbd')
            areyousure.resizable(width=False, height=False)
            label = Label(areyousure, text = "   ", bg='#bdbdbd').grid(row = 0, column = 0, stick = W)
            label = Label(areyousure, text = "   ", bg='#bdbdbd').grid(row = 1, column = 0, stick = W)
            yesbuttonlabel = StringVar()
            nobuttonlabel = StringVar()
            def finish():
                complete()
                areyousure.destroy()
            if curlang.get() == 0: #localization of the shown labels and buttons
                areyousure.title("Are you sure?")
                label = Label(areyousure, text = "Are you sure that you want to change the password?", bg='#bdbdbd').grid(row = 0, column = 1, stick = W)
                yesbuttonlabel.set("Yes")
                nobuttonlabel.set("NO")
            elif curlang.get() == 1: #localization of the shown labels and buttons
                areyousure.title("Вы уверены?")
                label = Label(areyousure, text = "Вы уверены что хотите поменять пароль?", bg='#bdbdbd').grid(row = 0, column = 1, stick = W)
                yesbuttonlabel.set("Да")
                nobuttonlabel.set("НЕТ")
            elif curlang.get() == 2: #localization of the shown labels and buttons
                areyousure.title("Είστε σίγουροι?")
                label = Label(areyousure, text = "Είστε σίγουροι ότι θέλετε να αλλάξετε τον κωδικό?", bg='#bdbdbd').grid(row = 0, column = 1, stick = W)
                yesbuttonlabel.set("Ναι")
                nobuttonlabel.set("ΟΧΙ")
            yes = Button(areyousure, text = yesbuttonlabel.get(), command = finish, width = 15, bg='lightgrey', borderwidth = 5).grid(row = 2, column = 2, stick = W) #defining the "Yes" button and it's properties and location
            no = Button(areyousure, text = nobuttonlabel.get(), command = passclose, width = 15, bg='lightgrey', borderwidth = 5).grid(row = 2, column = 0, stick = W) #defining the "No" button and it's properties and location
        def complete():
            def areyousure2(password, newpassword):
                mainfile = open("Encrypted Password Storage.txt", "r+")
                lines = mainfile.readlines()
                print(lines)
                mainfile.close()
                mainfile = open("Encrypted Password Storage Temp.txt", "w+")
                mainfile.truncate(0)
                todecnextline = 0
                for line in lines:
                    if "Name:" in line:
                        todecnextline = 1
                        mainfile.write("Name: \n")
                    elif "Encrypted Password:" in line:
                        todecnextline = 1
                        mainfile.write("Encrypted Password:\n")
                    elif todecnextline == 1:
                        try:
                            k = decrypt(str(line), password)
                            todecnextline = 0
                            l = encrypt2(k, newpassword)
                            mainfile.write(str(l) + "\n")
                        except:
                            mainfile.close()
                            os.remove("Encrypted Password Storage Temp.txt")
                            failedwin()
                            return
                    else:
                        mainfile.write(line)
                mainfile.close()
                mainfile = open("Encrypted Password Storage Temp.txt", "r+")
                lines = mainfile.readlines()
                print(lines)
                mainfile.close()
                mainfile = open("Encrypted Password Storage.txt", "w+")
                mainfile.truncate(0)
                for line in lines:
                    mainfile.write(line)
                mainfile.close()
                successwin("Changed")
                os.remove("Encrypted Password Storage Temp.txt")
            if len(e.get()) != 0 and len(e2.get()) != 0: #check if the password entry is empty
                if e.get() == e2.get(): #if the two password fields are equal
                    temp = mypassword.get()
                    mypassword.set(e.get()) #get the password entry's contents
                    setpassopen.set(0) #confirm that the process is done and the window will be closed after this command
                    areyousure2(temp, mypassword.get())
                    e3.delete('1.0', "end")
                    e6.delete('1.0', "end")
                    e4.delete('1.0', "end")
                    e5.delete('1.0', "end")
                    recentrating.set(0)
                    if curlang.get() == 0:
                        passstrength.set("Strength: \n" + str(recentrating.get()))
                    elif curlang.get() == 1:
                        passstrength.set("Прочность: \n" + str(recentrating.get()))
                    elif curlang.get() == 2:
                        passstrength.set("Αντοχή: \n" + str(recentrating.get()))
                    encpass.set("")
                    setapass.destroy() #closing window after successful password entry
                else: #if the two password fields are not equal then show a warning in the correct language
                    if curlang.get() == 0:
                        warninglabel.set("The two passwords are not equal!")
                    elif curlang.get() == 1:
                        warninglabel.set("Пароли не совпадают!")
                    elif curlang.get() == 2:
                        warninglabel.set("Οι δύο κωδικοί είναι διαφορετικοί!")
            else: #if the password fields are empty then show a warning
                if curlang.get() == 0:
                    warninglabel.set("Password fields shouldn't be empty!")
                elif curlang.get() == 1:
                    warninglabel.set("Пароли не могут быть пустыми!")
                elif curlang.get() == 2:
                    warninglabel.set("Οι κωδικοί δεν μπορούν να είναι άδειοι!")
        if curlang.get() == 0: #localization of the shown labels
            setpasslabel.set("Set the new password:")
            setpassbuttonlabel.set("Change password")
            setapass.title("Set A New Password")
            confirmpasslabel.set("Confirm Password:")
            setapass.geometry("550x110")
        elif curlang.get() == 1:
            setpasslabel.set("Назначьте новый пароль:")
            setpassbuttonlabel.set("Сменить пароль")
            setapass.title("Сменить Пароль")
            confirmpasslabel.set("Введите еще раз:")
            setapass.geometry("560x110")
        elif curlang.get() == 2:
            setpasslabel.set("Βάλτε τον νέο κωδικό:")
            setpassbuttonlabel.set("Αλλαγή")
            setapass.title("Αλλαγή Κωδικού")
            confirmpasslabel.set("Άλλη μια φορά:")
            setapass.geometry("570x110")
        blanklabel = Label(mainframe, text = " ", bg='#bdbdbd').grid(row = 0) #used for the UI >>>>
        warnlabel = Label(setapass, textvariable = warninglabel, bg='#bdbdbd', fg = "red").grid(row = 3, stick = W)
        label = Label(mainframe, text = setpasslabel.get(), bg='#bdbdbd', font=("Sans Serif", 10, "bold")).grid(row = 1, stick = W)
        label = Label(mainframe, text = confirmpasslabel.get(), bg='#bdbdbd', font=("Sans Serif", 10, "bold")).grid(row = 2, stick = W)
        e.grid(row = 1, column = 1, stick = W) #setting the location of the first password field
        e2.grid(row = 2, column = 1, stick = W) #setting the location of the second password field
        e2.config(show="*") #hide entered password >
        e.config(show="*") #>
        blanklabel = Label(mainframe, text = "    ", bg='#bdbdbd').grid(row = 1, column = 2, stick = W) #>>>>
        setpass = Button(mainframe, text = setpassbuttonlabel.get(), command = areyousure2, width = 15, bg='lightgrey', borderwidth = 5, font=("Arial", 10, "bold")).grid(row = 2, column = 3, stick = W) #"Set Password" button definition
    refreshpassesbuttonlabel = StringVar()
    changepassbuttonlabel = StringVar()
    if curlang.get() == 0:
        refreshpassesbuttonlabel.set("Refresh")
        changepassbuttonlabel.set("Change Password")
    elif curlang.get() == 1:
        refreshpassesbuttonlabel.set("Обновить")
        changepassbuttonlabel.set("Сменить Пароль")
    elif curlang.get() == 2:
        refreshpassesbuttonlabel.set("Επαναφόρτωση")
        changepassbuttonlabel.set("Αλλαγή Κωδικού")
    refreshpassesbutton = Button(secframe, text = refreshpassesbuttonlabel.get(), width = 20, command = refreshpasses).grid(row = 0, column = 0)
    changepassbutton = Button(secframe, text = changepassbuttonlabel.get(), width = 20, command = changepassword).grid(row = 1, column = 0)


def openimp():
    impage = Toplevel(master)
    impage.config(bg='#bdbdbd')
    impage.resizable(width = False, height = False)
    if curlang.get() == 0:
        impage.title("Important Note")
        l10 = Label (impage, text = "IMPORTANT!!!!", font=("Courier", 18, "bold"), bg='#bdbdbd').grid(row = 0)
        l10 = Label (impage, text = "\n\nBackup the file to decrypt the passwords in the future!!!\nFile name:\nEncrypted Password Storage.txt\n\nIf you were using a version before v1.4 then, to transfer the passwords,\n just copy the decrypted passwords from saved passwords window\n and paste them into the saved passwords window of the new version!", font=("Courier", 12, "bold"), bg='#bdbdbd').grid(row = 1)
    elif curlang.get() == 1:
        impage.title("Важная Записка")
        l10 = Label (impage, text = "ВАЖНО!!!!", font=("Courier", 18, "bold"), bg='#bdbdbd').grid(row = 0)
        l10 = Label (impage, text = "\n\nСохраните этот файл чтобы расшифровать пароли в будущем!!!\nНазвание Файла:\nEncrypted Password Storage.txt\n\nЕсли вы пользовались версией до v1.4 тогда, чтобы перевести \nпароли в новую версию, просто скопируйте все расшифрованные пароли из\n старой версии и введите их в окно со сохраннеными паролями новой версии!", font=("Courier", 12, "bold"), bg='#bdbdbd').grid(row = 1)
    elif curlang.get() == 2:
        impage.title("Σημαντική Παρατήρηση")
        l10 = Label (impage, text = "ΣΗΜΑΝΤΙΚΟ!!!!", font=("Courier", 18, "bold"), bg='#bdbdbd').grid(row = 0)
        l10 = Label (impage, text = "\n\nΑποθηκεύστε σε ασφαλή μέρος το παρακάτω αρχείο\n για την αποκρυπτογράφηση των κωδικών σας στο μέλλον!!!\nΌνομα Αρχείου:\nEncrypted Password Storage.txt\n\nΕαν χρησιμοποιουσατε εκδοση του προγραμματος πριν το v1.4,\n τοτε για να μεταφερετε τους κωδικους θα πρεπει να αντιγραψετε\n τους αποκρυπτογραφημενους κωδικους του παλιου προγραμματος στο\n παραθυρο με τους αποθηκευμενους κωδικους της νεας εκδοσης!", font=("Courier", 12, "bold"), bg='#bdbdbd').grid(row = 1)
    
def openab():
    abpage = Toplevel(master)
    abpage.geometry("520x150")
    abpage.config(bg='#bdbdbd')
    abpage.resizable(width = False, height = False)
    if curlang.get() == 0:
        abpage.title("About us")
        l11 = Label(abpage, text="Made by inf2021221 & inf2021198 & inf2021119 for a \npython project at IONIO University of Informatics\n2021-2022\n\ngithub.com/maxiikk/passwordgenerator", font=("Courier", 13, "italic"), bg='#bdbdbd').grid(row = 0)
    elif curlang.get() == 1:
        abpage.title("О нас")
        abpage.geometry("760x150")
        l11 = Label(abpage, text="Эта программа создана совместно с inf2021221 & inf2021198 & inf2021119 ради \nпроекта по программированию в Ионическом Университете Информатики\n2021-2022\n\ngithub.com/maxiikk/passwordgenerator", font=("Courier", 13, "italic"), bg='#bdbdbd').grid(row = 0)
    elif curlang.get() == 2:
        abpage.title("Ποιοί Είμαστε")
        abpage.geometry("800x150")
        l11 = Label(abpage, text="Προγραμματισμένο ομαδικά από τους inf2021221 & inf2021198 & inf2021119 για μια \nεργασία προγραμματισμού στο τμήμα πληροφορηκής του Ιονίου Πανεπιστημίου\n2021-2022\n\ngithub.com/maxiikk/passwordgenerator", font=("Courier", 13, "italic"), bg='#bdbdbd').grid(row = 0)

about = Menu(menu, tearoff = 0)
lang = Menu(menu, tearoff = 0)
extraopt = Menu(menu, tearoff = 0)
changepasswordlabel = StringVar()
aboutuscaslabel = StringVar()
langlabel = StringVar()
savedpasslabel = StringVar()
aboutuslabel = StringVar()
importantlabel = StringVar()
viewsavedlabel = StringVar()
hidepassvar = IntVar()
passstrength = StringVar()
recentrating = IntVar()
recentrating.set(0)
def setenglish(): #localization to English
    curlang.set(0)
    master.title("Password Generator")
    master.geometry("580x290")
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
    aboutuscaslabel.set("About us")
    passstrength.set("Strength: \n" + str(int(recentrating.get())))
    langlabel.set("Language")
    savedpasslabel.set("Saved Passwords")
    if usingsimilarchars.get() == 0:
        extraopt.entryconfigure(0, label = "Include Similar Characters")
    elif usingsimilarchars.get() == 1:
        extraopt.entryconfigure(0, label = "Exclude Similar Characters")
    if usingambiguoussymbs.get() == 0:
        extraopt.entryconfigure(1, label = "Include Ambiguous Symbols")
    elif usingambiguoussymbs.get() == 1:
        extraopt.entryconfigure(1, label = "Exclude Ambiguous Symbols")
    aboutuslabel.set("About us")
    importantlabel.set("Important Note")
    viewsavedlabel.set("View Saved Passwords")

def setrussian(): #localization to Russian
    curlang.set(1)
    master.title("Генератор Паролей")
    master.geometry("670x290")
    yourpasswordislabel.set("Пароль: ")
    passwordnamelabel.set('Название Пароля')
    passwordlengthlabel.set('Размер Пароля')
    clearbuttonlabel.set("Очистить")
    decryptbutton.set("Расшифровать")
    generatebutton.set("[Сгенерировать]")
    about.entryconfigure(0, label = "Важная Записка")
    about.entryconfigure(1, label = "О нас")
    savedpasses.entryconfigure(0, label = "Просмотр Сохраненных Паролей")
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
    passstrength.set("Прочность: \n" + str(int(recentrating.get())))
    decryptedpasslabel.set("Расшифрованно: ")
    yourencpasswordlabel.set("Пароль в зашифрованном виде:")
    aboutuscaslabel.set("О нас")
    if usingsimilarchars.get() == 0:
        extraopt.entryconfigure(0, label = "Использовать Похожие Символы")
    elif usingsimilarchars.get() == 1:
        extraopt.entryconfigure(0, label = "Не Использовать Похожие Символы")
    if usingambiguoussymbs.get() == 0:
        extraopt.entryconfigure(1, label = "Использовать Двусмысленные Символы")
    elif usingambiguoussymbs.get() == 1:
        extraopt.entryconfigure(1, label = "Не Использовать Двусмысленные Символы")
    langlabel.set("Язык")
    savedpasslabel.set("Сохранненые Пароли")
    aboutuslabel.set("О нас")
    importantlabel.set("Важная Записка")
    viewsavedlabel.set("Посмотреть Сохранненые Пароли")

def setgreek(): #localization to Greek
    curlang.set(2)
    master.title("Γεννήτρια Κωδικών Πρόσβασης")
    master.geometry("630x290")
    yourpasswordislabel.set("Κωδικός Πρόσβασης: ")
    passwordnamelabel.set('Όνομα Κωδικού')
    passwordlengthlabel.set('Μέγεθος')
    decryptbutton.set("Αποκρυπτογράφηση")
    passstrength.set("Αντοχή: \n" + str(int(recentrating.get())))
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
    if usingsimilarchars.get() == 0:
        extraopt.entryconfigure(0, label = "Χρήση Παρόμοιων Χαρακτήρων")
    elif usingsimilarchars.get() == 1:
        extraopt.entryconfigure(0, label = "Μη-Χρήση Παρόμοιων Χαρακτήρων")
    if usingambiguoussymbs.get() == 0:
        extraopt.entryconfigure(1, label = "Χρήση Διφορούμενων Συμβόλων")
    elif usingambiguoussymbs.get() == 1:
        extraopt.entryconfigure(1, label = "Μη-Χρήση Διφορούμενων Συμβόλων")
    lowercheck.set("Μικρά Γράμματα")
    about.entryconfigure(0, label = "Σημαντική Παρατήρηση")
    about.entryconfigure(1, label = "Ποιοί είμαστε")
    savedpasses.entryconfigure(0, label = "Αποθηκεύμενοι Κωδικοί")
    encryptedpasslabel.set("Κρυπτογραφημένος: ")
    decryptedpasslabel.set("Αποκρυπτογραφημένος: ")
    yourencpasswordlabel.set("Κρυπτογραφημένος Κωδικός:")
    aboutuscaslabel.set("Ποιοί Είμαστε")
    langlabel.set("Γλώσσα")
    savedpasslabel.set("Αποθηκευμένοι Κωδικοί")
    aboutuslabel.set("Ποιοί Είμαστε")
    importantlabel.set("Σημαντική Παρατήρηση")
    viewsavedlabel.set("Άνοιγμα Αποθηκευμένων Κωδικών")


def usesimilarchars():
    if usingsimilarchars.get() == 1:
        usingsimilarchars.set(0)
        if curlang.get() == 0:
            extraopt.entryconfigure(0, label = "Include Similar Characters")
        elif curlang.get() == 1:
            extraopt.entryconfigure(0, label = "Использовать Похожие Символы")
        elif curlang.get() == 2:
            extraopt.entryconfigure(0, label = "Χρήση Παρόμοιων Χαρακτήρων")
    elif usingsimilarchars.get() == 0:
        usingsimilarchars.set(1)
        if curlang.get() == 0:
            extraopt.entryconfigure(0, label = "Exclude Similar Characters")
        elif curlang.get() == 1:
            extraopt.entryconfigure(0, label = "Не Использовать Похожие Символы")
        elif curlang.get() == 2:
            extraopt.entryconfigure(0, label = "Μη-Χρήση Παρόμοιων Χαρακτήρων")
def useambiguoussymbs():
    if usingambiguoussymbs.get() == 1:
        usingambiguoussymbs.set(0)
        if curlang.get() == 0:
            extraopt.entryconfigure(1, label = "Include Ambiguous Symbols")
        elif curlang.get() == 1:
            extraopt.entryconfigure(1, label = "Использовать Двусмысленные Символы")
        elif curlang.get() == 2:
            extraopt.entryconfigure(1, label = "Χρήση Διφορούμενων Συμβόλων")
    elif usingambiguoussymbs.get() == 0:
        usingambiguoussymbs.set(1)
        if curlang.get() == 0:
            extraopt.entryconfigure(1, label = "Exclude Ambiguous Symbols")
        elif curlang.get() == 1:
            extraopt.entryconfigure(1, label = "Не Использовать Двусмысленные Символы")
        elif curlang.get() == 2:
            extraopt.entryconfigure(1, label = "Μη-Χρήση Διφορούμενων Συμβόλων")
aboutuscaslabel.set("About us")
changepasswordlabel.set("Set Password")
langlabel.set("Language")
savedpasslabel.set("Saved Passwords")
aboutuslabel.set("About us")
importantlabel.set("Important Note")
viewsavedlabel.set("View Saved Passwords")
menu.add_cascade(label = "About us", menu = about)
menu.add_cascade(label = "Language", menu = lang)
lang.add_command(label = 'English', command = setenglish)
lang.add_command(label = 'Русский', command = setrussian)
lang.add_command(label = 'Ελληνικά', command = setgreek)
savedpasses = Menu(menu, tearoff = 0)
menu.add_cascade(label = "Saved Passwords", menu = savedpasses)
menu.add_cascade(label = "Extra Generation Options", menu = extraopt)
extraopt.add_command(label = "Exclude Similar Characters", command = usesimilarchars)
extraopt.add_command(label = "Exclude Ambiguous Symbols", command = useambiguoussymbs)
savedpasses.add_command(label=viewsavedlabel.get(), command = openpasses)
about.add_command(label=importantlabel.get(), command = openimp)
about.add_command(label=aboutuslabel.get(), command = openab)
decpass = StringVar()
encpass = StringVar()
yourpasswordislabel = StringVar()
yourpasswordislabel.set("Your Password is: ")
l2 = Label(secframe, textvariable = yourpasswordislabel, bg='#bdbdbd').grid(row = 4, column = 0, stick = E)
passstrength.set("Strength: \n0")
l00 = Label(secframe, textvariable = passstrength, bg= '#bdbdbd', font=("Arial", 10, "bold")).grid(row = 4, column = 5, stick = W)
yourencpasswordlabel = StringVar()
yourencpasswordlabel.set("Your Password in encrypted format:")
l3 = Label(secframe, textvariable = yourencpasswordlabel, anchor = 'w', bg='#bdbdbd').grid(row = 5, column = 0, ipadx = 1, stick = E)
blank = Label(secframe, text = " ", anchor=W, bg='#bdbdbd').grid(row = 3, column = 2, ipadx = 1, stick = W)
decryptedpasslabel = StringVar()
decryptedpasslabel.set("Decrypted: ")
l5 = Label(secframe, textvariable = decryptedpasslabel, bg='#bdbdbd').grid(row = 9, column = 0, ipadx = 1, stick = E)
encryptedpasslabel = StringVar()
encryptedpasslabel.set("Encrypted: ")
l10 = Label(secframe, textvariable = encryptedpasslabel, bg='#bdbdbd').grid(row = 6, column = 0, ipadx = 1, stick = E)
e3 = Text(secframe, width = 20, borderwidth = 2, bg='lightgrey', height = 2) #Encrypted Password Entry
e3.grid(row = 6, column = 1, stick = W)
e4 = Text(secframe, width = 20, borderwidth = 2, bg='lightgrey', height = 2) #Your Password is Entry
e4.grid(row= 4, column = 1, stick = W)
e5 = Text(secframe, width = 20, borderwidth = 2, bg='lightgrey', height = 2) #Decrypted Password Entry
e5.grid(row= 9, column = 1, stick = W)
e6 = Text(secframe, width = 20, borderwidth = 2, bg='lightgrey', height = 2) #Password in encrypted format entry
e6.grid(row= 5, column = 1, stick = W)

def ratepass (passtorate): #function for rating generated passwords
    rating = 0 #starting value for the rating
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
    recentrating.set(int(rating))
    return int(rating)

def generate (o, symbsbase): #main function for generating passwords
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
    l = encrypt(l)
    encpass.set(l)
    e6.insert(INSERT, l)
    encpass2 = ""

def gen (s, n, u, l): #initialization of the main function for generating passwords
    symbs = []
    sym = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', '=', '?', '[', ']', '{', '}', '/', '\\', ";", ":", ".", "~", "`", "<", ">", ',']
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
    
    if usingsimilarchars.get() == 0:
        if n == 1 and l == 1 and u == 1:
            symbs.remove('0')
            symbs.remove('o')
            symbs.remove('O')
            symbs.remove('l')
            symbs.remove('L')
            symbs.remove('i')
            symbs.remove('1')
            symbs.remove('j')
            symbs.remove('I')
        elif l == 1 and u == 1:
            symbs.remove('o')
            symbs.remove('O')
            symbs.remove('l')
            symbs.remove('L')
            symbs.remove('i')
            symbs.remove('j')
            symbs.remove('I')
    
    if usingambiguoussymbs.get() == 0 and s == 1:
        symbs.remove('[')
        symbs.remove(']')
        symbs.remove('(')
        symbs.remove(')')
        symbs.remove('{')
        symbs.remove('}')
        symbs.remove('<')
        symbs.remove('>')
        symbs.remove('`')
        symbs.remove('.')
        symbs.remove(';')
        symbs.remove(':')
        symbs.remove('/')
        symbs.remove('\\')
        symbs.remove('~')
        symbs.remove(',')
    generate(int(e2.get()), symbs)

def savetofile (passname, passtosave): #saving the generated passwords to the encrypted password storage file when the button "Save" is clicked
    if len(passtosave) != 0: #save only if there is a password and not an empty field to avoid unwanted behaviour
        file = open("Encrypted Password Storage.txt", "a")
        l = encrypt(passname)
        file.write("\nName: \n" + l + "\nEncrypted Password:\n" + str(passtosave))
        file.write("\n")
        file.close()

def decrypt2 (todec, mode = 0): #function for decrypting passwords
    todec = todec.encode().decode('unicode_escape').encode("raw_unicode_escape")
    def remove_bytes(buffer, start, end): #function to remove unecessary symbols after converting string to bytes format
        fmt = '%ds %dx %ds' % (start, end-start, len(buffer)-end)
        return b''.join(struct.unpack(fmt, buffer))
    todec = remove_bytes(todec, (len(todec)-1), (len(todec)))
    cipher = AES_Encryption(key=mypassword.get(), iv = 'dsfgsjklcvb45eso')
    decr = cipher.decrypt(todec)
    decr = str(decr)
    if mode == 1: #two modes for returning the decrypted password and refreshing the decrypted password field in the main window
        e5.delete('1.0',"end") #emptying the decrypted password field
        e5.insert(INSERT, str(decr)) #setting the decrypted password to the decrypted password field
    else:
        return str(decr)

def copy2 (passtocopy): #copying the decrypted password to clipboard
    clip.copy(str(passtocopy.replace("\n", "")))

def hidepassword(): #function for hiding the generated and decrypted password fields
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
def dothis(): #checking if all the requirements are met before running the initialization of the password generation
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

def clearencpass(): #function for clearing the encrypted-for-decryption password field for convinience
    e3.delete('1.0', "end")

passwordnamelabel = StringVar()
passwordnamelabel.set('Password Name')
Label(mainframe, textvariable = passwordnamelabel, bg='#bdbdbd', font=("Arial", 10, "bold")).grid(row=0, ipadx = 1, stick = W)
passwordlengthlabel = StringVar()
passwordlengthlabel.set('Length')
Label(mainframe, textvariable = passwordlengthlabel, bg='#bdbdbd', font=("Arial", 10, "bold")).grid(row=1, ipadx = 1, stick = W)
e1 = Entry(mainframe, bg='lightgrey') #Entry for the password name
e1.insert(0, "Test")
e2 = Entry(mainframe, bg='lightgrey') #Entry for the password length
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
hidepassbutton = Button(secframe, textvariable = hidepassbuttonlabel, command = hidepassword, bg='lightgrey', borderwidth = 5).grid(row = 4, column = 4, ipadx = 1, stick = W)
clearbutton = Button (secframe, textvariable = clearbuttonlabel, command = clearencpass, bg='lightgrey', borderwidth = 5).grid(row = 6, column = 4, ipadx = 1, stick = W)
b2 = Button(secframe , textvariable = savebutton, command = lambda: savetofile(str(e1.get()), str(encpass.get())), bg='lightgrey', borderwidth = 5).grid(row = 5, column = 3, ipadx = 1, stick = W)
b5 = Button(secframe , textvariable = copybutton, command = lambda: copy2(str(encpass.get())), bg='lightgrey', borderwidth = 5).grid(row = 5, column = 4, ipadx = 1, stick = W)
b3 = Button(secframe, textvariable = decryptbutton, command = lambda: decrypt2(e3.get("1.0","end"), 1), bg='lightgrey', borderwidth = 5).grid(row = 6, column = 3, ipadx = 1, stick = W)
b4 = Button(secframe, textvariable = copybutton, command = lambda: copy2(str(e5.get("1.0","end"))), bg='lightgrey', borderwidth = 5).grid(row = 9, column = 3, ipadx = 1, stick = W)
b6 = Button(secframe, textvariable = copybutton, command = lambda: copy2(str(e4.get("1.0","end"))), bg='lightgrey', borderwidth = 5).grid(row = 4, column = 3, ipadx = 1, stick = W)
b1 = Button(mainframe, textvariable = generatebutton, command = dothis, bg='lightgreen', borderwidth = 5, font=("Arial", 10, "bold")).grid(row=1, column=3, ipadx = 1, stick = W)
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
Checkbutton(mainframe, textvariable =symbolscheck, variable=var1, anchor = 'w', bg='#bdbdbd', font=("Arial", 10, "bold")).grid(row=3, column = 1, ipadx = 1, stick = W) #checkbuttons for the symbols that the user has to choose whether to include in the newly generated password >>>>
Checkbutton(mainframe, textvariable=numberscheck, variable=var2, anchor = 'w', bg='#bdbdbd', font=("Arial", 10, "bold")).grid(row=3, column = 0, ipadx = 1, stick = W) #>>>>
Checkbutton(mainframe, textvariable=uppercheck, variable=var3, anchor = 'w', bg='#bdbdbd', font=("Arial", 10, "bold")).grid(row=2, column = 0, ipadx = 1, stick = W) #>>>>
Checkbutton(mainframe, textvariable=lowercheck, variable=var4, anchor = 'w', bg='#bdbdbd', font=("Arial", 10, "bold")).grid(row=2, column = 1, ipadx = 1, stick = W) #>>>>
setpassword() #running the setpassword() function after everything is defined and works correctly
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

Needed modules for python:
    1.wheel
    2.pyperclip
    3.AES-Encryptor
    4.pycryptodome

Version: 1.6



MIT License

Copyright (c) 2022 MaxiiKK

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
