import PySimpleGUI as sg
import logic
from tabulate import tabulate

def main():
    sg.theme('LightBlue2')

    layout = [
        [sg.Text("Ласкаво просимо до гри 'Вгадай число'!", size=(30, 1), justification='center')],
        [sg.Text("Введіть число між 1 та 100:", size=(30, 1), justification='center')],
        [sg.InputText(size=(10, 1), key='-INPUT-')],
        [sg.Button('Вгадати'), sg.Button('Вийти'), sg.Button('Рекорди')],
        [sg.Text('', size=(30, 1), key='-OUTPUT-', justification='center')],
    ]

    window = sg.Window('Гра "Вгадай число"', layout, finalize=True)

    logic.setup_game()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, 'Вийти'):
            break
        elif event == 'Рекорди':
            scores_table = logic.get_scores_table()
            scores_str = tabulate(scores_table, headers=['Місце', 'Спроби'], tablefmt='pretty')
            sg.popup_scrolled(scores_str, title='Рекорди')

        result = logic.play_round(values['-INPUT-'])
        window['-OUTPUT-'].update(result)

    window.close()

if __name__ == "__main__":
    main()
