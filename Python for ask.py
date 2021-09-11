print("Selamat datang ke sistem untuk mengira bil elektrik kepada 2 bulan")
print("Sistem ini akan mengira bil elektrik kepada 2 bulan dan harga KWTBB serta harga service tax")
kWh=int(input("Sila masukkan blok tarif (kWH) yang digunakan kepada bulan 1: "))
if kWh<=200:
    bil=(kWh*0.218)*1.016
    print("Harga bil elektrik anda kepada bulan 1 ialah:RM",round(bil,2))
elif kWh<=300:
    bil=(200*0.218)+((kWh-200)*0.334)*1.016
    bilb1=round(bil,2)
    print("Harga bil elektrik anda kepada bulan 1 ialah:RM",round(bil,2))
elif kWh<=600:
    bil=(200*0.218)+(100*0.334)+((kWh-300)*0.516)*1.016
    bilb1=round(bil,2)
    print("Harga bil elektrik anda kepada bulan 1 ialah:RM",round(bil,2))
else:
    bil=(200*0.218)+(100*0.334)+(300*0.516)+((kWh-600)*0.546)*1.016*1.06
    print("Harga bil elektrik anda kepada bulan 1 ialah:RM",round(bil,2))
    ServiceTax=float(bil*6/100)
    print("Service Tax telah dicaj kerana penggunaan blok tarif telah melebihi 600")
    print("Harga Service Tax ialah (Harga 6% daripada harga bil elektrik)")
    print("Harga Service Tax anda kepada bulan 1 ialah:RM",round(ServiceTax,2))
KWTBB=float(bil*1.6/100)
print("Harga KWTBB ialah (Harga 1.6% daripada harga bil elektrik)")
print("Harga KWTBB anda kepada bulan 1 ialah:RM",round(KWTBB,2))
kWh2=int(input("Sila masukkan blok tarif (kWh) yang digunakan kepada bulan 2: "))
if kWh2<=200:
    bil2=(kWh2*0.218)
    print("Harga bil elektrik anda kepada bulan 1 ialah:RM",round(bil,2))
elif kWh2<=300:
    bil2=(200*0.218)+(kWh2-200)*0.334
    print("Harga bil elektrik anda kepada bulan 1 ialah:RM",round(bil,2))
elif kWh2<=600:
    bil2=(200*0.218)+(100*0.334)+(kWh2-300)*0.516
    print("Harga bil elektrik anda kepada bulan 1 ialah:RM",round(bil,2))
else:
    bil2=(200*0.218)+(100*0.334)+(300*0.516)+((kWh2-600)*0.546)*1.06
    print("Harga bil elektrik anda kepada bulan 1 ialah:RM",round(bil,2))
    ServiceTax=float(bil*6/100)
    print("Service Tax telah dicaj kerana penggunaan blok tarif telah melebihi 600")
    print("Harga Service Tax ialah (Harga 6% daripada harga bil elektrik)")
    print("Harga Service Tax anda kepada bulan 2 ialah:RM",round(ServiceTax,2))
KWTBB=float(bil*1.6/100)
print("Harga KWTBB ialah (Harga 1.6% daripada harga bil elektrik)")
print("Harga KWTBB anda kepada bulan 2 ialah:RM",round(KWTBB,2))
jumlah=bil+bil2
print("Jumlah harga bil elektrik anda kepada 2 bulan ialah:RM",round(jumlah,2))
print("Terima Kasih kerana menggunakan sistem ini.")


