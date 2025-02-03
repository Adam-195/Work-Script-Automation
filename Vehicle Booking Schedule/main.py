import PySimpleGUI as sg
from datetime import datetime
import pandas as pd

excel_file = 'xxxx' # Removed link to CSV due to data protection
df = pd.read_excel(excel_file)

#The Theme
font = ("Usual", 11)

#Layout of data to be inputed
layout = [
    [sg.Text('Fill out the following fields: ', background_color='#142032', font = ("Usual ExtraBold", 16), justification='centre')],
    [sg.Text('EIN', size=(15,1), background_color='#142032'), sg.InputText(key= 'EIN')],
    [sg.Text('Name', size=(15,1), background_color='#142032'), sg.InputText(key= 'Name')],
    [sg.Text('OUC', size=(15,1), background_color='#142032'), sg.InputText(key= 'OUC')],
    [sg.Text('Pool Van Reg', size=(15,1), background_color='#142032'), sg.Combo(['VFZ5696', 'Test'], key='Pool Van Reg')], #autopull the regs from somewhere
    [sg.Input(key='Date Collected', size=(15,1), background_color='#142032'), sg.CalendarButton('Date Collected', close_when_date_chosen=True)],
    [sg.Input(key='Date Returned', size=(15,1), background_color='#142032'), sg.CalendarButton('Date Returned', close_when_date_chosen=True)],
    [sg.Submit(button_color='#3EA66C'), sg.Exit(button_color='#142032')]
]

window = sg.Window('Pool Vehicle Booking', layout, background_color='#142032', button_color='#50535A', font=font)

#Open & Exit Application
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        df = df._append(values, ignore_index=True)
        df.to_excel(excel_file, index=False)
        sg.popup('Pool Van now booked! Please Reach out to X to get the Keys')
window.close()