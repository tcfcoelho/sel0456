import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, GObject
import math

builder = Gtk.Builder()

class Handler:
    
    def on_window1_remove(self, *args):
        Gtk.main_quit()

    def on_botão1_clicked(self, button):
        global builder
        print('Botão clicado')

        corrente = builder.get_object('corrente')
        i = corrente.get_text()

        comprimento = builder.get_object('comprimento')
        l = comprimento.get_text()

        t1 = builder.get_object('127')
        if t1.get_active():
            t = 127
 
        t2 = builder.get_object('220')
        if t2.get_active():
            t = 220

        t3 = builder.get_object('380')
        if t3.get_active():
            t = 127

        circ = builder.get_object('select')
        tipo = circ.get_text()

        if tipo == 'Monofásico':
            print('Executando Equação 1')
            s = (200*(1/56)*float(i)*float(l))/(2.5*float(t))

        elif tipo == 'Trifásico':
            print('Executando Equação 2')
            s = (100*math.sqrt(3)*(1/56)*float(i)*float(l))/(2.5*float(t))

        r = builder.get_object('result')
        r.set_text('{:.2f}'.format(s))


builder.add_from_file("main.glade")

builder.connect_signals(Handler())

w1 = builder.get_object('window1')
w1.show_all()

Gtk.main()