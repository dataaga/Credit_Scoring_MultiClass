import streamlit as st
import pickle
import joblib
import pandas as pd
from zipfile import ZipFile
import os
from src import transform_resp
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import urllib


st.set_page_config(page_title='KreditDulu Credit Scoring App', page_icon='💳', layout='wide',
                   initial_sidebar_state='auto', 
     )

###LOAD PHASE###

scaler = pickle.load(open('scaler_mockup.obj', 'rb'))
model = pickle.load(open('XGB_creditscoring_final_mockup.obj', 'rb'))




###INITIAL PHASE###

age_default = None
annual_income_default = 0.00
monthly_income_default = 0.00
accounts_default = 0
interest_rate_default = None
num_loan_default = 0
credit_cards_default = 0
changed_credit_limit_default = 0
delayed_payments_default = 0
delay_duration_default = 0
month_default = 0
new_credit_default = 0
outstanding_debt_default = 0.00
emi_monthly_default = 0.00
credit_history_default = 0
loans_default = None
minimum_payment_default = 0


logo = Image.open(urllib.request.urlopen('https://github.com/dataaga/Credit_Scoring_MultiClass/blob/main/LogoKredit.png?raw=true'))
col1, col2, col3 = st.columns([0.1,0.8,0.1])
with col1:
    st.write(' ')

with col2:
    st.image(logo)

with col3:
    st.write(' ')


st.title('Credit Scoring Prediction')

st.markdown('''
            Ever wondered how to figure out someone's creditworthiness?
            Say hello to our Credit Scoring Prediction app to see a clear picture of an individual's borrowing potential.
            By blending manual data & alternate data, it will give you view of a person's credit story.
            Our app's here to help you understand better whether you're lending the money or not.
''')

###PICKING PROFILE FROM 1 NAME PHASE###

profile = st.radio('Choose a profile:', options=['Bapak Joko', 'Ibu Marina', 'Bapak Tega'], horizontal=True)
if profile == 'Bapak Joko':
    age_default = 37
    annual_income_default = 30000.00
    monthly_income_default = 2400.00
    accounts_default = 3
    interest_rate_default = 7
    num_loan_default = 2
    credit_cards_default = 4
    changed_credit_limit_default = 0
    delayed_payments_default = 5
    delay_duration_default = 0
    month_default = 0
    new_credit_default = 0
    outstanding_debt_default = 100.00
    emi_monthly_default = 80.00
    credit_history_default = 222
    loans_default = ['Mortgage_Loan']
    minimum_payment_default = ['No']
elif profile == 'Ibu Marina':
    age_default = 52
    annual_income_default = 50000.00
    monthly_income_default = 3000.00
    accounts_default = 4
    interest_rate_default = 3
    num_loan_default = 2
    credit_cards_default = 10
    changed_credit_limit_default = 10
    delayed_payments_default = 5
    delay_duration_default = 5
    month_default = 0
    new_credit_default = 3
    outstanding_debt_default = 1000.00
    emi_monthly_default = 350.00
    credit_history_default = 350
    loans_default = ['Personal_Loan', 'Debt_Consolidation_Loan']
    minimum_payment_default = ['No']
elif profile == 'Bapak Tega':
    age_default = 28
    annual_income_default = 30085.00
    monthly_income_default = 2000.00
    accounts_default = 3
    interest_rate_default = 0
    num_loan_default = 2
    credit_cards_default = 4
    changed_credit_limit_default = 2
    delayed_payments_default = 5
    delay_duration_default = 3
    month_default = 6
    new_credit_default = 3
    outstanding_debt_default = 500.00
    emi_monthly_default = 250.00
    credit_history_default = 100
    loans_default = ['Student_Loan']
    minimum_payment_default = ['Yes']

st.subheader("Don't Forget to click :violet[RUN] button on the left side bar &mdash;\
            💰📈💹🏦📊💵")
st.markdown('Note: Some of feature had to drop because some technical issues')


###INPUT FROM PROFILE OR FROM SIDEBAR ONLY PHASE###

with st.sidebar:
    st.header('You Can fill Your Data Here')
    age = st.slider('What is your age?', min_value=18, max_value=100, step=1, value=age_default)
    annual_income = st.number_input('What is your Annual Income?', min_value=0.00, max_value=300000.00, value=annual_income_default)
    monthly_income = st.number_input('What is your Monthly Income?', min_value=0.00, max_value=15000.00, value=monthly_income_default)
    accounts = st.number_input('How many bank accounts do you have?', min_value=0, max_value=20, step=1, value=accounts_default)
    interest_rate = st.number_input('What is the last interest rate do you have?', min_value=0, max_value=30, step=1, value=interest_rate_default)
    num_loan = st.number_input('How many number of loan do you have?', min_value=0, max_value=9, step=1, value=num_loan_default)
    credit_cards = st.number_input('How many credit cards do you have?', min_value=0, max_value=12, step=1, value=credit_cards_default)
    changed_credit_limit = st.number_input('How is the limit of credit changed?', min_value=0, max_value=36, step=1, value=changed_credit_limit_default)
    delayed_payments = st.number_input('How many delayed payments do you have?', min_value=0, max_value=20, step=1, value=delayed_payments_default)
    delay_duration = st.number_input('How long delayed payments?', min_value=0, max_value=67, step=1, value=delay_duration_default)
    month = st.number_input('What month?', min_value=0, max_value=8, step=1, value=month_default) 
    new_credit = st.number_input('How many new credit do you have?', min_value=0, max_value=17, step=1, value=new_credit_default)
    outstanding_debt = st.number_input('How much debt you owed?', min_value=0.00, max_value=4990.00, value=outstanding_debt_default)
    emi_monthly = st.number_input('How much EMI do you pay monthly?', min_value=0.00, max_value=5000.00, value=emi_monthly_default)
    credit_history = st.number_input('How many months old is your credit history?', min_value=0, max_value=500, step=1, value=credit_history_default)
    loans = st.multiselect('Which loans do you have?', ['Auto_Loan', 'Credit-Builder_Loan', 'Personal_Loan',
                                                        'Home_Equity_Loan', 'Mortgage_Loan', 'Student_Loan',
                                                        'Debt_Consolidation_Loan', 'Payday_Loan'],
                                                        loans_default)
    minimum_payment = minimum_payment_default
    minimum_payment = st.radio('Have you paid the minimum amount on at least one of your credit cards?', ['Yes', 'No'])

    run = st.button( 'Run the numbers!')

st.header('Credit Score Results')


###RUN THE MODEL PHASE###

creditscore_container = st.container()

if run:
    resp = {
            'age': age,
            'annual_income': annual_income,
            'monthly_income': monthly_income,
            'accounts': accounts,
            'interest_rate': interest_rate,
            'num_loan': num_loan,
            'credit_cards': credit_cards,
            'changed_credit_limit': changed_credit_limit,
            'delayed_payments': delayed_payments,
            'delay_duration': delay_duration,
            'month': month,
            'new_credit': new_credit,
            'outstanding_debt': outstanding_debt,
            'emi_monthly': emi_monthly,
            'credit_history': credit_history,
            'loans': loans,
            'minimum_payment': minimum_payment
        }
    output = transform_resp(resp)
    output = pd.DataFrame(output, index=[0])
    output.loc[:,:] = scaler.transform(output)

    credit_score = model.predict(output)[0]
        
    if credit_score == 2:
        st.balloons()
        creditscore_container.markdown('Your credit score is **GOOD**! Congratulations!')
        creditscore_container.markdown('Indicates that the likelihood of borrower to repay the loan is high which may lead low probability of default. The risk is LOW. Meanwhile the borrowers will charge with low interest rates.')
        logo_good = Image.open(urllib.request.urlopen('https://github.com/dataaga/Credit_Scoring_MultiClass/blob/main/YOUR%20SCORE_GOOD.png?raw=true'))
        st.image(logo_good)
    elif credit_score == 1:
        creditscore_container.markdown('Your credit score is **STANDARD**.')
        creditscore_container.markdown('Indicates that the likelihood of borrower to repay the loan is standard which may lead medium probability of default. The risk is MEDIUM. Meanwhile the borrowers will charge with middle interest rates.')
        logo_standard = Image.open(urllib.request.urlopen('https://github.com/dataaga/Credit_Scoring_MultiClass/blob/main/YOUR%20SCORE_STANDARD.png?raw=true'))
        st.image(logo_standard)
    elif credit_score == 0:
        creditscore_container.markdown('Your credit score is **POOR**. BE Careful!')
        creditscore_container.markdown('Indicates that the likelihood of borrower to repay the loan is low which can lead high probability of default. The risk is HIGH. Meanwhile the borrowers may face elevated interest rates.')
        logo_poor = Image.open(urllib.request.urlopen('https://github.com/dataaga/Credit_Scoring_MultiClass/blob/main/YOUR%20SCORE_POOR.png?raw=true'))
        st.image(logo_poor)

