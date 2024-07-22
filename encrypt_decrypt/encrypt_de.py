from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)

#encryption
pss = b"mypassword"
encrypted_pss = cipher_suite.encrypt(pss)
print(encrypted_pss.decode())   # .decode removes b before the string from the string that is converted to binary

#decrypt
decrypted_pss = cipher_suite.decrypt(encrypted_pss)
print(decrypted_pss.decode())
