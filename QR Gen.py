import qrcode
import time
from PIL import Image


<<<<<<< HEAD
link = "http://127.0.0.1:3000/index1.html"
=======
link = "www.google.com"
>>>>>>> b7e051be1b93e594cdcd8668ecd23e802de6ebad

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
    img.save("qrcode.png")

# Generate and display QR codes every 5 seconds
try:
    while True:
        generate_qr_code(link)
        time.sleep(1)
except KeyboardInterrupt:
    print("QR code generation stopped.")
