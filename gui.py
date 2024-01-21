#GUI using PYsimpleGUI
import PySimpleGUI as sg

layout = [[sg.Text("Video File:"), sg.Input(key = "video_input_location"), sg.FileBrowse(file_types = (("Video Files", "*.mp4*")))],
        [sg.Exit("Next")]],

window = sg.Window("Video to Spectrogram", layout)
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit", sg.Button("Next"), "Next"):
        break
window.close()
