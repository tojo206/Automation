

header = [
    {
        "FileType": "QDOI",
        "ClientIdentifier": "0000",
        "ServiceIdentifier": "0022",
        "LayoutIdentifier": "0031",
        "LayoutRevision": "V17",
        "SequenceNumber": "0027",
        "CreationDate": "20231102",
        "Month": "202311",
        "ClientIdentifier2": "00013585",
        "Period": "",
        "ConvertAccout": "",
        "UniversalBranchCode": ""
    }
]

transaction = [
    {
        "FileType1": "QONE",
        "Surname": "WINU",
        "Initials": "VWX",
        "IDNumber": "9407305633081",
        "BankIdentifier":"BIDVEST",
        "AccountType": "01",
        "BranchCode": "462005",
        "AccountNumber": "11636667301",
        "EmployerIdentifier": "0000",
        "EmployerName": "",
        "PayrollNumber": "",
        "Department": "",
        "EmployeeNumber": "",
        "DeductionType": "0010",
        "ReferenceNumber": "00000005EC",
        "Amount": "0000004000",
        "Balance": "0000000000",
        "StartDate": "20231101",
        "EndDate": "00000000",
        "Frequency": "O",
        "ActionDay": "24",
        "VariableActionDay": "",
        "NewDeductionType": "",
        "CorrectReferenceNumber": "4082068932/8932/0000000002",
        "ErrorCode": "0000",
        "TrackID": "00002507291",
        "SequenceNumber": "0000",
        "RDDate": "00000000",
        "Comments": "",
        "TransactionNumber": "0000000428",
        "CollectionMethod": "28",
        "TrackingIndicator": "01",
        "DatePresented": "20231101",
        "CollectionMonth": "202311",
        "CollecionRule": "00",
        "AccountHolderID": "8202280586086",
        "TrackingStart": "00",
        "DateCollected": "00000000",
        "CellularNumber": "",
        "AccountActive": "0",
        "PassportNumber": "",
        "CompanyRegistration": "",
        "batchNumber": "KNOW",
        "CreditCardIssueDate": "",
        "CreditCardExpDate": "",
        "CreditCardCVV2Value": "",
        "SMSIndicator": "",
        "HomingAccoutNumber": "",
        "NaedoIndicator": "",
        "Product": "",
        "BankReference": "00000005ED 230724",
        "Combine": "N",
        "DoubleDebitIndicator": "",
        "ClientActionDate": "00000000",
        "DateOfCommence": "00000000",
        "NonPaymentAction": "00",
        "CycleDate": "231101",
        "RiskIndicator": "",
        "DistributionChannel": "",
        "DistributionAgency": "",
        "DistributionAgent": "",
        "ProductCategory": "",
        "SubReference": "20230724",
        "BusinessUnitCode": "0",
        "StartMonthIndicator": "00",
        "BankProcessDate": "00000000",
        "TransactionOriginator": "",

    }
]

Trailer = [
    {
    "FileType": "QEND",
    "RecordCount": "0000000003",
    "CheckTotal": "00000000000000004000",
    }
]


header_array_name = "Header"
transaction_array_name = "TransactionRecord"
Trailer_array_name = "TrailerRecord"
desired_lengths = {
    #Header Record Layout
    "FileType": 4,
    "ClientIdentifier": 4,
    "ServiceIdentifier": 4,
    "LayoutIdentifier": 4,
    "LayoutRevision": 3,
    "SequenceNumber": 4,
    "CreationDate": 8,
    "Month": 6,
    "ClientIdentifier2": 8,
    "Period": 1,
    "ConvertAccout": 1,
    "UniversalBranchCode": 1,

}


desired_lengthss = {
    #Transaction Record Layout
        "FileType1": 4,
        "Surname": 25,
        "Initials": 8,
        "IDNumber": 13,
        "BankIdentifier": 8,
        "AccountType": 2,
        "BranchCode": 6,
        "AccountNumber": 30,
        "EmployerIdentifier": 4,
        "EmployerName": 50,
        "PayrollNumber": 2,
        "Department": 50,
        "EmployeeNumber": 15,
        "DeductionType": 4,
        "ReferenceNumber": 30,
        "Amount": 10,
        "Balance": 10,
        "StartDate": 8,
        "EndDate": 8,
        "Frequency": 1,
        "ActionDay": 2,
        "VariableActionDay": 1,
        "NewDeductionType": 4,
        "CorrectReferenceNumber": 30,
        "ErrorCode": 4,
        "TrackID": 11,
        "SequenceNumber": 4,
        "RDDate": 8,
        "Comments": 30,
        "TransactionNumber": 10,
        "CollectionMethod": 2,
        "TrackingIndicator": 2,
        "MovementIndicator": 1,
        "DatePresented": 8,
        "CollectionMonth": 6,
        "CollecionRule": 2,
        "AccountHolderID": 13,
        "TrackingStart": 2,
        "DateCollected": 8,
        "CellularNumber": 15,
        "AccountActive": 1,
        "PassportNumber": 20,
        "CompanyRegistration": 20,
        "batchNumber": 4,
        "CreditCardIssueDate": 6,
        "CreditCardExpDate": 6,
        "CreditCardCVV2Value": 3,
        "SMSIndicator": 1,
        "HomingAccoutNumber": 30,
        "NaedoIndicator": 1,
        "Product": 10,
        "BankReference": 20,
        "Combine": 1,
        "DoubleDebitIndicator": 1,
        "ClientActionDate": 8,
        "DateOfCommence": 8,
        "NonPaymentAction": 2,
        "CycleDate": 6,
        "RiskIndicator": 2,
        "DistributionChannel": 10,
        "DistributionAgency": 30,
        "DistributionAgent": 10,
        "ProductCategory": 20,
        "SubReference": 10,
        "BusinessUnitCode": 10,
        "StartMonthIndicator": 2,
        "BankProcessDate": 8,
        "TransactionOriginator": 50,
}

desired_lengthsR = {
    #Trailer Record Layout
    "FileType": 4,
    "RecordCount": 10,
    "CheckTotal": 20,
}

filename = "ProcessedDOIEFile.txt"
with open(filename, "w") as file:
    # Write the "Header" data on the first line
    
    for person_data in header:
         for field, length in desired_lengths.items():
                field_data = person_data.get(field, '')
                field_data = field_data.ljust(length)  # Fill with spaces to reach the desired length

                if len(field_data) > length:
                 print(f"You have exceeded the desired length for {field} length {length} on the HeaderRecord")
                

            
                file.write(f"{field_data}")
                

    # Write the "TransactionRecord" data on the second line
    file.write(f" \n")
    for person_data in transaction:
         for field, length in desired_lengthss.items():
                field_data = person_data.get(field, '')
                field_data = field_data.ljust(length)  # Fill with spaces to reach the desired length

                if len(field_data) > length:
                 print(f"You have exceeded the desired length for {field} length {length} on the TransactionRecord")
                file.write(f"{field_data}")

    file.write(f" \n")
    for person_data in Trailer:
         for field, length in desired_lengthsR.items():
                field_data = person_data.get(field, '')
                field_data = field_data.ljust(length)  # Fill with spaces to reach the desired length

                if len(field_data) > length:
                 print(f"You have exceeded the desired length for {field} length {length} on the TrailerRecord")
                file.write(f"{field_data}")

file.close()
print(f"Your File Has been Successfully Created - FileName is {filename}") 
