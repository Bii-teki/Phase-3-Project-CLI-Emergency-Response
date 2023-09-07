import click
import random

from seed import session
from models import  Patient, Transport, Hospital



@click.command()
@click.option(
    "--choice",
    prompt="Enter your choice:\n1 to Add Patient\n2 to View Patient\n3 to Delete Patient\n4 to View Patient\n5 to Quit\n",
    type=click.IntRange(1, 5),
)
def menu(choice):
    if choice == 1:
        add_schedule(session)
    elif choice == 2:
        view_patient(session)
    elif choice == 3:
        delete_patient(session)
    elif choice == 4:
        view_patient(session)
    elif choice == 5:
        click.echo("Quitting the program.")
    else:
        click.echo("Invalid choice. Please select 1, 2, 3, or 4.")

def add_schedule(session):
    print("Adding Patient...")
    title = click.prompt("Enter Name")
    contact = click.prompt("Enter Contact...")
    location = click.prompt("Enter Location...")
    address = click.prompt("Enter Address...")

    hospitals_query = session.query(Hospital).filter(Hospital.bed_capacity >= 1)
    hospitals = hospitals_query.all()

    
    hospitals_list = list(hospitals)
    print( hospitals_list)
    
    if not  hospitals_list:
        click.echo("No hospitals with available beds found.")
        return

    random_hospital = random.choice(hospitals_list)
    patients = session.query(Patient).filter_by(admit=True).all()
    transports = []
    
    for patient in patients:
        new_transport = Transport(
            title=title,
            contact=contact,
            location=location,
            address=address,
            hospital_id=random_hospital.id,
            patient_id=patient.id,  
        )
        session.add(new_transport)
        session.commit()
        transports.append(new_transport)
        
        patients_to_update = session.query(Patient).filter(Patient.admit == True).all()
        for patient in patients_to_update:
            patient.admit = False
        session.commit()
        
    random_hospital.bed_capacity -= 1  

    click.echo(f"Added {title} with {len(patients)} bed capacity to the database.")



def view_patient(session):
    print("View Patients Who Have Not Been Admitted...")
    patients = session.query(Patient).filter_by(admit=False).all()
    
    if patients:
        for patient in patients:
            print(f"Patient Name: {patient.name}")
            print(f"Contact: {patient.contact}")
            print(f"Location: {patient.location}")
            print(f"Address: {patient.address}")
            print(f"Admitted: {patient.admit}")
            print("-" * 20)
    else:
        print("No patients found who have not been admitted.")



def view_patients(Patient):
    name = session.query(Patient).all()
    for i in name:
        click.echo(f"{i.name}")


def delete_patient(session):
    print("Delete a Patient...")
    name = click.prompt("Enter name")

    
    patient = session.query(Patient).filter_by(name=name).first()

    if patient:
        session.delete(patient)
        try:
            session.commit()
            print(f"Patient {name} has been deleted successfully.")
        except Exception as e:
            session.rollback()
            print(f"An error occurred while deleting the patient: {str(e)}")
    else:
        print(f"No patient with the name {name} was found in our records.")



if __name__ == "__main__":
    menu()
