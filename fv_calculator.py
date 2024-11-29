import streamlit as st

# Title
st.title("Future Value Calculator")

# Inputs from the user
principal = st.slider("Principal Amount (per period)", min_value=1000, max_value=100000, step=1000)
rate = st.slider("Rate of Interest (p.a.)", min_value=0.1, max_value=15.0, step=0.1) / 100
years = st.slider("Time Period (in years)", min_value=1, max_value=50, step=1)
compounding_frequency = st.selectbox("Compounding Frequency", ["Yearly", "Half-Yearly", "Quarterly", "Monthly", "Weekly"])

# Determine number of compounding periods per year
if compounding_frequency == "Yearly":
    n = 1
elif compounding_frequency == "Half-Yearly":
    n = 2
elif compounding_frequency == "Quarterly":
    n = 4
elif compounding_frequency == "Monthly":
    n = 12
elif compounding_frequency == "Weekly":
    n = 52

# Total Investment Calculation
total_investment = principal * (n * years)

# Future Value Calculation
future_value = principal * ((1 + (rate / n)) ** (n * years))

# Total Interest Calculation
total_interest = future_value - total_investment

# Display the results
st.write(f"Principal Amount (per period): ₹{principal}")
st.write(f"Total Investment: ₹{total_investment}")
st.write(f"Total Interest: ₹{total_interest}")
st.write(f"Future Value: ₹{future_value}")
