
# Teste do build_text_scope.py

# from build_text_scope import main

# print(main('escopo.pdf'))

# Teste do segregate_text.py

from app.segregate_text import searchElement

list1 = ["1nd", 'flask', 'pain']

text = "Teste ae flask 1ndteste pain aaaa pain aaaaaaaa"

searchElement(text, list1)

print(f'AAAAAAAAAAAAAA: {text[15+len(list1[0]):]}')