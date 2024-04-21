import PySimpleGUI as sg

label1 = sg.Text('Select files to compress:')
input1 = sg.InputText()
button1 = sg.FilesBrowse('Choose', key='files')

label2 = sg.Text('Select destination folder:')
input2 = sg.InputText()
button2 = sg.FolderBrowse("Choose", key='folder')
button3 = sg.Button('Compress')

window = sg.Window('File Compressor', layout=[[label1, input1, button1],
                                              [label2, input2, button2],
                                              [button3]],
                                              font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(';')
    folder = values['folder']
    print(filepaths)




window.close()