import json
json_introducido = {
    "course": [
        { 
          "name" : ["Refresco de Lata", "Malta Caribia", "Refresco Manzanita", "Seven-up", "Pinita", "Agua", "Energizante", "Jugo de Caja", "Batido de Helado"],
          "price" : [220, 230, 290, 240, 225, 180, 245, 175, 450]
          }
    ]
}

json_ordenado = []
for course in json_introducido["course"]:
    names = course["name"]
    prices = course["price"]
    for name, price in zip(names, prices):
        course_dict = {
            "name": name,
            "price": price
        }
        json_ordenado.append(course_dict)
for course in json_ordenado:
    print(course)