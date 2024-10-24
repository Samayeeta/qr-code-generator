import qrcode

data = input("Enter URL: ").strip()
file_name = input("Enter filename (without extension): ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)

image = qr.make_image(fill_color='black', back_color='white')

file_name_with_extension = f"{file_name}.png"
image.save(file_name_with_extension)

print(f'QR code saved as {file_name_with_extension}')