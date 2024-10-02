import test_configuration
from segregate_text import __search__
from format_list import organizar_indices

list1 = ["1nd", 'flask', 'pain', 'cbol']

text = "Teste ae flask 1ndteste pain aaaa pain aaaaaaaa pain pain pain AAAAAAAAAA cbol teste teste"

lista = __search__(text, list1)

print(f'AAAAAAAAAAAAAA: {text[28:]}')

print(organizar_indices(lista))