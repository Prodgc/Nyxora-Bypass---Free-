import random

# Rastgele görünmeyen olmayan Unicode karakteri oluşturan fonksiyon
def generate_random_unicode():
    # Özel karakter aralıkları
    unicode_ranges = [
        (0x0020, 0x007F),  # Latin harfleri ve rakamlar
        (0x00A0, 0x00FF),  # Latin genişletilmiş
        (0x2000, 0x206F),  # Punctuation and symbols
    ]
    
    # Rastgele bir aralık seç
    chosen_range = random.choice(unicode_ranges)
    
    # Aralıktan rastgele bir karakter seç
    random_unicode = random.randint(chosen_range[0], chosen_range[1])
    
    # Unicode karakterini döndür
    return chr(random_unicode)

# Rastgele Unicode karakterini iki parantez içinde yazdır
print(f"({generate_random_unicode()})")
