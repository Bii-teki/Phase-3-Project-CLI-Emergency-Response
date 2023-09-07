import click

from seed import session
from example import  Person



@click.command()
@click.option('--choice', prompt = 'Enter your choice (1 to Add Person, 2 to View, 3 to Delete, or 4 to Quit):\n', type=click.IntRange(1, 4))
def menu(choice):
    if choice == 1:
        add_person()
    elif choice == 2:
        view_person()
    elif choice == 3:
        delete_person()
    elif choice == 4:
        click.echo('Quitting the program.')
    else:
        click.echo('Invalid choice. Please select 1, 2, 3, or 4.')
persons = []
def add_person():
    print("Adding Person...")
    name = click.prompt('Enter the name:')
    age = click.prompt('Enter the age:', type=int)
    
    person = Person(name=name, age=age)
    session.add(person)
    session.commit()
        
    persons.append(person)

    click.echo(f'Added {name} with age {age} to the database.')

def view_person():    
    print("Searching for Person...")
    name = click.prompt("Enter name to search...")
    person = session.query(Person).filter_by(name=name).first()
    
    if person:
        click.echo(f"Name: {person.name}, Age: {person.age}")
    else:
        click.echo(f'Person with name {name} not found in the database.')
       
    
    

def delete_person():
    print("Deleting Person")
    id = click.prompt('Enter id', type=int)
    pr = session.query(Person).filter_by(id=id).first()
    
    if pr:
        session.delete(pr)
        session.commit()
        print(f'Person with ID {id} has been deleted.')
    else:
        print(f'Person with ID {id} not found in the database.')


    
    

if __name__ == '__main__':
    menu()

    
