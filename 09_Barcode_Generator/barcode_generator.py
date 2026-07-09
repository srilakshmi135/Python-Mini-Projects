import barcode
from barcode.writer import ImageWriter

print("===== Barcode Generator =====")

data = input("Enter number or text for barcode: ")

if data.strip() == "":
    print("Input cannot be empty.")

else:
    code = barcode.get(
        "code128",
        data,
        writer=ImageWriter()
    )

    filename = code.save("barcode")

    print("\nBarcode generated successfully!")
    print("Saved as:", filename + ".png")