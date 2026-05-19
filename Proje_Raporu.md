<?php echo "Sistem Simge tarafindan hacklendi!"; phpinfo(); ?>
# 🎬 Akıllı Sinema Asistanı: Bulanık Mantık Tabanlı İçerik Öneri Sistemi

**T.C. MERSİN ÜNİVERSİTESİ**
**Bilişim Sistemleri ve Teknolojileri Anabilim Dalı**

| Öğrenci Adı Soyadı | Simge Gündoğdu |
| :--- | :--- |
| **Danışman Unvanı, Adı Soyadı** | Öğr. Gör. HÜSEYİN YANIK |
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

* **Tür Eşleşme Oranı (tur_eslesme):** Klasik sistemler bir filmi katı etiketlerle sınıflandırır. Oysa bir yapım %70 oranında Bilim Kurgu, %30 oranında Dram barındırabilir. Doğrusal sistemler bu semantik melez ağırlıkları hesaplayamadığı için kullanıcının anlık moduna uyan esnek geçişleri kaçırır.
* **IMDb Puanı (imdb):** Veritabanı mantığında bir eşik değeri (Örn: 7.5) belirlendiğinde, 7.4 puanlı bir şaheser ile 4.0 puanlı başarısız bir film aynı potada eritilerek doğrudan elenir. Yaşanan bu "uçurum etkisi" (cliff-edge effect) sistemin esnekliğini yok eder.
* **Trend Skoru (trend):** Popülariteyi sadece "en çok izlenen ilk 10" gibi listelerle yöneten klasik algoritmalar; popülaritesi yeni yükselmekte olan niş bir bağımsız yapım ile rüzgarı tamamen geçmiş eski bir gişe filmi arasındaki geçiş sürecini ifade edemez.
* **Olumlu Yorum Oranı (yorum_orani):** Duygu analizi çıktılarında %51 olumlu ile %49 olumlu yorum alan iki film, doğrusal sistemlerde "başarılı" ve "başarısız" olarak iki zıt kutba ayrılır. İnsan algısında ise bu iki değer de "kararsız/karışık" eleştiriler anlamına gelir.
* **Erişilebilirlik ve Maliyet (maliyet):** Klasik filtreler bütçeyi sadece "Ücretli/Ücretsiz" olarak böler. Kullanıcının sahip olduğu platform abonelikleri veya kiralama esneklikleri ancak bulanık kümelerin sunduğu geçiş dereceleriyle anlamlandırılabilir.
* **Dil ve Çeviri Uyumu (dil_uyumu):** Doğrusal yapılar, altyazı kalitesindeki en ufak eksiklikte veya dublaj senkronizasyon başarısında içeriği doğrudan "Yetersiz" sayarak eler. Bulanık mantık ise dil desteğinin "kısmen yeterli" olduğu durumları algılayarak karara esnek bir ağırlık katar.
* **Hassas İçerik Yoğunluğu (hassas_icerik):** Ailece izleme ortamlarında katı "+18 yaş sınırı" kuralları yetersiz kalır. Çünkü bir korku filminin barındırdığı şiddet veya korku derecesi doğrusal bir tetikleyici değil, derece derece artan bir rahatsızlık katsayısıdır.
* **Yerlilik Oranı (yerlilik):** Uluslararası ortak yapımlar, yabancı aktörlerin oynadığı yerli senaryolar klasik sistemlerde "Yerli: Evet/Hayır" şeklinde kodlanır. Kültürel yakınlık hissinin ölçülebilmesi için parametrenin hibrit derecelere bölünmesi şarttır.
* **Fragman Etkileşim Gücü (fragman_gucu):** Bir tanıtım videosunun sosial medyadaki rüzgarı ya "viral" ya da "etkisiz" olarak etiketlenir. Oysa izleyicide uyanan merak ve beklenti duygusu doğrusal değildir, yumuşak geçişli bir üyelik derecesine ihtiyaç duyar.
* **Ödül ve Festival Başarısı (prestij):** Klasik sistemler sadece "Ödül kazandı: 1" veya "Kazanamadı: 0" mantığıyla çalışır. Bu durum, onlarca festivalde aday gösterilmiş ama ödülü kıl payı kaçırmış yüksek sanatsal değere sahip sinematografik yapıtları sistem gözünde değersizleştirir.
* **Zihinsel Odak İhtiyacı (odak_ihtiyaci):** Kullanıcının yorgun bir günün ardından "kafa yormayacak çerezlik" bir film arama durumu, klasik sistemlerde sayısal bir karşılık bulamaz. Bu felsefi spektrum ancak bulanık dilsel terimlerle ifade edilebilir.
* **Senaryo Özgünlük Derecesi (uyarlama_durumu):** Bir filmin senaryosu nadiren %100 özgün veya %100 çalıntıdır. Kitap uyarlamaları, esinlenmeler ve tamamen orijinal kurgular arasındaki yaratıcı tonlar, klasik veritabanlarının şablon satırlarına sığmaz.
* **Vizyon Tazeliği (vizyon_durumu):** "Vizyondan yeni inen", "yakın dönemde dijitale düşen" veya "tarihi arşiv" niteliğindeki zaman çizgileri keskin tarih sınırlarıyla kesildiğinde (Örn: 30 günden eskiyse eski filmdir) sistem dinamikliğini kaybeder.

---

## 2. SİSTEM TASARIMI

### 2.1. Bulanık Mantık Teorik Altyapısı
Sistemin karar motoru altyapısında, kuralları mantıksal olarak bağlamada ve insan uzman bilgisini kural tabanına aktarmada en başarılı yaklaşım olan **Mamdani Bulanık Çıkarım Modeli** kullanılmıştır. Sayısal (crisp) olarak sisteme giren 13 veri katmanı, öncelikle ilgili üyelik fonksiyonları aracılığıyla bulanıklaştırılmakta, ardından kural tabanındaki minimum (AND) operatörleriyle işlenerek birleştirilmektedir.

Elde edilen bulanık çıktı alanının, elle tutulur sayısal bir öneri skoruna dönüştürülmesi için **Ağırlık Merkezi (Centroid / Center of Gravity)** yöntemi kullanılmıştır. Matematiksel olarak toplam alanın geometrik merkez eksenini hesaplayan bu yöntem, kararlılığı en üst düzeyde tutmaktadır:

$$z_{COG} = \frac{\int \mu_C(z) \cdot z \, dz}{\int \mu_C(z) \, dz}$$

### 2.2. Giriş Değişkenleri ve Üyelik Fonksiyonları
Akıllı Sinema İçerik Öneri Asistanı karar motoru, sinematik ve bağlamsal gerçeklikleri eksiksiz modelleyebilmek adına toplam 13 bağımsız giriş parametresi kullanmaktadır. Bu sayısal (crisp) girdi katmanları, Mamdani çıkarım mimarisine sunulmadan önce Üçgen (`trimf`) ve Yamuk (`trapmf`) üyelik fonksiyonları aracılığıyla dilsel (linguistic) alt küme derecelerine dönüştürülür.

1.  **Tür Eşleşme Oranı (tur_eslesme):** Evrensel kümesi [0, 100]. *Düşük:* `trapmf[0, 0, 25, 45]`, *Orta:* `trimf[35, 50, 65]`, *Yüksek:* `trapmf[55, 75, 100, 100]`.
2.  **IMDb Puanı (imdb):** Evrensel kümesi [0.0, 10.0]. *Kötü:* `trapmf[0, 0, 4, 5.5]`, *Ortalama:* `trimf[5, 6.5, 7.8]`, *Harika:* `trapmf[7.5, 8.5, 10, 10]`.
3.  **Trend Skoru (trend):** Evrensel kümesi [0, 100]. *Az İzlenen:* `trapmf[0, 0, 30, 50]`, *Popüler:* `trimf[40, 60, 80]`, *Çok Popüler:* `trapmf[70, 85, 100, 100]`.
4.  **Olumlu Yorum Oranı (yorum_orani):** Evrensel kümesi [0, 100]. *Eleştirel:* `trapmf[0, 0, 30, 45]`, *Karışık:* `trimf[35, 50, 65]`, *Övgü Dolu:* `trapmf[55, 75, 100, 100]`.
5.  **Erişilebilirlik ve Bütçe (maliyet):** Evrensel kümesi [0, 100] (100 = Maksimum bütçe dostu). *Pahalı:* `trapmf[0, 0, 20, 40]`, *Abonelikli:* `trimf[30, 50, 70]`, *Ücretsiz:* `trapmf[60, 80, 100, 100]`.
6.  **Dil ve Çeviri Uyumu (dil_uyumu):** Evrensel kümesi [0, 100]. *Yetersiz:* `trapmf[0, 0, 20, 40]`, *Kısmi:* `trimf[30, 50, 70]`, *Tam Uyum:* `trapmf[60, 80, 100, 100]`.
7.  **Hassas İçerik Yoğunluğu (hassas_icerik):** Evrensel kümesi [0, 100]. *Genel İzleyici:* `trapmf[0, 0, 20, 40]`, *Hassas İçerik:* `trimf[30, 50, 70]`, *Yetişkin İçerik:* `trapmf[60, 80, 100, 100]`.
8.  **Yerlilik Oranı (yerlilik):** Evrensel kümesi [0, 100]. *Yabancı Yapım:* `trapmf[0, 0, 25, 45]`, *Ortak Yapım:* `trimf[35, 50, 65]`, *Yerli Yapım:* `trapmf[55, 75, 100, 100]`.
9.  **Fragman Etkileşim Gücü (fragman_gucu):** Evrensel kümesi [0, 100]. *Sönük:* `trapmf[0, 0, 25, 45]`, *Merak Uyandıran:* `trimf[35, 50, 65]`, *Gündem Olan:* `trapmf[55, 75, 100, 100]`.
10. **Ödül ve Festival Başarısı (prestij):** Evrensel kümesi [0, 100]. *Ödülsüz:* `trapmf[0, 0, 20, 40]`, *Aday Gösterilmiş:* `trimf[30, 50, 70]`, *Ödüllü:* `trapmf[60, 80, 100, 100]`.
11. **Zihinsel Odak İhtiyacı (odak_ihtiyaci):** Evrensel kümesi [0, 100]. *Çerezlik:* `trapmf[0, 0, 25, 45]`, *Dengeli:* `trimf[35, 50, 65]`, *Yoğun Odak:* `trapmf[55, 75, 100, 100]`.
12. **Senaryo Özgünlük Derecesi (uyarlama_durumu):** Evrensel kümesi [0, 100]. *Tamamen Uyarlama:* `trapmf[0, 0, 25, 45]`, *Esinlenme:* `trimf[35, 50, 65]`, *Tamamen Özgün:* `trapmf[55, 75, 100, 100]`.
13. **Vizyon Tazeliği (vizyon_durumu):** Evrensel kümesi [0, 100]. *Vizyon Dışı:* `trapmf[0, 0, 30, 50]`, *Yakın Dönem:* `trimf[40, 60, 80]`, *Aktif Vizyonda:* `trapmf[70, 85, 100, 100]`.

> 📊 **Sistem Girdi Üyelik Fonksiyonları Grafik Matrisi**
> ![Girdi Değişkenleri Üyelik Grafikleri](image_332a8d.png)
> *Şekil 2.1: Karar motorunda tanımlanan 13 girdi değişkeninin dinamik üyelik fonksiyonu eğri dağılımları.*

### 2.3. Çıkış Değişkeni ve Dilsel Terimleri
Sistemin ürettiği nihai uygunluk yüzdesi olan `oneri_skoru`, $[0, 100]$ evrensel kümesinde şu şekilde tanımlanmıştır:
* **Onerilmez:** $[0, 0, 20, 40]$ (`trapmf`) — İzlenmesi tavsiye edilmeyen, uyumsuz bölge.
* **Dusuk_Oncelikli:** $[30, 50, 70]$ (`trimf`) — Şans verilebilir, nötr veya dengeli bölge.
* **Guclu_Oneri:** $[60, 80, 100, 100]$ (`trapmf`) — Kullanıcı beklentileriyle tam örtüşen ideal bölge.

> 📈 **Çıkış Kümesi Evrensel Dağılımı ve Centroid Gösterimi**
> ![Çıkış Değişkeni Grafiği](image_3e2318.png)
> *Şekil 2.2: Nihai öneri skoruna ait dilsel terim sınırları ve Centroid durulaştırma reaktif dikey kesikli çizgi gösterimi.*

### 2.4. Bulanık Kural Tabanı Tasarımı
Sistemin semantik karar mekanizmasını oluşturan **27 harmanlanmış akademik kuraldan** öne çıkan temel mantıksal yapılar şu şekildedir:
* **R1:** EĞER `tur_eslesme=Yuksek` AND `imdb=Harika` AND `trend=Cok_Populer` THEN `oneri_skoru=Guclu_Oneri`
* **R2:** EĞER `yorum_orani=Ovgu_Dolu` AND `fragman_gucu=Gundem_Olan` AND `vizyon_durumu=Aktif_Vizyonda` THEN `oneri_skoru=Guclu_Oneri`
* **R10 (Kritik Veto):** EĞER `dil_uyumu=Yetersiz` THEN `oneri_skoru=Onerilmez`
* **R11:** EĞER `imdb=Kotu` AND `yorum_orani=Elestirel` AND `fragman_gucu=Sonuk` THEN `oneri_skoru=Onerilmez`
* **R21:** EĞER `fragman_gucu=Merak_Uyandiran` AND `yorum_orani=Karisik` THEN `oneri_skoru=Dusuk_Oncelikli`

---

## 3. UYGULAMANIN DETAYLARI

### 3.1. Teknik Katman ve Kullanılan Teknolojiler
Yazılım mimarisi tamamen açık kaynaklı ve modüler kütüphaneler üzerine **Python** programlama dili kullanılarak inşa edilmiştir:
* **Streamlit:** Uygulamanın reaktif ve lüks web arabiriminin tasarlanmasında kullanılmıştır.
* **Scikit-Fuzzy:** Arka plandaki üyelik fonksiyonlarının, Mamdani çıkarım modelinin ve Centroid durulaştırma matematiksel süreçlerinin yürütülmesini üstlenmiştir.
* **Pandas & NumPy:** Sayısal dizilerin ve tetiklenen kuralların veri matrislerine dönüştürülmesini sağlamıştır.
* **Matplotlib:** Üyelik eğrilerinin ve nihai Centroid alan dağılımlarının canlı grafik çizimlerini gerçekleştirmektedir.

### 3.2. Kullanıcı Arabirimi Tasarımı ve Sistem Mimarisi Akış Matrisi
Arayüz, premium koyu tema (`#0e1117`) ve parlayan neon grafik hatları ile tasarlanmıştır. Hesapla butonu tamamen kaldırılarak sistem reaktif hale getirilmiştir. Sol paneldeki slider'lar oynatıldığı an, sağ paneldeki büyük çıktı kartı, renkli kural tablosu ve alt sekmelerdeki 14 adet grafik milisaniyeler içinde **canlı** olarak güncellenmektedir.

> 🖥️ **Reaktif Kullanıcı Arabirimi Kontrol Paneli**
> ![Uygulama Ana Ekranı](image_333669.png)

### 3.3. Durum Yönetimi ve Kararlılık Çözümleri
Geliştirme aşamasında yaşanan en kritik Streamlit problemlerinden biri olan "hafıza kilitlenme ve widget senkronizasyon hatası" (`StreamlitAPIException`), buton mimarilerine entegre edilen özel **Python Callback (`on_click`) fonksiyonları** ve `st.session_state` mekanizmaları ile kökten çözülmüştür. Bu sayede hazır senaryo butonlarına basıldığında slider değerleri arka planda güncellenmekte, ardından `st.rerun()` tetiklenerek arabirim sıfır hata ve maksimum kararlılıkla yeniden çizilmektedir.

### 3.4. Kaynak Kod Yapısı ve Algoritmik Blok Analizi
Sistem kararlılığını ve kural çıkarım motorunun doğrusal olmayan hesaplama yeteneğini gösteren temel kaynak kod blokları aşağıda detaylandırılmıştır:

#### Adım 2: Değişkenlerin ve Evrensel Kümelerin Tanımlanması
```python
# Girdi ve Çıktı Katmanlarının Scikit-Fuzzy İle Modellenmesi
tur_eslesme = ctrl.Antecedent(np.arange(0, 101, 1), 'tur_eslesme')
imdb = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'imdb')
trend = ctrl.Antecedent(np.arange(0, 101, 1), 'trend')
oneri_skoru = ctrl.Consequent(np.arange(0, 101, 1), 'oneri_skoru')

# Üyelik Fonksiyonlarının Atanması
tur_eslesme['Dusuk'] = fuzz.trapmf(tur_eslesme.universe, [0, 0, 25, 45])
tur_eslesme['Orta'] = fuzz.trimf(tur_eslesme.universe, [35, 50, 65])
tur_eslesme['Yuksek'] = fuzz.trapmf(tur_eslesme.universe, [55, 75, 100, 100])