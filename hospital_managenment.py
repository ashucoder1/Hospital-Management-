import pandas as pd
from datetime import datetime
import random

# Create an empty DataFrame to store patient data
columns = ['PatientID', 'Name', 'DOB', 'AdmitDate', 'Ward', 'BedNo', 'PhoneNumber']
patient_data = pd.DataFrame(columns=columns)

def add_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Name: ")

    # Validate Date of Birth
    while True:
        try:
            dob = input("Enter Date of Birth (DD-MM-YYYY): ")
            dob = datetime.strptime(dob, '%d-%m-%Y').strftime('%Y-%m-%d')
            break  # Break out of the loop if the date is valid
        except ValueError:
            print("Invalid date format. Please enter a valid date.")

    admit_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ward = input("Enter Ward: ")

    # Generate a random bed number between 01-100
    bed_no = f"{random.randint(1, 100):02d}"

    phone_number = input("Enter Phone Number: ")

    new_patient = pd.DataFrame([[patient_id, name, dob, admit_date, ward, bed_no, phone_number]],
                               columns=columns)
    global patient_data
    patient_data = patient_data._append(new_patient, ignore_index=True)
    print("Patient added successfully!\n")



def delete_patient():
    patient_id = input("Enter Patient ID to delete: ")
    global patient_data
    patient_data = patient_data[patient_data['PatientID'] != patient_id]
    print(f"Patient with ID {patient_id} deleted successfully!\n")

def show_data():
    print("\nPatient Data:")
    if not patient_data.empty:
        formatted_data = patient_data.copy()
        formatted_data['DOB'] = pd.to_datetime(formatted_data['DOB'], errors='coerce').dt.strftime('%d-%m-%Y')
        formatted_data['AdmitDate'] = pd.to_datetime(formatted_data['AdmitDate'], errors='coerce').dt.strftime('%d-%m-%Y %H:%M:%S')
        print(formatted_data.to_string(index=False, col_space=15))
    else:
        print("No patient data available.\n")

# Main program with switch case
  # Import the random module for generating random bed numbers

while True:
    print("\nHospital Management System")
    print("1. Add New Patient")
    print("2. Delete Patient")
    print("3. Show Patient Data")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_patient()
    elif choice == '2':
        delete_patient()
    elif choice == '3':
        show_data()
    elif choice == '4':
        print("Signing Off from Hospital. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
