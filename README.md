# 🎬 Akıllı Sinema İçerik Öneri Asistanı
**Mamdani Bulanık Mantık ve Streamlit Tabanlı Reaktif Karar Destek Sistemi**

---

## 📌 Proje Hakkında Genel Bakış

Bu proje, Mersin Üniversitesi Bilişim Sistemleri ve Teknolojileri Bölümü mezuniyet projesi kapsamında geliştirilmiştir. Günümüz dijital yayıncılık ekosisteminde kullanıcıların karşılaştığı içerik seçme karmaşasını (content paralysis) ve karar verme güçlüğünü, insan düşünce yapısına en yakın matematiksel model olan **Bulanık Mantık (Fuzzy Logic)** ile çözen akıllı bir asistan uygulamasıdır.

Geleneksel "katı" filtreleme sistemlerinin aksine (Örn: "IMDb puanı 7.5'ten küçükse önerme"), bu asistan 13 farklı sinematik ve bağlamsal parametreyi "gri alanlarda" işleyerek doğrusal olmayan, esnek ve insani muhakeme yeteneğine sahip reaktif öneriler üretir.

---

## 🛠️ Sistem Mimarisi ve Karar Motoru Operasyonel Akışı

Projenin kalbi olan Mamdani Bulanık Mantık mimarisi, dört ana aşamadan oluşan entegre bir akış matrisi ile çalışmaktadır:

> 🖼️ **Görsel: Sistem Operasyonel Akış Şeması**
> <img width="1861" height="958" alt="image" src="https://github.com/user-attachments/assets/ea351891-7dad-4d3d-acbf-90dd34fbb012" />

> ![Sistem Mimarisi Operasyonel Akış Matrisi]([BURAYA_image_5.png_LINKINI_EKLE])

### 1. Giriş Parametreleri ve Bulanıklaştırma (Fuzzification)
Sistem, kullanıcının Kontrol Paneli üzerinden belirlediği **13 sayısal girdiyi** işler. Bu girdiler, evrensel küme aralıklarında tanımlanmış `trimf (üçgen)` ve `trapmf (yamuk)` üyelik fonksiyonları kullanılarak dilsel üyelik derecelerine dönüştürülür.

**Kullanılan Temel Girdi Katmanları:**
1.  **Tür Eşleşme Oranı:** Kullanıcının moduyla içeriğin uyumu.
2.  **IMDb Puanı:** Küresel kalite tescili.
3.  **Trend Skoru:** Anlık popülarite rüzgarı.
4.  **Hassas İçerik Yoğunluğu (+18):** Ailece izleme güvenliği.
5.  **Dil ve Çeviri Uyumu:** Sert engelleyici (Veto) parametresi.
6.  **Senaryo Özgünlük Derecesi:** Sanatsal özgünlük ile endüstriyel formüllerin ayrımı.
7.  **(Ve 7 diğer parametre...)**
<img width="1852" height="913" alt="image" src="https://github.com/user-attachments/assets/9cacbd60-2f96-4c58-ac93-f4c0ae414f5b" />

> 🖼️ **Görsel: Girdi Değişkenleri ve Üyelik Fonksiyonları Canlı Simülasyonu**
> ![Girdi Değişkenleri Grafik Matrisi]([BURAYA_image_3.png_LINKINI_EKLE])

### 2. Çıkarım Motoru ve 27 Akıllı Kural
Sinematik ve bağlamsal uzman bilgisini temsil eden **27 adet harmanlanmış kural**, Mamdani çıkarım yöntemi doğrultusunda `MIN (ve)` mantıksal operatörü kullanılarak anlık olarak ateşlenir. Kurallar, "Gizli Hazine", "Bayram Modu" veya "Kritik Veto" gibi karmaşık senaryoları yönetir.
<img width="1747" height="802" alt="image" src="https://github.com/user-attachments/assets/ad79179d-51b8-43c1-86bb-2f3442cee823" />

### 3. Birleştirme (Aggregation)
Aktif hale gelen tüm kuralların ürettiği kısmi bulanık çıktı alanları, `MAX (veya)` operatörüyle süzülerek tek bir nihai bulanık çıktı kümesi alanına indirgenir.

### 4. Durulaştırma (Defuzzification)
Oluşan nihai bulanık çıktı alanının geometrik **Ağırlık Merkezi (Centroid Metodu)** entegral tabanlı hesaplanarak, %0 ile %100 arasında net (crisp) bir içerik öneri uygunluk skoruna dönüştürülür.

> 🖼️ **Görsel: Nihai Çıktı Kümesi ve Centroid Durulaştırma Noktası Grafik Çıktısı**
> ![Çıkış Değişkeni Grafik Alanı]([BURAYA_image_4.png_LINKINI_EKLE])
<img width="1501" height="634" alt="image" src="https://github.com/user-attachments/assets/45370741-742c-4065-a1a0-3cd5bb168f88" />

---

## 📲 Uygulama Özellikleri ve Akademik Test Senaryoları

Uygulama, Python ve Streamlit kullanılarak geliştirilmiş premium koyu tema tabanlı, reaktif ve lüks bir kullanıcı arabirimine sahiptir. Jürinin sistemi test edebilmesi için gelişmiş akademik senaryolar Kontrol Paneline entegre edilmiştir.

### Parametre Kontrol Paneli
Kullanıcıların 13 farklı değişkeni ve 27 kuralın aktivasyon durumunu anlık ısı haritası tablosuyla izleyebileceği interaktif alan.
<img width="470" height="901" alt="image" src="https://github.com/user-attachments/assets/4630dd71-641e-4de7-8d1d-aba1160dba49" />
<img width="535" height="848" alt="image" src="https://github.com/user-attachments/assets/0d4e7292-2583-4e08-ad4c-75e5972d60e1" />

> 🖼️ **Görsel: Reaktif Parametre Kontrol Paneli**


### Öne Çıkan Akademik Test Senaryoları
* **🏆 Kült Başyapıt:** Tüm kalite parametrelerinin zirvede olduğu ideal durum testi.
* **🍬 Bayram Modu (Geniş Aile):** Yeşilçam sıcaklığında, risksiz ve bütçe dostu aile içerikleri filtresi.
* **🎬 Gizli Hazine:** Popülaritesi düşük ama kalitesi ve özgünlüğü zirvede olan underrated yapıtlar keşfi.
* **🛑 Kritik Veto (Hard Constraint):** Dil uyumu eksikliği gibi sert engelleyicilerin, diğer 12 parametre zirvede olsa bile sistemi "Önerilmez" bölgesine kilitleme testi.

---

## 💻 Kurulum ve Çalıştırma

Projenin yerel bilgisayarınızda çalıştırılabilmesi için aşağıdaki adımları takip edebilirsiniz:

1.  **Depoyu Klonlayın:**
    ```bash
    git clone [https://github.com/KULLANICI_ADIN/akilli-sinema-asistani.git](https://github.com/KULLANICI_ADIN/akilli-sinema-asistani.git)
    cd akilli-sinema-asistani
    ```

2.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Uygulamayı Başlatın:**
    ```bash
    streamlit run app.py
    ```

---
**Geliştirici:** Mersin Üniversitesi Bilişim Sistemleri ve Teknolojileri Bölümü Öğrencisi.
