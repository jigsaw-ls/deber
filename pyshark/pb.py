import os
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(filename):
    """
    Extracts metadata from image file and returns as dictionary
    """
    image = Image.open(filename)
    exifdata = image.getexif()
    metadata = {}
    for tag_id, value in exifdata.items():
        tag = TAGS.get(tag_id, tag_id)
        metadata[tag] = value
    return metadata

def browse_file():
    """
    Opens a file dialog to select an image file and extracts its metadata
    """
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    if filename:
        metadata = extract_metadata(filename)
        show_metadata(metadata)

def show_metadata(metadata):
    """
    Shows metadata in a table in tkinter
    """
    if not metadata:
        return
    metadata_window = Toplevel(root)
    metadata_window.title("Metadata")
    treeview = ttk.Treeview(metadata_window)
    treeview.pack()
    treeview["columns"] = ("value")
    treeview.column("#0", width=120)
    treeview.column("value", width=300)
    treeview.heading("#0", text="Metadata")
    treeview.heading("value", text="Value")
    for key, value in metadata.items():
        treeview.insert("", "end", text=key, values=value)


# create tkinter GUI
root = Tk()
root.title("Extract Metadata")
root.geometry("300x100")

# add browse button to select file
browse_button = Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=10)

root.mainloop()
