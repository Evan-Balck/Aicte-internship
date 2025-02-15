import cv2

def decrypt_message(Image, Length, password, original_password):
    img = cv2.imread(Image)
    c = {i: chr(i) for i in range(255)}

    message = ""
    n, m, z = 0, 0, 0

    if password == original_password:
        for i in range(Length):
            message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3
        print("Decryption message:", message)
    else:
        print("YOU ARE NOT AUTHORIZED")

Image = "encryptedImage.png"


with open("config.txt", "r") as f:
    Length, stored_password = f.read().splitlines()
    Length = int(Length)

pas = input("Enter passcode for Decryption: ")
decrypt_message(Image, Length, pas, stored_password)
