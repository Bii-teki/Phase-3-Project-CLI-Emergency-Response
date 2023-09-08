import click
from hospital import hospital_menu
from transport import menu
from patient import patient_menu


print("Emergency Response Management System")
@click.command()
@click.option(
    "--choice",
    prompt="Enter your choice:\n1 for Hospital\n2 for Transport\n3 for Patients\n4 to Quit\n",
    type=click.IntRange(1, 5),
)
def main_menu(choice):
    if choice == 1:
        hospital_menu()
    elif choice == 2:
        menu()
    elif choice == 3:
        patient_menu()
    
    elif choice == 4:
        click.echo("Quitting the program.")
    else:
        click.echo("Invalid choice. Please select 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main_menu()
