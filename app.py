import streamlit as st
import pandas as pd
import altair as alt
import datetime

st.set_page_config(page_title="Bottom-X Reversal Backtest", layout="wide")
st.title("📉 Backtesting Reversal Strategy")

# Sidebar inputs
st.sidebar.header("Backtest Configuration")

available_funds = ["SPY", "QQQ", "VTI", "DIA", "DJI"]
tickers = st.sidebar.multiselect("Select Index Fund(s) (ETF)", options=available_funds, default=["SPY"])
bottom_n = st.sidebar.slider("Number of Bottom Performing Stocks (X)", 1, 20, 5)
holding_days = st.sidebar.slider("Holding Period (Y days)", 1, 30, 5)
start_date = st.sidebar.date_input("Start Date", datetime.date(2022, 1, 1), format="DD/MM/YYYY")
end_date = st.sidebar.date_input("End Date", datetime.date(2023, 1, 1), format="DD/MM/YYYY")

initial_capital = 100_000

if tickers:
    selected_tickers = ", ".join(tickers)
    st.subheader(f"Backtesting {selected_tickers} from {start_date} to {end_date}")
    st.write(f"Initial Capital: ${initial_capital:,.0f}")

    # Placeholder DataFrame for performance plot
    index_performance_df = pd.DataFrame({
        "dates": pd.date_range(start=start_date, end=end_date, periods=100),
        "investment_value": [initial_capital * (1 + i / 100) for i in range(100)]
    })

    # Plotting portfolio performance
    st.markdown("### Investment Value Over Time")
    line_chart = alt.Chart(index_performance_df).mark_line().encode(
        x=alt.X("dates:T", axis=alt.Axis(title="Dates")),
        y=alt.Y("investment_value:Q", axis=alt.Axis(title="Investment Value"))
    ).properties(
        width=1200,
        height=400
    )
    st.altair_chart(line_chart, use_container_width=True)

    # Placeholder for performance metrics table
    st.markdown("### Performance Metrics")
    st.dataframe({
        "Metric": ["Final Portfolio Value", "Annualized Return", "Max Drawdown", "Sharpe Ratio"],
        "Value": ["$XXX,XXX", "XX.X%", "-X.X%", "XX"]
    })

else:
    st.warning("Please select at least one index fund to run the backtest.")