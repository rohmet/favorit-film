# presentation_layer.py

import business_layer

def tampilkan_film():
    print("\n--- Daftar Film Favorit ---")
    films = business_layer.get_films()
    if not films:
        print("Belum ada film favorit.")
        return
    
    print(f"{'No.':<5} | {'Judul Film':<30} | {'Tahun':<5}")
    print("-" * 45)
    for i, film in enumerate(films):
        print(f"{i+1:<5} | {film['judul']:<30} | {film['tahun']}")

def menu_tambah_film():
    print("\n--- Tambah Film Favorit ---")
    judul = input("Judul film: ").strip()
    tahun = input("Tahun rilis: ")
    
    sukses, pesan = business_layer.add_new_film(judul, tahun)
    print(pesan)

def menu_ubah_film():
    print("\n--- Ubah Informasi Film ---")
    tampilkan_film()
    if not business_layer.get_films():
        return
        
    try:
        nomor_str = input("Pilih nomor film yang ingin diubah (0 untuk batal): ")
        nomor = int(nomor_str)
        if nomor == 0:
            print("Perubahan dibatalkan.")
            return

        film_lama = business_layer.get_films()[nomor - 1]
        judul_baru = input(f"Judul baru untuk '{film_lama['judul']}' (tekan enter jika tidak ingin mengubah): ").strip()
        tahun_baru = input(f"Tahun rilis baru ({film_lama['tahun']}) (tekan enter jika tidak ingin mengubah): ").strip()
        
        sukses, pesan = business_layer.update_existing_film(nomor, judul_baru, tahun_baru)
        print(pesan)

    except (ValueError, IndexError):
        print("Input tidak valid atau nomor film tidak ditemukan.")

def menu_hapus_film():
    print("\n--- Hapus Film Favorit ---")
    tampilkan_film()
    if not business_layer.get_films():
        return

    try:
        nomor_str = input("Pilih nomor film yang ingin dihapus (0 untuk batal): ")
        nomor = int(nomor_str)
        if nomor == 0:
            print("Penghapusan dibatalkan.")
            return

        sukses, pesan = business_layer.delete_film(nomor)
        print(pesan)
    except ValueError:
        print("Input harus berupa angka!")