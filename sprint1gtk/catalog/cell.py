import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from detail_window import Detail
from gi.repository import GdkPixbuf

class Cell(Gtk.EventBox):
    name = None
    image = Gtk.Image()
    descripcion = None

    def __init__(self, name, image):
        super().__init__()
        self.name = name
        self.image = image
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        box.pack_start(Gtk.Label(label=name), False, False, 0)
        box.pack_start(image, True, True, 0)
        self.add(box)
        self.connect("button-release-event", self.on_click)

    def on_click(self, widget, event):
        self.image = self.getImage()
        self.asignar_desripcion()
        win = Detail(self.name, self.image, self.descripcion)
        win.show_all()
        Gtk.main()

    def asignar_desripcion(self):
        if self.name == "Call of Duty":
            self.descripcion = "Call od Duty Modern Warfare"
        elif self.name=="God of War":
            self.descripcion="God of War"
        elif self.name=="Mafia":
            self.descripcion="Mafia 3"
        elif self.name == "Mario Kart":
            self.descripcion = "Mario Kart 8"
        elif self.name == "Minecraft":
            self.descripcion="Minecraft"
    def getImage(self):
        img = Gtk.Image()
        pixbuf = None
        if self.name == "Call of Duty":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/cod.jpg", 200, 200, False)
        elif self.name == "God of War":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/gow.jpg", 200, 200, False)
        elif self.name == "Mafia":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/mafia.jpg", 200, 200, False)
        elif self.name == "Mario Kart":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/mariokart.jpg", 200, 200, False)
        elif self.name == "Minecraft":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/minecraft.jpg", 200, 200, False)
        img.set_from_pixbuf(pixbuf)
        return img