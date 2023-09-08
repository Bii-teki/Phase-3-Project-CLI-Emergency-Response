import click
import re
from seed import session
from models import Patient

@click.command()
@click.option(
    "--choice",
    prompt="Enter your choice:\n1 to Add Patient\n2 to View Patient\n3 to Delete Patient\n4 to View Patients\n5 to Quit\n",
    type=click.IntRange(1, 5),
)
def patient_menu(choice):
    if choice == 1:
        add_patient(session)
    elif choice == 2:
        view_patient(session)
    elif choice == 3:
        delete_patient(session)
    elif choice == 4:
        view_patients(session)
    elif choice == 5:
        click.echo("Quitting the program.")
    else:
        click.echo("Invalid choice. Please select 1, 2, 3, 4, or 5.")

def add_patient(session):
    print("Adding Patients...")
    patients = []  # Create a list to store patient objects

    
    name = click.prompt("Enter Name")
    contact = click.prompt("Enter Contact...")
    location = click.prompt("Enter Location...")
    address = click.prompt("Enter Address...")
    admit = click.prompt("Is the patient admitted? (yes/no)").lower() == 'yes'

    if not re.match("^[A-Za-z]*$", name):
            print("Error! Make sure you only use letters in your name")
    elif not contact.isdigit():
            print("Contact should contain only numeric characters.")
    else:
            patient = Patient(
                name=name,
                contact=contact,
                location=location,
                address=address,
                admit=admit
            )
            session.add(patient)
            session.commit()
            
            patients.append(patient)

            click.echo(f"Added {name} to the database.")

        

  

def view_patient(session):
    print("View this Patient...")
    name = click.prompt("Enter name")

    patient = session.query(Patient).filter_by(name=name).first()
    if patient:
        click.echo(f"Patient: {patient.name}")
    else:
        print("No patient found")

def view_patients(session):
    patients = session.query(Patient).all()
    if patients:
        for patient in patients:
            print(f"Patient Name: {patient.name}, Contact: {patient.contact}, Address: {patient.address}")
    else:
        print("No patients found in the database.")

def delete_patient(session):
    print("Deleting Patient...")
    name = click.prompt("Enter name")
    patient = session.query(Patient).filter_by(name=name).first()
    if patient:
        session.delete(patient)
        session.commit()
        click.echo(f"Deleted patient with name {name} from our records.")
    else:
        click.echo(f"No patient with the name {name} found in our records.")

if __name__ == "__main__":
    patient_menu()
