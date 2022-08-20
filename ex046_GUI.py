#pip install PySimpleGUI
#pip install Pillow

from fileinput import filename
from PySimpleGUI import PySimpleGUI as sg

#Layout
def janelaLogin(): #TELA INICIAL

    sg.theme('Reddit')
    layout = [
        [sg.Text('Usuário'), sg.Input(key='usuario', size=(25,1))],
        [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(26,1))],
        [sg.Button('Entrar')],
        [sg.Text('', key='mensagem')] #MENSAGEM VARIAVEL
    ]
    return sg.Window('Login', layout=layout, finalize=True)

img = ''
bemvindo = ''
def janelaLogado(): #USUARIO LOGADO

    sg.theme('DarkTeal9')
    layout = [
        [sg.Image(filename=img, key='img')], #IMAGEM VARIAVEL; IMAGEM DO USUARIO
        [sg.Text('LOGADO COM SUCESSO!')],
        [sg.Text(bemvindo)], #MENSAGEM VARIAVEL; NOME DO USUARIO
        [sg.Button('Voltar')]
    ]
    return sg.Window('Logado', layout=layout, finalize=True)

def maxTentativas():

    sg.theme('Reddit')
    layout = [
        [sg.Text('MÁXIMO DE TENTATIVAS')]
    ]
    return sg.Window('MAXIMO DE TENTATIVAS', layout=layout, finalize=True)

#Janela
janela1, janela2, janela_max_tentativas = janelaLogin(), None, None
#Imagens

#Eventos
erro = 3

while erro >= 0:
    window, eventos, valores = sg.read_all_windows()

    if window == janela1 and eventos == sg.WIN_CLOSED:
        break
    if window == janela2 and eventos == sg.WINDOW_CLOSED:
        break
    if window == janela_max_tentativas and eventos == sg.WINDOW_CLOSED:
        break
#ENTRAR
    if eventos == 'Entrar':

        if valores['usuario'] == 'duzera' and valores['senha'] == '':
            bemvindo = 'Bem-vindo, ' + valores['usuario'] + '!'
            img = 'duzera.png'
            janela2 = janelaLogado()
            janela1.hide()
            erro = 3

        elif valores['usuario'] == 'USER10' and valores['senha'] == 'PASSWORD1234':
            bemvindo = 'Bem-vindo, ' + valores['usuario'] + '!'
            img = 'user10.png'
            janela2 = janelaLogado()
            janela1.hide()
            erro = 3
        
        elif valores['usuario'] == 'guinho' and valores['senha'] == 'james':
            bemvindo = 'Bem-vindo, ' + valores['usuario'] + '!'
            img = 'guinho.png'
            janela2 = janelaLogado()
            janela1.hide()
            erro = 3

        else:
            window['mensagem'].update('USUÁRIO NÃO ENCONTRADO!\nVOCÊ TEM %s TENTATIVAS!' %(erro - 1))
            if erro - 1 == 1:
                window['mensagem'].update('USUÁRIO NÃO ENCONTRADO!\nVOCÊ SÓ TEM %s TENTATIVA!' %(erro - 1))

            if erro == 1: #ERROS
                janela_max_tentativas = maxTentativas()
                janela1.hide()
            erro -= 1
#VOLTAR
    if eventos == 'Voltar':
        
        if window == janela2:
            janela1 = janelaLogin()
            janela2.hide()