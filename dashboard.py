import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard", layout="wide")

st.markdown("""
<style>

body {
background-color:#0f0f0f;
color:white;
}

.block-container {
padding-top:2rem;
}

h1,h2,h3{
color:#ff5c00;
}

</style>
""", unsafe_allow_html=True)

st.title("Shopping Trends Dashboard")


# ── Încărcare date ────────────────────────────────────────────────
fisier = st.file_uploader("Încarcă fișierul CSV", type=["csv"])

if fisier is None:
    st.info("Încarcă un fișier CSV pentru a continua.")
    st.stop()

df = pd.read_csv(fisier)

# ── Statistici generale ───────────────────────────────────────────
st.header(" Date și statistici")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Număr clienți",len(df))
col2.metric("Vârstă medie",round(df["Age"].mean(),1))
col3.metric("Cheltuială medie",round(df["Purchase Amount (USD)"].mean(),2))
col4.metric("Rating mediu",round(df["Review Rating"].mean(),2))

st.dataframe(df.head(10),use_container_width=True)

st.markdown("---")

# ── Filtre în sidebar ─────────────────────────────────────────────
st.sidebar.header("Filtre")

gen = st.sidebar.multiselect(
"Gen",
df["Gender"].unique(),
default=df["Gender"].unique()
)

sezon = st.sidebar.multiselect(
"Sezon",
df["Season"].unique(),
default=df["Season"].unique()
)

categorie = st.sidebar.multiselect(
"Categorie",
df["Category"].unique(),
default=df["Category"].unique()
)

df_filtrat = df[
(df["Gender"].isin(gen)) &
(df["Season"].isin(sezon)) &
(df["Category"].isin(categorie))
]

# ── Grafic 1 — Plotly ─────────────────────────────────────────────
st.header("Vizualizări și interpretări")

col1, col2 = st.columns([2,1])

# calcul distributie
gender_counts = df_filtrat["Gender"].value_counts()

male = gender_counts.get("Male",0)
female = gender_counts.get("Female",0)

total = male + female

male_pct = round(male/total*100,1) if total>0 else 0
female_pct = round(female/total*100,1) if total>0 else 0

fig1 = px.pie(
    df_filtrat,
    names="Gender",
    title="Distribuția clienților după gen",
    color="Gender",
    color_discrete_map={
        "Female": "#ffc0cb",
        "Male": "#4c78a8"
    }
)

col1.plotly_chart(fig1, use_container_width=True)

col2.markdown(f"""
### Interpretare

În datasetul analizat există **{male} bărbați** și **{female} femei**.

Observăm că datasetul este **dominant masculin**, ceea ce poate influența rezultatele analizelor privind comportamentul de cumpărare.

""")

st.markdown("---")

col1, col2 = st.columns([2,1])

fig2 = px.bar(
    df_filtrat.groupby("Category")["Purchase Amount (USD)"].mean().reset_index(),
    x="Category",
    y="Purchase Amount (USD)",
    color="Category",
    title="Cheltuiala medie pe categorie de produse"
)

col1.plotly_chart(fig2, use_container_width=True)

col2.markdown("""
###  Interpretare

Graficul arată **cheltuiala medie pentru fiecare categorie de produs**.

Acesta ne ajută să identificăm:
- ce categorii generează **venituri mai mari**
- ce produse sunt **mai populare**

""")

st.markdown("---")

st.markdown("##  Relația dintre sezon, categorie și gen")

fig3 = px.sunburst(
    df_filtrat,
    path=["Season","Category","Gender"],
    values="Purchase Amount (USD)",
    title="Cum se distribuie cumpărăturile în funcție de sezon și categorie"
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
### 
Putem observa:
- în ce **sezon** se fac cele mai multe cumpărături
- ce **categorii de produse** sunt populare în fiecare sezon
- diferențe între **genuri** în comportamentul de cumpărare.

Acest tip de vizualizare este util pentru identificarea **pattern-urilor de consum**.
""")
