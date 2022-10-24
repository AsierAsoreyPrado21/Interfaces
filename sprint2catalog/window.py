import gi # Imports necesarios
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from cell import Cell

# Esta clase será una ScrolledWindow que contendrá una FLowBox

class MainWindow(Gtk.Window): #Herencia de Window
    flowbox = Gtk.FlowBox() # Generamos una FlowBox como variable de clase

    def __init__(self, data_source):
        super().__init__(title="Catalogo")
        self.connect("destroy", Gtk.main_quit)
        self.set_position(Gtk.WindowPosition.CENTER) #Posiciona en el medio la segunda ventana al hacer clik
        self.set_border_width(15)
        self.set_default_size(400, 400)


        header = Gtk.HeaderBar(title="Imagenes")
        header.set_subtitle("Colección")
        header.props.show_close_button = True

        self.set_titlebar(header)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)  # Añadimos a la ScrolledWindow nuestra FlowBox

        #Creamos un menú que contendra un elemento que desplegará un mensaje
        mb = Gtk.MenuBar() #Elemento GTK menu Bar

        filemenu = Gtk.Menu() #Elemento GTK menu con sus items
        fileM = Gtk.MenuItem("Ayuda")
        fileM.set_submenu(filemenu)

        acercaDe = Gtk.MenuItem("Acerca De") #Otro menu Item
        acercaDe.connect("activate", self.click)
        filemenu.append(acercaDe)
        mb.append(fileM)

        vbox = Gtk.VBox(False, 2) #Creamos una box que tendra el menu Bar y la ventana con scroll
        vbox.pack_start(mb, False, False, 0)
        vbox.pack_start(scrolled, True, True, 0)
        self.add(vbox)

        for item in data_source: #Clase que recibe el data source y que genera ventanas
            cell = Cell(item.get("name"), item.get("gtk_image"), item.get("description"))
            self.flowbox.add(cell)
    #Funcion que contendra el mensaje
    def click(self, event): #Funcion que se activa con el click en "Ayuda" y "Acerca de" que genera un alabel con texto
        win = Gtk.Window(title="acerca del desarrollador")
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        label = Gtk.Label("La pestaña Desarrollador es el lugar al que puede ir cuando quiera hacer o usar comandos")
        box.pack_start(label, True, True, 0)
        win.add(box)
        win.show_all()
        Gtk.main()