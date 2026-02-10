from model.biker import Biker


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
