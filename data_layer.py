# data_layer.py

# Data store (sumber data), dibuat "private" dengan underscore
_film_favorit = [
    {"judul": "Interstellar", "tahun": 2014},
    {"judul": "Spirited Away", "tahun": 2001}
]

def get_all_films():
    """Mengembalikan semua data film."""
    return _film_favorit

def add_film(film):
    """Menambahkan satu film ke dalam data store."""
    _film_favorit.append(film)

def get_film_by_index(index):
    """Mengambil satu film berdasarkan indeksnya."""
    if 0 <= index < len(_film_favorit):
        return _film_favorit[index]
    return None

def update_film_by_index(index, updated_film):
    """Memperbarui film pada indeks tertentu."""
    if 0 <= index < len(_film_favorit):
        _film_favorit[index] = updated_film
        return True
    return False

def delete_film_by_index(index):
    """Menghapus film dari data store berdasarkan indeks."""
    if 0 <= index < len(_film_favorit):
        return _film_favorit.pop(index)
    return None