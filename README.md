# shopping-trends-dashboard

Această aplicație este un instrument interactiv de analiză a datelor comerciale, creat pentru a identifica tiparele de consum în funcție de demografie, sezonalitate și categorii de produse. Proiectul a fost realizat pentru materia **Pachete Software**.

**Link aplicație:** [https://shopping-trends-dashboard-akbpkyoranfwpjh2zwnf2d.streamlit.app/](https://shopping-trends-dashboard-akbpkyoranfwpjh2zwnf2d.streamlit.app/)

---

## Scurta descriere:
Aplicația procesează seturi de date în format CSV referitoare la tendințele de cumpărături și oferă vizualizări dinamice pentru a facilita luarea deciziilor bazate pe date brute.

### Funcționalități principale:
* **Încărcare Date:** Interfață de tip drag-and-drop pentru fișiere CSV.
* **Statistici Generale:** Calcul automat și afișare metrici (Vârstă medie, Cheltuială medie, Rating).
* **Filtrare Dinamică:** Sidebar interactiv pentru filtrarea datelor după Gen, Sezon și Categorie.
* **Vizualizări Interactive (Plotly):**
    * **Pie Chart:** Distribuția clienților pe genuri.
    * **Bar Chart:** Analiza cheltuielilor medii pe categorii de produse.
    * **Sunburst Chart:** Analiza ierarhică a relației dintre Sezon, Categorie și Gen.

---

##  Instalare și Rulare Locală
Dacă doriți să rulați proiectul pe propriul calculator:

1. Clonați repository-ul.
2. Instalați dependințele necesare:
   ```bash
   pip install -r requirements.txt
3. Lansați aplicația în browser:
      ```bash
   streamlit run dashboard.py
