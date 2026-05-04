import pyzipper

def create_encrypted_zip(zip_name, file_to_zip, content, password):
    with pyzipper.AESZipFile(zip_name, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(password.encode('utf-8'))
        zf.writestr(file_to_zip, content)
    print(f"File {zip_name} created with password: {password}")

if __name__ == "__main__":
    create_encrypted_zip('secret.zip', 'message.txt', 'Bravo, tu as casse le code !', 'penguin')
