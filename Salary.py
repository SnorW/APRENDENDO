from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('BlueMono')
layout = [
    [sg.Text('Salário'), sg.Input(key='salario', size=(20, 1)), ],
    [sg.Text('Carga horária'), sg.Input(key='horas', size=(20, 1))],
    [sg.CB('Calcular por hora', key='boxhora',), sg.CB('Calcular por dia', key='boxdia')],
    [sg.Button('Calcular'), sg.Output(size=(20, 1))]
]
# Janela
janela = sg.Window('Calculadora de salário', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    # Valores
    salario = float(valores['salario'])
    horas_trabalho = float(valores['horas']) * 30
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Calcular':
        if valores['salario'] != '' and valores['horas'] != '':
            if valores['boxhora']:
                print(f'{salario/horas_trabalho:.2f} R$ Por hora')
            elif valores['boxdia']:
                print(f'{salario/30:.2f} R$ Por dia')
