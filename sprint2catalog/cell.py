import copy     # Imports necesarios
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from detail_window import Detail
from gi.repository import GdkPixbuf

# Esta clase serán celdas que incluiremos en una FlowBox
class Cell(Gtk.EventBox): # Herencia de EventBox

    def __init__(self, name, image, description): # Hacemos que cell reciba los parámetros nombre e imagen
        super().__init__()
        self.name = name
        self.image = image
        self.description = description
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        box.pack_start(Gtk.Label(label=name), False, False, 0)
        box.pack_start(image, True, True, 0)
        self.add(box) # Añadimos la box a la ventana generada
        self.connect("button-release-event", self.on_click) # Conectamos la acción de clickar y soltar el botón con las imagenes

    def on_click(self, widget, event):
        im = Gtk.Image()
        im.set_from_pixbuf(self.image.get_pixbuf())
        win = Detail(self.name, im, self.description)
        win.show_all()
        Gtk.main()