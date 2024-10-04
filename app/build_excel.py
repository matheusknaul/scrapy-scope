import openpyxl

def __make_excel__(lista):

    wb = openpyxl.Workbook()
    ws = wb.active

    ws['A1'] = 'Produto'
    ws['B1'] = 'Ensaio'

    for item in range(len(lista)):
        ws[f'A{item + 2}'] = lista[item][0]
        ws[f'B{item + 2}'] = lista[item][1]

    wb.save('app/tabela_ensaio.xlsx')
    print('Arquivo excel criado com sucesso!')
