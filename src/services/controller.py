from model.biker import Biker

# Define un objeto lista de usuarios vacia
bikers: list[Biker] = []

def add_biker(biker: Biker) -> None:
    bikers.append(biker)

# Busca la lista de usuarios si no hay usuarios retorna una lista vacia
# Si no retorna la lista de usuarios y los imprime en formato diccionario
def list_bikers() -> list[Biker]:
    if not bikers:
        return []
    return bikers   

    
# Busca un usuario por su ID
def find_biker_by_id(rut: str) -> Biker | None:
    for biker in bikers:
        if biker.rut == rut:
            return biker   
    return None

# Elimina una tarea por su ID
def delete_biker_by_id(biker_id: int) -> bool:
    for i, biker in enumerate(bikers):
        if biker.rut == biker_id:
            bikers.pop(i)
            return True
    return False

def validate_rut(biker_rut: int) -> bool:
    return any(biker.rut == biker_rut for biker in bikers)
