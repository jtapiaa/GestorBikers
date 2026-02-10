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
from utils.file_manager import load_bikers_from_file, save_bikers_to_file
from utils.module_11 import validate_rut


def main():
    while True:
        print("\n********** Menu opciones. **********\n")
        print("1. Add biker")
        print("2. List biker")
        print("3. Find biker by ID")
        print("4. Delete biker by ID")
        print("5. Save biker to File")
        print("6. Load biker from File")
        print("7. Exit")
        option = input("Select an option: ")
        try:
            match option:
                case "1":
                    while True:
                        rut = input("Enter Biker RUT: ")
                        if not validate_rut(rut):
                            print("Invalid RUT format. Please try again.")
                            continue
                        if find_biker_by_id(rut) is not None:
                            print("RUT already exists. Please enter a different one.")
                            continue
                        break
                    name = input("Enter Biker name: ")
                    last_name = input("Enter Biker last name: ")
                    while True:
                        age = input("Enter Biker age: ")
                        try:
                            age = int(age)
                            if age <= 0:
                                print(
                                    "Age must be a positive integer. Please try again."
                                )
                                continue
                            break
                        except ValueError:
                            print("Age must be a positive integer. Please try again.")
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
                    biker_rut = input("Enter biker Rut to search: ")
                    biker = find_biker_by_id(biker_rut)
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
                    file_path = "src/data/bikers.txt"
                    save_bikers_to_file(list_bikers(), file_path)
                case "6":
                    file_path = "src/data/bikers.txt"
                    bikers_dict = load_bikers_from_file(file_path)
                    print("Bikers loaded from file:", list(bikers_dict.values()))
                case "7":
                    print("Exiting...")
                    break
                case _:
                    print("****** Invalid option. Please try again. ******")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
