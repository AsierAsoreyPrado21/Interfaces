import gi
from gi.repository import Gtk

gi.require_version("Gtk", "3.0")


class NoWindow(Gtk.Window): # Herencia de window
    box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL) #Definimos la box
    label = Gtk.Label("No, lo odio") #Label con texto

    def __init__(self):
        super().__init__(title="No")
        self.add(self.box1)
        self.box1.pack_start(self.label, True, True, 0) #Añadimos la label
