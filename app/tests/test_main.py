import test_configuration
from segregate_text import __search__
from format_list import organizar_indices
from build_table import __build__
from build_text_scope import __build_text__
from configuration import produtos_1, produtos_2, classes_1, area_atividade_1, area_atividade_2
from build_row import __make_text__
from build_excel import __make_excel__

texto = __build_text__('escopo.pdf')
lista = __search__(texto, produtos_2)
lista_new = organizar_indices(lista)
lista_segregada = __build__(lista_new)
rows = __make_text__(texto, lista_segregada)
__make_excel__(rows)
