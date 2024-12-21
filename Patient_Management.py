patients = []
def patient_rec():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    disease = input("Enter patient disease: ")
    patients.append({"Name": name, "Age": age, "Disease": disease})
    print(patients)
def search_patient(disease):
    found = False
    for p in patients:
        if p["Disease"].lower() == disease.lower():
            print(f"Patient with Disease {p['Disease']} is  {p['Name']}")
            found = True
    if not found:
        print(f"No patients found with the disease '{disease}'.")
def display():
    while True:
        print("\nMenu:")
        print("1. Add patient record")
        print("2. Search patient by disease")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            patient_rec()
        elif choice == 2:
            disease_to_search = input("Enter disease name: ")
            search_patient(disease_to_search)
        elif choice == 3:
            print("Exiting the system")
            break
        else:
            print("Invalid choice. Please try again.")
display()