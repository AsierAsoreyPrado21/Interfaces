import gi
from gi.repository import Gtk

gi.require_version("Gtk", "3.0")


class NoWindow(Gtk.Window):
    box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    label = Gtk.Label("No, lo odio")

    def __init__(self):
        super().__init__(title="No")
        self.add(self.box1)
        self.box1.pack_start(self.label, True, True, 0)
