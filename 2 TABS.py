from PySimpleGUI import PySimpleGUI as sg

# Tabs
tab1_layout = [
    [sg.T('Salário p/hora ou p/dia')],
    [sg.Text('Salário por mês'), sg.In(key='tab1_salario', size=(20, 1)), ],
    [sg.Text('Carga horária'), sg.In(key='tab1_horas', size=(20, 1))],
    [sg.Checkbox('Calcular por hora', key='tab1_boxhora', ), sg.Checkbox('Calcular por dia', key='tab1_boxdia')],
    [sg.Button('Calcular', key='tab1_calcular')]
]

tab2_layout = [
    [sg.T('Salário p/mês ou p/ano')],
    [sg.Text('Salário por hora'), sg.In(key='tab2_salario', size=(20, 1)), ],
    [sg.Text('Carga horária'), sg.In(key='tab2_horas', size=(20, 1))],
    [sg.Checkbox('Calcular por mes', key='tab2_boxmes', ), sg.Checkbox('Calcular por ano', key='tab2_boxano')],
    [sg.Button('Calcular', key='tab2_calcular')]
]

# Layout
sg.theme('BlueMono')
layout = [
    [sg.TabGroup([[sg.Tab('P/mês para p/hora', tab1_layout),
                   sg.Tab('P/hora para p/mês', tab2_layout)]])],
    [sg.Output(size=(30, 2))]
]
# Janela
janela = sg.Window('Calculadora de salário').Layout(layout)

# Valores


# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
# Calular por dia ou hora
    if eventos == 'tab1_calcular':
        salario_tab1 = float(valores['tab1_salario'])
        horas_trabalho_tab1 = float(valores['tab1_horas']) * 30
        if valores['tab1_salario'] != '' and valores['tab1_horas'] != '':
            if valores['tab1_boxhora']:
                print(f'{salario_tab1 / horas_trabalho_tab1:.2f}$ Por hora')
            elif valores['tab1_boxdia']:
                print(f'{salario_tab1 / 30:.2f} R$ Por dia')
# Calcular por mês ou ano
    if eventos == 'tab2_calcular':
        salario_tab2 = float(valores['tab2_salario'])
        horas_trabalho_tab2 = float(valores['tab2_horas']) * 30
        if valores['tab2_salario'] != '' and valores['tab2_horas'] != '':
            if valores['tab2_boxmes']:
                print(f'{salario_tab2 / horas_trabalho_tab2:.2f} R$ por mês')
            elif valores['tab2_boxano']:
                print(f'{salario_tab2 / 30:.2f} R$ Por dia')
