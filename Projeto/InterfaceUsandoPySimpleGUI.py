from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    # entra de input onde o usuario ira colocar o seu dados para passa para proxima etapa
    [sg.Text('Nome'),sg.Input(key='Usuario',size=(15,2))],
    [sg.Text('Sobrenome'),sg.Input(key='Sobrenome',size=(15,2))],
    # senha do usuario para entra no seu login
    [sg.Text('Senha '),sg.Input(key='Senha',password_char='*',size=(15,2))],
    
    # caixa vazia para selecionar se  você deseja que seja salvo =
    [sg.Checkbox('Salvar o login')],
    [sg.Button('Entrar')]
]
# Janela
janela= sg.Window('Tela',layout)
# Ler os Eventos
while True:
    # Manter a página aberta, e o break é para fechar a pag 
    eventos, valores =  janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores ['Usuario'] == 'Gabriel' and valores ['Senha'] == '04012008' and valores ['Sobrenome'] == 'Silva':
            print('Seu login esta correto, seja Bem-vindo')
        else:
            print('Seu login esta incorreto')
   # GBSJ008
   
