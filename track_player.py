import customtkinter as ctk
import font_manager as fonts
from view_tracks import TrackViewer
from create_track_list import CreateTrackList
from update_track import UpdateTrack

# Functions to handle button clicks
def view_tracks_clicked():
    status_lbl.configure(text="View Tracks button was clicked!")
    TrackViewer(ctk.CTkToplevel(window))

def create_track_list_clicked():
    status_lbl.configure(text="Create Tracks button was clicked!")
    CreateTrackList(ctk.CTkToplevel(window))

def update_track_clicked():
    status_lbl.configure(text="Update Tracks button was clicked!")
    UpdateTrack(ctk.CTkToplevel(window))

# Initialize the main window
window = ctk.CTk()
window.geometry("520x150")
window.title("JukeBox")

ctk.set_appearance_mode("light")  # Set light mode, can be switched to "dark"
ctk.set_default_color_theme("blue")  # Set default theme

fonts.configure()

# Header label
header_lbl = ctk.CTkLabel(
    window,
    text="Select an option by clicking one of the buttons below",
    font=("Helvetica", 12)
)
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Buttons for various options
view_tracks_btn = ctk.CTkButton(window, height=40, text="View Tracks", command=view_tracks_clicked)
view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

create_track_list_btn = ctk.CTkButton(window, height=40, text="Create Track List", command=create_track_list_clicked)
create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_tracks_btn = ctk.CTkButton(window, height=40, text="Update Tracks", command=update_track_clicked)
update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

# Status label
status_lbl = ctk.CTkLabel(window, text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Start the application
window.mainloop()
