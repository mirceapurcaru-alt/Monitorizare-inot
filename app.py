import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Analiză Video Înot", page_icon="🏊‍♂️", layout="centered")

st.title("🏊‍♂️ Monitorizare & Viteză Segmente")
st.write("Introdu timpii direct de pe filmare (time-stamps) pentru a calcula automat duratele și vitezele.")

sportivi = ["Vlad Mihalache", "Vlad Matei", "Sportiv 3", "Sportiv 4"]
sportiv_selectat = st.selectbox("Selectează Sportivul:", sportivi)

optiuni_distanta = ["Ultimii 5m", "15m lpsa V1", "15m lpsa V2", "25m", "35m", "40m", "50m"]
distanta_proba = st.selectbox("Distanța / Proba:", optiuni_distanta)

nr_splituri = st.selectbox("În câte split-uri împarți distanța?", [1, 2, 3, 4], index=1)

st.divider()

def la_secunde(s, sut):
    return (s or 0) + ((sut or 0) / 100)

def la_text(timp_sec):
    sec = int(timp_sec)
    sut = int(round((timp_sec - sec) * 100))
    return f"{sec}.{sut:02d} s"

if 'istoric_detaliat' not in st.session_state:
    st.session_state.istoric_detaliat = []

st.subheader("⏱️ Introducere Timpi de pe Filmare")

st.write("**📍 START Video (Reperul Zero):**")
col_st1, col_st2 = st.columns(2)
with col_st1: sec_start = st.number_input("Secunde Start", min_value=0, step=1, key="sec_start")
with col_st2: sut_start = st.number_input("Sutimi Start", min_value=0, max_value=99, step=1, key="sut_start")
t_start = la_secunde(sec_start, sut_start)

st.write("---")
metraje = []
timpi_split = []

for i in range(nr_splituri):
    st.write(f"**Split {i+1}:**")
    col_m, col_s, col_sut = st.columns([2, 3, 3])
    with col_m:
        m = st.number_input(f"Metri (Split {i+1})", min_value=0.0, max_value=100.0, value=float((i+1)*10), step=0.5, key=f"m_{i}")
        metraje.append(m)
    with col_s: s = st.number_input(f"Secunde (Split {i+1})", min_value=0, step=1, key=f"s_{i}")
    with col_sut: sut = st.number_input(f"Sutimi (Split {i+1})", min_value=0, max_value=99, step=1, key=f"sut_{i}")
    timpi_split.append(la_secunde(s, sut))

st.divider()

if st.button("📊 Calculează și Salvează", type="primary"):
    eroare = False
    toți_timpii = [t_start] + timpi_split
    for k in range(len(toți_timpii) - 1):
        if toți_timpii[k+1] <= toți_timpii[k]:
            eroare = True
            st.error(f"Eroare: Timpul de la Split {k+1} trebuie să fie mai mare decât cel dinaintea lui!")
            break
    for k in range(len(metraje) - 1):
        if metraje[k+1] <= metraje[k]:
            eroare = True
            st.error("Eroare: Metrajele split-urilor trebuie să fie în ordine crescătoare!")
            break

    if not eroare and timpi_split[0] > 0:
        st.subheader("📈 Rezultate Segmente:")
        desfasurare_text = []
        reper_timp_anterior = t_start
        reper_metri_anterior = 0.0
        
        for idx in range(nr_splituri):
            distanta_segment = metraje[idx] - reper_metri_anterior
            durata_segment = timpi_split[idx] - reper_timp_anterior
            viteza_segment = distanta_segment / durata_segment if durata_segment > 0 else 0
            eticheta_segment = f"{reper_metri_anterior}m -> {metraje[idx]}m"
            text_rezultat = f"{eticheta_segment}: {la_text(durata_segment)} | Viteza: {viteza_segment:.2f} m/s"
            st.info(text_rezultat)
            desfasurare_text.append(text_rezultat)
            reper_timp_anterior = timpi_split[idx]
            reper_metri_anterior = metraje[idx]
            
        timp_total_calculat = timpi_split[-1] - t_start
        st.success(f"⏱️ **Timp Total Cursă ({metraje[-1]}m): {la_text(timp_total_calculat)}**")
        
        rand_nou = {
            "Data/Ora": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
            "Sportiv": sportiv_selectat,
            "Proba Selectată": distanta_proba,
            "Distanța Totală (m)": metraje[-1],
            "Timp Total": la_text(timp_total_calculat),
            "Desfășurare Segmente & Viteze": " | ".join(desfasurare_text)
        }
        st.session_state.istoric_detaliat.append(rand_nou)

st.divider()

st.subheader("📋 Istoric Antrenament Curent")
if st.session_state.istoric_detaliat:
    df = pd.DataFrame(st.session_state.istoric_detaliat)
    st.dataframe(df, use_container_width=True)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Descarcă fișier pentru Excel (CSV)", data=csv, file_name="analiza_viteza_inot.csv", mime="text/csv")
else:
    st.info("Introduceți datele și apăsați butonul de calcul pentru a genera istoricul.")
