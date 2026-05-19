# 🎬 Akıllı Sinema Asistanı: Bulanık Mantık Tabanlı İçerik Öneri Sistemi

**T.C. MERSİN ÜNİVERSİTESİ** **Bilişim Sistemleri ve Teknolojileri Anabilim Dalı**

| Akademik Kimlik Bilgileri | Tanımlamalar ve Değerler |
| :--- | :--- |
| **Öğrencinin Adı ve Soyadı** | Simge Gündoğdu |
| **Danışmanın Unvanı, Adı ve Soyadı** | Öğr. Gör. HÜSEYİN YANIK |
| **Bitirme Projesi Başlığı** | Akıllı Sinema Asistanı: Bulanık Mantık Tabanlı İçerik Öneri Sistemi |
| **Rapor Tarihi** | 21 / 05 / 2026 |

---

## 1. GİRİŞ VE PROBLEM TANIMI

### 1.1. Projenin Amacı ve Önemi
Gelişen internet altyapısı ve dijital dönüşüm süreçleri, eğlence ve yayıncılık sektöründe devasa bir veri hacmi (Big Data) meydana getirmiştir. Günümüzde kullanıcılar, binlerce içerik arasından kendi kişisel beklentilerine, bütçelerine, sosyo-kültürel bağlamlarına ve anlık zihinsel durumlarına en uygun filmi seçerken "içerik felci" (content paralysis) ve karar verme güçlüğü yaşamaktadır.

Bu projenin amacı; kullanıcıların karşılaştığı bu çok kriterli karmaşık karar verme problemini, insan muhakeme yeteneğine ve düşünce yapısına en yakın matematiksel model olan **Mamdani Bulanık Mantık (Fuzzy Logic) Karar Destek Sistemi** mimarisiyle çözmektir. Geliştirilen "Akıllı Sinema Asistanı", klasik algoritmaların aksine kullanıcıları tek bir izleme döngüsüne hapsetmez. İçeriğin sanatsal kalitesini, finansal erişilebilirliğini, dil senkronizasyonunu ve anlık bağlamsal senaryoları tek bir reaktif matriste eriterek doğrusal olmayan, esnek ve akıllı bir öneri mekanizması sunar.

### 1.2. Problemin Genel Tanımı
Günümüz dijital yayıncılık platformlarında kullanılan mevcut öneri motorları, genellikle İşbirlikçi Filtreleme (Collaborative Filtering) veya İçerik Tabanlı Filtreleme (Content-Based Filtering) yöntemlerine dayanmaktadır. Bu sistemlerin temel yapısal kusuru, kararları keskin sınırlarla (crisp boundaries) ayıran ikili mantık (Boolean 0-1) mimarisiyle çalışmalarıdır. Klasik ilişkisel veritabanı sorguları (SELECT / WHERE komutları) veya doğrusal kod blokları, bir veriyi ya tamamen kümenin içinde ya da tamamen dışında kabul eder.

Ancak insan tercihleri doğası gereği muğlak (fuzzy) yapılardan oluşur. Bir filmin popülerliğinin az olması onun mutlak anlamda kötü olduğu anlamına gelmediği gibi, kullanıcıların zihinsel yorgunluk ve sosyal ortam kısıtları da matematiksel olarak katı sınırlarla (If-Else yapılarıyla) ifade edilemez. Klasik sistemlerin bu esneklikten uzak yapısı, öneri kalitesinde tıkanmalara ve kullanıcı memnuniyetsizliğine yol açmaktadır.

### 1.3. 13 Girdi Parametresi Odağında Geleneksel Yöntemlerin Yetersizlikleri
Projemizde modellenen 13 girdi parametresi özelinde, geleneksel ikili (binary) sistemlerin yaşadığı matematiksel ve mantıksal yetersizlikler şu şekildedir:

* **Tür Eşleşme Oranı (tur_eslesme):** Klasik sistemler bir filmi katı etiketlerle sınıflandırır. Oysa bir yapım %70 oranında Bilim Kurgu, %30 oranında Dram barındabilir. Doğrusal sistemler bu semantik melez ağırlıkları hesaplayamadığı için kullanıcının anlık moduna uyan esnek geçişleri kaçırır.
* **IMDb Puanı (imdb):** Veritabanı mantığında bir eşik değeri (Örn: 7.5) belirlendiğinde, 7.4 puanlı bir şaheser ile 4.0 puanlı başarısız bir film aynı potada eritilerek doğrudan elenir. Yaşanan bu "uçurum etkisi" (cliff-edge effect) sistemin esnekliğini yok eder.
* **Trend Skoru (trend):** Popülariteyi sadece "en çok izlenen ilk 10" gibi listelerle yöneten klasik algoritmalar; popülaritesi yeni yükselmekte olan niş bir bağımsız yapım ile rüzgarı tamamen geçmiş eski bir gişe filmi arasındaki geçiş sürecini ifade edemez.
* **Olumlu Yorum Oranı (yorum_orani):** Duygu analizi çıktılarında %51 olumlu ile %49 olumlu yorum alan iki film, doğrusal sistemlerde "başarılı" ve "başarısız" olarak iki zıt kutba ayrılır. İnsan algısında ise bu iki değer de "kararsız/karışık" eleştiriler anlamına gelir.
* **Erişilebilirlik ve Maliyet (maliyet):** Klasik filtreler bütçeyi sadece "Ücretli/Ücretsiz" olarak böler. Kullanıcının sahip olduğu platform abonelikleri veya kiralama esneklikleri ancak bulanık kümelerin sunduğu geçiş dereceleriyle anlamlandırılabilir.
* **Dil ve Çeviri Uyumu (dil_uyumu):** Doğrusal yapılar, altyazı kalitesindeki en ufak eksiklikte veya dublaj senkronizasyon başarısında içeriği doğrudan "Yetersiz" sayarak eler. Bulanık mantık ise dil desteğinin "kısmen yeterli" olduğu durumları algılayarak karara esnek bir ağırlık katar.
* **Hassas İçerik Yoğunluğu (hassas_icerik):** Ailece izleme ortamlarında katı "+18 yaş sınırı" kuralları yetersiz kalır. Çünkü bir korku filminin barındırdığı şiddet veya korku derecesi doğrusal bir tetikleyici değil, derece derece artan bir rahatsızlık katsayısıdır.
* **Yerlilik Oranı (yerlilik):** Uluslararası ortak yapımlar, yabancı aktörlerin oynadığı yerli senaryolar klasik sistemlerde "Yerli: Evet/Hayır" şeklinde kodlanır. Kültürel yakınlık hissinin ölçülebilmesi için parametrenin hibrit derecelere bölünmesi şarttır.
* **Fragman Etkileşim Gücü (fragman_gucu):** Bir tanıtım videosunun sosyal medyadaki rüzgarı ya "viral" ya da "etkisiz" olarak etiketlenir. Oysa izleyicide uyanan merak ve beklenti duygusu doğrusal değildir, yumuşak geçişli bir üyelik derecesine ihtiyaç duyar.
* **Ödül ve Festival Başarısı (prestij):** Klasik sistemler sadece "Ödül kazandı: 1" veya "Kazanamadı: 0" mantığıyla çalışır. Bu durum, onlarca festivalde aday gösterilmiş ama ödülü kıl payı kaçırmış yüksek sanatsal değere sahip sinematografik yapıtları sistem gözünde değersizleştirir.
* **Zihinsel Odak İhtiyacı (odak_ihtiyaci):** Kullanıcının yorgun een bir günün ardından "kafa yormayacak çerezlik" bir film arama durumu, klasik sistemlerde sayısal bir karşılık bulamaz. Bu felsefi spektrum ancak bulanık dilsel terimlerle ifade edilebilir.
* **Senaryo Özgünlük Derecesi (uyarlama_durumu):** Bir filmin senaryosu nadiren %100 özgün veya %100 çalıntıdır. Kitap uyarlamaları, esinlenmeler ve tamamen orijinal kurgular arasındaki yaratıcı tonlar, klasik veritabanlarının şablon satırlarına sığmaz.
* **Vizyon Tazeliği (vizyon_durumu):** "Vizyondan yeni inen", "yakın dönemde dijitale düşen" veya "tarihi arşiv" niteliğindeki zaman çizgileri keskin tarih sınırlarıyla kesildiğinde (Örn: 30 günden eskiyse eski filmdir) sistem dinamikliğini kaybeder.

---

## 2. SİSTEM TASARIMI

### 2.1. Bulanık Mantık Teorik Altyapısı
Sistemin karar motoru altyapısında, kuralları mantıksal olarak bağlamada ve insan uzman bilgisini kural tabanına aktarmada en başarılı yaklaşım olan **Mamdani Bulanık Çıkarım Modeli** kullanılmıştır. Sayısal (crisp) olarak sisteme giren 13 veri katmanı, öncelikle ilgili üyelik fonksiyonları aracılığıyla bulanıklaştırılmakta, ardından kural tabanındaki minimum (AND) operatörleriyle işlenerek birleştirilmektedir.

Elde edilen bulanık çıktı alanının, elle tutulur sayısal bir öneri skoruna dönüştürülmesi için **Ağırlık Merkezi (Centroid / Center of Gravity)** yöntemi kullanılmıştır. Matematiksel olarak toplam alanın geometrik merkez eksenini hesaplayan bu yöntem, kararlılığı en üst düzeyde tutmaktadır:

$$z_{COG} = \frac{\int \mu_C(z) \cdot z \, dz}{\int \mu_C(z) \, dz}$$

### 2.2. Giriş Değişkenleri ve Üyelik Fonksiyonları Sınır Değerleri
Sistem toplam 13 bağımsız giriş parametresi kullanmaktadır. Bu girdi katmanları, Üçgen (trimf) ve Yamuk (trapmf) üyelik fonksiyonları aracılığıyla dilsel (linguistic) alt küme derecelerine dönüştürülür. Geometrik eğri sınırlarının sayısal koordinatları aşağıda detaylandırılmıştır:

1.  **Tür Eşleşme Oranı (tur_eslesme):** Evrensel küme aralığı $[0, 100]$.
    * *Düşük Kümesi:* $[0, 0, 25, 45]$ (Yamuk)
    * *Orta Kümesi:* $[35, 50, 65]$ (Üçgen)
    * *Yüksek Kümesi:* $[55, 75, 100, 100]$ (Yamuk)
2.  **IMDb Puanı (imdb):** Evrensel küme aralığı $[0.0, 10.0]$.
    * *Kötü Kümesi:* $[0, 0, 4, 5.5]$ (Yamuk)
    * *Ortalama Kümesi:* $[5, 6.5, 7.8]$ (Üçgen)
    * *Harika Kümesi:* $[7.5, 8.5, 10, 10]$ (Yamuk)
3.  **Trend Skoru (trend):** Evrensel küme aralığı $[0, 100]$.
    * *Az İzlenen Kümesi:* $[0, 0, 30, 50]$ (Yamuk)
    * *Popüler Kümesi:* $[40, 60, 80]$ (Üçgen)
    * *Çok Popüler Kümesi:* $[70, 85, 100, 100]$ (Yamuk)
4.  **Olumlu Yorum Oranı (yorum_orani):** Evrensel küme aralığı $[0, 100]$.
    * *Eleştirel Kümesi:* $[0, 0, 30, 45]$ (Yamuk)
    * *Karışık Kümesi:* $[35, 50, 65]$ (Üçgen)
    * *Övgü Dolu Kümesi:* $[55, 75, 100, 100]$ (Yamuk)
5.  **Erişilebilirlik ve Bütçe (maliyet):** Evrensel küme aralığı $[0, 100]$ (100 = En bütçe dostu).
    * *Pahalı Kümesi:* $[0, 0, 20, 40]$ (Yamuk)
    * *Abonelikli Kümesi:* $[30, 50, 70]$ (Üçgen)
    * *Ücretsiz Kümesi:* $[60, 80, 100, 100]$ (Yamuk)
6.  **Dil ve Çeviri Uyumu (dil_uyumu):** Evrensel küme aralığı $[0, 100]$.
    * *Yetersiz Kümesi:* $[0, 0, 20, 40]$ (Yamuk)
    * *Kısmi Kümesi:* $[30, 50, 70]$ (Üçgen)
    * *Tam Uyum Kümesi:* $[60, 80, 100, 100]$ (Yamuk)
7.  **Hassas İçerik Yoğunluğu (hassas_icerik):** Evrensel küme aralığı $[0, 100]$.
    * *Genel İzleyici Kümesi:* $[0, 0, 20, 40]$ (Yamuk)
    * *Hassas İçerik Kümesi:* $[30, 50, 70]$ (Üçgen)
    * *Yetişkin İçerik Kümesi:* $[60, 80, 100, 100]$ (Yamuk)
8.  **Yerlilik Oranı (yerlilik):** Evrensel küme aralığı $[0, 100]$.
    * *Yabancı Yapım Kümesi:* $[0, 0, 25, 45]$ (Yamuk)
    * *Ortak Yapım Kümesi:* $[35, 50, 65]$ (Üçgen)
    * *Yerli Yapım Kümesi:* $[55, 75, 100, 100]$ (Yamuk)
9.  **Fragman Etkileşim Gücü (fragman_gucu):** Evrensel küme aralığı $[0, 100]$.
    * *Sönük Kümesi:* $[0, 0, 25, 45]$ (Yamuk)
    * *Merak Uyandıran Kümesi:* $[35, 50, 65]$ (Üçgen)
    * *Gündem Olan Kümesi:* $[55, 75, 100, 100]$ (Yamuk)
10. **Ödül ve Festival Başarısı (prestij):** Evrensel küme aralığı $[0, 100]$.
    * *Ödülsüz Kümesi:* $[0, 0, 20, 40]$ (Yamuk)
    * *Aday Gösterilmiş Kümesi:* $