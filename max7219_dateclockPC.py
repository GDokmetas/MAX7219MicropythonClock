# written by Gökhan Dökmetaş
# Veriler daima 8 baytlık çerçevede gönderilecek!

import serial
import time
from datetime import datetime
ser = serial.Serial("COM10", "9600", timeout=0, parity=serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE , bytesize = serial.EIGHTBITS, rtscts=0)

# Hata ayıklama için.
ser.write("000000--".encode('Ascii'))

while True:
    tarihsaat = str(datetime.now())
    tarih = tarihsaat[8:10] + "-" + tarihsaat[5:7] + "-" + tarihsaat[2:4]
    for i in range(80):
        saat = str(datetime.now())
        saat_yazdir = saat[11:13] + "." + saat[14:16] + "." + saat[17:19]
        print(saat_yazdir)
        ser.write(saat_yazdir.encode('Ascii'))
        time.sleep(0.1)
    print(saat)
    ser.write(tarih.encode('Ascii'))
    time.sleep(2)

    
