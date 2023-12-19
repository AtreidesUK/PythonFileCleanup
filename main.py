import customtkinter as ctk
import os
from pathlib import Path
import shutil

window = ctk.CTk()
window.title("Atreides-Demo")
window.geometry("500x350")

#File Add Functionality
def file_add():
    file_name = new_file_name.get()
    os.chdir('C:\\Users\\user\\Documents\\')
    Path(file_name).mkdir(exist_ok=True)
    file_output_string.set('Successfully added the file')

def doc_sort():
    os.chdir('Downloads')
    

#Main Title
title_label = ctk.CTkLabel(master = window, text = 'Atreides File Sort', font=('calibri', 24, 'bold'))
title_label.pack()

#Subheading
file_title_label = ctk.CTkLabel(master = window, text = 'Add File', font=('calibri', 20, 'bold'))
file_title_label.pack(pady = 7)

#Add File Input Field
file_frame = ctk.CTkFrame(master = window)
new_file_name = ctk.StringVar()
name_entry = ctk.CTkEntry(master = file_frame, textvariable=new_file_name)
file_add_button = ctk.CTkButton(master=file_frame, text='Add', command=file_add)
file_frame.pack(pady=5)
name_entry.pack(side='left', padx=10)
file_add_button.pack(side='left')

#Add File Confirmation
file_output_string = ctk.StringVar()
file_output_label = ctk.CTkLabel(
    master = window,
    text = 'output',
    font = ('calibri', 15, 'bold'),
    textvariable = file_output_string)
file_output_label.pack()

#Document Sort Button
doc_sort_title = ctk.CTkLabel(master = window, text = 'Document Sort', font=('calibri', 20, 'bold'))
doc_sort_title.pack(pady=10)
doc_sort_frame = ctk.CTkFrame(master = window)
doc_sort_button = ctk.CTkButton(master=doc_sort_frame, text='sort', command = doc_sort)
doc_sort_frame.pack(pady=5)
doc_sort_button.pack()

window.mainloop()