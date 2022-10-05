import gi
from gi.repository import Gtk
from cell import Cell

gi.require_version("Gtk", "3.0")


class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()

    def __init__(self):
        super().__init__(title="Videojuegos")
        self.connect("destroy", Gtk.main_quit)
        self.add(self.flowbox)
        cell_one = Cell("Call Of Duty", Gtk.Image.new_from_file("data/edited/cod.jpg"))
        cell_two = Cell("God Of War", Gtk.Image.new_from_file("data/edited/gow.jpg"))
        cell_three = Cell("Mafia 3", Gtk.Image.new_from_file("data/edited/mafia.jpg"))
        cell_four = Cell("Mario Kart", Gtk.Image.new_from_file("data/edited/mariokart.jpg"))
        cell_five = Cell("Minecraft", Gtk.Image.new_from_file("data/edited/minecraft.jpg"))
        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)
