import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# 1. Creamos un Frame que actuará como nuestra barra de menú personalizada
frame_barra = tk.Frame(root, bg="lightgray", relief="raised", bd=1)
frame_barra.pack(side="top", fill="x")

# 2. Creamos un Menubutton y lo metemos en nuestro Frame
boton_archivo = tk.Menubutton(frame_barra, text="Archivo", activebackground="gray")
boton_archivo.pack(side="left", padx=5)

# 3. Creamos el menú que se desplegará de ese botón
menu_archivo = tk.Menu(boton_archivo, tearoff=0)
menu_archivo.add_command(label="Nuevo")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)

# 4. Enlazamos el menú al botón
boton_archivo.config(menu=menu_archivo)

root.mainloop()