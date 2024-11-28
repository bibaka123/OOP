import customtkinter as ctk
import track_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", ctk.END)
    text_area.insert("1.0", content)

class CreateTrackList():
    def __init__(self, window):  
        self.list_track = []
        window.geometry("750x350")  
        window.title("Create Tracks List")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue") 

        list_tracks_btn = ctk.CTkButton(window, text="Create Track List", command=self.list_tracks_click)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10) 

        enter_lbl = ctk.CTkLabel(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)  

        self.input_txt = ctk.CTkEntry(window, width=50)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10, sticky="W")  

        add_track_btn = ctk.CTkButton(window, text="Add Track", command=self.add_tracks_click)
        add_track_btn.grid(row=0, column=3, padx=10, pady=10, sticky="E")

        self.list_txt = ctk.CTkTextbox(window, width=350, height=200)
        self.list_txt.grid(row=1, column=0, columnspan=3, rowspan=2, sticky="W", padx=10, pady=10)  

        self.track_txt = ctk.CTkTextbox(window, width=350, height=150)
        self.track_txt.grid(row=1, column=3, rowspan=3, columnspan=4, sticky="NW", padx=10, pady=10)  

        self.status_lbl = ctk.CTkLabel(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        reset_track_btn = ctk.CTkButton(window, text="Reset Playlist", command=self.reset_track_btn_click)
        reset_track_btn.grid(row=2, column=3, rowspan=2, columnspan=4, sticky="WE", padx=10, pady=10)

        play_track_btn = ctk.CTkButton(window, text="Play List", command=self.play_track_btn_click)
        play_track_btn.grid(row=0, column=4, padx=10, pady=10, sticky="E")

        self.list_tracks_click()

    def add_tracks_click(self):
        key = self.input_txt.get() 
        name = lib.get_name(key)  
        if name is not None:
            self.track_txt.insert(ctk.END, f"{name} - Rate:{lib.get_rating(key)} - Playcount:{lib.get_play_count(key)}\n")
            self.list_track.append(key)
        else:
            set_text(self.track_txt, f"Track {key} not found")  
        self.status_lbl.configure(text="Add Track button was clicked!") 

    def reset_track_btn_click(self):
        self.track_txt.delete("1.0", ctk.END)
        self.list_track = []

    def play_track_btn_click(self):
        self.track_txt.delete("1.0", ctk.END)     
        for key in self.list_track:
            lib.increment_play_count(key)
            text = f"{lib.get_name(key)} - Plays: {lib.get_play_count(key)}\n"
            self.track_txt.insert(ctk.END, text)

    def list_tracks_click(self):
        track_list = lib.list_all()  
        set_text(self.list_txt, track_list) 
        self.status_lbl.configure(text="List Tracks button was clicked!")

if __name__ == "__main__":  
    window = ctk.CTk() 
    fonts.configure()  
    CreateTrackList(window) 
    window.mainloop()
