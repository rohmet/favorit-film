# main.py
import presentation_layer as ui

def main():
    while True:
        print("\n=== SISTEM FILM FAVORIT ===")
        print("1. Lihat Daftar Film Favorit")
        print("2. Tambah Film Favorit")
        print("3. Ubah Informasi Film")
        print("4. Hapus Film")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == '1':
            ui.tampilkan_film()
        elif pilihan == '2':
            ui.menu_tambah_film()
        elif pilihan == '3':
            ui.menu_ubah_film()
        elif pilihan == '4':
            ui.menu_hapus_film()
        elif pilihan == '5':
            print("\nTerima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            
if __name__ == "__main__":
    main()