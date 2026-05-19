# 🎬 Akıllı Sinema Asistanı: Bulanık Mantık Tabanlı İçerik Öneri Sistemi

**T.C. MERSİN ÜNİVERSİTESİ** **Bilişim Sistemleri ve Teknolojileri Anabilim Dalı**

| Akademik Kimlik Bilgileri | Tanımlamalar ve Değerler |
| :--- | :--- |
| **Öğrencinin Adı ve Soyadı** | [cite_start]Simge Gündoğdu [cite: 2] |
| **Danışmanın Unvanı, Adı ve Soyadı** | Öğr. Gör. [cite_start]HÜSEYİN YANIK [cite: 2] |
| **Bitirme Projesi Başlığı** | [cite_start]Akıllı Sinema Asistanı: Bulanık Mantık Tabanlı İçerik Öneri Sistemi [cite: 2] |
| **Rapor Tarihi** | [cite_start]21 / 05 / 2026 [cite: 1] |

---

## 1. GİRİŞ VE PROBLEM TANIMI

### 1.1. Projenin Amacı ve Önemi
[cite_start]Gelişen internet altyapısı ve dijital dönüşüm süreçleri, eğlence ve yayıncılık sektöründe devasa bir veri hacmi (Big Data) meydana getirmiştir[cite: 5]. [cite_start]Günümüzde kullanıcılar, binlerce içerik arasından kendi kişisel beklentilerine, bütçelerine, sosyo-kültürel bağlamlarına ve anlık zihinsel durumlarına en uygun filmi seçerken "içerik felci" (content paralysis) ve karar verme güçlüğü yaşamaktadır[cite: 6].

[cite_start]Bu projenin amacı; kullanıcıların karşılaştığı bu çok kriterli karmaşık karar verme problemini, insan muhakeme yeteneğine ve düşünce yapısına en yakın matematiksel model olan **Mamdani Bulanık Mantık (Fuzzy Logic) Karar Destek Sistemi** mimarisiyle çözmektir[cite: 7]. [cite_start]Geliştirilen "Akıllı Sinema Asistanı", klasik algoritmaların aksine kullanıcıları tek bir izleme döngüsüne hapsetmez[cite: 8]. [cite_start]İçeriğin sanatsal kalitesini, finansal erişilebilirliğini, dil senkronizasyonunu ve anlık bağlamsal senaryoları tek bir reaktif matriste eriterek doğrusal olmayan, esnek ve akıllı bir öneri mekanizması sunar[cite: 9].

### 1.2. Problemin Genel Tanımı
[cite_start]Günümüz dijital yayıncılık platformlarında kullanılan mevcut öneri motorları, genellikle İşbirlikçi Filtreleme (Collaborative Filtering) veya İçerik Tabanlı Filtreleme (Content-Based Filtering) yöntemlerine dayanmaktadır[cite: 11]. [cite_start]Bu sistemlerin temel yapısal kusuru, kararları keskin sınırlarla (crisp boundaries) ayıran ikili mantık (Boolean 0-1) mimarisiyle çalışmalarıdır[cite: 12]. [cite_start]Klasik ilişkisel veritabanı sorguları (SELECT / WHERE komutları) veya doğrusal kod blokları, bir veriyi ya tamamen kümenin içinde ya da tamamen dışında kabul eder[cite: 13].

[cite_start]Ancak insan tercihleri doğası gereği muğlak (fuzzy) yapılardan oluşur[cite: 14]. [cite_start]Bir filmin popülerliğinin az olması onun mutlak anlamda kötü olduğu anlamına gelmediği gibi, kullanıcıların zihinsel yorgunluk ve sosyal ortam kısıtları da matematiksel olarak katı sınırlarla (If-Else yapılarıyla) ifade edilemez[cite: 14]. [cite_start]Klasik sistemlerin bu esneklikten uzak yapısı, öneri kalitesinde tıkanmalara ve kullanıcı memnuniyetsizliğine yol açmaktadır[cite: 15].

### 1.3. 13 Girdi Parametresi Odağında Geleneksel Yöntemlerin Yetersizlikleri
[cite_start]Projemizde modellenen 13 girdi parametresi özelinde, geleneksel ikili (binary) sistemlerin yaşadığı matematiksel ve mantıksal yetersizlikler şu şekildedir[cite: 17]:

* [cite_start]**Tür Eşleşme Oranı (tur_eslesme):** Klasik sistemler bir filmi katı etiketlerle sınıflandırır[cite: 18]. [cite_start]Oysa bir yapım %70 oranında Bilim Kurgu, %30 oranında Dram barındabilir[cite: 19]. [cite_start]Doğrusal sistemler bu semantik melez ağırlıkları hesaplayamadığı için kullanıcının anlık moduna uyan esnek geçişleri kaçırır[cite: 20].
* **IMDb Puanı (imdb):** Veritabanı mantığında bir eşik değeri (Örn: 7.5) belirlendiğinde, 7.4 puanlı bir şaheser ile 4.0 puanlı başarısız bir film aynı potada eritilerek doğrudan elenir[cite: 21]. Yaşanan bu "uçurum etkisi" (cliff-edge effect) sistemin esnekliğini yok eder[cite: 22].
* [cite_start]**Trend Skoru (trend):** Popülariteyi sadece "en çok izlenen ilk 10" gibi listelerle yöneten klasik algoritmalar; popülaritesi yeni yükselmekte olan niş bir bağımsız yapım ile rüzgarı tamamen geçmiş eski bir gişe filmi arasındaki geçiş sürecini ifade edemez[cite: 23, 24].
* [cite_start]**Olumlu Yorum Oranı (yorum_orani):** Duygu analizi çıktılarında %51 olumlu ile %49 olumlu yorum alan iki film, doğrusal sistemlerde "başarılı" ve "başarısız" olarak iki zıt kutba ayrılır[cite: 25]. [cite_start]İnsan algısında ise bu iki değer de "kararsız/karışık" eleştiriler anlamına gelir[cite: 26].
* [cite_start]**Erişilebilirlik ve Maliyet (maliyet):** Klasik filtreler bütçeyi sadece "Ücretli/Ücretsiz" olarak böler[cite: 27]. [cite_start]Kullanıcının sahip olduğu platform abonelikleri veya kiralama esneklikleri ancak bulanık kümelerin sunduğu geçiş dereceleriyle anlamlandırılabilir[cite: 28].
* [cite_start]**Dil ve Çeviri Uyumu (dil_uyumu):** Doğrusal yapılar, altyazı kalitesindeki en ufak eksiklikte veya dublaj senkronizasyon başarısında içeriği doğrudan "Yetersiz" sayarak eler[cite: 29]. [cite_start]Bulanık mantık ise dil desteğinin "kısmen yeterli" olduğu durumları algılayarak karara esnek bir ağırlık katar[cite: 30].
* [cite_start]**Hassas İçerik Yoğunluğu (hassas_icerik):** Ailece izleme ortamlarında katı "+18 yaş sınırı" kuralları yetersiz kalır[cite: 31]. [cite_start]Çünkü bir korku filminin barındırdığı şiddet veya korku derecesi doğrusal bir tetikleyici değil, derece derece artan bir rahatsızlık katsayısıdır[cite: 32].
* [cite_start]**Yerlilik Oranı (yerlilik):** Uluslararası ortak yapımlar, yabancı aktörlerin oynadığı yerli senaryolar klasik sistemlerde "Yerli: Evet/Hayır" şeklinde kodlanır[cite: 33]. [cite_start]Kültürel yakınlık hissinin ölçülebilmesi için parametrenin hibrit derecelere bölünmesi şarttır[cite: 34].
* [cite_start]**Fragman Etkileşim Gücü (fragman_gucu):** Bir tanıtım videosunun sosyal medyadaki rüzgarı ya "viral" ya da "etkisiz" olarak etiketlenir[cite: 35]. [cite_start]Oysa izleyicide uyanan merak ve beklenti duygusu doğrusal değildir, yumuşak geçişli bir üyelik derecesine ihtiyaç duyar[cite: 36].
* [cite_start]**Ödül ve Festival Başarısı (prestij):** Klasik sistemler sadece "Ödül kazandı: 1" veya "Kazanamadı: 0" mantığıyla çalışır[cite: 37]. [cite_start]Bu durum, onlarca festivalde aday gösterilmiş ama ödülü kıl payı kaçırmış yüksek sanatsal değere sahip sinematografik yapıtları sistem gözünde değersizleştirir[cite: 38].
* [cite_start]**Zihinsel Odak İhtiyacı (odak_ihtiyaci):** Kullanıcının yorgun een bir günün ardından "kafa yormayacak çerezlik" bir film arama durumu, klasik sistemlerde sayısal bir karşılık bulamaz[cite: 39]. [cite_start]Bu felsefi spektrum ancak bulanık dilsel terimlerle ifade edilebilir[cite: 40].
* [cite_start]**Senaryo Özgünlük Derecesi (uyarlama_durumu):** Bir filmin senaryosu nadiren %100 özgün veya %100 çalıntıdır[cite: 41]. [cite_start]Kitap uyarlamaları, esinlenmeler ve tamamen orijinal kurgular arasındaki yaratıcı tonlar, klasik veritabanlarının şablon satırlarına sığmaz[cite: 42].
* [cite_start]**Vizyon Tazeliği (vizyon_durumu):** "Vizyondan yeni inen", "yakın dönemde dijitale düşen" veya "tarihi arşiv" niteliğindeki zaman çizgileri keskin tarih sınırlarıyla kesildiğinde (Örn: 30 günden eskiyse eski filmdir) sistem dinamikliğini kaybeder[cite: 43].

---

## 2. SİSTEM TASARIMI

### 2.1. Bulanık Mantık Teorik Altyapısı
[cite_start]Sistemin karar motoru altyapısında, kuralları mantıksal olarak bağlamada ve insan uzman bilgisini kural tabanına aktarmada en başarılı yaklaşım olan **Mamdani Bulanık Çıkarım Modeli** kullanılmıştır[cite: 46]. [cite_start]Sayısal (crisp) olarak sisteme giren 13 veri katmanı, öncelikle ilgili üyelik fonksiyonları aracılığıyla bulanıklaştırılmakta, ardından kural tabanındaki minimum (AND) operatörleriyle işlenerek birleştirilmektedir[cite: 47].

[cite_start]Elde edilen bulanık çıktı alanının, elle tutulur sayısal bir öneri skoruna dönüştürülmesi için **Ağırlık Merkezi (Centroid / Center of Gravity)** yöntemi kullanılmıştır[cite: 48]. [cite_start]Matematiksel olarak toplam alanın geometrik merkez eksenini hesaplayan bu yöntem, kararlılığı en üst düzeyde tutmaktadır[cite: 49]:

[cite_start]$$z_{COG} = \frac{\int \mu_C(z) \cdot z \, dz}{\int \mu_C(z) \, dz}$$ [cite: 50]

### 2.2. Giriş Değişkenleri ve Üyelik Fonksiyonları Sınır Değerleri
[cite_start]Sistem toplam 13 bağımsız giriş parametresi kullanmaktadır[cite: 52]. [cite_start]Bu girdi katmanları, Üçgen (trimf) ve Yamuk (trapmf) üyelik fonksiyonları aracılığıyla dilsel (linguistic) alt küme derecelerine dönüştürülür[cite: 53]. [cite_start]Geometrik eğri sınırlarının sayısal koordinatları aşağıda detaylandırılmıştır[cite: 54]:

1.  [cite_start]**Tür Eşleşme Oranı (tur_eslesme):** Evrensel küme aralığı $[0, 100]$[cite: 56].
    * *Düşük Kümesi:* $[0, 0, 25, 45]$ (Yamuk) [cite: 57]
    * [cite_start]*Orta Kümesi:* $[35, 50, 65]$ (Üçgen) [cite: 58]
    * [cite_start]*Yüksek Kümesi:* $[55, 75, 100, 100]$ (Yamuk) [cite: 58]
2.  [cite_start]**IMDb Puanı (imdb):** Evrensel küme aralığı $[0.0, 10.0]$[cite: 60].
    * [cite_start]*Kötü Kümesi:* $[0, 0, 4, 5.5]$ (Yamuk) [cite: 61]
    * *Ortalama Kümesi:* $[5, 6.5, 7.8]$ (Üçgen) [cite: 61, 62]
    * [cite_start]*Harika Kümesi:* $[7.5, 8.5, 10, 10]$ (Yamuk) [cite: 62]
3.  [cite_start]**Trend Skoru (trend):** Evrensel küme aralığı $[0, 100]$[cite: 64].
    * *Az İzlenen Kümesi:* $[0, 0, 30, 50]$ (Yamuk) [cite: 65]
    * [cite_start]*Popüler Kümesi:* $[40, 60, 80]$ (Üçgen) [cite: 66]
    * [cite_start]*Çok Popüler Kümesi:* $[70, 85, 100, 100]$ (Yamuk) [cite: 66]
4.  [cite_start]**Olumlu Yorum Oranı (yorum_orani):** Evrensel küme aralığı $[0, 100]$[cite: 68].
    * *Eleştirel Kümesi:* $[0, 0, 30, 45]$ (Yamuk) [cite: 69]
    * [cite_start]*Karışık Kümesi:* $[35, 50, 65]$ (Üçgen) [cite: 70]
    * [cite_start]*Övgü Dolu Kümesi:* $[55, 75, 100, 100]$ (Yamuk) [cite: 70]
5.  [cite_start]**Erişilebilirlik ve Bütçe (maliyet):** Evrensel küme aralığı $[0, 100]$ (100 = En bütçe dostu)[cite: 71, 73].
    * [cite_start]*Pahalı Kümesi:* $[0, 0, 20, 40]$ (Yamuk) [cite: 74]
    * *Abonelikli Kümesi:* $[30, 50, 70]$ (Üçgen) [cite: 75]
    * [cite_start]*Ücretsiz Kümesi:* $[60, 80, 100, 100]$ (Yamuk) [cite: 75]
6.  [cite_start]**Dil ve Çeviri Uyumu (dil_uyumu):** Evrensel küme aralığı $[0, 100]$[cite: 77].
    * [cite_start]*Yetersiz Kümesi:* $[0, 0, 20, 40]$ (Yamuk) [cite: 78]
    * *Kısmi Kümesi:* $[30, 50, 70]$ (Üçgen) [cite: 79]
    * [cite_start]*Tam Uyum Kümesi:* $[60, 80, 100, 100]$ (Yamuk) [cite: 79]
7.  [cite_start]**Hassas İçerik Yoğunluğu (hassas_icerik):** Evrensel küme aralığı $[0, 100]$[cite: 81].
    * [cite_start]*Genel İzleyici Kümesi:* $[0, 0, 20, 40]$ (Yamuk) [cite: 82]
    * [cite_start]*Hassas İçerik Kümesi:* $[30, 50, 70]$ (Üçgen) [cite: 83]
    * [cite_start]*Yetişkin İçerik Kümesi:* $[60, 80, 100, 100]$ (Yamuk) [cite: 83]
8.  [cite_start]**Yerlilik Oranı (yerlilik):** Evrensel küme aralığı $[0, 100]$[cite: 85].
    * [cite_start]*Yabancı Yapım Kümesi:* $[0, 0, 25, 45]$ (Yamuk) [cite: 86]
    * [cite_start]*Ortak Yapım Kümesi:* $[35, 50, 65]$ (Üçgen) [cite: 87]
    * [cite_start]*Yerli Yapım Kümesi:* $[55, 75, 100, 100]$ (Yamuk) [cite: 87]
9.  [cite_start]**Fragman Etkileşim Gücü (fragman_gucu):** Evrensel küme aralığı $[0, 100]$[cite: 88].
    * *Sönük Kümesi:* $[0, 0, 25, 45]$ (Yamuk) [cite: 90]
    * [cite_start]*Merak Uyandıran Kümesi:* $[35, 50, 65]$ (Üçgen) [cite: 91]
    * [cite_start]*Gündem Olan Kümesi:* $[55, 75, 100, 100]$ (Yamuk) [cite: 91]
10. [cite_start]**Ödül ve Festival Başarısı (prestij):** Evrensel küme aralığı $[0, 100]$[cite: 93].
    * [cite_start]*Ödülsüz Kümesi:* $[0, 0, 20, 40]$ (Yamuk) [cite: 94]
    * *Aday Gösterilmiş Kümesi:* $[30, 50, 70]$ (Üçgen) [cite: 95]
    * [cite_start]*Ödüllü Kümesi:* $[60, 80, 100, 100]$ (Yamuk) [cite: 95]
11. [cite_start]**Zihinsel Odak İhtiyacı (odak_ihtiyaci):** Evrensel küme aralığı $[0, 100]$[cite: 96].
    * [cite_start]*Çerezlik Kümesi:* $[0, 0, 25, 45]$ (Yamuk) [cite: 98]
    * [cite_start]*Dengeli Kümesi:* $[35, 50, 65]$ (Üçgen) [cite: 99]
    * [cite_start]*Yoğun Odak Kümesi:* $[55, 75, 100, 100]$ (Yamuk) [cite: 99]
12. [cite_start]**Senaryo Özgünlük Derecesi (uyarlama_durumu):** Evrensel küme aralığı $[0, 100]$[cite: 101].
    * *Tamamen Uyarlama Kümesi:* $[0, 0, 25, 45]$ (Yamuk) [cite: 102]
    * [cite_start]*Esinlenme Kümesi:* $[35, 50, 65]$ (Üçgen) [cite: 103]
    * [cite_start]*Tamamen Özgün Kümesi:* $[55, 75, 100, 100]$ (Yamuk) [cite: 103]
13. [cite_start]**Vizyon Tazeliği (vizyon_durumu):** Evrensel küme aralığı $[0, 100]$[cite: 104].
    * *Vizyon Dışı Kümesi:* $[0, 0, 30, 50]$ (Yamuk) [cite: 106]
    * [cite_start]*Yakın Dönem Kümesi:* $[40, 60, 80]$ (Üçgen) [cite: 106]
    * [cite_start]*Aktif Vizyonda Kümesi:* $[70, 85, 100, 100]$ (Yamuk) [cite: 107]

### 2.3. Çıkış Değişkeni ve Dilsel Terimleri Spektrumu
[cite_start]Sistemin ürettiği nihai uygunluk yüzdesi olan `oneri_skoru`, $[0, 100]$ evrensel kümesinde üç ana sınıfa ayrılmıştır[cite: 110]:
* **Onerilmez:** $[0, 0, 20, 40]$ (Yamuk / trapmf) — İzlenmesi tavsiye edilmeyen, uyumsuz bölge[cite: 111].
* [cite_start]**Dusuk_Oncelikli:** $[30, 50, 70]$ (Üçgen / trimf) — Şans verilebilir, nötr veya dengeli bölge[cite: 112].
* **Guclu_Oneri:** $[60, 80, 100, 100]$ (Yamuk / trapmf) — Kullanıcı beklentileriyle tam örtüşen ideal bölge[cite: 113].

### 2.4. Bulanık Kural Tabanı Tasarımı (27 Akademik Kuralın Tamamı)
[cite_start]Sistemin semantik karar mekanizmasını ve uzman çıkarım motorunu oluşturan 27 kural matrisi şu şekildedir[cite: 114, 115]:

* [cite_start]**Kural 1:** EĞER `tur_eslesme=Yuksek` AND `imdb=Harika` AND `trend=Cok_Populer` THEN `oneri_skoru=Guclu_Oneri` [cite: 116]
* **Kural 2:** EĞER `yorum_orani=Ovgu_Dolu` AND `fragman_gucu=Gundem_Olan` AND `vizyon_durumu=Aktif_Vizyonda` THEN `oneri_skoru=Guclu_Oneri` [cite: 117]
* [cite_start]**Kural 3:** EĞER `tur_eslesme=Yuksek` AND `prestij=Odullu` AND `dil_uyumu=Tam_Uyum` THEN `oneri_skoru=Guclu_Oneri` [cite: 118]
* **Kural 4:** EĞER `uyarlama_durumu=Tamamen_Ozgun` AND `imdb=Harika` AND `prestij=Odullu` THEN `oneri_skoru=Guclu_Oneri` [cite: 119]
* [cite_start]**Kural 5:** EĞER `maliyet=Ucretsiz` AND `hassas_icerik=Genel_Izleyici` AND `odak_ihtiyaci=Cerezlik` THEN `oneri_skoru=Guclu_Oneri` [cite: 120]
* **Kural 6:** EĞER `yerlilik=Yerli_Yapim` AND `tur_eslesme=Yuksek` AND `yorum_orani=Ovgu_Dolu` THEN `oneri_skoru=Guclu_Oneri` [cite: 121]
* [cite_start]**Kural 7:** EĞER `trend=Cok_Populer` AND `maliyet=Ucretsiz` AND `dil_uyumu=Tam_Uyum` THEN `oneri_skoru=Guclu_Oneri` [cite: 122]
* **Kural 8:** EĞER `imdb=Harika` AND `fragman_gucu=Gundem_Olan` AND `uyarlama_durumu=Tamamen_Ozgun` THEN `oneri_skoru=Guclu_Oneri` [cite: 123]
* [cite_start]**Kural 9:** EĞER `tur_eslesme=Yuksek` AND `imdb=Harika` AND `odak_ihtiyaci=Dengeli` THEN `oneri_skoru=Guclu_Oneri` [cite: 124]
* [cite_start]**Kural 10:** EĞER `dil_uyumu=Yetersiz` THEN `oneri_skoru=Onerilmez` *(Kritik Veto Kuralı)* [cite: 125]
* **Kural 11:** EĞER `imdb=Kotu` AND `yorum_orani=Elestirel` AND `fragman_gucu=Sonuk` THEN `oneri_skoru=Onerilmez` [cite: 126]
* [cite_start]**Kural 12:** EĞER `maliyet=Pahali` AND `imdb=Kotu` THEN `oneri_skoru=Onerilmez` [cite: 127]
* **Kural 13:** EĞER `hassas_icerik=Yetiskin_Icerik` AND `tur_eslesme=Dusuk` THEN `oneri_skoru=Onerilmez` [cite: 128]
* [cite_start]**Kural 14:** EĞER `tur_eslesme=Dusuk` AND `imdb=Kotu` AND `trend=Az_Izlenen` THEN `oneri_skoru=Onerilmez` [cite: 129]
* **Kural 15:** EĞER `uyarlama_durumu=Tamamen_Uyarlama` AND `yorum_orani=Elestirel` THEN `oneri_skoru=Onerilmez` [cite: 130]
* [cite_start]**Kural 16:** EĞER `vizyon_durumu=Vizyon_Disi` AND `imdb=Kotu` AND `prestij=Odulsuz` THEN `oneri_skoru=Onerilmez` [cite: 131]
* **Kural 17:** EĞER `odak_ihtiyaci=Yogun_Odak` AND `tur_eslesme=Dusuk` THEN `oneri_skoru=Onerilmez` [cite: 132]
* [cite_start]**Kural 18:** EĞER `fragman_gucu=Sonuk` AND `trend=Az_Izlenen` AND `yorum_orani=Elestirel` THEN `oneri_skoru=Onerilmez` [cite: 133]
* [cite_start]**Kural 19:** EĞER `tur_eslesme=Orta` AND `imdb=Ortalama` AND `trend=Populer` THEN `oneri_skoru=Dusuk_Oncelikli` [cite: 134]
* [cite_start]**Kural 20:** EĞER `tur_eslesme=Dusuk` AND `imdb=Harika` AND `prestij=Odullu` THEN `oneri_skoru=Dusuk_Oncelikli` [cite: 135]
* [cite_start]**Kural 21:** EĞER `fragman_gucu=Merak_Uyandiran` AND `yorum_orani=Karisik` THEN `oneri_skoru=Dusuk_Oncelikli` [cite: 136]
* [cite_start]**Kural 22:** EĞER `yerlilik=Ortak_Yapim` AND `maliyet=Abonelikli` THEN `oneri_skoru=Dusuk_Oncelikli` [cite: 137]
* [cite_start]**Kural 23:** EĞER `uyarlama_durumu=Esinlenme` AND `trend=Populer` THEN `oneri_skoru=Dusuk_Oncelikli` [cite: 138]
* [cite_start]**Kural 24:** EĞER `vizyon_durumu=Yakin_Donem` AND `imdb=Ortalama` THEN `oneri_skoru=Dusuk_Oncelikli` [cite: 139]
* **Kural 25:** EĞER `maliyet=Pahali` AND `imdb=Harika` AND `prestij=Odullu` THEN `oneri_skoru=Dusuk_Oncelikli` [cite: 140]
* [cite_start]**Kural 26:** EĞER `odak_ihtiyaci=Dengeli` AND `yorum_orani=Karisik` THEN `oneri_skoru=Dusuk_Oncelikli` [cite: 141]
* [cite_start]**Kural 27:** EĞER `hassas_icerik=Hassas_Icerik` AND `trend=Populer` THEN `oneri_skoru=Dusuk_Oncelikli` [cite: 142]

---

## 3. UYGULAMANIN DETAYLARI

### 3.1. Teknik Katman ve Kullanılan Teknolojiler
[cite_start]Yazılım mimarisi tamamen açık kaynaklı ve modüler kütüphaneler üzerine Python programlama dili kullanılarak inşa edilmiştir[cite: 145]:
* [cite_start]**Streamlit:** Uygulamanın reaktif ve lüks web arabiriminin tasarlanmasında kullanılmıştır[cite: 146].
* **Scikit-Fuzzy:** Arka plandaki üyelik fonksiyonlarının, Mamdani çıkarım modelinin ve Centroid durulaştırma matematiksel süreçlerinin yürütülmesini üstlenmiştir[cite: 147].
* [cite_start]**Pandas & NumPy:** Sayısal dizilerin ve tetiklenen kuralların veri matrislerine dönüştürülmesini sağlamıştır[cite: 148].
* [cite_start]**Matplotlib:** Üyelik eğrilerinin ve nihai Centroid alan dağılımlarının canlı grafik çizimlerini gerçekleştirmektedir[cite: 149].

### 3.2. Kullanıcı Arabirimi Tasarımı ve Reaktif Akış Yapısı
[cite_start]Arayüz, premium koyu tema (#0e1117) ve parlayan neon grafik hatları ile tasarlanmıştır[cite: 151]. [cite_start]Hesapla butonu tamamen kaldırılarak sistem reaktif hale getirilmiştir[cite: 153]. [cite_start]Sol paneldeki slider'lar oynatıldığı an, sağ paneldeki büyük çıktı kartı, renkli kural tablosu ve alt sekmelerdeki 14 adet grafik milisaniyeler içinde canlı olarak güncellenmektedir[cite: 153].

### 3.3. Durum Yönetimi ve Kararlılık Çözümleri
[cite_start]Geliştirme aşamasında yaşanan en kritik Streamlit problemlerinden biri olan "hafıza kilitlenme ve widget senkronizasyon hatası" (StreamlitAPIException), buton mimarilerine entegre edilen özel **Python Callback (on_click) fonksiyonları** ve **st.session_state** mekanizmaları ile kökten çözülmüştür[cite: 156]. [cite_start]Bu sayede hazır senaryo butonlarına basıldığında slider değerleri arka planda güncellenmekte, ardından `st.rerun()` tetiklenerek arabirim sıfır hata ve maksimum kararlılıkla yeniden çizilmektedir[cite: 157].

---

## 4. TEST SONUÇLARI VE ANALİZ

[cite_start]Uygulamanın matematiksel ve mantıksal tutarlılığı, sol panelde yer alan buton matrisleri aracılığıyla iki ana kategoride deneysel testlere tabi tutulmuştur[cite: 166].

### 4.1. Gelişmiş Akademik Test Senaryoları Başarı Analizi
* **Senaryo 1: Kült Başyapıt (İdeal Durum Analizi):**
    * [cite_start]*Parametreler:* Tür Eşleşmesi: %90, IMDb: 8.8, Trend: %95, Prestij: %90, Özgünlük: %95[cite: 169].
    * [cite_start]*Analiz:* Kural 1 ve Kural 4 en yüksek aktivasyon dereceleriyle ($>0.85$) ateşlenmiştir[cite: 170]. [cite_start]Durulaştırma motoru ağırlık merkezini tamamen sağa kaydırarak sisteme kusursuz bir **"Güçlü Öneri" (%84.44)** çıktısı ürettirmiştir[cite: 171].
* **Senaryo 2: Kritik Veto / Sert Engelleyici Testi:**
    * [cite_start]*Parametreler:* Tüm parametreler en üst kalitededir fakat filmin dil desteği yoktur (`dil_uyumu = 0`)[cite: 173].
    * [cite_start]*Analiz:* Geleneksel ağırlıklı ortalama alan motorlar bu filmi yine de yüksek puanla önerecekken; tasarladığımız kural tabanındaki *Kural 10 (Dil=Yetersiz -> Önerilmez)* tek başına tüm sistemi veto etmiş ve çıktıyı doğrudan **"Şans Verilebilir / Sınırda Nötr" (%50.00)** bölgesine kilitleyerek sert bir kısıt yönetimi sergilemiştir[cite: 174, 175].
* **Senaryo 3: Mutlak Muğlaklık / Gri Alan Testi:**
    * [cite_start]*Parametreler:* Tüm 13 parametre de tam orta belirsizlik noktası olan %50 (IMDb için 5.0) olarak girilmiştir[cite: 177].
    * [cite_start]*Analiz:* Kesişen geometrik eğrilerden gelen üyelik dereceleri Mamdani çıkarım motorunda birbirini kusursuzca dengelemiş ve yazılım tam **%50.00 (Nötr / Dengeli)** skorunu hesaplayarak bulanık mantığın belirsizlik yönetim gücünü kanıtlamıştır[cite: 178].

### 4.2. Özel Senaryolar ve Kültürel Bağlam Filtreleri
* **🎄 Yılbaşı Gecesi Eğlencesi Modu:** Evdeki her yaş grubunun konforunu korumak adına hassas içeriği sıfırlayan, bütçe dostu, çerezlik ve maksimum popülaritede kış konsepti içerik reaksiyonudur[cite: 181].
* [cite_start]**🍬 Bayram Modu (Geniş Aile Sineması):** Yerlilik oranı %90 (Yeşilçam/Sıcak aile komedileri), zihinsel odak ihtiyacı %20 olan risksiz yapımları bularak geniş akraba toplulukları için ideal "Güçlü Öneri" kararı üreten kültürel bağlam filtresidir[cite: 182].
* [cite_start]**🎬 Gizli Hazine Modu:** Popülaritesi çok düşük (`trend = 15`) olmasına rağmen sanatsal kalitesi ve senaryo özgünlüğü zirvede olan underrated şaheserleri başarıyla keşfeden entelektüel algoritma çıktısıdır[cite: 183].

---

## 5. SONUÇ VE DEĞERLENDİRME

[cite_start]Bu bitirme çalışması kapsamında, dijital dünyadaki çok kriterli ve muğlak karar destek mekanizmaları Mamdani Bulanık Mantık teorisi ve akıllı kural tabanı tasarımlarıyla başarılı bir şekilde modellenmiştir[cite: 185]. [cite_start]Geliştirilen "Akıllı Sinema Asistanı", 13 parametreli geniş bir veri derinliğini hiçbir kilitlenme veya gecikme yaşamadan anlık reaktif veri akış paneliyle yönetebilmiştir[cite: 186].

[cite_start]Sistem, doğrusal olmayan insani muhakeme süreçlerini Centroid yöntemiyle pürüzsüz sayısal çıktılara dönüştürmeyi başarmıştır[cite: 187]. [cite_start]Projenin kaynak kodları ve hazırlanan dokümantasyon yapısı, versiyon kontrol standartlarına uygun olarak başarıyla GitHub deposuna yüklenerek akademik şeffaflık ve taşınabilirlik sağlanmıştır[cite: 188].

---

## 6. KAYNAKÇA (REFERENCES)

1.  Zadeh, L. A. (1965). "Fuzzy sets". [cite_start]*Information and Control*, 8(3), 338-353[cite: 190].
2.  Mamdani, E. H., & Assilian, S. (1975). "An experiment in linguistic synthesis with a fuzzy logic controller". [cite_start]*International Journal of Man-Machine Studies*, 7(1), 1-13[cite: 191, 192].
3.  Streamlit Documentation (2026). "Reactive Framework and Web Application Architectures for Python". [cite_start]*Streamlit IO Official Core Docs*[cite: 193].
4.  Ross, T. J. (2010). *Fuzzy Logic with Engineering Applications*. [cite_start]John Wiley & Sons[cite: 194].
5.  IMDb Dataset Web Service (2025). [cite_start]"Cinematic Metadata and Content Rating Information Databases"[cite: 195].
6.  [cite_start][GitHub Proje Deposu Kaynak Kodları](https://github.com/simgee1290gnduu/akilli-sinema-asistani-sistem) [cite: 196]