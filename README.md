# Credit Scoring Prediction
**Background Project**: \
KreditDulu as Credit Company using Machine Learning (ML) based on Alternate Data + Manual (Traditional) Credit Data to help them deciding credit scoring for each borrower in order to enables provision of fair interest rate and reduce risk of potential default (also collections stage to assess how likely a customer in collections is to pay back their debt).

**Objective**: \
KreditDulu requires Credit Scoring through the utilization of Machine Learning, as well as manual data and alternate data, to assist the lender in determining whether to approve/extend or deny credit to borrowers

**Expected Output**: \
KreditDulu can use a machine learning model that can classify the credit score.

Dataset: https://www.kaggle.com/datasets/parisrohan/credit-score-classification


**Features**: \
Features Description:<br>
A. Traditional Information:
1. ID: A unique identifier for each record
2. Customer_ID: A unique identifier for each customer
3. Payment_Behaviour: An indicator of the customer's payment patterns & spending habits (in USD).
4. Num_of_Loan: The number of loans the customer has taken.
5. Type_of_Loan: The type or types of loans the customer has, indicated as a comma-separated list.
6. Delay_from_due_date: The delay in payment from the due date for loans or credit payments.
7. Num_of_Delayed_Payment: The number of payments that have been delayed.
8. Changed_Credit_Limit: A change in the credit limit, typically for a credit card.
9. Num_Credit_Inquiries: The number of credit inquiries/inspection made by potential lenders or creditors.
10. Credit_Mix: Information about the types of credit accounts held by the customer.
11. Outstanding_Debt: The amount of outstanding (huge) debt owed by the customer (in USD).
12. Credit_Utilization_Ratio: The credit utilization ratio, calculated as the credit card balance divided by the credit limit.
13. Credit_History_Age: The age of the credit history in years and months.
14. Payment_of_Min_Amount: Indicates whether the customer makes only the minimum payment on credit cards.
15. Total_EMI_per_month: The total Equated Monthly Installment (EMI) or equal repayment amount paid by the customer.

B. Non-Traditional Information:

B.1. Investing Information: <br>
16. Amount_invested_monthly (If the source of investment data is non-traditional) <br>

B.2. Demographic Information: <br>
17. Name: The name of the customer. <br>
18. Age: The age of the customer in years. <br>
19. SSN: Social Security Number (SSN) of the customer, a unique identifier used for personal identification. <br>
20. Occupation: The occupation or job role of the customer. <br>
21. Annual_Income: The annual income of the customer in monetary units (e.g., dollars). <br>
22. Monthly_Inhand_Salary: The monthly income after deductions, often referred to as take-home pay. <br>

B.3.  Bank & Credit  Information: <br>
23. Num_Bank_Accounts: The number of bank accounts the customer holds. <br>
24. Num_Credit_Card: The number of credit cards the customer possesses. <br>
25. Monthly_Balance: The monthly balance in the customer's account. <br>
26. Interest_Rate: The interest rate for some financial product. <br>
27. Month: The month of the record <br>

C. Target Variable: <br>
28. Credit_Score (Target variable, Poor, Standard, Good)
