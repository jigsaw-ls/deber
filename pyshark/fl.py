from tkinter import filedialog



filename = filedialog.askopenfilename(initialdir="/", title="Seleccionar archivo",
                                      filetypes=(("Archivos de texto", "*.txt"),
                                                 ("Todos los archivos", "*.*")))
