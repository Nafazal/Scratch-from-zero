print("="*30)
print("KALKULATOR".center(30))
print("="*30)

def hitung(a, b, operator):
            if operator == "+":
                return a + b
            elif operator == "-":
                return a-b
            elif operator == "*":
                return a*b
            elif operator == "/":
                if b != 0:
                    return a / b
                else:
                    return "Tidak bisa membagi dengan nol!"
            else:
                return "Operator salah"

while True:
    print("\nMenu:")
    print("\nA. Hitung")
    print("B. Keluar")
    pilihan=input("Pilih menu:")
    print("\n")
    print("-"*30)

    if pilihan.lower() == "a":
        print("\n")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")
        print("\n")
        menu = int(input("pilih operator: "))
        if menu == 1:
            operator = "+"
        elif menu == 2:
            operator = "-"
        elif menu == 3:
            operator = "*"
        elif menu == 4:
            operator = "/"
        elif menu == 5:
            continue
        else:
            print("Menu tidak tersedia")
            continue
        print("-"*30)
        a = float(input("Masukan angka pertama: "))
        b = float(input("Masukan angka kedua: "))

        hasil = hitung(a, b, operator)
        print("-"*30)
        print("HASIL".center(30))
        print("-"*30)
        print(f"{a} {operator} {b} = {hasil}")
        print("-"*30)
    
    elif pilihan.lower() == "b":
        print("Selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")
