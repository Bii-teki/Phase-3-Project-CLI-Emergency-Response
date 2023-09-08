import click
import random

from seed import session
from models import Patient, Transport, Hospital


@click.command()
@click.option(
    "--choice",
    prompt="Enter your choice:\n1 to Respond to Resquests \n2 to View Patients with Request \n3 to Delete Request\n4 to View Patient\n5 to Check for Availble Hospitals\n6 to Check for patients in a particular hospital \n7 to Quit\n",
    type=click.IntRange(1, 7),
)
def menu(choice):
    print(f"Selected choice: {choice}")
    if choice == 1:
        add_schedule(session)
    elif choice == 2:
        view_patient(session)
    elif choice == 3:
        delete_patient(session)
    elif choice == 4:
        view_patients(session)
    elif choice == 5:
        available_hospitals(session)
    elif choice == 6:
        print("Option 6 selected")
        patients_in_hospital(session)
    elif choice == 7:
        print("Option 7 selected")
        click.echo("Quitting the program.")
    else:
        click.echo("Invalid choice. Please select 1, 2, 3, 4, 5, 6, or 7.")


def add_schedule(session):
    print("Adding Patient...")
    title = click.prompt("Enter Name")
    contact = click.prompt("Enter Contact...")
    location = click.prompt("Enter Location...")
    address = click.prompt("Enter Address...")

    hospitals_query = session.query(Hospital).filter(Hospital.bed_capacity >= 1)
    hospitals = hospitals_query.all()
    hospitals_list = list(hospitals)
    print(hospitals_list)

    if not hospitals_list:
        print("No hospitals with available beds found.")
    else:
        random_hospital = random.choice(hospitals_list)
        patients = session.query(Patient).filter_by(admit=False).all()
        if not patients:
            print("No hospitals with available beds found.")
        else:
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

                patient.admit = True
                random_hospital.bed_capacity -= 1
                session.commit()
                click.echo(
                    f"Added {title} with {len(patients)} bed capacity to the database."
                )
                break


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

    patient = session.query(Transport).filter_by(title=name).first()

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


def available_hospitals(session):
    available = session.query(Hospital).filter(Hospital.bed_capacity > 0).all()
    available_hospitals_list = list(available)
    if len(available_hospitals_list) > 0:
        for i in available:
            # print(available_hospitals_list)
            print(f"Hospital Name: {i.name}")
            print(f"Contact: {i.contact}")
            print(f"Location: {i.location}")
            print(f"Address: {i.address}")
            print("-" * 20)
    else:
        print("All Hospitals are occuppied")


def patients_in_hospital(session):
    print("Check patients admitted in this Hospital...")
    id = click.prompt("Enter id of the Hospital", type=int)

    hospital_ids = session.query(Transport.hospital_id).filter(Transport.patient_id == id).all()

    for hospital_id in hospital_ids:
        hospital = session.query(Hospital).get(hospital_id[0])

        if hospital:
            print(f"Hospital Name: {hospital.name}")
            print(f"Contact: {hospital.contact}")
            print(f"Location: {hospital.location}")
            print(f"Address: {hospital.address}")
            print("-" * 20)
        else:
            print(f"No hospital found with ID {hospital_id[0]}")

    


if __name__ == "__main__":
    menu()
