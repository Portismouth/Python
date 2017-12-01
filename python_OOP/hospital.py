class Patient(object):
    patient_count = 1
    def __init__(self, name, *allergies):
        self.id = Patient.patient_count
        self.name = name
        self.allergies = allergies
        self.bed = 0
        Patient.patient_count += 1
    def info(self):
        print self.id, self.name, self.allergies

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        self.beds = self.initialize_beds()

    def initialize_beds(self):
        beds = []
        for i in range(0, self.capacity):
            beds.append({
                "bed_id" : i,
                "Available" : True
            })
        return beds

    def admit(self, patient):
        if len(self.patients) <= self.capacity:
            self.patients.append(patient)
            for i in range(1, len(self.beds)):
                if self.beds[i]["Available"]:
                    patient.bed_num = self.beds[i]["bed_id"]
                    self.beds[i]["Available"] = False
                    break
            print "Patient #{} admitted to bed #{}".format(patient.id, patient.bed_num)
        else:
            "Hospital is at full capacity"

    def discharge(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                # free up bed
                for bed in self.beds:
                    if bed["bed_id"] == patient.bed_num:
                        bed["Available"] = True
                        break

                self.patients.remove(patient)
                return "Patient #{} sucessfully discharged.  Bed #{} now available".format(patient.id, patient.bed_num)
        return "Patient not found"



patient1 = Patient("Ozzy Gonzalez", "Penicillin", "Selfa")
patient2 = Patient("Jenny", "Penicillin", "Selfa")
patient3 = Patient("Matt", "Penicillin", "Selfa")
patient4 = Patient("Brad", "Penicillin", "Selfa")
patient5 = Patient("Priti", "Penicillin", "Selfa")
patient6 = Patient("Lyndon", "Penicillin", "Selfa")

st_judes = Hospital("St Judes", 5)
st_judes.admit(patient1)
st_judes.admit(patient2)
st_judes.admit(patient3)
st_judes.admit(patient4)
st_judes.admit(patient5)
st_judes.admit(patient6)
