#function: BMI Calculator:Show people's BMI and whether they are overweight, underweight or normal weight
#BMI=weight(kg)/height(m)^2
#Input weight and height
weight = float(input('Enter your weight in kg:'))
height = float(input('enter your height in m:'))
#clculator BMI
BMI = weight /(height**2)
#If BMI<18.5, State=underweight
#If 18.5<=BMI<25, State=normal weight
#If BMI>=25, State=overweight
print('Your BMI is', str(BMI))
if BMI < 18.5:
    print('You are underweight')
elif BMI > 30:
    print('You are obese')
else:
    #Print BMI and State
    print('You are normal wweight')
