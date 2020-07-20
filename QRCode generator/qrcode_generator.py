import sys
import qrcode

def main():
    data = "I am Learning How to create QRCode."

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5,
    )

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", black_color="white")

    img.save("my_qrcode.png")


if __name__ == "__main__":
    sys.exit(main())