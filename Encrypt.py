import cv2

def encrypt_message(Image, Output, msg, password):
    img = cv2.imread(Image)
    d = {chr(i): i for i in range(255)}
    
    n, m, z = 0, 0, 0
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n += 1
        m += 1
        z = (z + 1) % 3

    cv2.imwrite(Output, img)
    return len(msg), password  

Image = "Image1.png"  
Output = "encryptedImage.png"
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

msg_length, stored_password = encrypt_message(Image, Output, msg, password)


with open("config.txt", "w") as f:
    f.write(f"{msg_length}\n{stored_password}")
