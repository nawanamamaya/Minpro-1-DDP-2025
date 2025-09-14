print("Nama    : Rija Aulia Mayatri")
print("NIM     : 2509116011")
print("Kelas   : Sistem Informasi (A)")
print("Program : Sistem Daftar Makanan")
print("-" * 31)



resep_makanan = input("Masukkan nama resep makanan:")

kategori_makanan = ["Makanan Utama, Snack, Dessert, Minuman"]
print("-" * 40)
print("Makanan Utama = 1")
print("Snack         = 2")
print("Dessert       = 3")    
print("Minuman       = 4")    
print("-" * 40)

pilih = int(input("\nPilih kategori makanan anda : "))
if pilih == 1:
    print("\nKategori = Makanan Utama")
elif pilih == 2: 
    print("Kategori = Snack")
elif pilih == 3:
    print("Kategori = Dessert")
elif pilih == 4:
    print("Kategori = Minuman")
else:
    print("Pilihan tidak valid")

bahan_makanan = input("\nBahan makanan yang digunakan : ")
peralatan = input("\nPeralatan yang digunakan :")
langkah_pembuatan = input("\nLangkah pembuatan : ")

# Konfirmasi resep
print("\n" + "-" * 40)
print("Ringkasan resep:")
print(f"Nama Resep                : {resep_makanan}")
print(f"Kategori Makanan          : {pilih}")
print(f"Bahan-bahan               : {bahan_makanan}")
print(f"Peralatan                 : {peralatan}")
print(f"Langkah-langkah Pembuatan : {langkah_pembuatan}")
print("\n" + "-" * 40)

konfirmasi = input("\nApakah resep anda sudah benar? (ketik Ya/Tidak):")

if konfirmasi == "Ya":
    print("Resep berhasil disimpan")
    print("\nTerima kasih karna sudah membagikan resep anda :)")
else:
    print("\nBagian mana yang ingin diubah?")
    print("1. Nama Resep")
    print("2. Kategori Makanan")
    print("3. Bahan-bahan")
    print("4. Peralatan")
    print("5. Langkah-langkah Pembuatan")
    mengedit = int(input("\nMasukkan pilihan [nomor 1-" \
    "5]:"))
    if mengedit == 1:
        resep_makanan = input("\nMasukkan nama resep makanan:")
    elif mengedit == 2:
        print("Makanan Utama = 1")
        print("Snack         = 2")
        print("Dessert       = 3")    
        print("Minuman       = 4") 
        pilih = int(input("\nPilih kategori makanan anda : "))
        if pilih == 1:
            print("\nKategori = Makanan Utama")
        elif pilih == 2: 
            print("\nKategori = Snack")
        elif pilih == 3:
             print("\nKategori = Dessert")
        elif pilih == 4:
             print("\nKategori = Minuman")
        else:
            print("\nPilihan tidak valid")
    elif mengedit == 3:
        bahan_makanan = input("\nBahan makanan yang digunakan : ")
    elif mengedit == 4:
        peralatan = input("\nPeralatan yang digunakan :")
    elif mengedit == 5:
        langkah_pembuatan = input("\nLangkah pembuatan : ")
    else:
        print("\nAnda salah memasukkan nomor, tolong pilih antara 1-5")
    print("\nPerubahan berhasil disimpan")
    print("\n" + "-" * 40)
    print("Hasil perubahan resep:")
    print(f"Nama Resep                : {resep_makanan}")
    print(f"Kategori Makanan          : {pilih}")
    print(f"Bahan-bahan               : {bahan_makanan}")
    print(f"Peralatan                 : {peralatan}")
    print(f"Langkah-langkah Pembuatan : {langkah_pembuatan}")
    print("\n" + "-" * 40)
    print("\nTerima kasih karna sudah membagikan resep anda ♡︎")

print("\n=====Selesai=====")






