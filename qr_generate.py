import qrcode
import sys

#   print usage
if len(sys.argv) == 1:
    print("Usage: qr_generate.py [QR code text] [filename]")
    sys.exit()

#   if one argument has been supplied, then it will be used both as information contained in the QR code
#   and filename + .svg

text = sys.argv[1]
#   if two arguments are supplied then the second argument will be used as a filename + .svg
if len(sys.argv) == 2:
    file_name = text + ".svg"
else:
    file_name = sys.argv[2] + ".svg"

#generating qrcode image
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(text)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="transparent")
img.save(file_name)

print("QR code saved as:", file_name)

