from Encryptor import AES_Encryption
import struct
#needed modules: pycryptodome and AES-Encryptor
mypassword = StringVar()
mypassword.set("apassword")

def encrypt(k):
    cipher = AES_Encryption(key=mypassword.get(), iv = 'dsfgsjklcvb45eso') #create the cipher for the encryption
    enc = cipher.encrypt(k) #encrypt with the password
    enc = str(enc) #convert from bytes to string
    l = "" #temporary variable to contain the encrypted password for the '' to be removed
    o = 0 #temporary variable used to track the position in the string
    for b in enc: #process for removing the b'' from the string for a more friendly look
        if o != 0 and o != 1 and o != (len(enc)-1):
            l += b
        o += 1
    return l



def decrypt2(todec): #function for decrypting passwords
    todec = todec.encode().decode('unicode_escape').encode("raw_unicode_escape")
    def remove_bytes(buffer, start, end): #function to remove unecessary symbols after converting string to bytes format
        fmt = '%ds %dx %ds' % (start, end-start, len(buffer)-end)
        return b''.join(struct.unpack(fmt, buffer))
    todec = remove_bytes(todec, (len(todec)-1), (len(todec)))
    cipher = AES_Encryption(key=mypassword.get(), iv = 'dsfgsjklcvb45eso')
    decr = cipher.decrypt(todec)
    decr = str(decr)
    return decr