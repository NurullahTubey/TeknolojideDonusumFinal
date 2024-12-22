
import json

def ogrenci_verilerini_al():
    # Öğrenci sayısını sor
    ogrenci_sayisi = int(input("Kaç öğrenci var? "))
    
    ogrenciler = []
    
    # Öğrenciler için verileri al
    for i in range(ogrenci_sayisi):
        print(f"\n{i+1}. Öğrencinin bilgilerini girin:")
        isim = input("Öğrencinin ismini girin: ")
        vize = float(input("Vize notunu girin: "))
        final = float(input("Final notunu girin: "))
        
        # Ortalama hesapla
        ortalama = (vize * 0.4) + (final * 0.6)
        
        # Öğrenci verilerini bir sözlük olarak ekle
        ogrenciler.append({
            'isim': isim,
            'vize': vize,
            'final': final,
            'ortalama': ortalama
        })
    
    # Öğrenci verilerini JSON dosyasına kaydet
    with open("ogrenci_notlari.json", "w") as dosya:
        json.dump(ogrenciler, dosya, indent=4)
    
    print("\nÖğrenci verileri başarıyla kaydedildi!")

# Fonksiyonu çalıştır
ogrenci_verilerini_al()
