import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from window import MainWindow
from load_window import LoadWindow

win = MainWindow # Generamos una instancia de MainWindow
win=LoadWindow()
win.show_all() # Mostramos la ventana
Gtk.main() # Hacemos que no se cierre
