def append_to (element, to=[]):
    to.append(element)
    return to


lista_1 = append_to("soproni")
lista_1 = append_to ("borsodi", lista_1)

lista_2 = append_to("heineken")
lista_2 = append_to("staropramen", lista_2)

lista_3 = append_to ("arany ászok", lista_1)

print(lista_1)
print(lista_2)
print(lista_3)
