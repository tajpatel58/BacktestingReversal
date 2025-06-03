# 📊 Backtest Dashboard: Bottom-X Stock Reversal Strategy

This Streamlit dashboard allows you to backtest a simple **bottom-X reversal strategy** on major index funds using historical stock data from `yfinance`.

---

## 🚀 Strategy Description

For each trading day in the historical window:

- Select the **X worst-performing stocks** in the selected index fund (based on daily % change).
- Buy all selected stocks at **close of day T**.
- Hold each for **Y days**.
- Sell them at **close of day T+Y**.
- Repeat daily and track the cumulative performance.

Default initial capital is **$100,000**, allocated equally among selected stocks.

---

## 📂 Project Structure

```text
backtest-dashboard/
│
├── app.py                    
├── requirements.txt           
├── README.md                   
│
├── data/
│   └── fetch_data.py   
│ 
│──  
