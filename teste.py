from PySimpleGUI import Window, Image

layout = [
    [Image(filename='du.png')]
]

window = Window(
    'Janela',
    layout = layout
)

print(window.read())

window.close()