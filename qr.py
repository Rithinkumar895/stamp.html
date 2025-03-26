import qrcode

# ✅ Replace this with your actual hosted URL
hosted_url = "https://github.com/Rithinkumar895/stamp.html.git"

# Generate QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(hosted_url)
qr.make(fit=True)

# Create and save QR code image
qr_image = qr.make_image(fill="black", back_color="white")
qr_image.save("verified_stamp_qr.png")

print(f"✅ QR Code generated successfully! URL: {hosted_url}")
