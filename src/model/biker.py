from dataclasses import dataclass
@dataclass
class Biker:
    rut: str
    name: str
    last_name: str
    age: int
    club: str
    city: str
    category: str

    def to_dict(self):
        return {
            "rut": self.rut,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age,
            "category": self.category,
            "city": self.city,
            "club": self.club
        }