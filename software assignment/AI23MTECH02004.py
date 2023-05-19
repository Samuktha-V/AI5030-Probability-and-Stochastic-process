# # Importing essential libraries



import numpy as np
import os
import random
import moviepy.editor


# # Reading the video file


#listing the directories in the folder
directories=os.listdir("C:/Users/Admin/Documents/Mtech AI/SEM 1/Probability/Untitled Folder")
#reading the video directories and apending them into array
vid=[]
for x in directories:
    if x=='Videos':
        #considering all the videoclips in the 'Videos' file
        vidlist=os.listdir("C:/Users/Admin/Documents/Mtech AI/SEM 1/Probability/Untitled Folder/Videos")
        for y in vidlist:
            #print(y)
            video = moviepy.editor.VideoFileClip("C:/Users/Admin/Documents/Mtech AI/SEM 1/Probability/Untitled Folder/Videos"+"/"+str(y))
            vid.append(video)
        


# # Extracting the audio files



#extracting the audio from the corresponding video file and appending them onto array
aud=[]
for i in range(len(vid)):
    aud.append(vid[i].audio)
    #saving the audio files
    aud[i].write_audiofile("Audio"+str(i)+".mp3")


# # Generating the Random number



#generating the random list to play the audio accordingly
arr=np.arange(0,20,1)
randomlist=random.sample(sorted(arr),k=20)   
print("The randomly geneearted sequence : ",randomlist)


# # The random audio playlist 



#playing audio according to the random generated numbers
for i in randomlist:
    print("Audio"+str(i)+".mp3")


# # Creating a GUI to play the random playlist



#creating the GUI to play the audio
import tkinter as tk
from pygame import mixer

class AudioPlayerGUI(tk.Tk):
    def __init__(self, audio_files):
        super().__init__()
        self.title("Audio Player")
        
        self.audio_files = audio_files
        self.current_file_index = 0

        self.mixer = mixer
        self.mixer.init()

        self.create_widgets()

    def create_widgets(self):
        self.play_button = tk.Button(self, text="Play", command=self.play_audio)
        self.play_button.pack()

        self.next_button = tk.Button(self, text="Next", command=self.play_next_audio)
        self.next_button.pack()

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack()

    def play_audio(self):
        audio_file = self.audio_files[self.current_file_index]
        self.mixer.music.load(audio_file)
        self.mixer.music.play()

    def play_next_audio(self):
        self.mixer.music.stop()
        self.current_file_index = (self.current_file_index + 1) % len(self.audio_files)
        self.play_audio()

if __name__ == "__main__":
    audio_files=[]
    for i in randomlist:
        audio_files.append("Audio"+str(i)+".mp3")

    app = AudioPlayerGUI(audio_files)
    app.mainloop()






