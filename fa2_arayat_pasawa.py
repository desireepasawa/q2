
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85


regular_patient = Patient("Juan", 15000)
senior_patient = SeniorPatient("Maria", 15000)
philhealth_patient = PhilHealthPatient("Pedro", 15000)

patients = [
    ("Regular Patient", regular_patient),
    ("Senior Citizen", senior_patient),
    ("PhilHealth Member", philhealth_patient)
]

for patient_type, patient in patients:
    print("\n", patient_type)
    print("Name:", patient.get_name())
    print("Original Bill:", patient.get_bill_amount())
    print("Final Bill:", patient.calculate_bill())
