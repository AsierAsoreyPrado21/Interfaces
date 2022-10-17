import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from proceso import Proceso
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
        win = Proceso(self.name, self.image, self.descripcion)
        win.show_all()
        Gtk.main()

    def asignar_desripcion(self):
        if self.name == "Piedra":
            self.descripcion = ""
        elif self.name=="Papel":
            self.descripcion=""
        elif self.name=="Tijera":
            self.descripcion=""
    def getImage(self):
        img = Gtk.Image()
        pixbuf = None
        if self.name == "Call of Duty":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/piedra.jpg", 200, 200, False)
        elif self.name == "God of War":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/papel.jpg", 200, 200, False)
        elif self.name == "Mafia":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/tijera.jpg", 200, 200, False)
        return img