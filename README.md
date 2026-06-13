# FirsNovavisionPackages

Bu paket, Novavision altyapısı üzerinde çalışan iki farklı işlem birimine (Executor) ve dinamik konfigürasyon yeteneklerine sahip bir demo paketidir.

## 🚀 Özellikler ve Kurallar

### 1. İşlem Birimleri (Executors)
* **FirstExecutor:** Tek bir metin girişi (`in1`) alır ve işlem sonucunda tek bir metin çıktısı (`out1`) üretir.
* **SecondExecutor:** Daha karmaşık senaryolar için bir metin (`in1`) ve bir sayı girişi (`in2`) alıp, iki farklı veri tipinde çıktı (`out1`, `out2`) üretir.

### 2. Dinamik Yapılandırma (Dynamic Configuration)
* Paket içeriğinde `dependentDropdown` mimarisi kullanılmıştır.
* Kullanıcılar seçtikleri opsiyona (`Secenek1` veya `Secenek2`) göre farklı veri giriş alanları (metin veya sayı) arasında dinamik geçiş yapabilirler.
* Her bir dropdown seçeneği kendi içinde 2 farklı tipte alana (`TextField` ve `NumberField`) bağlıdır.
