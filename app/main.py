from build_text_scope import __build__
from segregate_text import searchElement
from configuration import produtos_1, produtos_2, classes_1, area_atividade_1, area_atividade_2
from app.format_list import formatar_resultado

global_text = __build__('escopo.pdf')

print(global_text)
