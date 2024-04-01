
def print_menu():               #The menu for the hospital management system
    print("\nHospital Management System")
    print("1. Print Queue of Patients")
    print("2. Schedule Appointment")
    print("3. Assign Prescription")
    print("4. Update Patient Record")
    print("5. Print Patient Details")
    print("6. Delete Patient")
    print("7. Exit")

def print_patient_details(patient):             #Function to print patient details
    print("ID:", patient._id)
    print("Name:", patient._name)
    print("Medical Records:", patient._medical_record)
    print("Current Diagnosis:", patient._current_diagnosis)
    print("Appointment :", patient.appointment)
    print("Prescriptions:")
    for prescription in patient.perscription:
        print("\tType:", prescription._type)
        print("\tDosage:", prescription._dosage)
    print()

class Patient:
    def __init__(self, id, name, medical_record, current_diagnosis):
        self._id = id
        self._name = name
        self._medical_record = medical_record
        self._current_diagnosis = current_diagnosis
        self.appointment = None
        self.perscription = []

class Doctor:
    def __init__(self, docname, docID, specialization):
        self.docname = docname
        self.docID = docID
        self.specialization = specialization
        self.schedule = []

class Perscription:
    def __init__(self, type, dosage):
        self._type = type
        self._dosage = dosage

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, patient):
        self.queue.append(patient)

    def is_empty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def print_queue(self):
        print("\nQueue of Patients:")
        for patient in self.queue:
            print("ID:", patient._id, "Name:", patient._name)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, perscription):
        self.stack.append(perscription)

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def print_stack(self):
        print("\nStack of Prescriptions:")
        for prescription in self.stack:
            print("Type:", prescription._type, "Dosage:", prescription._dosage)

class Hospital:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.patient_queue = Queue()
        self.perscription_stack = Stack()

    def new_patient(self, patient):
        self.patients[patient._id] = patient

    def update_record(self, patient_id, updated_details):
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            patient._name = updated_details.get('name', patient._name)
            patient._medical_record = updated_details.get('medical_record', patient._medical_record)
            patient._current_diagnosis = updated_details.get('current_diagnosis', patient._current_diagnosis)
            patient.appointment = updated_details.get('appointment', patient.appointment)
            print("Record updated successfully.")
        else:
            print("This patient has no record available/found.")

    def delete_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]
        else:
            print("There is no patient found with this ID.")

    def schedule_appointment(self, patient_id, docID, appointment):
        if patient_id in self.patients and docID in self.doctors:
            patient = self.patients[patient_id]
            doctor = self.doctors[docID]
            patient.appointment = appointment
            doctor.schedule.append(patient)
        else:
            print("The patient or Doctor was not found.")

    def assign_perscription(self, patient_id, perscription):
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            patient.perscription.append(perscription)
            self.perscription_stack.push(perscription)
        else:
            print("The given patient ID was not found.")

    def find_patient(self, patient_id):
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            return patient
        else:
            print("This patient was not found.")

def menu_based():               #Applying menu-based interfernce on the test cases
    hospital = Hospital()

    # Test cases from original code
    patient1 = Patient(1234, "Mahra Alameri", "None", "Fever")
    patient2 = Patient(4321, "Aliya Alshabibi", "Diabetes Type 1", "High blood pressure")
    patient3 = Patient(5678, "Khaled Alharmoodi", "Asthma", "Cough")
    doctor1 = Doctor("Dr. Mohammed", 555, "General Doctor")
    doctor2 = Doctor("Dr. John", 999, "Cardiologist")
    doctor3 = Doctor("Dr. Fatima", 777, "Ear Nose and Throat Specialist")
    prescription1 = Perscription("Ibuprofen", "1500mg")
    prescription2 = Perscription("ACE inhibitors", "200mg")
    prescription3 = Perscription("Lozenge", "15mg")

    hospital.new_patient(patient1)
    hospital.new_patient(patient2)
    hospital.new_patient(patient3)

    hospital.doctors[doctor1.docID] = doctor1
    hospital.doctors[doctor2.docID] = doctor2
    hospital.doctors[doctor3.docID] = doctor3

    hospital.schedule_appointment(1234, 555, "Monday, April 1st 2024. 12:00pm.")
    hospital.assign_perscription(1234, prescription1)

    hospital.schedule_appointment(4321, 999, "Monday, April 1st 2024. 12:00pm.")
    hospital.assign_perscription(4321, prescription2)

    hospital.schedule_appointment(5678, 777, "Monday, April 1st 2024. 12:00pm.")
    hospital.assign_perscription(5678, prescription3)

    update_details = {'id': '1234', 'name': 'Mahra Al Ameri', 'medical_record': 'Allergies', 'current_diagnosis': 'Fever', 'appointment': 'Tuesday, April 2nd 2024. 10:00am.'}
    hospital.update_record(1234, update_details)

    #queue of test case patients that matches the users input
    test_case_queue = Queue()
    test_case_queue.enqueue(patient1)
    test_case_queue.enqueue(patient2)
    test_case_queue.enqueue(patient3)

    #applying Menu-based interface
    while True:
        print_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":               #It will print the queue of the patients
            test_case_queue.print_queue()

        elif choice == "2":                         #It will schedual an appoitment
            patient_id = input("Enter patient ID: ")
            doc_id = input("Enter doctor ID: ")
            appointment = input("Enter appointment details: ")
            hospital.schedule_appointment(int(patient_id), int(doc_id), appointment)

        elif choice == "3":             #It will assign prescription
            patient_id = input("Enter patient ID: ")
            prescription_type = input("Enter prescription type: ")
            dosage = input("Enter dosage: ")
            prescription = Perscription(prescription_type, dosage)
            hospital.assign_perscription(int(patient_id), prescription)

        elif choice == "4":         #It will update the patient record
            patient_id = input("Enter patient ID: ")
            updated_details = {}
            updated_details['id'] = patient_id
            updated_details['name'] = input("Enter new name (press enter to skip): ")
            updated_details['medical_record'] = input("Enter new medical record (press enter to skip): ")
            updated_details['current_diagnosis'] = input("Enter new current diagnosis (press enter to skip): ")
            updated_details['appointment'] = input("Enter new appointment (press enter to skip): ")
            hospital.update_record(int(patient_id), updated_details)

        elif choice == "5":         #It will print patients detail
            patient_id = input("Enter patient ID: ")
            patient = hospital.find_patient(int(patient_id))
            if patient:
                print_patient_details(patient)
            else:
                print("Patient not found.")

        elif choice == "6":             #It will detele a patient
            patient_id = input("Enter patient ID to delete: ")
            patient = hospital.find_patient(int(patient_id))
            if patient:
                hospital.delete_patient(int(patient_id))
                test_case_queue.queue.remove(patient)  #remove the patient from the test case queue
            else:
                print("Patient not found.")

        elif choice == "7":         #It will exit the hospital managment system
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


menu_based()
