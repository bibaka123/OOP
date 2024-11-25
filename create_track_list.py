from tkinter import *
from tkinter import messagebox as msg

import tkinter as tk
import tkinter.scrolledtext as tkst

import track_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class CreateTrackList():
    def __init__(self, window):  
        self.list_track = []
        window.geometry("750x350")  
        window.title("Create Tracks List") 

        list_tracks_btn = tk.Button(window, text="Create Track List", command=self.list_tracks_click)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10) 

        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)  

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10, sticky=W)  

        add_track_btn = tk.Button(window, text="Add Track", command=self.add_tracks_click)
        add_track_btn.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        self.list_txt = tkst.ScrolledText(window, width=35, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, rowspan=2, sticky="W", padx=10, pady=10)  

        self.track_txt = tk.Text(window, width=40, height=9, wrap="none")
        self.track_txt.grid(row=1, column=2, rowspan=3, sticky="NW", padx=10, pady=10)  

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        reset_track_btn = tk.Button(window, text="Reset Playlist", command=self.reset_track_btn_click)
        reset_track_btn.grid(row=2, column=2, rowspan=2, sticky="WE", padx=10, pady=10)

        play_track_btn = tk.Button(window, text="Play List", command=self.play_track_btn_click)
        play_track_btn.grid(row=0, column=2, padx=10, pady=10, sticky=N)

        self.list_tracks_click()

    def add_tracks_click(self):
            key = self.input_txt.get() 
            name = lib.get_name(key)  
            if name is not None:
                self.track_txt.insert(END, f"Track: {name}\nRate:{lib.get_rating(key)}\nPlaycount:{lib.get_play_count(key)}\n--------------------\n")
                self.list_track.append(key)
            else:
                set_text(self.track_txt, f"Track {key} not found")  
            self.status_lbl.configure(text="Add Track button was clicked!") 

    def reset_track_btn_click(self):
        self.track_txt.delete("1.0", END)
        self.list_track = []

    def play_track_btn_click(self):
        self.track_txt.delete("1.0", END)     
        for key in self.list_track:
            lib.increment_play_count(key)
            text = (f"Track: {lib.get_name(key)}\nPlays: {lib.get_play_count(key)}\n--------------------\n")
            self.track_txt.insert(END, text)

    def list_tracks_click(self):
        track_list = lib.list_all()  
        set_text(self.list_txt, track_list) 
        self.status_lbl.configure(text="List Tracks button was clicked!")

if __name__ == "__main__":  
    window = tk.Tk() 
    fonts.configure()  
    CreateTrackList(window) 
    window.mainloop()  
