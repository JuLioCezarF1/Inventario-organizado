inventario = {
    'Célula de Energia':{'quantidade': 10, 'tipo': 'Combustível'},
    'Ração de Sobrevivência': {'quantidade': 35, 'tipo': 'Mantimentos'},
    'Filtro de Oxigênio': {'quantidade': 2, 'tipo': 'Suporte de Vida'},
    'Kit Médico': {'quantidade': 15, 'tipo': 'Saúde'},
    'Parafuso de Titânio': {'quantidade': 200, 'tipo': 'Manutenção'},
    'Escudo Térmico': {'quantidade': 3, 'tipo': 'Defesa'}
}
inventario.pop('Parafuso de Titânio') #Aqui estou simulando que esse item acabou, por isso estou removendo da lista
item_procurado = input('Digite o item desejado: ')

print(f"Exite(m) o total de: {inventario[item_procurado]['quantidade']} do {item_procurado}")
