def transform_resp(resp):
    def yes_no(column):
        if resp[column] == 'Yes':
            return 1
        else:
            return 0
 
    
    loans = {
        'Auto_Loan': 0,
        'Credit-Builder_Loan': 0,
        'Personal_Loan': 0,
        'Home_Equity_Loan': 0,
        'Mortgage_Loan': 0,
        'Student_Loan': 0,
        'Debt_Consolidation_Loan': 0,
        'Payday_Loan': 0
    }

    if resp['loans'] == None:
        loans['Auto_Loan'] = 0
        loans['Credit-Builder_Loan'] = 0
        loans['Personal_Loan'] = 0
        loans['Home_Equity_Loan'] = 0
        loans['Mortgage_Loan'] = 0
        loans['Student_Loan'] = 0
        loans['Debt_Consolidation_Loan'] = 0
        loans['Payday_Loan'] = 0
    else:
        for key_ans in loans.keys():
            if key_ans in resp['loans']:
      
                loans[key_ans] = 1

    output = {
        'Age': resp['age'],
        'Annual_Income': resp['annual_income'],
        'Monthly_Inhand_Salary': resp['monthly_income'], ##
        'Num_Bank_Accounts': resp['accounts'],
        'Interest_Rate': resp['interest_rate'], ##  
        'Num_of_Loan': resp['num_loan'], ##
        'Num_Credit_Card': resp['credit_cards'],
        'Changed_Credit_Limit': resp['changed_credit_limit'], ##
        'Num_of_Delayed_Payment': resp['delayed_payments'],
        'Delay_from_due_date': resp['delay_duration'], ##
        'Month': resp['month'], ##
        'Num_Credit_Inquiries': resp['new_credit'], ##
        'Outstanding_Debt':resp['outstanding_debt'], ##
        'Total_EMI_per_month': resp['emi_monthly'],
        'Credit_History_months': resp['credit_history'],
        'Auto_Loan': loans['Auto_Loan'],
        'Credit-Builder_Loan': loans['Credit-Builder_Loan'],
        'Personal_Loan': loans['Personal_Loan'],
        'Home_Equity_Loan': loans['Home_Equity_Loan'],
        'Mortgage_Loan': loans['Mortgage_Loan'],
        'Student_Loan': loans['Student_Loan'],
        'Debt_Consolidation_Loan': loans['Debt_Consolidation_Loan'],
        'Payday_Loan': loans['Payday_Loan'],
        'Payment_of_Min_Amount': yes_no('minimum_payment')
    }

    return output