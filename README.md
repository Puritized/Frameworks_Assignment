
# Frameworks_Assignment – CORD-19 Data Explorer

## 📌 Overview
This project analyses the **CORD-19 metadata.csv** dataset, which contains information about COVID-19 research papers.  
We performed data cleaning, basic exploratory analysis, and built a **Streamlit app** to visualise findings interactively.

---

## ⚙️ Tools Used
- Python 3.8+
- pandas (data cleaning)
- matplotlib & seaborn (visualisation)
- WordCloud (text analysis)
- Streamlit (interactive app)
- Jupyter Notebook (exploration)

---

## 📊 Key Findings
- **Publications by Year**: Research output peaked in 2020–2021 due to the COVID-19 pandemic.
- **Top Journals**: Certain journals contributed the highest volume of COVID-19 related publications.
- **Common Words**: Titles often include terms like *COVID-19*, *SARS-CoV-2*, *pandemic*, and *health*.

---

## 🚀 Running the Project
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Frameworks_Assignment.git
   cd Frameworks_Assignment
   ```
2. Install requirements:
   ```bash
   pip install pandas matplotlib seaborn wordcloud streamlit
   ```
3. Run analysis notebook in Jupyter:
   ```bash
   jupyter notebook analysis.ipynb
   ```
4. Launch Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## 📘 Reflection
- **Challenges**: Handling missing values in titles, abstracts, and dates. The dataset is large, so filtering was important.
- **What I learned**:
  - How to clean and prepare real-world research data.
  - Generating simple but meaningful visualisations.
  - Building an interactive dashboard with Streamlit.

---

## 📂 Repo Structure
```
Frameworks_Assignment/
│── analysis.ipynb
│── app.py
│── README.md
│── metadata.csv (sample, not full dataset)
```
