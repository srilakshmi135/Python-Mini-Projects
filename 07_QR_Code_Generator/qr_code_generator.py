import qrcode

print("===== QR Code Generator =====")

data = input("Enter text or URL: ")

if data.strip() == "":
    print("Input cannot be empty.")
else:
    img = qrcode.make(data)
    img.save("my_qrcode.png")

    print("\nQR Code generated successfully!")
    print("Saved as my_qrcode.png")