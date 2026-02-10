from os import path
from unittest import case
from model.biker import Biker
from services.controller import (
    add_biker,
    delete_biker_by_id,
    find_biker_by_id,
    list_bikers,
    validate_rut,
)
from utils.file_manager import save_bikers_to_file
from utils.module_11 import validate_rut


def main():
    while True:
        print("\n********** Menu opciones. **********\n")
        print("1. Add biker")
        print("2. List biker")
        print("3. Find biker by ID")
        print("4. Delete biker by ID")
        print("5. Save biker to File")
        print("6. Exit")
        option = input("Select an option: ")
        try:
            match option:
                case "1":
                    rut = input("Enter Biker RUT: ")
                    while not validate_rut(rut):
                        print("Invalid RUT. Please try again.")
                        rut = input("Enter Biker RUT: ")
                    name = input("Enter Biker name: ")
                    last_name = input("Enter Biker last name: ")
                    age = int(input("Enter Biker age: "))
                    while type(age) != int or age <= 0:
                        print("Age must be a positive integer. Please try again.")
                        age = int(input("Enter Biker age: "))
                    category = input("Enter Biker category: ")
                    city = input("Enter Biker City: ")
                    club = input("Enter Biker Club: ")
                    biker = Biker(
                            rut=rut,
                            name=name,
                            last_name=last_name,
                            age=age,
                            category=category,
                            city=city,
                            club=club,
                        )
                    print(biker)
                    add_biker(biker)
                    print("Biker added successfully.")
                case "2":
                    bikers = list_bikers()
                    if not bikers:
                        print("No bikers found.")
                    else:
                        for biker in bikers:
                            print(biker.to_dict())
                case "3":
                    biker_id = input("Enter biker ID to search: ")
                    biker = find_biker_by_id(biker_id)
                    if biker:
                        print("Biker found:", biker.to_dict())
                    else:
                        print("Biker not found.")
                case "4":
                    biker_id = input("Enter biker ID to delete: ")
                    if delete_biker_by_id(biker_id):
                        print("Biker deleted successfully.")
                    else:
                        print("Biker not found.")
                case "5":
                    file_path = input("Enter file path to save bikers: ")
                    save_bikers_to_file(list_bikers(), file_path)
                case "6":
                    print("Exiting...")
                    break
                case _:
                    print("****** Invalid option. Please try again. ******")
        except Exception as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    main()
