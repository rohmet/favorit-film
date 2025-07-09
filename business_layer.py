# business_layer.py

import data_layer

def get_films():
    """Mendapatkan daftar semua film."""
    return data_layer.get_all_films()

def add_new_film(judul, tahun):
    """
    Memvalidasi dan menambahkan film baru.
    Mengembalikan (True, "Pesan Sukses") atau (False, "Pesan Error").
    """
    if not judul:
        return False, "Judul tidak boleh kosong!"
    
    try:
        tahun_int = int(tahun)
        film_baru = {"judul": judul, "tahun": tahun_int}
        data_layer.add_film(film_baru)
        return True, f"Film '{judul}' berhasil ditambahkan!"
    except ValueError:
        return False, "Tahun rilis harus berupa angka!"

def update_existing_film(nomor, judul_baru, tahun_baru_str):
    """
    Memvalidasi dan memperbarui film yang ada.
    Mengembalikan (True, "Pesan Sukses") atau (False, "Pesan Error").
    """
    index = nomor - 1
    total_films = len(get_films())
    
    if not (1 <= nomor <= total_films):
        return False, "Nomor film tidak valid."

    film_to_update = data_layer.get_film_by_index(index).copy()

    if judul_baru:
        film_to_update['judul'] = judul_baru
    
    if tahun_baru_str:
        try:
            film_to_update['tahun'] = int(tahun_baru_str)
        except ValueError:
            return False, "Tahun rilis baru harus berupa angka!"

    data_layer.update_film_by_index(index, film_to_update)
    return True, "Data film berhasil diperbarui."

def delete_film(nomor):
    """
    Memvalidasi dan menghapus film.
    Mengembalikan (True, "Pesan Sukses") atau (False, "Pesan Error").
    """
    index = nomor - 1
    total_films = len(get_films())

    if not (1 <= nomor <= total_films):
        return False, "Nomor film tidak valid."
        
    film_yang_dihapus = data_layer.delete_film_by_index(index)
    if film_yang_dihapus:
        return True, f"Film '{film_yang_dihapus['judul']}' berhasil dihapus."
    return False, "Gagal menghapus film."