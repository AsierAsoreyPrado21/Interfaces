import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from ejecucion import Ejecución

class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()

    def __init__(self):
        super().__init__(title="Juego")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(400, 400)

        header = Gtk.HeaderBar(title="Juego")
        header.set_subtitle("Piedra/Papel/Tijera")
        header.props.show_close_button = True

        self.set_titlebar(header)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        self.add(scrolled)

        image1 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/piedra.jpg", 200, 200, False)
        image1.set_from_pixbuf(pixbuf)

        image2 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/papel.jpg", 200, 200, False)
        image2.set_from_pixbuf(pixbuf)

        image3 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/tijera.jpg", 200, 200, False)
        image3.set_from_pixbuf(pixbuf)

        ejecución_one = Ejecución("Piedra", image1)
        ejecución_two = Ejecución("Papel", image2)
        ejecución_three = Ejecución("Tijera", image3)

        self.flowbox.add(ejecución_one)
        self.flowbox.add(ejecución_two)
        self.flowbox.add(ejecución_three)
