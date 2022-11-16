import gi # Imports necesarios
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf

class MainWindow(Gtk.Window): #Herencia de Window

    def __init__(self, data_source):
        super().__init__(title="Ahorcado") # Generamos una ventana con el texto Ahorcado
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(800, 800)

    def click(self, event): # Función que se activa al hacer click en la opción de "Ayuda" y dentro de ayuda en "Acerca de"
       pass

    def getFallos(self):
        pass