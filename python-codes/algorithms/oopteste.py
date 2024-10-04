class Microwave:
    def __init__(self, brand:str, power_rating:str) -> None:
        self.brand = brand
        self.power_rating = power_rating

smeg: Microwave = Microwave("Bom dia turma", "Sete pecados capitais")
print(smeg)
print(smeg.power_rating)