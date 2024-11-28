import customtkinter as ctk
from tkinter import messagebox as msg

import track_library as lib
import font_manager as fonts

# Function to set the content of a text area
def set_text(text_area, content):
    text_area.delete("1.0", ctk.END)
    text_area.insert("1.0", content)

class UpdateTrack:
    def __init__(self, window):  
        self.list_track = []
        window.geometry("750x350")  
        window.title("Update Tracks") 

        ctk.set_appearance_mode("light")  # Set to "light" or "dark" for mode
        ctk.set_default_color_theme("blue")  # Default color theme

        # Button to list all tracks
        list_tracks_btn = ctk.CTkButton(window, text="Update Tracks", command=self.list_tracks_click)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        # Label for entering track number
        enter_lbl = ctk.CTkLabel(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Entry for track number
        self.input_txt = ctk.CTkEntry(window, width=50)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Label for new rating
        lbl_newrating = ctk.CTkLabel(window, text="New Rating")
        lbl_newrating.grid(row=0, column=3, padx=10, pady=10, sticky="W")

        # Scrolled text for displaying all tracks
        self.list_txt = ctk.CTkTextbox(window, width=350, height=200)
        self.list_txt.grid(row=1, column=0, columnspan=3, rowspan=2, sticky="w", padx=10, pady=10)

        # Textbox for displaying specific track details
        self.track_txt = ctk.CTkTextbox(window, width=300, height=150)
        self.track_txt.grid(row=1, column=3, rowspan=3, sticky="nw", padx=10, pady=10)

        # Status label
        self.status_lbl = ctk.CTkLabel(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="w", padx=10, pady=10)

        # Button to update a track
        update_track_btn = ctk.CTkButton(window, text="Update Track", command=self.update_track_btn)
        update_track_btn.grid(row=2, column=3, rowspan=2, sticky="we", padx=10, pady=10)

        # Entry for new rating
        self.new_rating = ctk.CTkEntry(window, width=50)
        self.new_rating.grid(row=0, column=3, sticky="N", padx=10, pady=10)

        # Automatically display the track list
        self.list_tracks_click()
        self.show()

    # Function to handle updating a track's rating
    def update_track_btn(self):
        try:
            key = self.input_txt.get()  
            name = lib.get_name(key) 
            rating = int(self.new_rating.get())  

            if 0 < rating <= 5:
                if name is not None:
                    lib.set_rating(key, rating) 
                    set_text(self.track_txt,f"Track: {lib.get_name(key)} \nNew rating: {lib.get_rating(key)}")
                    self.show() 
                else:
                    msg.showwarning("Error", "Cannot find that track")
            else:
                msg.showerror("Error", "Rating must be 5 or below!")
        except ValueError:
            msg.showerror("Error", "Rating must be an integer!")

    # Function to list all tracks
    def list_tracks_click(self):
        track_list = lib.list_all()  
        set_text(self.list_txt, track_list) 
        self.status_lbl.configure(text="List Tracks button was clicked!")

    # Refresh the track list
    def show(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)

# Main block to run the application
if __name__ == "__main__":  
    window = ctk.CTk()
    fonts.configure()
    UpdateTrack(window)
    window.mainloop()
