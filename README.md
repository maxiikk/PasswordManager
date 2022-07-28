
This is a simple and secure app that uses AES encryption to encrypt and decrypt your passwords, it is fully offline and requires the following libraries to work (**if you run the python script and not the standalone version which has the .exe extension**):
  1. AES-Encryptor
  2. pyperclip
  3. pycryptodome

Open your command prompt (not the python idle!) and type **pip install packagename** where packagename is the name of each of the above libraries (type the names exactly as shown above)

What can this app do?
  1. Hide your decrypted passwords on the main screen
  2. Copy to clipboard
  3. Change the password that your password-vault is encrypted with
  4. Choose between 3 languages (Russian, Greek, English)
  5. Decrypt passwords from another vault with the same password
  6. Add new passwords to the vault by typing them manually the same way as the program saves the generated passwords
  7. Delete passwords from the vault manually and save the changes to the vault
  8. Exclude ambiguous symbols and similar symbols
  9. Get a rating for the generated password

Plans:
  1. Implement a "Trash" system (im thinking about using vault versioning and finding the parts that have been deleted after making changes and saving the vault)
  2. Show statistics about how many passwords are saved in the vault and how many of them are weak
  3. Add an option to generate a passphrase from a dictionary


Current state of the app:

![pythonw_NsJWZp0jkO](https://user-images.githubusercontent.com/85651296/176317071-14683008-b538-4902-aadc-a66931336dad.png)
![PasswordGeneratorWithGUI_v1 8_uHBiMgYkLo](https://user-images.githubusercontent.com/85651296/181611776-3c7cd5d4-1914-4273-84fd-7904714d4fd8.png)


If you have any questions or suggestions, ill be here to help
