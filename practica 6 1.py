menu = [
    {"id": 1, "desc": "Arroz", "precio": 50},
    {"id": 2, "desc": "Habichuelas", "precio": 60},
    {"id": 3, "desc": "Aceite", "precio": 300},
    {"id": 4, "desc": "Lechuga", "precio": 80},
    {"id": 5, "desc": "Pollo", "precio": 90},
    {"id": 6, "desc": "Carne", "precio": 120},
    {"id": 7, "desc": "Pasta", "precio": 70},
    {"id": 8, "desc": "Papas", "precio": 40},
    {"id": 9, "desc": "Tomate", "precio": 25},
    {"id": 10, "desc": "Cebolla", "precio": 30},
    {"id": 11, "desc": "Huevos", "precio": 10},
    {"id": 12, "desc": "Queso", "precio": 100},
    {"id": 13, "desc": "Pan", "precio": 15},
    {"id": 14, "desc": "Refresco", "precio": 55},
    {"id": 15, "desc": "Yogurt", "precio": 65},
]

def imprimir_menu(menu):
    print("ID   Descripción     Precio")
    print("|===========================|")
    for producto in menu:
        print(f"{producto['id']:2}   {producto['desc']:13}   {producto['precio']:5}")

def comprar(menu):
    carrito = []
    salir_o_no = 1
    while salir_o_no == 1:
        imprimir_menu(menu)
        opc = int(input("Ingresa el numero del producto que deseas: "))
        cantidad = int(input("Ingresa la cantidad que deseas comprar: "))
        producto = buscar_producto(opc, menu)
        if producto == -1:
            print("Opción inválida")
        else:
            producto["cantidad"] = cantidad
            carrito.append(producto)
        salir_o_no = int(input("Deseas agregar más productos? 1. Sí 2. No: "))
    return carrito

def buscar_producto(id, menu):
    for producto in menu:
        if producto["id"] == id:
            return producto
    return -1

def calcular_total(productos):
    subtotal = 0
    for producto in productos:
        subtotal += producto["precio"] * producto["cantidad"]
    impuesto = subtotal * 0.18
    total = subtotal + impuesto
    return subtotal, impuesto, total

def imprimir_recibo(productos):
   
    print("Producto      Cantidad     Precio unitario     Subtotal")
    print("|========================================================|")
    for producto in productos:
        subtotal_producto = producto["precio"] * producto["cantidad"]
        print(f"{producto['desc']:11}   {producto['cantidad']:8}   {producto['precio']:15}   {subtotal_producto}")
    subtotal, impuesto, total = calcular_total(productos)
    print("\nSubtotal:", subtotal)
    print("ITBIS 18%:", impuesto)
    print("Total:", total)

productos = comprar(menu)
imprimir_recibo(productos)
