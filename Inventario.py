inventario = [
    ("Célula de Energia", 10, "Combustível"),
    ("Ração de Sobrevivência", 50, "Mantimentos"),
    ("Filtro de Oxigênio", 2, "Suporte de Vida"),
    ("Kit Médico", 5, "Saúde"),
    ("Parafuso de Titânio", 200, "Manutenção")
]
inventario.append(("Escudo Térmico", 3, "Defesa"))

estoque_baixo = [

]

for item in inventario:
    if item[1] < 5:
        estoque_baixo.append(item)        

inventario_ordenado = sorted(inventario, key=lambda item: item[1], reverse=True)
inventario.sort()

print(f"Itens com baixo estoque: {estoque_baixo}")
print("\n Inventário completo :")
for itens in inventario_ordenado:
    print(itens)
