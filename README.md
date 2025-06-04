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
```

---

## 📈 Dashboard Features

- Select a major ETF or index fund (e.g., SPY, QQQ, VTI).
- Slider to choose how many bottom-performing stocks to buy each day.
- Slider to select how many days to hold each position.
- Visual outputs:
  - Cumulative strategy PnL
  - Daily returns time series
  - Trade summary and parameters

---

## ✅ Supported Index Funds

Use any valid `yfinance`-compatible ticker. Common examples:

| Fund Name               | Ticker |
|------------------------|--------|
| S&P 500 ETF            | SPY    |
| NASDAQ 100 ETF         | QQQ    |
| Total US Market ETF    | VTI    |
| Dow Jones ETF          | DIA    |

Modify or extend tickers in `data/fetch_data.py`.

---

## ⚠️ Assumptions & Simplifications

- Equal-weighted portfolio allocation
- Prices use **adjusted close**
- No slippage or transaction costs modeled
- Perfect liquidity assumed
- No rebalancing between holding periods


## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/tajpatel58/BacktestingReversal.git
cd BacktestingReversal
```

---

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to avoid dependency conflicts:

```bash
python -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

Install all required Python packages using pip:

```bash
pip install -r requirements.txt
```

---

### 4. Run the Streamlit App

Launch the dashboard:

```bash
streamlit run app.py
```

Then open your browser to [http://localhost:8501](http://localhost:8501) if it doesn't open automatically.

---
