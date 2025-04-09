weight = int(input('Enter the weight of the patient in kg: '))
paracetamol = int(input('Enter the dose of paracetamol in mg/5ml(either 120mg/5ml or 250mg/5ml): '))
def drug_dose_calculator():
    if 10 < weight < 100:
        if paracetamol == 120:
            recommended_dose = weight * 15
            print(f'The recommended dose of paracetamol is {recommended_dose}mg')
        elif paracetamol == 250:
            recommended_dose = weight * 20
            print(f'The recommended dose of paracetamol is {recommended_dose}mg')
        else:
            print('Invalid paracetamol dose. Please enter either 120mg/5ml or 250mg/5ml.')
    else:
        print('Weight must be between 10kg and 100kg.')
    return recommended_dose
drug_dose_calculator()