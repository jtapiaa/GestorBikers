import os
from model.biker import Biker
from services.controller import add_biker


def save_bikers_to_file(bikers: list[Biker], path: str) -> None:
    if not bikers:
        print("No bikers to save.")
        return
    try:
        with open(path, "a", encoding="utf-8") as file:
            for biker in bikers:
                file.write(
                    f"{biker.rut},{biker.name},{biker.last_name},{biker.age},{biker.category},{biker.city},{biker.club}\n"
                )
            print("Bikers saved to file successfully.")
    except OSError as e:
        print(f"Error saving biker to file: {e}")


def load_bikers_from_file(path: str = "data/bikers.txt") -> dict[str, Biker]:
    bikers: dict[str, Biker] = {}
    if not os.path.exists(path):
        print("File not found.")
        return bikers
    with open(path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rut, name, last_name, age, category, city, club = line.split(",")
                biker = Biker(
                    rut=rut,
                    name=name,
                    last_name=last_name,
                    age=age,
                    category=category,
                    city=city,
                    club=club,
                )
                add_biker(biker)
            except ValueError:
                print(f"Invalid format on line {line_number}: {line}")
    return bikers
