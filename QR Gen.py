import qrcode
import time
from PIL import Image


link = "https://example.com"

# Function to generate and display a QR code
def generate_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Display the QR code image
    img.save("QR.png")

# Generate and display QR codes every 5 seconds
try:
    while True:
        generate_qr_code(link)
        time.sleep(5)
except KeyboardInterrupt:
    print("QR code generation stopped.")
