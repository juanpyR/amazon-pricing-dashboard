# 📦 Amazon Pricing Dashboard

An interactive dashboard for Amazon product analysis and dynamic pricing insights built with Python, Streamlit, and data visualization tools.

---

## 🚀 Key Features

- Load and analyze Amazon product datasets
- Dynamic filtering by:
  - Category
  - Brand
  - Price range
- Business KPIs:
  - Revenue
  - Profit
  - Margin
  - Ratings
- Visualizations:
  - Bar charts (e.g., top brands by profit)
  - Histograms
  - Scatter plots
  - Pie charts (optional)
- Table of top 10 most profitable products
- Download filtered data as CSV

---

## 🛠 Technologies Used

- Python 3.x
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [NumPy](https://numpy.org/)

---
## 🖼 Screenshots

### 📊 Metrics Panel

![Metrics](https://github.com/juanpyR/amazon-pricing-dashboard/raw/main/Images/Metrics.png)

### 🎛 Filters

![Filters](https://github.com/juanpyR/amazon-pricing-dashboard/raw/main/Images/Filters.png)

### 📈 Charts

![Charts](https://github.com/juanpyR/amazon-pricing-dashboard/raw/main/Images/charts.png)

### 🔍 Filtered Data

![Filtered](https://github.com/juanpyR/amazon-pricing-dashboard/raw/main/Images/filtered.png)

### 🏆 Top 10 Products

![Top10](https://github.com/juanpyR/amazon-pricing-dashboard/raw/main/Images/top10.png)

## ▶️ How to Run

1. Clone this repository:

```
git clone https://github.com/tuUsuario/amazon-pricing-dashboard.git
cd amazon-pricing-dashboard
```

2. Install dependencies:

```
pip install -r requirements.txt
```

> Or install manually:

```
pip install streamlit pandas numpy scikit-learn matplotlib seaborn
```

3. Run the app:

```
streamlit run amazon-pricing-dashboard.py
```

4. The app will open automatically at `http://localhost:8501` (or another available port) in your browser.

## 📊 Usage Summary
| Feature                        | Description                          |
|-------------------------------|------------------------------------|
| File Upload                   | Upload Amazon products CSV          |
| Filters                       | Select categories, brands, price   |
| Metrics                       | Revenue, profit, margin, ratings   |
| Visualizations                | Bar charts, scatter plots, histograms |
| Data Export                   | Download filtered data as CSV      |

## 🤝 Contributions
Contributions are welcome! If you find bugs or have ideas, please open an issue or submit a pull request.

## 📄 License
MIT License – you're free to use, modify, and distribute this project.
