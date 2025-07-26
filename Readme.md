# 📦 Amazon Pricing Dashboard

An interactive dashboard for Amazon product analysis and dynamic pricing insights built with Python, Streamlit, and data visualization tools.

---

## 🚀 Key Features

- Upload and dynamically filter Amazon product CSV datasets.
- Key metrics including total revenue, profit, average margin, top-performing products, and more.
- Visualizations:
  - Units sold by category
  - Profit by brand (top 15)
  - Margin vs. price scatter plot
  - Product rating distribution (if available)
- View top 10 most profitable products.
- Download filtered dataset as CSV.
- User-friendly and customizable interface.

---

## 🛠 Technologies Used

- Python 3.x
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [NumPy](https://numpy.org/)

---

## 📁 Project Structure

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
