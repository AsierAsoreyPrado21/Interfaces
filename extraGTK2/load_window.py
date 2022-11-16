import shutil
import gi # Imports necesarios
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
import requests, threading
from window import MainWindow

class LoadWindow(Gtk.Window):
    label = Gtk.Label("Cargando elementos...")
    spinner = Gtk.Spinner()
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)

    def __init__(self):
        super().__init__(title="Pantalla de Carga")
        self.set_position(Gtk.WindowPosition.CENTER) #Posicionamos la ventana en el centro nada más se genera
        self.set_default_size(400, 400)
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(60)
        self.set_resizable(False)
        self.spinner.props.active = True # Activamos el spinner

        self.box.pack_start(self.label, False, False, 0)
        self.box.pack_start(self.spinner, False, False, 0)
        self.add(self.box)                                    # Añadimos a la ventana la box

        self.launch_load() # Llamammos a la función de la clase de nombre launch_load

    def launch_load(self): # Inicia otro hilo en paralelo con el principal
        thread = threading.Thread(target=self.load_json(), args=())
        thread.start()

    def load_json(self):  # Función que se encarga de recuperar la información almacenada en un JSON mediante una petición GET
        response = requests.get("https://github.com/AsierAsoreyPrado21/Interfaces/blob/main/extraGTK2/Ahorcado.json")
        json_list = response.json()

        result = [] # Generamos una lista llamada result

        for json_item in json_list:
            fallos = json_item.get("fallos")
            image_url = json_item.get("image_url")
            r = requests.get(image_url, stream=True)
            with open ("temp.png", "wb") as f:
                shutil.copyfileobj(r.raw, f)
            image = Gtk.Image.new_from_file("temp.png")
            result.append({"fallos": fallos, "gtk_image": image})

        GLib.idle_add(self.start_main_window, result) # Pasamos al hilo principal y ejecutamos la función start_main_window

    def start_main_window(self, loaded_item_list): # Función que genera una ventana MainWindow
        win = MainWindow(loaded_item_list)
        win.show_all()
        self.disconnect_by_func(Gtk.main_quit)
        self.close()