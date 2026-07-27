import tkinter as tk
import tkinter.messagebox as msb
import tkinter.filedialog as fd

from ui.interfaces import ViewInterface

class FileDialogView(ViewInterface):
    def __init__(self, ancho: int, alto: int):
        super().__init__()
        self._ancho = ancho
        self._alto  = alto

    def build_frame(self, master: tk.Tk) -> tk.Frame:
        main_frame = tk.Frame(master, width=self._ancho, height=self._alto)
        main_frame.pack(expand=True, fill="both")

        main_frame.pack_propagate(False)

        self._construir_widgets(main_frame)

        return main_frame

    def _construir_widgets(self, frame: tk.Frame) -> None:
        # Etiqueta para mostrar la ruta seleccionada
        self._lbl_ruta = tk.Label(frame, text="Ningún archivo seleccionado", fg="gray")
        self._lbl_ruta.pack(pady=(50, 10))

        # Botón para detonar el FileDialog
        tk.Button(
            frame, 
            text="Seleccionar Archivo .txt", 
            command=self._abrir_selector_archivos
        ).pack()

    # --- Nuevo manejador de eventos ---
    def _abrir_selector_archivos(self) -> None:
        # 2. Configuración estricta del diálogo
        ruta_archivo = fd.askopenfilename(
            title="Selecciona un documento de texto",
            initialdir="/", # Abre en C:/ o en la raíz de Linux/macOS
            # Filtro de seguridad (clave para la UX):
            filetypes=(
                ("Archivos de texto", "*.txt"),
                ("Todos los archivos", "*.*")
            )
        )

        # 3. La Validación Crítica (Si el usuario presionó 'Cancelar')
        if not ruta_archivo:
            # Puedes usar tu método estático si lo deseas, o ignorarlo
            msb.showwarning("Operación Cancelada", "No seleccionaste ningún archivo.")
            return
            
        # Si pasó la guardia, usamos la ruta
        self._lbl_ruta.config(text=f"Ruta: {ruta_archivo}", fg="black")
        
        # PRO-TIP: Aquí es donde normalmente abrirías el archivo con Python
        # with open(ruta_archivo, 'r') as file:
        #     contenido = file.read()