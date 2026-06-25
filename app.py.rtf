{\rtf1\mac\ansicpg10000\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import pandas as pd\
import datetime\
\
st.set_page_config(page_title="Analiz\uc0\u259  Video \'cenot", page_icon="\u55356 \u57290 \u8205 \u9794 \u65039 ", layout="centered")\
\
st.title("\uc0\u55356 \u57290 \u8205 \u9794 \u65039  Monitorizare & Vitez\u259  Segmente")\
st.write("Introdu timpii direct de pe filmare (time-stamps) pentru a calcula automat duratele \uc0\u537 i vitezele.")\
\
# 1. Selectare Sportiv\
sportivi = ["Vlad Mihalache", "Vlad Matei", "Sportiv 3", "Sportiv 4"]\
sportiv_selectat = st.selectbox("Selecteaz\uc0\u259  Sportivul:", sportivi)\
\
# 2. Selectare Distan\uc0\u539 \u259  / Tip Prob\u259 \
optiuni_distanta = [\
    "Ultimii 5m",\
    "15m lpsa V1",\
    "15m lpsa V2",\
    "25m",\
    "35m",\
    "40m",\
    "50m"\
]\
distanta_proba = st.selectbox("Distan\uc0\u539 a / Proba:", optiuni_distanta)\
\
# 3. Configurare Split-uri\
nr_splituri = st.selectbox("\'cen c\'e2te split-uri \'eempar\uc0\u539 i distan\u539 a?", [1, 2, 3, 4], index=1)\
\
st.divider()\
\
# Func\uc0\u539 ii ajut\u259 toare pentru timp\
def la_secunde(s, sut):\
    return (s or 0) + ((sut or 0) / 100)\
\
def la_text(timp_sec):\
    sec = int(timp_sec)\
    sut = int(round((timp_sec - sec) * 100))\
    return f"\{sec\}.\{sut:02d\} s"\
\
# Ini\uc0\u539 ializare istoric \'een memorie\
if 'istoric_detaliat' not in st.session_state:\
    st.session_state.istoric_detaliat = []\
\
# --- FORMULAR INTRODUCERE DATE ---\
st.subheader("\uc0\u9201 \u65039  Introducere Timpi de pe Filmare")\
\
# Reperul de Start (0m sau linia LPSA)\
st.write("**\uc0\u55357 \u56525  START Video (Reperul Zero):**")\
col_st1, col_st2 = st.columns(2)\
with col_st1: sec_start = st.number_input("Secunde Start", min_value=0, step=1, key="sec_start")\
with col_st2: sut_start = st.number_input("Sutimi Start", min_value=0, max_value=99, step=1, key="sut_start")\
t_start = la_secunde(sec_start, sut_start)\
\
# Generare dinamic\uc0\u259  c\'e2mpuri pentru fiecare split\
metraje = []\
timpi_split = []\
\
st.write("---")\
for i in range(nr_splituri):\
    st.write(f"**Split \{i+1\}:**")\
    \
    # Coloana 1: Distan\uc0\u539 a \'een metri, Coloana 2 & 3: Timpul pe filmare\
    col_m, col_s, col_sut = st.columns([2, 3, 3])\
    \
    with col_m:\
        m = st.number_input(f"Metri (Split \{i+1\})", min_value=0.0, max_value=100.0, value=float((i+1)*10), step=0.5, key=f"m_\{i\}")\
        metraje.append(m)\
        \
    with col_s:\
        s = st.number_input(f"Secunde (Split \{i+1\})", min_value=0, step=1, key=f"s_\{i\}")\
    with col_sut:\
        sut = st.number_input(f"Sutimi (Split \{i+1\})", min_value=0, max_value=99, step=1, key=f"sut_\{i\}")\
        \
    timpi_split.append(la_secunde(s, sut))\
\
st.divider()\
\
# --- CALCUL \uc0\u536 I AFI\u536 ARE REZULTATE ---\
if st.button("\uc0\u55357 \u56522  Calculeaz\u259  \u537 i Salveaz\u259 ", type="primary"):\
    eroare = False\
    \
    # Validare de baz\uc0\u259  a timpilor introdu\u537 i\
    to\uc0\u539 i_timpii = [t_start] + timpi_split\
    for k in range(len(to\uc0\u539 i_timpii) - 1):\
        if to\uc0\u539 i_timpii[k+1] <= to\u539 i_timpii[k]:\
            eroare = True\
            st.error(f"Eroare: Timpul de la Split \{k+1\} trebuie s\uc0\u259  fie mai mare dec\'e2t cel dinaintea lui!")\
            break\
            \
    # Validare metraje cresc\uc0\u259 toare\
    for k in range(len(metraje) - 1):\
        if metraje[k+1] <= metraje[k]:\
            eroare = True\
            st.error("Eroare: Metrajele split-urilor trebuie s\uc0\u259  fie \'een ordine cresc\u259 toare!")\
            break\
\
    if not eroare and timpi_split[0] > 0:\
        st.subheader("\uc0\u55357 \u56520  Rezultate Segmente:")\
        \
        desfasurare_text = []\
        reper_timp_anterior = t_start\
        reper_metri_anterior = 0.0\
        \
        # Parcurgem fiecare segment pentru a calcula distan\uc0\u539 a par\u539 ial\u259 , durata \u537 i viteza\
        for idx in range(nr_splituri):\
            distanta_segment = metraje[idx] - reper_metri_anterior\
            durata_segment = timpi_split[idx] - reper_timp_anterior\
            viteza_segment = distanta_segment / durata_segment if durata_segment > 0 else 0\
            \
            eticheta_segment = f"\{reper_metri_anterior\}m -> \{metraje[idx]\}m"\
            text_rezultat = f"\{eticheta_segment\}: \{la_text(durata_segment)\} | Viteza: \{viteza_segment:.2f\} m/s"\
            \
            # Afi\uc0\u537 are direct \'een interfa\u539 \u259 \
            st.info(text_rezultat)\
            desfasurare_text.append(text_rezultat)\
            \
            # Reset\uc0\u259 m reperele pentru urm\u259 torul segment\
            reper_timp_anterior = timpi_split[idx]\
            reper_metri_anterior = metraje[idx]\
            \
        # Timp total curs\uc0\u259  (de la Start la ultimul split)\
        timp_total_calculat = timpi_split[-1] - t_start\
        st.success(f"\uc0\u9201 \u65039  **Timp Total Curs\u259  (\{metraje[-1]\}m): \{la_text(timp_total_calculat)\}**")\
        \
        # Salvare \'een istoric\
        rand_nou = \{\
            "Data/Ora": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),\
            "Sportiv": sportiv_selectat,\
            "Proba Selectat\uc0\u259 ": distanta_proba,\
            "Distan\uc0\u539 a Total\u259  (m)": metraje[-1],\
            "Timp Total": la_text(timp_total_calculat),\
            "Desf\uc0\u259 \u537 urare Segmente & Viteze": " | ".join(desfasurare_text)\
        \}\
        st.session_state.istoric_detaliat.append(rand_nou)\
\
st.divider()\
\
# 5. Afi\uc0\u537 are Istoric Antrenament\
st.subheader("\uc0\u55357 \u56523  Istoric Antrenament Curent")\
if st.session_state.istoric_detaliat:\
    df = pd.DataFrame(st.session_state.istoric_detaliat)\
    st.dataframe(df, use_container_width=True)\
    \
    # Export CSV\
    csv = df.to_csv(index=False).encode('utf-8')\
    st.download_button("\uc0\u55357 \u56549  Descarc\u259  fi\u537 ier pentru Excel (CSV)", data=csv, file_name="analiza_viteza_inot.csv", mime="text/csv")\
else:\
    st.info("Introduce\uc0\u539 i datele \u537 i ap\u259 sa\u539 i butonul de calcul pentru a genera istoricul.")}