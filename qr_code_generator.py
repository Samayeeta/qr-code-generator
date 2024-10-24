import qrcode
from PIL import Image

def content_type():
    print("Choose the content type:")
    print("1. URL")
    print("2. Text")
    print("3. Email")
    print("4. Phone Number")
    
    while True:
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            return input("Enter the URL: ").strip()
        elif choice == '2':
            return input("Enter the text: ").strip()
        elif choice == '3':
            email = input("Enter the email: ").strip()
            if "@" in email:  
                return f"mailto:{email}"
            else:
                print("Invalid email format. Please try again.")
        elif choice == '4':
            phone = input("Enter the phone number: ").strip()
            if phone.isdigit():  
                return f"tel:{phone}"
            else:
                print("Invalid! Please enter digits only.")
        else:
            print("Invalid! Please select a number between 1 and 4.")

def view_qr_code(file_path):
    try:
        Image.open(file_path).show()  
    except Exception as e:
        print(f"Unable to open image: {e}")

def create_qr_code():
    data = content_type()
    file_name = input("Enter filename (do not add an extension): ").strip()
    
    while True:
        file_format = input("Enter your preferred file format (png, jpg, bmp): ").strip().lower()
        if file_format in ['png', 'jpg', 'bmp']:
            break
        else:
            print("Invalid file format. Please enter png, jpg, or bmp.")
    
    fill_color = input("Enter the fill color (default: black): ").strip() or 'black'
    back_color = input("Enter the bg color (default: white): ").strip() or 'white'
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    file_name_with_extension = f"{file_name}.{file_format}"
    image.save(file_name_with_extension)
    print(f'QR code saved as {file_name_with_extension}')
    
    view = input("Do you want to view the code now? (y/n): ").lower().strip()
    if view == 'y':
        view_qr_code(file_name_with_extension)

if __name__ == "__main__":
    while True:
        create_qr_code()
        cont = input("Do you want to create another QR code? (y/n): ").lower().strip()
        if cont == 'n':
            print("Thanks for using the generator!")
            break
