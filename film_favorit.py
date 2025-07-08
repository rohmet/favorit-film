film_favorit = [
    {"judul": "Interstellar", "tahun": 2014},
    {"judul": "Spirited Away", "tahun": 2001}
]

def tampilkan_film():
    print("\n--- Daftar Film Favorit ---")
    if not film_favorit:
        print("Belum ada film favorit.")
        return
    
    print(f"{'No.':<5} | {'Judul Film':<30} | {'Tahun':<5}")
    print("-" * 45)
    for i, film in enumerate(film_favorit):
        print(f"{i+1:<5} | {film['judul']:<30} | {film['tahun']}")

def tambah_film():
    print("\n--- Tambah Film Favorit ---")
    judul = input("Judul film: ").strip()
    if not judul:
        print("Judul tidak boleh kosong!")
        return
    
    try:
        tahun = int(input("Tahun rilis: "))
        film_baru = {"judul": judul, "tahun": tahun}
        film_favorit.append(film_baru)
        print(f"Film '{judul}' berhasil ditambahkan!")
    except ValueError:
        print("Tahun rilis harus berupa angka!")

def ubah_film():
    print("\n--- Ubah Informasi Film ---")
    tampilkan_film()
    if not film_favorit:
        return
    
    try:
        nomor = int(input("Pilih nomor film yang ingin diubah (0 untuk batal): "))
        if nomor == 0:
            print("Perubahan dibatalkan.")
            return
        if 1 <= nomor <= len(film_favorit):
            film = film_favorit[nomor - 1]
            judul_baru = input(f"Judul baru untuk '{film['judul']}' (tekan enter jika tidak ingin mengubah): ")
            tahun_baru = input(f"Tahun rilis baru ({film['tahun']}): ")

            if judul_baru:
                film['judul'] = judul_baru
            if tahun_baru:
                film['tahun'] = int(tahun_baru)

            print("Data film berhasil diperbarui.")
        else:
            print("Nomor film tidak valid.")
    except ValueError:
        print("Input tidak valid!")

def hapus_film():
    print("\n--- Hapus Film Favorit ---")
    tampilkan_film()
    if not film_favorit:
        return

    try:
        nomor = int(input("Pilih nomor film yang ingin dihapus (0 untuk batal): "))
        if nomor == 0:
            print("Penghapusan dibatalkan.")
            return
        if 1 <= nomor <= len(film_favorit):
            film = film_favorit.pop(nomor - 1)
            print(f"Film '{film['judul']}' berhasil dihapus.")
        else:
            print("Nomor film tidak valid.")
    except ValueError:
        print("Input harus berupa angka!")

def main():
    while True:
        print("\n=== SISTEM FILM FAVORIT ===")
        print("1. Lihat Daftar Film Favorit")
        print("2. Tambah Film Favorit")
        print("3. Ubah Informasi Film")
        print("4. Hapus Film") # Opsi menu baru dari Rizka
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == '1':
            tampilkan_film()
        elif pilihan == '2':
            tambah_film()
        elif pilihan == '3':
            ubah_film()
        elif pilihan == '4': # Pilihan baru ditambahkan
            hapus_film()
        elif pilihan == '5':
            print("\nTerima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            
if __name__ == "__main__":
    main()