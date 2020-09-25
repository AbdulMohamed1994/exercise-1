contract_type =str(input("Please state your contract type: "))
if contract_type == "permanent":
    print("income_tax = 0.295") #29.5% income tax
elif contract_type == "casual":
    print("income tax is 0.25") #25% income tax
Annual_salary = int(input("Please enter your annual salary: "))
income_tax=float(input("please enter your percentage tax: "))
gross_monthly_salary = (Annual_salary / 12)
print(gross_monthly_salary)
tax_per_month = (gross_monthly_salary * income_tax)
print('tax_per_month: ', tax_per_month)
net_monthly_salary = (gross_monthly_salary - tax_per_month)
print(net_monthly_salary)
