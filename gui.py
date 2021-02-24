import PySimpleGUI as sg
import Calculations

cal = Calculations.Kalkulator(1, 1)

class Graphic:
    def __init__(self):
        self.layout = [[sg.Text('Liczba1: '), sg.Text('', key='l1', size=(100, 1))],
                       [sg.Text('Liczba2: '), sg.Text('', key='l2', size=(100, 1))],
                  [sg.Text('Wynik'),sg.Text('', key='-OUT-', size=(100, 1))],
                  [sg.Text('Operacje', key='oper', size=(100, 1))],
                  [sg.B('1'), sg.B('2'), sg.B('3'), sg.B('/')],
                  [sg.B('4'), sg.B('5'), sg.B('6'), sg.B('*')],
                  [sg.B('7'), sg.B('8'), sg.B('9'), sg.B('-')],
                  [sg.B('0'), sg.B('=', size=(7, 1)), sg.B('+')],
                  [sg.B('Exit')]]

        self.window = sg.Window('Title', self.layout, size=(300, 300))

        self.liczba1 = ""
        self.liczba2 = ""

    def work(self):
        flag = 0
        while True:

            event, values = self.window.read()
            if event is None or event == 'Exit':
                break
            elif event in '1234567890' and flag==0:
                self.liczba1 = self.liczba1 + event
                cal.a=int(self.liczba1)

            elif event in '1234567890' and flag==1:
                self.liczba2 = self.liczba2 + event
                cal.b = int(self.liczba2)
            elif event in '+-/*' and flag == 0:
                flag=1
                whattodo=event

            elif event == '=':
                flag=0
                if whattodo == '+':
                    self.window['-OUT-'].update(cal.Dodawanie())

                if whattodo == '-':
                    self.window['-OUT-'].update(cal.Odejmowanie())
                if whattodo == '/':
                    self.window['-OUT-'].update(cal.Dzielenie())
                if whattodo == '*':
                    self.window['-OUT-'].update(cal.Mnozenie())
                self.liczba1 = ""
                self.liczba2 = ""


            #if flag==0:
            self.window['l1'].update(self.liczba1)
            #if flag ==1:
            self.window['l2'].update(self.liczba2)



        self.window.close()

gui =Graphic()
gui.work()