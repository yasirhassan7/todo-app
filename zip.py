import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Compress")

label2 = sg.Text("Select destination output:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Upload")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor",
                   layout=[[label1,input1,choose_button1],
                   [label2,input2,choose_button2],
                           [compress_button]])

window.read()
window.close()

