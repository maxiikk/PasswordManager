
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

![pythonw_MRQIMFojyR](https://user-images.githubusercontent.com/85651296/192152795-88982530-a328-486d-80a8-ba793b009a2f.jpg)
![pythonw_qLS6a3Mudb](https://user-images.githubusercontent.com/85651296/192152799-8de4ca1b-f7d0-4277-9c64-1cc3ca76daac.jpg)
