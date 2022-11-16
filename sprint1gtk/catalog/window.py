import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from cell import Cell

class MainWindow(Gtk.Window): #Herencia de Window
    flowbox = Gtk.FlowBox()

    def __init__(self):
        # Generamos una ventana  mediante llamada al constructor de la super clase
        super().__init__(title="Catalogo")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(400, 400)

        header = Gtk.HeaderBar(title="Videojuegos")  # Añadimos un header
        header.set_subtitle("Videojuegos mas relevantes")
        header.props.show_close_button = True

        self.set_titlebar(header)
        # Generamos una instancia de ScrolledWindow
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        self.add(scrolled)

        image1 = Gtk.Image() # Generamos una imagen
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/cod.jpg", 200, 200, False) # Usamos pixbuf
        image1.set_from_pixbuf(pixbuf) # Asignamos la imagen a la variable imagen
        # Se repite el proceso en cada una de las imagenes
        image2 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/gow.jpg", 200, 200, False)
        image2.set_from_pixbuf(pixbuf)

        image3 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/mafia.jpg", 200, 200, False)
        image3.set_from_pixbuf(pixbuf)

        image4 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/mariokart.jpeg", 200, 200, False)
        image4.set_from_pixbuf(pixbuf)

        image5 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/minecraft.jpg", 200, 200, False)
        image5.set_from_pixbuf(pixbuf)

        cell_one = Cell("Call of Duty", image1)
        cell_two = Cell("God of War", image2)
        cell_three = Cell("Mafia 3", image3)
        cell_four = Cell("Mario Kart", image4)
        cell_five = Cell("Minecraft", image5)

        # Añadimos todas nuestras celdas a la FlowBox
        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)