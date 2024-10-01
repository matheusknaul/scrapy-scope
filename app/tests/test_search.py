import test_configuration

# Teste do segregate_text.py

from segregate_text import __search__

list1 = ["1nd", 'flask', 'pain']

text = "Teste ae flask 1ndteste pain aaaa pain aaaaaaaa"

lista = __search__(text, list1)

print(f'AAAAAAAAAAAAAA: {text[28:]}')

print(lista)