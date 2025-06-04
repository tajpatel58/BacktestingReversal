import streamlit as st
import datetime

st.set_page_config(page_title="Bottom-X Reversal Backtest", layout="wide")
st.title("📉 Backtesting Bottom-X Stock Reversal Strategy")

# Sidebar inputs
st.sidebar.header("Backtest Configuration")

available_funds = ["SPY", "QQQ", "VTI", "DIA", "DJI"]
tickers = st.sidebar.multiselect("Select Index Fund(s) (ETF)", options=available_funds, default=["SPY"])
bottom_n = st.sidebar.slider("Number of Bottom Performing Stocks (X)", 1, 20, 5)
holding_days = st.sidebar.slider("Holding Period (Y days)", 1, 30, 5)
start_date = st.sidebar.date_input("Start Date", datetime.date(2022, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.date(2023, 1, 1))

initial_capital = 100_000

if tickers:
    selected_tickers = ", ".join(tickers)
    st.subheader(f"Backtesting {selected_tickers} from {start_date} to {end_date}")
    st.write(f"Initial Capital: ${initial_capital:,.0f}")

    # Placeholder for performance metrics table
    st.markdown("### Strategy Metrics (Coming Soon)")
    st.dataframe({
        "Metric": ["Final Portfolio Value", "Annualized Return", "Max Drawdown"],
        "Value": ["$XXX,XXX", "XX.X%", "-X.X%"]
    })
else:
    st.warning("Please select at least one index fund to run the backtest.")
