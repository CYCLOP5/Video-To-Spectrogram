import os
import cv2
import numpy as np
import fnmatch
import librosa
import matplotlib.pyplot as plt
from tqdm import tqdm
from moviepy.editor import VideoFileClip, AudioFileClip
import PySimpleGUI as sg
import subprocess
import shlex
import shutil
import time

class Generator:
    def __init__(self, input_video_path, frames_folder, val):
        self.input_video_path = input_video_path
        self.frames_folder = frames_folder
        self.max_freq = 360
        self.val = val
        self.FinalLocation = None
        self.progress_value = 0  
        
        if self.val == 1:
            if os.path.exists(frames_folder):
                print("Frames folder exists, continuing frame generation where last left off.")
            else:
                os.mkdir(frames_folder)

    def load_video(self, progress_bar_callback=None):
        cap = cv2.VideoCapture(self.input_video_path)
        framesFolder = 'frames'
        path = os.path.abspath(framesFolder)
        count = len(fnmatch.filter(os.listdir(path), '*.*'))
        self.frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.FinalFrameCount = cap.set(1, count)

        buf = np.empty(((self.frameCount - count), frameHeight, frameWidth, 3), np.dtype('uint8'))

        fc = 0
        ret = True

        while (fc < (self.frameCount - count) and ret):
            ret, buf[fc] = cap.read()
            fc += 1
            self.progress_value = int((fc / (self.frameCount - count)) * 100)  
            if progress_bar_callback:
                progress_bar_callback(self.progress_value, fc + count)  

        cap.release()
        return buf[..., 0]

    def generate_frequency_swipe(self):
        frequencies = np.linspace(1, self.max_freq, self.max_freq).astype('int32')
        time = np.linspace(0, 1, self.max_freq * 2)
        frequency_swipe = []
        for frequency in frequencies:
            sine = np.sin(time * frequency * 2 * np.pi)
            frequency_swipe.append(sine)
        return np.array(frequency_swipe)

    def audio_from_frame(self, frame, frequency_swipe):
        _, binary_frame = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY)
        binary_frame = ((binary_frame / 255 - 1) * (-1)).astype('int8')

        audio_frame = []
        for column in binary_frame.T:
            column = np.expand_dims(column, 1)
            column = np.repeat(column, self.max_freq * 2, axis=1)
            audio_frame.append(np.sum(frequency_swipe * column, axis=0))

        audio_frame = np.concatenate(audio_frame)
        return audio_frame

    def save_output_frame(self, audio_frame, frame_name):
        spec = librosa.stft(audio_frame, n_fft=1024)
        fig, ax = plt.subplots(figsize=(8, 8), nrows=2, gridspec_kw={'height_ratios': [3, 1]})
        ax[0].imshow(np.abs(spec),
                     interpolation='bilinear',
                     aspect='auto',
                     cmap='plasma',
                     vmin=0,
                     vmax=1467,
                     extent=[0, 480, 360, 0])
        ax[0].set(ylabel='Frequency [Hz]', xlabel='Time [s]')
        ax[1].plot(audio_frame)
        ax[1].set(ylabel='Amplitude', xlabel='Time [s]')
        plt.savefig(os.path.join(self.frames_folder, frame_name), dpi=100)
        fig.clear()
        plt.close(fig)

    def create_video(self):
        self.video_name = 'Spectrogram.avi'
        framesFolder = 'frames'
        path = os.path.abspath(framesFolder)
        frameCount = len(fnmatch.filter(os.listdir(path), '*.*'))
        filenames = [f'frame{i}.png' for i in range(1, frameCount + 1)]
        frame = cv2.imread(os.path.join(self.frames_folder, filenames[0]))
        height, width, _ = frame.shape
        vid = cv2.VideoCapture(self.input_video_path)
        fps = vid.get(cv2.CAP_PROP_FPS)
        video = cv2.VideoWriter(self.video_name, 0, fps, (width, height))
        print("Generating video...")

        for image in tqdm(filenames):
            video.write(cv2.imread(os.path.join(self.frames_folder, image)))

        cv2.destroyAllWindows()
        video.release()

    def add_audio(self):
        cap = cv2.VideoCapture(self.FinalLocation)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        end_time = frame_count / cap.get(cv2.CAP_PROP_FPS)
        start_time = 0
        og_clip = VideoFileClip(self.input_video_path)
        extracted_audio = AudioFileClip(self.input_video_path).subclip(start_time, end_time)
        final_video = VideoFileClip(self.FinalLocation)
        final_video = final_video.set_audio(extracted_audio)
        output_video_path = 'Final.mp4'
        final_video.write_videofile(output_video_path, codec='libx264', audio_codec='aac')

        og_clip.close()
        final_video.close()
        extracted_audio.close()

        os.remove(self.FinalLocation)

class GeneratorGUI:
    def __init__(self, SpectroMaker):
        self.SpectroMaker = SpectroMaker
        sg.theme("DarkAmber")
        working_directory = os.getcwd()
        self.progress_value = 0
        self.progress_bar_element = None
        self.progress_text_element = None
        self.pause_flag = False
        self.window_closed = False  

        self.layout = [
            [sg.Text("Spectrogram Generator", font=("Helvetica", 20), justification="center", size=(40, 1))],
            [sg.Text("Select Input Video:", font=("Helvetica", 12))],
            [sg.InputText(key="video_input_location", size=(40, 1)),
             sg.FileBrowse(initial_folder=working_directory, file_types=[("MP4 Files", "*.mp4")],
                           font=("Helvetica", 10))],
            [sg.Radio("Generate Frames", "RADIO1", default=True, key="gen_frames", font=("Helvetica", 12)),
             sg.Radio("Create Spectrogram", "RADIO1", key="create_spec", font=("Helvetica", 12))],
            [sg.ProgressBar(100, orientation='h', size=(20, 20), key='progressbar', visible=False)],
            [sg.Text("", key='progress_text')],
            [sg.Button("Start", size=(20, 1)),sg.Button("Delete Frames", size=(20, 1)), sg.Button("Pause & Exit", size=(20, 1))]
        ]
        self.window = sg.Window("Spectrogram Generator", self.layout, finalize=True, grab_anywhere=True)


    def update_progress_bar(self, value, total_frames_done):
        self.progress_value = value
        if self.progress_bar_element is None:
            self.progress_bar_element = self.window['progressbar']
        self.progress_bar_element.update_bar(value)
        self.window['progress_text'].update(f'Processing frame {total_frames_done} out of {self.SpectroMaker.frameCount}')
        self.window.refresh()

    def successful_generation_popup(self, message):
        sg.popup_ok(message, title="Successful Generation")

    def error_popup(self, message):
        sg.popup_error(message, title="Error")

    def run(self):
        while True:
            event, values = self.window.read(timeout=100)

            if event == sg.WINDOW_CLOSED:
                self.window_closed = True
                break

            if event == "Start":
                if values["gen_frames"]:
                    val = 1
                elif values["create_spec"]:
                    val = 2
                else:
                    sg.popup_error("Select an option.")
                    continue

                OGvid = values["video_input_location"]
                thevideo = os.path.abspath(OGvid)
                checksum = os.path.isfile(thevideo)

                if not checksum:
                    sg.popup_error("Input.mp4 not detected. Make sure the file is named 'Input.mp4'.")
                    continue

                self.SpectroMaker = Generator(thevideo, frames_folder='frames', val=val)
                
                if val == 1:
                    try:
                        video_buf = self.SpectroMaker.load_video(progress_bar_callback=self.update_progress_bar)
                        frequency_swipe = self.SpectroMaker.generate_frequency_swipe()
                        framesFolder = 'frames'
                        path = os.path.abspath(framesFolder)
                        count = len(fnmatch.filter(os.listdir(path), '*.*'))

                        self.progress_bar_element = self.window['progressbar']
                        self.progress_text_element = self.window['progress_text']
                        self.progress_bar_element.update(visible=True)
                        self.progress_text_element.update(visible=True)

                        for i, frame in enumerate(video_buf):
                            event, values = self.window.read(timeout=100)

                            if event == sg.WINDOW_CLOSED:
                                break

                            while self.pause_flag:
                                event, values = self.window.read(timeout=100)

                                if event == "Pause & Exit" or event == sg.WINDOW_CLOSED:
                                    break

                            if self.pause_flag:
                                continue

                            if event == "Pause & Exit":
                                confirm_exit = sg.popup_yes_no("Are you sure you want to exit?", title="Confirm Exit")
                                if confirm_exit == "Yes":
                                    break

                            audio_frame = self.SpectroMaker.audio_from_frame(frame, frequency_swipe)
                            self.SpectroMaker.save_output_frame(audio_frame, f'frame{i + count + 1}')
                            self.update_progress_bar(int(((i + 1) / len(video_buf)) * 100), i + count + 1)

                            if self.pause_flag:
                                break

                        self.progress_bar_element.update(visible=False)
                        self.progress_text_element.update(visible=False)
                        self.successful_generation_popup("Frame generation completed successfully!")
                    except Exception as e:
                        self.error_popup(f"Error during frame generation: {str(e)}")
                    

                elif val == 2:
                    try:
                        self.SpectroMaker.create_video()
                        subprocess.run(shlex.split('ffmpeg -y -i Spectrogram.avi -strict -2 ConvertedSpectrogram.mp4'))
                        SpectrogramVideo = 'ConvertedSpectrogram.mp4'
                        self.SpectroMaker.FinalLocation = os.path.abspath(SpectrogramVideo)
                        self.SpectroMaker.add_audio()
                        self.successful_generation_popup("Video generation completed successfully!")
                    except Exception as e:
                        self.error_popup(f"Error during video generation: {str(e)}")

                self.SpectroMaker = Generator(thevideo, frames_folder='frames', val=val)
            
            if event == "Delete Frames":
                confirm_delete = sg.popup_yes_no("Manual interruption was detected. If frame generation is underaway it will continue where you left off next time but the latest frame may not be fully generated. Do you really want to exit?", title="Confirm Delete")
                if confirm_delete == "Yes":
                    if os.path.exists('frames'):
                        shutil.rmtree('frames')
                    sg.popup("Frames deleted successfully.")

            if event == "Pause & Exit":
                if not self.pause_flag:
                    self.pause_flag = True
                else:
                    confirm_exit = sg.popup_yes_no("Manual interruption was detected. If frame generation is underaway it will continue where you left off next time but the latest frame may not be fully generated. Do you really want to exit?" ,title="Confirm Exit")
                    if confirm_exit == "Yes":
                        break
            if self.window_closed or event == "Pause & Exit":
                break

        self.window.close()

if __name__ == "__main__":
    gui = GeneratorGUI(None)
    gui.run()