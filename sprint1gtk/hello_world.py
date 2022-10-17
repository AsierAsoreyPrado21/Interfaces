import gi # Importamos las librerías
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
window = Gtk.Window(title="Hello World") # Generamos elemento
window.show()
window.connect("destroy", Gtk.main_quit) # Accion destroy conectada con cerrar ventana
Gtk.main()
