#GUI using PYsimpleGUI
from pathlib import Path  # core python module
import PySimpleGUI as sg

def is_valid_path(filepath):
    if filepath and Path(filepath).exists():
        return True
    sg.popup_error("Filepath does not exist")
    return False

layout = [[sg.Text("Video File:"), sg.Input(key = "video_input_location"), sg.FileBrowse(file_types = (("Video Files", "*.mp4*")))],
        [sg.Exit(), sg.Button("Create Frames"), sg.Button("Create Spectrogram from frames")]],

window = sg.Window("Video to Spectrogram", layout)
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit", "Next"):
        break
    if event == "Create Frames":
        if is_valid_path(values["video_input_location"]):
            value = 1
            break
    if event == "Create Spectrogram from frames":
        if is_valid_path(values["video_input_location"]):
            value = 2
            break


window.close()
