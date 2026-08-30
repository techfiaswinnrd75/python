cons = int(input("Enter No. of Units Consumed: "))
charges = 0
if cons <= 200:
    charges = cons * 0.5

elif cons <= 400:
    charges = 100 + (cons-200)*0.65

elif cons <= 600:
    charges = 230 + (cons - 400)*0.8

else:
    charges = 425 + (cons - 600)*1.25

print("Your Electricity Consumption Charge is", charges)