import qrcode

data = input("Enter website or text: ")

img = qrcode.make(data)

img.save("my_qrcode.png")

print("QR Code generated successfully!")
