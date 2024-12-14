from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    # entra de input onde o usuario ira colocar o seu dados para passa para proxima etapa
    [sg.Text('Usuário'),sg.Input(key='Usuario',size=(20,1))],
    
    # senha do usuario para entra no seu login
    [sg.Text('Senha '),sg.Input(key='Senha',password_char='*',size=(20,1))],
    
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
        if valores ['Usuario'] == 'Gabriel' and valores ['Senha'] == '04012008': 
            print('Seu login esta correto, seja Bem-vindo')

   # GBSJ008
