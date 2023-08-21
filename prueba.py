import random
import string

def generar_nombre():
    frutas = ["Manzanas", "Peras", "Platanos", "Fresas", "Uvas", "Naranjas", "Sandías", "Cerezas", "Melones", "Kiwis", "Mangos", "Papayas", "Piñas", "Duraznos", "Ciruelas", "Higos", "Moras", "Frambuesas", "Granadas", "Pomelos"]
    verduras = ["Zanahorias", "Papas", "Tomates", "Espinacas", "Lechugas", "Pepinos", "Brócoli", "Calabazas", "Cebollas", "Acelgas", "Pimientos", "Apio", "Espárragos", "JudíasVerdes", "Calabacines", "Coliflor", "Aguacates", "Berenjenas", "Rábanos", "Calabacitas"]
    
    if random.random() < 0.5:
        return random.choice(frutas)
    else:
        return random.choice(verduras)

def generar_producto():
    nombre = generar_nombre()
    cantidad = random.randint(50, 300)
    precio_unitario = round(random.uniform(1.22, 9.78), 2)
    ubicacion = f"Bodega{random.choice(string.ascii_uppercase[:-1])}"
    
    return f"crear_producto {nombre};{cantidad};{precio_unitario:.2f};{ubicacion}"

for i in range(100):
    print(generar_producto())
