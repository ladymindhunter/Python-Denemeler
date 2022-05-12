from datetime import datetime

import datetime

doğum_tarihi=int(input("Doğum yılınızı giriniz: "))

şuan=datetime.datetime.now()

gün=şuan.day
ay=şuan.month
yıl=şuan.year
saat=şuan.hour
dakika=şuan.minute
saniye=şuan.second

print(f"{gün}/{ay}/{yıl} {saat}:{dakika}:{saniye}", f"itibariyle {yıl-doğum_tarihi} yaşındasınız!")
