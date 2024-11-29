import streamlit as st

# Title
st.title("Future Value Calculator")

# Input fields
principal = st.number_input("Principal Amount (₹)", min_value=0.0, step=100.0)
rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, step=0.1)
time = st.number_input("Time Period (Years)", min_value=0, step=1)
compounding_frequency = st.selectbox("Compounding Frequency", ["Yearly", "Half-Yearly", "Quarterly", "Monthly", "Daily"])

# Frequency mapping
frequency_map = {"Yearly": 1, "Half-Yearly": 2, "Quarterly": 4, "Monthly": 12, "Daily": 365}
n = frequency_map[compounding_frequency]

# Calculation
if st.button("Calculate"):
    future_value = principal * ((1 + (rate / 100) / n) ** (n * time))
    total_interest = future_value - principal
    total_investment = principal  # Total Investment is the initial amount provided by the user
    
    # Display Results
    st.subheader(f"Future Value: ₹{future_value:,.2f}")
    st.subheader(f"Total Interest Earned: ₹{total_interest:,.2f}")
    st.subheader(f"Total Investment: ₹{total_investment:,.2f}")
