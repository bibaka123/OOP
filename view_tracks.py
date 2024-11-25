import tkinter as tk  # Importing the Tkinter library for GUI components
import tkinter.scrolledtext as tkst  # Importing the scrolled text widget from Tkinter

import track_library as lib  # Importing the custom library for track-related data handling
import font_manager as fonts  # Importing the custom library for font configuration

# Function to set text in a text area widget
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Clear the content of the text area
    text_area.insert(1.0, content)  # Insert new content at the beginning

# Class for creating the Track Viewer GUI
class TrackViewer():
    def __init__(self, window):  # Constructor method for initializing the GUI
        window.geometry("750x350")  # Set the dimensions of the main window
        window.title("View Tracks")  # Set the title of the main window

        # Create and position a button to list all tracks
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        # Create and position a label for track number input
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Create and position a text entry widget for track number input
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Create and position a button to view details of a specific track
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        # Create and position a scrolled text widget for listing all tracks
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Create and position a text widget for displaying individual track details
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Create and position a label for displaying status messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Automatically list all tracks upon initializing the GUI
        self.list_tracks_clicked()

    # Method to handle the "View Track" button click
    def view_tracks_clicked(self):
        key = self.input_txt.get()  # Get the track number entered by the user
        name = lib.get_name(key)  # Retrieve the track name using the library
        if name is not None:  # Check if the track exists
            artist = lib.get_artist(key)  # Retrieve the artist of the track
            rating = lib.get_rating(key)  # Retrieve the rating of the track
            play_count = lib.get_play_count(key)  # Retrieve the play count of the track
            # Format the track details and display them
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details)  # Display the track details in the text widget
        else:
            # Display an error message if the track is not found
            set_text(self.track_txt, f"Track {key} not found")
        # Update the status label to indicate the button was clicked
        self.status_lbl.configure(text="View Track button was clicked!")

    # Method to handle the "List All Tracks" button click
    def list_tracks_clicked(self):
        track_list = lib.list_all()  # Retrieve a list of all tracks using the library
        set_text(self.list_txt, track_list)  # Display the list of tracks in the scrolled text widget
        # Update the status label to indicate the button was clicked
        self.status_lbl.configure(text="List Tracks button was clicked!")

# Main block to run the GUI application
if __name__ == "__main__":  # Check if the script is being run as the main module
    window = tk.Tk()  # Create the main Tkinter window object
    fonts.configure()  # Configure fonts using the custom font manager library
    TrackViewer(window)  # Instantiate the TrackViewer class with the main window
    window.mainloop()  # Start the Tkinter event loop to display the GUI and handle events
