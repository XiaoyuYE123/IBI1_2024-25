class patients:
    def __init__(self, name, age, date_of_latest_admission, medical_history):
        self.name = name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.medical_history = medical_history
    def description_of_patient(self):
        return f"Patient {self.name} is {self.age} years old. Last admitted on {self.date_of_latest_admission}. Medical history: {self.medical_history}."
p1 = patients("John Doe", 30, "2023-10-01", "Diabetes, Hypertension")
print(p1.description_of_patient())
    