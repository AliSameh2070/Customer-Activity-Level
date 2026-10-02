
import numpy as np
import pandas as pd
import streamlit as st
import pickle as pkl

st.set_page_config(
    page_title="Customer Activity level",
    page_icon="👦🏼",
    layout="centered"
)

with open("KMeans3_model.pkl", "rb") as file:
    model = pkl.load(file)

df = pd.read_csv("CC GENERAL.csv")
df_clustered = pd.read_csv("CC GENERAL_clustered.csv")

df['MINIMUM_PAYMENTS'].fillna(df['MINIMUM_PAYMENTS'].median(), inplace=True)
df['CREDIT_LIMIT'].fillna(df['CREDIT_LIMIT'].mean(), inplace=True)

df_no_na = df.copy()

df_no_na['CREDIT_LIMIT_PER_TENURE'] = df_no_na['CREDIT_LIMIT'] / df_no_na['TENURE']

df_no_na['BALANCE_PER_TENURE'] = df_no_na['BALANCE'] / df_no_na['TENURE']

df_no_na['REMAINING_CREDIT_LIMIT'] = df_no_na['CREDIT_LIMIT'] - df_no_na['BALANCE']

df_FE = df_no_na.copy()

X = df_FE.drop(['CUST_ID'], axis=1)

st.title ("👨🏼 Customer Activity Level")

st.write("Enter the customer's information to determine the Activity Level")

balance = st.number_input(
    "Balance",
    min_value=float(df_no_na["BALANCE"].min()),
    max_value=float(df_no_na["BALANCE"].max()),
    value=float(df_no_na["BALANCE"].median())
)

balance_frequency = st.number_input(
    "Balance Frequency",
    min_value=float(df_no_na["BALANCE_FREQUENCY"].min()),
    max_value=float(df_no_na["BALANCE_FREQUENCY"].max()),
    value=float(df_no_na["BALANCE_FREQUENCY"].median())
)

purchases = st.number_input(
    "Purchases",
    min_value=float(df_no_na["PURCHASES"].min()),
    max_value=float(df_no_na["PURCHASES"].max()),
    value=float(df_no_na["PURCHASES"].median())
)

oneoff_purchases = st.number_input(
    "One-off Purchases",
    min_value=float(df_no_na["ONEOFF_PURCHASES"].min()),
    max_value=float(df_no_na["ONEOFF_PURCHASES"].max()),
    value=float(df_no_na["ONEOFF_PURCHASES"].median())
)

installments_purchases = st.number_input(
    "Installments Purchases",
    min_value=float(df_no_na["INSTALLMENTS_PURCHASES"].min()),
    max_value=float(df_no_na["INSTALLMENTS_PURCHASES"].max()),
    value=float(df_no_na["INSTALLMENTS_PURCHASES"].median())
)

cash_advance = st.number_input(
    "Cash Advance",
    min_value=float(df_no_na["CASH_ADVANCE"].min()),
    max_value=float(df_no_na["CASH_ADVANCE"].max()),
    value=float(df_no_na["CASH_ADVANCE"].median())
)

purchases_frequency = st.number_input(
    "Purchases Frequency",
    min_value=float(df_no_na["PURCHASES_FREQUENCY"].min()),
    max_value=float(df_no_na["PURCHASES_FREQUENCY"].max()),
    value=float(df_no_na["PURCHASES_FREQUENCY"].median())
)

oneoff_purchases_frequency = st.number_input(
    "One-off Purchases Frequency",
    min_value=float(df_no_na["ONEOFF_PURCHASES_FREQUENCY"].min()),
    max_value=float(df_no_na["ONEOFF_PURCHASES_FREQUENCY"].max()),
    value=float(df_no_na["ONEOFF_PURCHASES_FREQUENCY"].median())
)

purchases_installments_frequency = st.number_input(
    "Purchases Installments Frequency",
    min_value=float(df_no_na["PURCHASES_INSTALLMENTS_FREQUENCY"].min()),
    max_value=float(df_no_na["PURCHASES_INSTALLMENTS_FREQUENCY"].max()),
    value=float(df_no_na["PURCHASES_INSTALLMENTS_FREQUENCY"].median())
)

cash_advance_frequency = st.number_input(
    "Cash Advance Frequency",
    min_value=float(df_no_na["CASHADVANCEFREQUENCY"].min()),
    max_value=float(df_no_na["CASHADVANCEFREQUENCY"].max()),
    value=float(df_no_na["CASHADVANCEFREQUENCY"].median())
)

cash_advance_trx = st.number_input(
    "Cash Advance Transactions",
    min_value=float(df_no_na["CASHADVANCETRX"].min()),
    max_value=float(df_no_na["CASHADVANCETRX"].max()),
    value=float(df_no_na["CASHADVANCETRX"].median())
)

purchases_trx = st.number_input(
    "Purchases Transactions",
    min_value=float(df_no_na["PURCHASES_TRX"].min()),
    max_value=float(df_no_na["PURCHASES_TRX"].max()),
    value=float(df_no_na["PURCHASES_TRX"].median())
)

credit_limit = st.number_input(
    "Credit Limit",
    min_value=float(df_no_na["CREDIT_LIMIT"].min()),
    max_value=float(df_no_na["CREDIT_LIMIT"].max()),
    value=float(df_no_na["CREDIT_LIMIT"].median())
)

payments = st.number_input(
    "Payments",
    min_value=float(df_no_na["PAYMENTS"].min()),
    max_value=float(df_no_na["PAYMENTS"].max()),
    value=float(df_no_na["PAYMENTS"].median())
)

minimum_payments = st.number_input(
    "Minimum Payments",
    min_value=float(df_no_na["MINIMUM_PAYMENTS"].min()),
    max_value=float(df_no_na["MINIMUM_PAYMENTS"].max()),
    value=float(df_no_na["MINIMUM_PAYMENTS"].median())
)

prc_full_payment = st.number_input(
    "Percent Full Payment",
    min_value=float(df_no_na["PRC_FULL_PAYMENT"].min()),
    max_value=float(df_no_na["PRC_FULL_PAYMENT"].max()),
    value=float(df_no_na["PRC_FULL_PAYMENT"].median())
)

tenure = st.number_input(
    "Tenure",
    min_value=float(df_no_na["TENURE"].min()),
    max_value=float(df_no_na["TENURE"].max()),
    value=float(df_no_na["TENURE"].median())
)

if st.button("Submit", use_container_width=True):

    input_data = pd.DataFrame({
        "BALANCE": [balance],
        "BALANCE_FREQUENCY": [balance_frequency],
        "PURCHASES": [purchases],
        "ONEOFF_PURCHASES": [oneoff_purchases],
        "INSTALLMENTS_PURCHASES": [installments_purchases],
        "CASH_ADVANCE": [cash_advance],
        "PURCHASES_FREQUENCY": [purchases_frequency],
        "ONEOFFPURCHASESFREQUENCY": [oneoff_purchases_frequency],
        "PURCHASES_INSTALLMENTS_FREQUENCY": [purchases_installments_frequency],
        "CASHADVANCEFREQUENCY": [cash_advance_frequency],
        "CASHADVANCETRX": [cash_advance_trx],
        "PURCHASES_TRX": [purchases_trx],
        "CREDIT_LIMIT": [credit_limit],
        "PAYMENTS": [payments],
        "MINIMUM_PAYMENTS": [minimum_payments],
        "PRC_FULL_PAYMENT": [prc_full_payment],
        "TENURE": [tenure]
    })

    input_data["CREDIT_LIMIT_PER_TENURE"] = (
        input_data["CREDIT_LIMIT"] / input_data["TENURE"]
    )

    input_data["BALANCE_PER_TENURE"] = (
        input_data["BALANCE"] / input_data["TENURE"]
    )

    input_data["REMAINING_CREDIT_LIMIT"] = (
        input_data["CREDIT_LIMIT"] - input_data["BALANCE"]
    )

    input_data = input_data[X.columns]

    cluster = model.predict(input_data)[0]

    if cluster == 0:
        st.success("Customer Activity Level: High Activity")
    else:
        st.info("Customer Activity Level: Low Activity")
    cluster_data = df_clustered[df_clustered["Cluster"] == cluster]

cluster_size = len(cluster_data)
cluster_percentage = cluster_size / len(df_clustered) * 100

st.write("Customers in this activity group:", cluster_size)
st.write("Percentage of customers:", f"{cluster_percentage:.2f}%")
