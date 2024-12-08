import FreeSimpleGUI as sg
from zip_creator import make_archive
import os


label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Compress",key="files")

label2 = sg.Text("Select destination output:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Upload",key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("File Compressor",
                   layout=[[label1,input1,choose_button1],
                   [label2,input2,choose_button2],
                           [compress_button, output_label]])


while True:
    event, values = window.read()
    filepaths = values["files"].split(";")
    folder = values["folder"].split(";")
    make_archive(filepaths,folder)
    window["output"].update(values["Compression Completed!"])


window.close()


