import qrcode  # Import the qrcode library to generate QR codes


def generate_qr(data, filename='qrcode.png'):
    # Create a QRCode object with configuration
    qr = qrcode.QRCode(
        # Controls the size of the QR code (1 to 40). Version 1 is the smallest.
        version=1,
        # Error correction level L (up to 7% error can be corrected)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Size of each individual box (pixel size)
        border=4,  # Width of the border (measured in box_size units)
    )

    qr.add_data(data)  # Add the input data (text or URL) to the QR code
    qr.make(fit=True)  # Adjust the size automatically based on content

    # Create the QR code image with color settings
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)  # Save the image to a file
    print(f"QR Code saved successfully! Filename: {filename}")


# Run this part only when executing the script directly (not when importing)
if __name__ == "__main__":
    text = input("Enter the text or URL to convert into a QR Code: ")
    generate_qr(text)
