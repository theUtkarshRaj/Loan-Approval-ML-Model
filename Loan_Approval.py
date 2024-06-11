import numpy as np
import pickle
import streamlit as st

#load the trained Model
loaded_model=pickle.load(open("trained_Loan_Approval.sav",'rb'))

def Loan_Approval(input_data):
    # Extracting input features
    
    Gender = input_data['Gender']
    Married = input_data['Married']
    Dependents = input_data['Dependents']
    Education = input_data['Education']
    Self_Employed = input_data['Self_Employed']
    ApplicantIncome = input_data['ApplicantIncome']
    CoapplicantIncome = input_data['CoapplicantIncome']
    LoanAmount = input_data['LoanAmount']
    Loan_Amount_Term = input_data['Loan_Amount_Term']
    Credit_History = input_data['Credit_History']
    Property_Area = input_data['Property_Area']

    # Data preprocessing
    Gender = 1 if Gender == 'Male' else 0
    Married = 1 if Married == 'Yes' else 0
    Self_Employed = 1 if Self_Employed == 'Yes' else 0
    Education = 1 if Education == 'Graduate' else 0
    Property_Area = {'Rural': 0, 'Semiurban': 1, 'Urban': 2}[Property_Area]

    # Convert to numpy array
    input_data = np.array([Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome,
                           CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area])

    # Reshape the input for prediction
    input_data_reshaped = input_data.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    
    if prediction ==0:
      return "Sorry , Loan not Approved"
    else:
      return "Congratulation Loan Approved"

def main():
    # Giving a title
    st.title("Loan Approval")

    # Getting input data from user
    col1, col2, col3 = st.columns(3)

    with col1:
        Gender = st.selectbox("Gender", ["Male", "Female"])
        Married = st.selectbox("Married", ["Yes", "No"])
        Dependents = st.text_input("Dependents")
        Education = st.selectbox("Education", ["Graduate", "Not Graduate"])

    with col2:
        Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
        ApplicantIncome = st.text_input("Applicant Income")
        CoapplicantIncome = st.text_input("Coapplicant Income")
        LoanAmount = st.text_input("Loan Amount")

    with col3:
        Loan_Amount_Term = st.text_input("Loan Amount Term")
        Credit_History = st.selectbox("Credit History", ["0", "1"])
        Property_Area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

    # Code for prediction
    approval_status = ''

    # Creating a button for prediction
    if st.button("Check Loan Approval"):
        # Check if any of the input fields are empty
        if any([Gender == '', Married == '', Dependents == '', Education == '', Self_Employed == '',
                ApplicantIncome == '', CoapplicantIncome == '', LoanAmount == '', Loan_Amount_Term == '',
                Credit_History == '', Property_Area == '']):
            st.error("Please fill in all the input fields.")
        else:
            # Prepare input data as dictionary
            input_data = {'Gender': Gender, 'Married': Married, 'Dependents': Dependents,
                          'Education': Education, 'Self_Employed': Self_Employed,
                          'ApplicantIncome': float(ApplicantIncome),
                          'CoapplicantIncome': float(CoapplicantIncome),
                          'LoanAmount': float(LoanAmount), 'Loan_Amount_Term': float(Loan_Amount_Term),
                          'Credit_History': float(Credit_History), 'Property_Area': Property_Area}
            # Call function for prediction
            approval_status = Loan_Approval(input_data)
            # Display result
            st.success(f"Loan Approval Status: {approval_status}")

if __name__ == '__main__':
    main()

  
  
