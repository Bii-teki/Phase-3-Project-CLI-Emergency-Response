import click

from seed import session
from models import  Hospital
import re

@click.command()
@click.option(
    "--choice",
    prompt="Enter your choice:\n1 to Add Hospital\n2 to View Hospital\n3 to Delete Hospital\n4 to View Hospitals\n5 to Quit\n",
    type=click.IntRange(1, 5),
)
def hospital_menu(choice):
    if choice == 1:
        add_hospital(session)
    elif choice == 2:
        view_hospital(session)
    elif choice == 3:
        delete_hospital(session)
    elif choice == 4:
        view_hospitals(session)
    elif choice == 5:
        click.echo("Quitting the program.")
    else:
        click.echo("Invalid choice. Please select 1, 2, 3, or 4.")


hospitals = []


def add_hospital(session):
    print("Adding Hospital...")
    name = click.prompt("Enter Name")
    if not re.match("^[A-Za-z]*$", name):
            print ("Error! Make sure you only use letters in your name")
            name = click.prompt("Enter Name")    
            
    contact = click.prompt("Enter Contact...")   
    if not contact.isdigit():            
             print("String contains only numeric characters.") 
             contact = click.prompt("Enter Contact...")  
    location = click.prompt("Enter Location...")
    address = click.prompt("Enter Address...")
    bed_capacity = click.prompt("Enter bed capacity... ", type=int)
    
    hospital = Hospital(
        name=name,
        contact=contact,
        location=location,
        address=address,
        bed_capacity=bed_capacity,
    )
    try:
        session.add(hospital)
        session.commit()
        hospitals.append(hospital)
        click.echo(f"Added {name} with {bed_capacity} bed capacity to the database.")
    except Exception as e:
        session.rollback() 
        click.echo(f"An error occurred: {str(e)}")



def view_hospital(session):
    print("View this Hospital...")
    name = click.prompt("Enter name")

    hospital = session.query(Hospital).filter_by(name=name).first()
    if hospital:
        click.echo(f"Hospital: {hospital.name}")
        click.echo(f"Contact: {hospital.contact}")
        click.echo(f"Location: {hospital.location}")
        click.echo(f"Address: {hospital.address}")
        click.echo(f"Bed Capacity: {hospital.bed_capacity}")
    else:
        click.echo("No hospital found with that name.")



def view_hospitals(session):
    hospitals = session.query(Hospital).all()
    if hospitals:
        for hospital in hospitals:
            click.echo(f"{hospital.name}")
    else:
        click.echo("No hospitals found in the database.")



def delete_hospital(session):
    print("View this Hospital...")
    name = click.prompt("Enter name")
    hospital = session.query(Hospital).filter_by(name=name).first()
    session.delete(hospital)
    d = session.commit()
    if d:
        print("Deleted successfuly")
    else:
        click.echo(f"No hospital with this name {name} on our records")


if __name__ == "__main__":
    hospital_menu()
