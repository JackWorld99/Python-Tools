import pyqrcode

qr = pyqrcode.create('https://www.youtube.com/')
qr.png('QRCODE.png', scale = 8)