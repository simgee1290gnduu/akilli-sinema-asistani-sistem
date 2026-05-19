import streamlit as st
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt
import pandas as pd

# Sayfa Genişlik ve Tema Ayarı
st.set_page_config(layout="wide", page_title="Akıllı Sinema Asistanı")

# CSS ile Arka Plan ve Kart Tasarımlarını Premium Yapma
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    div[data-testid="stMetricValue"] { font-size: 28px; font-weight: bold; color: #ff4b4b; }
    iframe { background-color: transparent !important; }
    </style>
""", unsafe_allow_html=True)


# ==============================================================================
# --- ADIM 1: YARDIMCI FONKSİYONLARIN TANIMLANMASI (NAMEERROR ENGELLEYİCİ KALKAN) ---
# ==============================================================================
def get_mu(var, term, val):
    return fuzz.interp_membership(var.universe, var[term].mf, val)


def ciz_havali_grafik(var, title, current_val):
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_facecolor('#1a1f2c')
    fig.patch.set_facecolor('#0e1117')
    colors = ['#3b82f6', '#10b981', '#ef4444']
    for i, term in enumerate(var.terms):
        color = colors[i % len(colors)]
        ax.plot(var.universe, var[term].mf, label=term, color=color, linewidth=2)
        ax.fill_between(var.universe, 0, var[term].mf, color=color, alpha=0.12)
        mu = get_mu(var, term, current_val)
        if mu > 0:
            ax.plot(current_val, mu, 'o', color='#ff4b4b', markersize=6, markeredgecolor='white')
    ax.axvline(x=current_val, color='#ff4b4b', linestyle='-', linewidth=1.8)
    ax.set_title(title, color='white', fontsize=10, fontweight='bold')
    ax.grid(True, color='#2d3748', linestyle=':', alpha=0.5)
    ax.tick_params(colors='white', labelsize=8)
    ax.legend(fontsize='x-small', facecolor='#11151c', edgecolor='#2d3748', labelcolor='white')
    return fig


def yukle_senaryo_callback(tur, imdb_val, trend_val, yorum_val, maliyet_val, dil_val, hassas_val, yerli_val,
                           fragman_val, prestij_val, odak_val, uyarlama_val, vizyon_val):
    st.session_state.s_tur = tur
    st.session_state.s_imdb = imdb_val
    st.session_state.s_trend = trend_val
    st.session_state.s_yorum = yorum_val
    st.session_state.s_maliyet = maliyet_val
    st.session_state.s_dil = dil_val
    st.session_state.s_hassas = hassas_val
    st.session_state.s_yerlilik = yerli_val
    st.session_state.s_fragman = fragman_val
    st.session_state.s_prestij = prestij_val
    st.session_state.s_odak = odak_val
    st.session_state.s_uyarlama = uyarlama_val
    st.session_state.s_vizyon = vizyon_val


# ==============================================================================
# --- ADIM 2: DEĞİŞKENLERİN VE EVRENSEL KÜMELERİN TANIMLANMASI ---
# ==============================================================================
tur_eslesme = ctrl.Antecedent(np.arange(0, 101, 1), 'tur_eslesme')
imdb = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'imdb')
trend = ctrl.Antecedent(np.arange(0, 101, 1), 'trend')
yorum_orani = ctrl.Antecedent(np.arange(0, 101, 1), 'yorum_orani')
maliyet = ctrl.Antecedent(np.arange(0, 101, 1), 'maliyet')
dil_uyumu = ctrl.Antecedent(np.arange(0, 101, 1), 'dil_uyumu')
hassas_icerik = ctrl.Antecedent(np.arange(0, 101, 1), 'hassas_icerik')
yerlilik = ctrl.Antecedent(np.arange(0, 101, 1), 'yerlilik')
fragman_gucu = ctrl.Antecedent(np.arange(0, 101, 1), 'fragman_gucu')
prestij = ctrl.Antecedent(np.arange(0, 101, 1), 'prestij')
odak_ihtiyaci = ctrl.Antecedent(np.arange(0, 101, 1), 'odak_ihtiyaci')
uyarlama_durumu = ctrl.Antecedent(np.arange(0, 101, 1), 'uyarlama_durumu')
vizyon_durumu = ctrl.Antecedent(np.arange(0, 101, 1), 'vizyon_durumu')

oneri_skoru = ctrl.Consequent(np.arange(0, 101, 1), 'oneri_skoru', defuzzify_method='centroid')

# --- ÜYELİK FONKSİYONLARININ ATANMASI ---
tur_eslesme['Dusuk'] = fuzz.trapmf(tur_eslesme.universe, [0, 0, 25, 45])
tur_eslesme['Orta'] = fuzz.trimf(tur_eslesme.universe, [35, 50, 65])
tur_eslesme['Yuksek'] = fuzz.trapmf(tur_eslesme.universe, [55, 75, 100, 100])

imdb['Kotu'] = fuzz.trapmf(imdb.universe, [0, 0, 4, 5.5])
imdb['Ortalama'] = fuzz.trimf(imdb.universe, [5, 6.5, 7.8])
imdb['Harika'] = fuzz.trapmf(imdb.universe, [7.5, 8.5, 10, 10])

trend['Az_Izlenen'] = fuzz.trapmf(trend.universe, [0, 0, 30, 50])
trend['Populer'] = fuzz.trimf(trend.universe, [40, 60, 80])
trend['Cok_Populer'] = fuzz.trapmf(trend.universe, [70, 85, 100, 100])

yorum_orani['Elestirel'] = fuzz.trapmf(yorum_orani.universe, [0, 0, 30, 45])
yorum_orani['Karisik'] = fuzz.trimf(yorum_orani.universe, [35, 50, 65])
yorum_orani['Ovgu_Dolu'] = fuzz.trapmf(yorum_orani.universe, [55, 75, 100, 100])

maliyet['Pahali'] = fuzz.trapmf(maliyet.universe, [0, 0, 20, 40])
maliyet['Abonelikli'] = fuzz.trimf(maliyet.universe, [30, 50, 70])
maliyet['Ucretsiz'] = fuzz.trapmf(maliyet.universe, [60, 80, 100, 100])

dil_uyumu['Yetersiz'] = fuzz.trapmf(dil_uyumu.universe, [0, 0, 20, 40])
dil_uyumu['Kismi'] = fuzz.trimf(dil_uyumu.universe, [30, 50, 70])
dil_uyumu['Tam_Uyum'] = fuzz.trapmf(dil_uyumu.universe, [60, 80, 100, 100])

hassas_icerik['Genel_Izleyici'] = fuzz.trapmf(hassas_icerik.universe, [0, 0, 20, 40])
hassas_icerik['Hassas_Icerik'] = fuzz.trimf(hassas_icerik.universe, [30, 50, 70])
hassas_icerik['Yetiskin_Icerik'] = fuzz.trapmf(hassas_icerik.universe, [60, 80, 100, 100])

yerlilik['Yabanci_Yapim'] = fuzz.trapmf(yerlilik.universe, [0, 0, 25, 45])
yerlilik['Ortak_Yapim'] = fuzz.trimf(yerlilik.universe, [35, 50, 65])
yerlilik['Yerli_Yapim'] = fuzz.trapmf(yerlilik.universe, [55, 75, 100, 100])

fragman_gucu['Sonuk'] = fuzz.trapmf(fragman_gucu.universe, [0, 0, 25, 45])
fragman_gucu['Merak_Uyandiran'] = fuzz.trimf(fragman_gucu.universe, [35, 50, 65])
fragman_gucu['Gundem_Olan'] = fuzz.trapmf(fragman_gucu.universe, [55, 75, 100, 100])

prestij['Odulsuz'] = fuzz.trapmf(prestij.universe, [0, 0, 20, 40])
prestij['Aday_Gosterilmis'] = fuzz.trimf(prestij.universe, [30, 50, 70])
prestij['Odullu'] = fuzz.trapmf(prestij.universe, [60, 80, 100, 100])

odak_ihtiyaci['Cerezlik'] = fuzz.trapmf(odak_ihtiyaci.universe, [0, 0, 25, 45])
odak_ihtiyaci['Dengeli'] = fuzz.trimf(odak_ihtiyaci.universe, [35, 50, 65])
odak_ihtiyaci['Yogun_Odak'] = fuzz.trapmf(odak_ihtiyaci.universe, [55, 75, 100, 100])

uyarlama_durumu['Tamamen_Uyarlama'] = fuzz.trapmf(uyarlama_durumu.universe, [0, 0, 25, 45])
uyarlama_durumu['Esinlenme'] = fuzz.trimf(uyarlama_durumu.universe, [35, 50, 65])
uyarlama_durumu['Tamamen_Ozgun'] = fuzz.trapmf(uyarlama_durumu.universe, [55, 75, 100, 100])

vizyon_durumu['Vizyon_Disi'] = fuzz.trapmf(vizyon_durumu.universe, [0, 0, 30, 50])
vizyon_durumu['Yakin_Donem'] = fuzz.trimf(vizyon_durumu.universe, [40, 60, 80])
vizyon_durumu['Aktif_Vizyonda'] = fuzz.trapmf(vizyon_durumu.universe, [70, 85, 100, 100])

oneri_skoru['Onerilmez'] = fuzz.trapmf(oneri_skoru.universe, [0, 0, 20, 40])
oneri_skoru['Dusuk_Oncelikli'] = fuzz.trimf(oneri_skoru.universe, [30, 50, 70])
oneri_skoru['Guclu_Oneri'] = fuzz.trapmf(oneri_skoru.universe, [60, 80, 100, 100])

# ==============================================================================
# --- ADIM 3: KURAL TABANI (27 KURAL) ---
# ==============================================================================
kurallar = [
    ctrl.Rule(tur_eslesme['Yuksek'] & imdb['Harika'] & trend['Cok_Populer'], oneri_skoru['Guclu_Oneri']),
    ctrl.Rule(yorum_orani['Ovgu_Dolu'] & fragman_gucu['Gundem_Olan'] & vizyon_durumu['Aktif_Vizyonda'],
              oneri_skoru['Guclu_Oneri']),
    ctrl.Rule(tur_eslesme['Yuksek'] & prestij['Odullu'] & dil_uyumu['Tam_Uyum'], oneri_skoru['Guclu_Oneri']),
    ctrl.Rule(uyarlama_durumu['Tamamen_Ozgun'] & imdb['Harika'] & prestij['Odullu'], oneri_skoru['Guclu_Oneri']),
    ctrl.Rule(maliyet['Ucretsiz'] & hassas_icerik['Genel_Izleyici'] & odak_ihtiyaci['Cerezlik'],
              oneri_skoru['Guclu_Oneri']),
    ctrl.Rule(yerlilik['Yerli_Yapim'] & tur_eslesme['Yuksek'] & yorum_orani['Ovgu_Dolu'], oneri_skoru['Guclu_Oneri']),
    ctrl.Rule(trend['Cok_Populer'] & maliyet['Ucretsiz'] & dil_uyumu['Tam_Uyum'], oneri_skoru['Guclu_Oneri']),
    ctrl.Rule(imdb['Harika'] & fragman_gucu['Gundem_Olan'] & uyarlama_durumu['Tamamen_Ozgun'],
              oneri_skoru['Guclu_Oneri']),
    ctrl.Rule(tur_eslesme['Yuksek'] & imdb['Harika'] & odak_ihtiyaci['Dengeli'], oneri_skoru['Guclu_Oneri']),

    ctrl.Rule(dil_uyumu['Yetersiz'], oneri_skoru['Onerilmez']),
    ctrl.Rule(imdb['Kotu'] & yorum_orani['Elestirel'] & fragman_gucu['Sonuk'], oneri_skoru['Onerilmez']),
    ctrl.Rule(maliyet['Pahali'] & imdb['Kotu'], oneri_skoru['Onerilmez']),
    ctrl.Rule(hassas_icerik['Yetiskin_Icerik'] & tur_eslesme['Dusuk'], oneri_skoru['Onerilmez']),
    ctrl.Rule(tur_eslesme['Dusuk'] & imdb['Kotu'] & trend['Az_Izlenen'], oneri_skoru['Onerilmez']),
    ctrl.Rule(uyarlama_durumu['Tamamen_Uyarlama'] & yorum_orani['Elestirel'], oneri_skoru['Onerilmez']),
    ctrl.Rule(vizyon_durumu['Vizyon_Disi'] & imdb['Kotu'] & prestij['Odulsuz'], oneri_skoru['Onerilmez']),
    ctrl.Rule(odak_ihtiyaci['Yogun_Odak'] & tur_eslesme['Dusuk'], oneri_skoru['Onerilmez']),
    ctrl.Rule(fragman_gucu['Sonuk'] & trend['Az_Izlenen'] & yorum_orani['Elestirel'], oneri_skoru['Onerilmez']),

    ctrl.Rule(tur_eslesme['Orta'] & imdb['Ortalama'] & trend['Populer'], oneri_skoru['Dusuk_Oncelikli']),
    ctrl.Rule(tur_eslesme['Dusuk'] & imdb['Harika'] & prestij['Odullu'], oneri_skoru['Dusuk_Oncelikli']),
    ctrl.Rule(fragman_gucu['Merak_Uyandiran'] & yorum_orani['Karisik'], oneri_skoru['Dusuk_Oncelikli']),
    ctrl.Rule(yerlilik['Ortak_Yapim'] & maliyet['Abonelikli'], oneri_skoru['Dusuk_Oncelikli']),
    ctrl.Rule(uyarlama_durumu['Esinlenme'] & trend['Populer'], oneri_skoru['Dusuk_Oncelikli']),
    ctrl.Rule(vizyon_durumu['Yakin_Donem'] & imdb['Ortalama'], oneri_skoru['Dusuk_Oncelikli']),
    ctrl.Rule(maliyet['Pahali'] & imdb['Harika'] & prestij['Odullu'], oneri_skoru['Dusuk_Oncelikli']),
    ctrl.Rule(odak_ihtiyaci['Dengeli'] & yorum_orani['Karisik'], oneri_skoru['Dusuk_Oncelikli']),
    ctrl.Rule(hassas_icerik['Hassas_Icerik'] & trend['Populer'], oneri_skoru['Dusuk_Oncelikli'])
]

onerici_sistemi = ctrl.ControlSystem(kurallar)
film_onerici = ctrl.ControlSystemSimulation(onerici_sistemi)

# ==============================================================================
# --- ADIM 4: SESSION STATE VE WIDGET INITIALIZATION ---
# ==============================================================================
varsayilanlar = {
    's_tur': 85, 's_imdb': 8.4, 's_trend': 75, 's_yorum': 80, 's_maliyet': 90,
    's_dil': 100, 's_hassas': 15, 's_yerlilik': 70, 's_fragman': 80, 's_prestij': 60,
    's_odak': 30, 's_uyarlama': 90, 's_vizyon': 85
}

for k, v in varsayilanlar.items():
    if k not in st.session_state:
        st.session_state[k] = v

# --- SIDEBAR PANEL DÜZENİ ---
# 1. PARAMETRE SLIDERLARI (En Üstte)
st.sidebar.header("🎛️ Parametre Kontrol Paneli")
val_tur = st.sidebar.slider("1. Tür Eşleşme Oranı (%)", 0, 100, key="s_tur")
val_imdb = st.sidebar.slider("2. IMDb Puanı", 0.0, 10.0, step=0.1, key="s_imdb")
val_trend = st.sidebar.slider("3. Trend Skoru (%)", 0, 100, key="s_trend")
val_yorum = st.sidebar.slider("4. Olumlu Yorum Oranı (%)", 0, 100, key="s_yorum")
val_maliyet = st.sidebar.slider("5. Erişilebilirlik (Maliyet) (%) [100=Ücretsiz]", 0, 100, key="s_maliyet")
val_dil = st.sidebar.slider("6. Dil ve Çeviri Uyumu (%)", 0, 100, key="s_dil")
val_hassas = st.sidebar.slider("7. Hassas İçerik Yoğunluğu (+18) (%)", 0, 100, key="s_hassas")
val_yerlilik = st.sidebar.slider("8. Yerlilik Oranı (%)", 0, 100, key="s_yerlilik")
val_fragman = st.sidebar.slider("9. Fragman Etkileşim Gücü (%)", 0, 100, key="s_fragman")
val_prestij = st.sidebar.slider("10. Ödül ve Festival Başarısı (%)", 0, 100, key="s_prestij")
val_odak = st.sidebar.slider("11. Zihinsel Odaklanma İhtiyacı (%)", 0, 100, key="s_odak")
val_uyarlama = st.sidebar.slider("12. Senaryo Özgünlük Derecesi (%) [100=Tam Özgün]", 0, 100, key="s_uyarlama")
val_vizyon = st.sidebar.slider("13. Vizyon Tazeliği (%) [100=Vizyonda]", 0, 100, key="s_vizyon")

# 2. SENARYO BUTONLARI (Sliderların Altında)
st.sidebar.markdown("---")
st.sidebar.header("📋 Gelişmiş Akademik Senaryolar")
c_btn1, c_btn2 = st.sidebar.columns(2)
with c_btn1:
    st.button("🌟 Kült Başyapıt", on_click=yukle_senaryo_callback,
              args=(90, 8.8, 95, 90, 50, 100, 20, 10, 95, 90, 80, 95, 85))
    st.button("🍿 Çerezlik Komedi", on_click=yukle_senaryo_callback,
              args=(50, 6.2, 70, 55, 100, 100, 10, 100, 60, 0, 20, 10, 20))
    st.button("❌ Pahalı Fiyasko", on_click=yukle_senaryo_callback,
              args=(20, 3.5, 15, 10, 10, 0, 90, 0, 20, 0, 70, 40, 90))
with c_btn2:
    st.button("🔒 Kritik Veto (Dil)", on_click=yukle_senaryo_callback,
              args=(95, 9.0, 90, 95, 90, 0, 10, 20, 90, 95, 50, 90, 80))
    st.button("📐 Gri Alan (%50)", on_click=yukle_senaryo_callback,
              args=(50, 5.0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50))
    st.button("🔀 Eleştirmen vs Halk", on_click=yukle_senaryo_callback,
              args=(85, 8.8, 5, 10, 40, 100, 20, 10, 30, 100, 85, 95, 30))

st.sidebar.header("🎭 Özel Senaryolar")
st.sidebar.button("🎄 Yılbaşı Gecesi Eğlencesi", on_click=yukle_senaryo_callback,
                  args=(90, 6.8, 80, 70, 100, 100, 5, 60, 85, 20, 25, 60, 50))
st.sidebar.button("🍬 Bayram Modu (Geniş Aile)", on_click=yukle_senaryo_callback,
                  args=(85, 7.5, 65, 85, 100, 100, 0, 90, 70, 30, 20, 70, 40))
st.sidebar.button("🎬 Gizli Hazine (Gözden Kaçanlar)", on_click=yukle_senaryo_callback,
                  args=(85, 8.2, 15, 90, 80, 100, 15, 20, 65, 75, 85, 95, 10))
st.sidebar.button("💝 İlk Randevu (Risksiz Bölge)", on_click=yukle_senaryo_callback,
                  args=(90, 7.4, 75, 85, 70, 100, 0, 45, 80, 40, 30, 70, 60))

st.sidebar.markdown("---")
st.sidebar.button("🔄 Değerleri Sıfırla", on_click=yukle_senaryo_callback,
                  args=(85, 8.4, 75, 80, 90, 100, 15, 70, 80, 60, 30, 90, 85))

# ==============================================================================
# --- ADIM 5: ANA SAYFA GÖRSEL MATRİS VE AKIŞ ŞEMASI ---
# ==============================================================================
# --- BULANIK MANTIK MİMARİ AKIŞ ŞEMASI (YENİLENMİŞ AKADEMİK MATRİS) ---
# --- BULANIK MANTIK MİMARİ AKIŞ ŞEMASI (SADE VE ŞIK BAŞLIK) ---
st.markdown("<h3 style='text-align: center; color: #24c6dc; margin-top: 15px; margin-bottom: 15px; font-size: 18px; font-weight: bold;'>🏗️ Bulanık Mantık Karar Motoru Sistem Mimarisi Akış Matrisi</h3>", unsafe_allow_html=True)

# MİMARİ AKIŞ ŞEMASI (ÖMER'İN PROJESİNDEKİ KOD TABANLI BLOK DÜZENİ)
st.markdown(f"""
    <div style='background-color: #1e222b; padding: 15px; border-radius: 8px; margin-top: 15px; border: 1px solid #2d3748;'>
        <h4 style='margin-top:0; color:#24c6dc; font-size:13px; text-transform:uppercase; letter-spacing:1px;'>🏗️ Bulanık Mantık Karar Motoru Sistem Mimarisi Akış Matrisi</h4>
        <div style='display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; text-align: center; font-size: 11px; font-family: monospace;'>
            <div style='background-color: #10141d; padding: 10px; border-radius: 5px; flex: 1; margin: 4px; border-top: 3px solid #3b82f6;'>
                <b style='color:#3b82f6;'>1. GİRİŞLER</b><br>13 Sayısal Değer<br><small style='color:#a0aec0;'>Slider / Hazır Modlar</small>
            </div>
            <div style='color: #24c6dc; font-weight: bold; font-size:16px;'>➔</div>
            <div style='background-color: #10141d; padding: 10px; border-radius: 5px; flex: 1; margin: 4px; border-top: 3px solid #10b981;'>
                <b style='color:#10b981;'>2. BULANIKLAŞTIRMA</b><br>Üyelik Fonksiyonları<br><small style='color:#a0aec0;'>trimf + trapmf Eğrileri</small>
            </div>
            <div style='color: #24c6dc; font-weight: bold; font-size:16px;'>➔</div>
            <div style='background-color: #10141d; padding: 10px; border-radius: 5px; flex: 1; margin: 4px; border-top: 3px solid #f59e0b;'>
                <b style='color:#f59e0b;'>3. ÇIKARIM MOTORU</b><br>27 Harmanlanmış Kural<br><small style='color:#a0aec0;'>Mamdani Çıkarımı (min)</small>
            </div>
            <div style='color: #24c6dc; font-weight: bold; font-size:16px;'>➔</div>
            <div style='background-color: #10141d; padding: 10px; border-radius: 5px; flex: 1; margin: 4px; border-top: 3px solid #ef4444;'>
                <b style='color:#ef4444;'>4. DURULAŞTIRMA</b><br>Ağırlık Merkezi Hesaplama<br><small style='color:#a0aec0;'>Centroid Metodu</small>
            </div>
            <div style='color: #24c6dc; font-weight: bold; font-size:16px;'>➔</div>
            <div style='background-color: #1a1f2c; padding: 10px; border-radius: 5px; flex: 1; margin: 4px; border: 1px dashed #24c6dc;'>
                <b style='color:#24c6dc;'>5. SİSTEM ÇIKISI</b><br>Öneri Skoru %<br><small style='color:#a0aec0;'>Anlık Dinamik Sonuç</small>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# --- ADIM 6: REAKTİF CANLI ÇIKARIM MATRİSİ HESAPLAMASI ---
# ==============================================================================
film_onerici.input['tur_eslesme'] = val_tur
film_onerici.input['imdb'] = val_imdb
film_onerici.input['trend'] = val_trend
film_onerici.input['yorum_orani'] = val_yorum
film_onerici.input['maliyet'] = val_maliyet
film_onerici.input['dil_uyumu'] = val_dil
film_onerici.input['hassas_icerik'] = val_hassas
film_onerici.input['yerlilik'] = val_yerlilik
film_onerici.input['fragman_gucu'] = val_fragman
film_onerici.input['prestij'] = val_prestij
film_onerici.input['odak_ihtiyaci'] = val_odak
film_onerici.input['uyarlama_durumu'] = val_uyarlama
film_onerici.input['vizyon_durumu'] = val_vizyon

try:
    film_onerici.compute()
    skor = film_onerici.output['oneri_skoru']
    hata_var = False
except ValueError:
    skor = 50.0
    hata_var = True

if hata_var:
    status_lbl = "Nötr / Dengeli"
    card_bg = "#4a5568"
    baskin_sonuc = "Nötr"
elif skor >= 65:
    card_bg = "#8b0000"  # Ömer Tarzı Premium Koyu Kırmızı
    status_lbl = "🌟 Güçlü Öneri"
    baskin_sonuc = "Güçlü Öneri"
elif skor >= 40:
    card_bg = "#d97706"  # Premium Altın Turuncu
    status_lbl = "🍿 Şans Verilebilir"
    baskin_sonuc = "Düşük Öncelikli"
else:
    card_bg = "#1e222b"  # Koyu Gri
    status_lbl = "❌ Önerilmez"
    baskin_sonuc = "Önerilmez"

st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("#### 🎯 Çıktı Değerlendirme Kartı")
    st.markdown(f"""
        <div style='background-color: #1a1f2c; padding: 25px; border-radius: 8px; border-bottom: 5px solid {card_bg}; text-align: center; box-shadow: 0px 4px 10px rgba(0,0,0,0.2);'>
            <span style='color: #a0aec0; font-size: 13px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;'>Nihai Öneri Uygunluk Skoru</span>
            <h1 style='color: white; margin: 8px 0; font-size: 46px; font-weight: bold;'>%{skor:.2f}</h1>
            <span style='background-color: {card_bg}; color: white; padding: 5px 16px; border-radius: 20px; font-size: 12px; font-weight: bold;'>{status_lbl}</span>
        </div>
    """, unsafe_allow_html=True)

    fig_out, ax_out = plt.subplots(figsize=(6, 3.2))
    ax_out.set_facecolor('#1a1f2c')
    fig_out.patch.set_facecolor('#0e1117')
    colors_out = ['#ef4444', '#f59e0b', '#10b981']
    for i, term in enumerate(oneri_skoru.terms):
        ax_out.plot(oneri_skoru.universe, oneri_skoru[term].mf, label=term, color=colors_out[i], linewidth=2)
        ax_out.fill_between(oneri_skoru.universe, 0, oneri_skoru[term].mf, color=colors_out[i], alpha=0.12)
    ax_out.axvline(x=skor, color='#ff4b4b', linestyle='--', linewidth=2.5, label=f'Centroid: {skor:.1f}')
    ax_out.set_title("Nihai Öneri Skoru Dağılımı (Centroid)", color='white', fontweight='bold', fontsize=10)
    ax_out.grid(True, color='#2d3748', linestyle=':', alpha=0.5)
    ax_out.tick_params(colors='white', labelsize=8)
    ax_out.legend(facecolor='#11151c', edgecolor='#2d3748', labelcolor='white', fontsize='small')
    st.pyplot(fig_out)

with col2:
    st.markdown("#### 📜 Akıllı Kurallar (Ateşlenen)")

    rule_specs = [
        {"no": 1, "desc": "Tür_Eşleşme=Yüksek + IMDb=Harika + Trend=Çok_Popüler", "output": "Güçlü Öneri",
         "act": min(get_mu(tur_eslesme, 'Yuksek', val_tur), get_mu(imdb, 'Harika', val_imdb),
                    get_mu(trend, 'Cok_Populer', val_trend))},
        {"no": 2, "desc": "Yorum=Övgü_Dolu + Fragman=Gündem_Olan + Vizyon=Aktif_Vizyonda", "output": "Güçlü Öneri",
         "act": min(get_mu(yorum_orani, 'Ovgu_Dolu', val_yorum), get_mu(fragman_gucu, 'Gundem_Olan', val_fragman),
                    get_mu(vizyon_durumu, 'Aktif_Vizyonda', val_vizyon))},
        {"no": 3, "desc": "Tür_Eşleşme=Yüksek + Prestij=Ödüllü + Dil=Tam_Uyum", "output": "Güçlü Öneri",
         "act": min(get_mu(tur_eslesme, 'Yuksek', val_tur), get_mu(prestij, 'Odullu', val_prestij),
                    get_mu(dil_uyumu, 'Tam_Uyum', val_dil))},
        {"no": 4, "desc": "Özgünlük=Tam_Özgün + IMDb=Harika + Prestij=Ödüllü", "output": "Güçlü Öneri",
         "act": min(get_mu(uyarlama_durumu, 'Tamamen_Ozgun', val_uyarlama), get_mu(imdb, 'Harika', val_imdb),
                    get_mu(prestij, 'Odullu', val_prestij))},
        {"no": 5, "desc": "Maliyet=Ücretsiz + Hassas=Genel_İzleyici + Odak=Çerezlik", "output": "Güçlü Öneri",
         "act": min(get_mu(maliyet, 'Ucretsiz', val_maliyet), get_mu(hassas_icerik, 'Genel_Izleyici', val_hassas),
                    get_mu(odak_ihtiyaci, 'Cerezlik', val_odak))},
        {"no": 6, "desc": "Yerlilik=Yerli_Yapım + Tür_Eşleşme=Yüksek + Yorum=Övgü_Dolu", "output": "Güçlü Öneri",
         "act": min(get_mu(yerlilik, 'Yerli_Yapim', val_yerlilik), get_mu(tur_eslesme, 'Yuksek', val_tur),
                    get_mu(yorum_orani, 'Ovgu_Dolu', val_yorum))},
        {"no": 7, "desc": "Trend=Çok_Popüler + Maliyet=Ücretsiz + Dil=Tam_Uyum", "output": "Güçlü Öneri",
         "act": min(get_mu(trend, 'Cok_Populer', val_trend), get_mu(maliyet, 'Ucretsiz', val_maliyet),
                    get_mu(dil_uyumu, 'Tam_Uyum', val_dil))},
        {"no": 8, "desc": "IMDb=Harika + Fragman=Gündem_Olan + Özgünlük=Tam_Özgün", "output": "Güçlü Öneri",
         "act": min(get_mu(imdb, 'Harika', val_imdb), get_mu(fragman_gucu, 'Gundem_Olan', val_fragman),
                    get_mu(uyarlama_durumu, 'Tamamen_Ozgun', val_uyarlama))},
        {"no": 9, "desc": "Tür_Eşleşme=Yüksek + IMDb=Harika + Odak=Dengeli", "output": "Güçlü Öneri",
         "act": min(get_mu(tur_eslesme, 'Yuksek', val_tur), get_mu(imdb, 'Harika', val_imdb),
                    get_mu(odak_ihtiyaci, 'Dengeli', val_odak))},
        {"no": 10, "desc": "Dil Uyumu = Yetersiz (Kritik Engelleyici)", "output": "Önerilmez",
         "act": get_mu(dil_uyumu, 'Yetersiz', val_dil)},
        {"no": 11, "desc": "IMDb=Kötü + Yorum=Eleştirel + Fragman=Sönük", "output": "Önerilmez",
         "act": min(get_mu(imdb, 'Kotu', val_imdb), get_mu(yorum_orani, 'Elestirel', val_yorum),
                    get_mu(fragman_gucu, 'Sonuk', val_fragman))},
        {"no": 12, "desc": "Maliyet=Pahalı + IMDb=Kötü", "output": "Önerilmez",
         "act": min(get_mu(maliyet, 'Pahali', val_maliyet), get_mu(imdb, 'Kotu', val_imdb))},
        {"no": 13, "desc": "Hassas=Yetişkin_İçerik + Tür_Eşleşme=Düşük", "output": "Önerilmez",
         "act": min(get_mu(hassas_icerik, 'Yetiskin_Icerik', val_hassas), get_mu(tur_eslesme, 'Dusuk', val_tur))},
        {"no": 14, "desc": "Tür_Eşleşme=Düşük + IMDb=Kötü + Trend=Az_İzlenen", "output": "Önerilmez",
         "act": min(get_mu(tur_eslesme, 'Dusuk', val_tur), get_mu(imdb, 'Kotu', val_imdb),
                    get_mu(trend, 'Az_Izlenen', val_trend))},
        {"no": 15, "desc": "Özgünlük=Tamamen_Uyarlama + Yorum=Eleştirel", "output": "Önerilmez",
         "act": min(get_mu(uyarlama_durumu, 'Tamamen_Uyarlama', val_uyarlama),
                    get_mu(yorum_orani, 'Elestirel', val_yorum))},
        {"no": 16, "desc": "Vizyon=Vizyon_Dışı + IMDb=Kötü + Prestij=Ödülsüz", "output": "Önerilmez",
         "act": min(get_mu(vizyon_durumu, 'Vizyon_Disi', val_vizyon), get_mu(imdb, 'Kotu', val_imdb),
                    get_mu(prestij, 'Odulsuz', val_prestij))},
        {"no": 17, "desc": "Odak=Yoğun_Odak + Tür_Eşleşme=Düşük", "output": "Önerilmez",
         "act": min(get_mu(odak_ihtiyaci, 'Yogun_Odak', val_odak), get_mu(tur_eslesme, 'Dusuk', val_tur))},
        {"no": 18, "desc": "Fragman=Sönük + Trend=Az_İzlenen + Yorum=Eleştirel", "output": "Önerilmez",
         "act": min(get_mu(fragman_gucu, 'Sonuk', val_fragman), get_mu(trend, 'Az_Izlenen', val_trend),
                    get_mu(yorum_orani, 'Elestirel', val_yorum))},
        {"no": 19, "desc": "Tür_Eşleşme=Orta + IMDb=Ortalama + Trend=Popüler", "output": "Düşük Öncelikli",
         "act": min(get_mu(tur_eslesme, 'Orta', val_tur), get_mu(imdb, 'Ortalama', val_imdb),
                    get_mu(trend, 'Populer', val_trend))},
        {"no": 20, "desc": "Tür_Eşleşme=Düşük + IMDb=Harika + Prestij=Ödüllü", "output": "Düşük Öncelikli",
         "act": min(get_mu(tur_eslesme, 'Dusuk', val_tur), get_mu(imdb, 'Harika', val_imdb),
                    get_mu(prestij, 'Odullu', val_prestij))},
        {"no": 21, "desc": "Fragman=Merak_Uyandırıcı + Yorum=Karışık", "output": "Düşük Öncelikli",
         "act": min(get_mu(fragman_gucu, 'Merak_Uyandiran', val_fragman), get_mu(yorum_orani, 'Karisik', val_yorum))},
        {"no": 22, "desc": "Yerlilik=Ortak_Yapım + Maliyet=Abonelikli", "output": "Düşük Öncelikli",
         "act": min(get_mu(yerlilik, 'Ortak_Yapim', val_yerlilik), get_mu(maliyet, 'Abonelikli', val_maliyet))},
        {"no": 23, "desc": "Özgünlük=Esinlenme + Trend=Popüler", "output": "Düşük Öncelikli",
         "act": min(get_mu(uyarlama_durumu, 'Esinlenme', val_uyarlama), get_mu(trend, 'Populer', val_trend))},
        {"no": 24, "desc": "Vizyon=Yakın_Dönem + IMDb=Ortalama", "output": "Düşük Öncelikli",
         "act": min(get_mu(vizyon_durumu, 'Yakin_Donem', val_vizyon), get_mu(imdb, 'Ortalama', val_imdb))},
        {"no": 25, "desc": "Maliyet=Pahalı + IMDb=Harika + Prestij=Ödüllü", "output": "Düşük Öncelikli",
         "act": min(get_mu(maliyet, 'Pahali', val_maliyet), get_mu(imdb, 'Harika', val_imdb),
                    get_mu(prestij, 'Odullu', val_prestij))},
        {"no": 26, "desc": "Odak=Dengeli + Yorum=Karışık", "output": "Düşük Öncelikli",
         "act": min(get_mu(odak_ihtiyaci, 'Dengeli', val_odak), get_mu(yorum_orani, 'Karisik', val_yorum))},
        {"no": 27, "desc": "Hassas=Hassas_İçerik + Trend=Popüler", "output": "Düşük Öncelikli",
         "act": min(get_mu(hassas_icerik, 'Hassas_Icerik', val_hassas), get_mu(trend, 'Populer', val_trend))}
    ]

    aktif_list = [r for r in rule_specs if r["act"] > 0]
    aktif_df = pd.DataFrame(aktif_list)
    if not aktif_df.empty:
        aktif_df = aktif_df.sort_values(by="act", ascending=False)

    if not aktif_df.empty:
        gosterim_df = aktif_df.rename(
            columns={"no": "Kural No", "desc": "Açıklama Mantığı", "act": "Aktivasyon Derecesi",
                     "output": "Çıktı Sınıfı"})

        # BUG FIX: Kolon seçim işlemini Pandas Styler objesine dönüşmeden ÖNCE yapıyoruz
        filtered_df = gosterim_df[["Kural No", "Açıklama Mantığı", "Aktivasyon Derecesi", "Çıktı Sınıfı"]]


        def ciz_renkli_hucre(val):
            if val >= 0.35:
                return 'background-color: #8b0000; color: white; font-weight: bold;'
            elif val >= 0.20:
                return 'background-color: #d97706; color: white; font-weight: bold;'
            elif val > 0.0:
                return 'background-color: #fef08a; color: black; font-weight: bold;'
            return ''


        styled_df = filtered_df.style.map(ciz_renkli_hucre, subset=['Aktivasyon Derecesi']).format(
            {'Aktivasyon Derecesi': '{:.6f}'})
        st.dataframe(styled_df, use_container_width=True, hide_index=True)
    else:
        st.info("Mevcut girdi kombinasyonuna bağlı olarak doğrudan tetiklenen bir kural bulunmuyor.")

    st.markdown("<br>", unsafe_allow_html=True)
    c_a, c_b, c_c = st.columns(3)
    c_a.metric(label="🔥 Ateşlenen Kural", value=f"{len(aktif_df)} / 27")
    max_aktivasyon = aktif_df["act"].max() if not aktif_df.empty else 0.0
    c_b.metric(label="📈 Maks Aktivasyon", value=f"{max_aktivasyon:.4f}")
    c_c.metric(label="🏆 Baskın Sonuç", value=baskin_sonuc)

# ==============================================================================
# --- ADIM 7: SEKMELİ KÜME GÖSTERİMLERİ (GİRİŞ/ÇIKIŞ BAĞIMSIZ GÖRÜNÜM) ---
# ==============================================================================
st.markdown("---")
st.markdown("### 🗺️ Sistem Yapısı ve Bulanık Küme Gösterimleri")

tab_giris, tab_cikis = st.tabs(
    ["📈 Giriş Değişkenleri — Üyelik Fonksiyonları", "🎯 Çıkış Değişkeni — Centroid Durulaştırma Kümesi"])

with tab_giris:
    st.write("Her giriş değişkeninin dilsel terimlerini ve mevcut dikey giriş çizgisini grafik üzerinde görün.")
    cx1, cx2, cx3 = st.columns(3)
    with cx1: st.pyplot(ciz_havali_grafik(tur_eslesme, "1. Tür Eşleşme Oranı", val_tur))
    with cx2: st.pyplot(ciz_havali_grafik(imdb, "2. IMDb Puanı", val_imdb))
    with cx3: st.pyplot(ciz_havali_grafik(trend, "3. Trend Skoru", val_trend))

    cx4, cx5, cx6 = st.columns(3)
    with cx4: st.pyplot(ciz_havali_grafik(yorum_orani, "4. Olumlu Yorum Oranı", val_yorum))
    with cx5: st.pyplot(ciz_havali_grafik(maliyet, "5. Erişilebilirlik (Maliyet)", val_maliyet))
    with cx6: st.pyplot(ciz_havali_grafik(dil_uyumu, "6. Dil ve Çeviri Uyumu", val_dil))

    cx7, cx8, cx9 = st.columns(3)
    with cx7: st.pyplot(ciz_havali_grafik(hassas_icerik, "7. Hassas İçerik Yoğunluğu", val_hassas))
    with cx8: st.pyplot(ciz_havali_grafik(yerlilik, "8. Yerlilik Oranı", val_yerlilik))
    with cx9: st.pyplot(ciz_havali_grafik(fragman_gucu, "9. Fragman Etkileşim Gücü", val_fragman))

    cx10, cx11, cx12 = st.columns(3)
    with cx10: st.pyplot(ciz_havali_grafik(prestij, "10. Ödül / Festival Başarısı", val_prestij))
    with cx11: st.pyplot(ciz_havali_grafik(odak_ihtiyaci, "11. Zihinsel Odak İhtiyacı", val_odak))
    with cx12: st.pyplot(ciz_havali_grafik(uyarlama_durumu, "12. Senaryo Özgünlük Derecesi", val_uyarlama))

    cx13, _, _ = st.columns(3)
    with cx13: st.pyplot(ciz_havali_grafik(vizyon_durumu, "13. Vizyon Tazeliği", val_vizyon))

with tab_cikis:
    st.write(
        "Çıkış değişkeninin tüm evrensel küme dağılım çizgileri ve dilsel terim sınırları kalıcı olarak görselleştirilmiştir.")
    fig_out_large, ax_out_large = plt.subplots(figsize=(10, 4.2))
    ax_out_large.set_facecolor('#1a1f2c')
    fig_out_large.patch.set_facecolor('#0e1117')

    colors_out = ['#ef4444', '#f59e0b', '#10b981']
    for i, term in enumerate(oneri_skoru.terms):
        ax_out_large.plot(oneri_skoru.universe, oneri_skoru[term].mf, label=term, color=colors_out[i], linewidth=2.5)
        ax_out_large.fill_between(oneri_skoru.universe, 0, oneri_skoru[term].mf, color=colors_out[i], alpha=0.15)

    ax_out_large.axvline(x=skor, color='#ff4b4b', linestyle='--', linewidth=3, label=f'Centroid Noktası: {skor:.2f}')
    ax_out_large.set_title("Nihai Öneri Skoru — Çıkış Kümesi Evrensel Dağılımı", color='white', fontweight='bold',
                           fontsize=12)
    ax_out_large.grid(True, color='#2d3748', linestyle=':', alpha=0.5)
    ax_out_large.tick_params(colors='white', labelsize=10)
    ax_out_large.legend(facecolor='#11151c', edgecolor='#2d3748', labelcolor='white', fontsize='medium')
    st.pyplot(fig_out_large)