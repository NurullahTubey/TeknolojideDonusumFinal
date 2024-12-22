import json

# JSON dosyasını kaydetme fonksiyonu
def save_to_json(data, filename="ogrenci_notlari.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# JSON dosyasını yükleme fonksiyonu
def load_from_json(filename="ogrenci_notlari.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Öğrenci bilgilerini güncelleme veya silme fonksiyonu
def ogrenci_bilgisi_islemleri():
    ogrenciler = load_from_json()

    if not ogrenciler:
        print("Kayıtlı öğrenci bulunmamaktadır.")
        return

    ad = input("Bilgilerini görüntülemek istediğiniz öğrencinin adını girin: ").strip()  # Boşlukları temizle
    ogrenci_bulundu = False

    for ogrenci in ogrenciler:
        if ogrenci["isim"].strip().lower() == ad.lower():  # Hem girdi hem de JSON'daki isimi temizle
            ogrenci_bulundu = True
            print("\nÖğrenci Bilgileri:")
            print(f"Ad: {ogrenci['isim']}")
            print(f"Vize: {ogrenci['vize']}")
            print(f"Final: {ogrenci['final']}")
            print(f"Ortalama: {ogrenci['ortalama']}")

            print("\n1. Notları güncelle")
            print("2. Öğrenciyi sil")
            print("3. Geri dön")
            secim = input("Seçiminizi yapın: ")

            if secim == "1":
                try:
                    vize = float(input(f"{ogrenci['isim']} için yeni vize notunu girin: "))
                    final = float(input(f"{ogrenci['isim']} için yeni final notunu girin: "))
                    ortalama = round((vize * 0.4) + (final * 0.6), 2)

                    ogrenci["vize"] = vize
                    ogrenci["final"] = final
                    ogrenci["ortalama"] = ortalama

                    save_to_json(ogrenciler)
                    print("Notlar başarıyla güncellendi!")
                except ValueError:
                    print("Lütfen geçerli bir sayı girin.")

            elif secim == "2":
                ogrenciler.remove(ogrenci)
                save_to_json(ogrenciler)
                print("Öğrenci başarıyla silindi!")

            elif secim == "3":
                print("Ana menüye dönülüyor...")
            else:
                print("Geçersiz seçim.")
            break

    if not ogrenci_bulundu:
        print("Aradığınız isimde bir öğrenci bulunamadı.")

# Ana program
ogrenciler = load_from_json()  # Önceki veriler varsa yükle

while True:
    print("\n1. Yeni öğrenci ekle")
    print("2. Kayıtlı öğrencileri göster")
    print("3. Öğrenci bilgilerini düzenle veya sil")
    print("4. Çıkış")
    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        try:
            ogrenci_sayisi = int(input("Kaç öğrenci eklemek istiyorsunuz? "))
            for _ in range(ogrenci_sayisi):
                ad = input("Öğrencinin adını girin: ")
                vize = float(input(f"{ad} için vize notunu girin: "))
                final = float(input(f"{ad} için final notunu girin: "))
                ortalama = round((vize * 0.4) + (final * 0.6), 2)

                ogrenciler.append({
                    "isim": ad,        # JSON'daki "isim" anahtarı kullanılıyor
                    "vize": vize,      # JSON'daki "vize" anahtarı kullanılıyor
                    "final": final,    # JSON'daki "final" anahtarı kullanılıyor
                    "ortalama": ortalama
                })

            save_to_json(ogrenciler)  # Yeni verileri JSON dosyasına kaydet
            print("Öğrenciler başarıyla kaydedildi!")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    elif secim == "2":
        if not ogrenciler:
            print("Kayıtlı öğrenci bulunmamaktadır.")
        else:
            print("\nKayıtlı Öğrenciler:")
            print("{:<20} {:<10} {:<10} {:<10}".format("isim", "vize", "final", "ortalama"))
            print("-" * 50)
            for ogrenci in ogrenciler:
                print("{:<20} {:<10} {:<10} {:<10}".format(ogrenci["isim"], ogrenci["vize"], ogrenci["final"], ogrenci["ortalama"]))

    elif secim == "3":
        ogrenci_bilgisi_islemleri()

    elif secim == "4":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Lütfen geçerli bir seçenek girin.")
