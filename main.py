import qrcode
from PIL import Image
import random
import os
import urllib.parse

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate high contrast fill and back colors
    def generate_contrasting_colors():
        while True:
            fill_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            back_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if contrast_ratio(fill_color, back_color) > 4.5:  # WCAG recommended contrast ratio
                return fill_color, back_color

    def contrast_ratio(color1, color2):
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        lum1 = 0.2126 * r1 + 0.7152 * g1 + 0.0722 * b1
        lum2 = 0.2126 * r2 + 0.7152 * g2 + 0.0722 * b2
        if lum1 > lum2:
            return (lum1 + 0.05) / (lum2 + 0.05)
        else:
            return (lum2 + 0.05) / (lum1 + 0.05)

    fill_color, back_color = generate_contrasting_colors()
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(os.path.join(os.getcwd(), filename))

if __name__ == "__main__":
    link = input("Enter the link: ")
    filename = f"qr_code_{urllib.parse.quote_plus(link)}.png"
    generate_qr_code(link, filename)


