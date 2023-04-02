# fungsi untuk menghitung total biaya
def hitung_biaya(jumlah_tiket, harga_tiket):
    total_biaya = jumlah_tiket * harga_tiket
    return total_biaya

# method untuk meminta input jumlah tiket
def masukkan_jumlah_tiket():
    while True:
        jumlah_tiket = input("Masukkan jumlah tiket yang dibeli: ")
        try:
            jumlah_tiket = int(jumlah_tiket)
            if jumlah_tiket <= 0:
                print("Jumlah tiket harus lebih besar dari 0.")
            else:
                return jumlah_tiket
        except ValueError:
            print("Input harus berupa bilangan bulat.")

# method untuk meminta input jenis tiket
def pilih_jenis_tiket():
    while True:
        jenis_tiket = input("Pilih jenis tiket (reguler/vip/vvip): ")
        if jenis_tiket in harga_tiket:
            return jenis_tiket
        else:
            print("Jenis tiket tidak tersedia.")

# program utama
print("Selamat datang di Aplikasi Pembelian Tiket")

# daftar harga tiket
harga_tiket = {
    "reguler": 20000,
    "vip": 50000,
    "vvip": 100000
}

# meminta input jenis tiket
jenis_tiket = pilih_jenis_tiket()

# meminta input jumlah tiket
jumlah_tiket = masukkan_jumlah_tiket()

# menghitung total biaya dan mencetak hasilnya
total_biaya = hitung_biaya(jumlah_tiket, harga_tiket[jenis_tiket])
print("Total biaya yang harus dibayar adalah Rp", total_biaya)

# konfirmasi pembelian
while True:
    konfirmasi = input("Apakah Anda yakin ingin membeli tiket ini? (y/n): ")
    if konfirmasi.lower() == 'y':
        print("Pembelian berhasil!")
        break
    elif konfirmasi.lower() == 'n':
        print("Pembelian dibatalkan.")
        break
    else:
        print("Input tidak valid.")