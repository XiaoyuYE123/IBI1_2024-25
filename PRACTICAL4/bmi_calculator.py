weight = float(input('Enter your weight in kg:'))
height = float(input('enter your height in m:'))
BMI = weight /(height**2)
print('Your BMI is', str(BMI))
if BMI < 18.5:
    print('You are underweight')
elif BMI > 30:
    print('You are obese')
else:
    print('You are normal wweight')
56