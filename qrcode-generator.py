import qrcode

url = input("Input URL: ")
file_path = "" # write file path

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code generated")
