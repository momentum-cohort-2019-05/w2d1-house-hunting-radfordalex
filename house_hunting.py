annual_salary = float(input("What is your annual salary?"))
portion_saved = float(input("What portion of your salary are you saving"))
total_cost = float(input("What is the cost of your house"))
monthly_salary = annual_salary/12
r = 0.04
current_savings = 0
months = 0
portion_down_payment = total_cost*0.25

while current_savings < portion_down_payment:
    monthly_additions = portion_saved*monthly_salary + current_savings*r/12 
    current_savings = current_savings + monthly_additions

    months += 1
    print(current_savings)
    print(months)












