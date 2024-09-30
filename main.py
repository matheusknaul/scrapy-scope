from build_text_scope import __build__
from segregate_text import searchElement
from configuration import produtos_1, produtos_2, classes_1, area_atividade_1, area_atividade_2
from format import formatar_resultado

global_text = __build__('escopo.pdf')

intervalList = searchElement(global_text, area_atividade_1)
formattedResult = formatar_resultado(intervalList)

group = []

for result in formattedResult:
    register = []
    register.append(result[0])
    NewIntervalList = searchElement(result[1], classes_1)
    NewFormattedResult = formatar_resultado(NewIntervalList)
    register.append(NewFormattedResult)
    group.append(register)

print(group)
