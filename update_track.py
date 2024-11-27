from tkinter import *
from tkinter import messagebox as msg

import tkinter as tk
import tkinter.scrolledtext as tkst

import track_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class UpdateTrack():
    def __init__(self, window):  
        self.list_track = []
        window.geometry("750x350")  
        window.title("Update Tracks") 

        list_tracks_btn = tk.Button(window, text="Update Tracks")
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10) 

        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)  

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)  

        lbl_newrating = tk.Label(window, text="New rating")
        lbl_newrating.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        self.list_txt = tkst.ScrolledText(window, width=45, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, rowspan=2, sticky="W", padx=10, pady=10)  

        self.track_txt = tk.Text(window, width=30, height=9, wrap="none")
        self.track_txt.grid(row=1, column=3, rowspan=3, sticky="NW", padx=10, pady=10)  

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        update_track_btn = tk.Button(window, text="Update Track", command=self.update_track_btn)
        update_track_btn.grid(row=2, column=3, rowspan=2, sticky="WE", padx=10, pady=10)

        self.new_rating = tk.Entry(window, width=3)
        self.new_rating.grid(row=0, column=3, padx=10, pady=10)

        self.list_tracks_click()
        self.show()

    def update_track_btn(self):
        try:
            key = self.input_txt.get()                   
            name = lib.get_name(key)                          
            rating = int(self.new_rating.get())        
            if rating <= 5:
                if name is not None :                              
                    lib.set_rating(key, rating)                    
                    set_text(self.track_txt, f"Name: {lib.get_name(key)} \nNew rating: {lib.get_rating(key)}" )  
                    self.show()
                else:                                          
                    msg.showwarning("Can not find tracj") 
            else:
                msg.showerror("Enter new rating fail")
        except ValueError :                                   
            msg.showerror("Rating must be an interger!")      

    def list_tracks_click(self):
        track_list = lib.list_all()  
        set_text(self.list_txt, track_list) 
        self.status_lbl.configure(text="List Tracks button was clicked!")

    def show(self):
        track_list = lib.list_all()                           
        set_text(self.list_txt, track_list)  

if __name__ == "__main__":  
    window = tk.Tk() 
    fonts.configure()  
    UpdateTrack(window) 
    window.mainloop()  
