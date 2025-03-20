import qrcode # type: ignore

def generate_simple_qr(data, filename="output/simple_qr_code.png"):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    data = input("Enter the data to encode in the QR code: ")
    generate_simple_qr(data)