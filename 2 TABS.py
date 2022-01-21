from PySimpleGUI import PySimpleGUI as sg

# Tabs
tab1_layout = [
    [sg.T('Selário p/mês para p/hora ou p/dia')],
    [sg.Text('Salário'), sg.Input(key='tab1_salario', size=(20, 1)), ],
    [sg.Text('Carga horária'), sg.Input(key='tab1_horas', size=(20, 1))],
    [sg.CB('Calcular por hora', key='tab1_boxhora', ), sg.CB('Calcular por dia', key='tab1_boxdia')],
    [sg.Button('Calcular', key='tab1_calcular'), sg.Output(size=(20, 1))]
]

tab2_layout = [
    [sg.T('Selário p/hora para p/mês')],
    [sg.Text('Salário'), sg.Input(key='tab2_salario', size=(20, 1)), ],
    [sg.Text('Carga horária'), sg.Input(key='tab2_horas', size=(20, 1))],
    [sg.CB('Calcular por hora', key='tab2_boxhora',), sg.CB('Calcular por dia', key='tab2_boxdia')],
    [sg.Button('Calcular', key='tab2_calcular'), sg.Output(size=(20, 1))]
]

# Layout
sg.theme('BlueMono')
layout = [
    [sg.TabGroup([[sg.Tab('P/mês para p/hora', tab1_layout),
                   sg.Tab('P/hora para p/mês', tab2_layout)]])]

]
# Janela
janela = sg.Window('Calculadora de salário').Layout(layout)

# Valores


# Ler os eventos
while True:
    eventos, valores = janela.read()
    salario_tab1 = float(valores['tab1_salario'])
    horas_trabalho_tab1 = float(valores['tab1_horas']) * 30
    salario_tab2 = float(valores['tab2_salario'])
    horas_trabalho_tab2 = float(valores['tab2_horas'])
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'tab1_calcular':
        if valores['tab1_salario'] != '' and valores['tab2_horas'] != '':
            if valores['tab1_boxhora']:
                print(f'{salario_tab1 / horas_trabalho_tab1:.2f} R$ Por hora')
            elif valores['tab1_boxdia']:
                print(f'{salario_tab1 / 30:.2f} R$ Por dia')
    elif eventos == 'tab2_calcular':
        if valores['tab2_salario'] != '' and valores['tab2_horas'] != '':
            if valores['tab2_boxhora']:
                print(f'{salario_tab2 / horas_trabalho_tab2:.2f} R$ Por hora')
            elif valores['tab2_boxdia']:
                print(f'{salario_tab2 / 30:.2f} R$ Por dia')

