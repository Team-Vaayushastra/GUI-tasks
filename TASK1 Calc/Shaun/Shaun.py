from PySimpleGUI import *

layout = [[Txt('' * 10,background_color='black')],
          [Text('', size=(15, 1), font=('Roboto', 18),
                text_color='black', key='input',background_color='#63D2EC')],
          [Txt('' * 10,background_color='black')],
          [ReadFormButton('C'), ReadFormButton('DEL'),ReadFormButton('**'),ReadFormButton('/')],
          [ReadFormButton('7'), ReadFormButton('8'), ReadFormButton('9'),ReadFormButton('+') ],
          [ReadFormButton('4'), ReadFormButton('5'), ReadFormButton('6'), ReadFormButton('*')],
          [ReadFormButton('1'), ReadFormButton('2'), ReadFormButton('3'), ReadFormButton('-')],
          [ReadFormButton('.'), ReadFormButton('0'),ReadFormButton('00'), ReadFormButton('=')],
          ]

form = FlexForm('MY CALCULATOR',background_color='black', default_button_element_size=(5, 2),
                auto_size_buttons=False, grab_anywhere=False)
form.Layout(layout)
def decimal_binary(num):
          if num >= 1:
                    DecimalToBinary(num // 2)
           print(num % 2, end = '')
          return num%2
# Result Value
Result = ''
while True:
    # Button Values
    button, value = form.Read()

    if button == 'C':
        Result = ''
        form.find_element('input').Update(Result)
    elif button == 'DEL':
        Result = Result[:-1]
        form.find_element('input').Update(Result)
    elif len(Result) == 16:
        pass

    elif button == '=':
            Answer = eval(Result)
            Answer = str(round(float(Answer), 3))
            form.find_element('input').Update(Answer)
            Result = Answer


    elif button == 'Quit' or button == None:
        break
    elif button =='Bin':
                    
                    form.find_element('input').Update(Result)
                    Answer=decimal_binary(value)
                    Result = Answer
    else:
        Result += button
        form.find_element('input').Update(Result)
