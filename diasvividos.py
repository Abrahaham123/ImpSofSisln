from datetime import datetime

fecha_nacimiento = input("Ingresa tu fecha de nacimiento (dd/mm/yyyy): ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
hoy = datetime.now()

dias_vividos = (hoy - fecha_nacimiento).days
print(f"Has vivido {dias_vividos} días.")
