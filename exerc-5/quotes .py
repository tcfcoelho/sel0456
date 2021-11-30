import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, GObject

from model import Model

builder = Gtk.Builder()
builder.add_from_file("main.glade")

class Handler(Model):

    # INICIALIZAÇÃO
    def __init__(self, *args, **kwargs):
        super(Handler, self).__init__(*args, **kwargs)
        self.start_inicial()
        self.renderer_inicial(self.search_inicial())

    # ENCERRAMENTO DO PROGRAMA
    def on_inicial_remove(self, *args):
        self.quotes_drop()
        Gtk.main_quit()

    # SET DE TEXTO DE DISPLAY
    def set_display (self, label, txt):
        set = builder.get_object(label)
        set.set_markup(txt)

    # SET DE TEXTO DO BUFFER 
    def set_quote(self, display, text):
        textview = builder.get_object(display)
        buffer = textview.get_buffer()
        buffer.set_text(text)

    # SET DE TEXTO DE TEXTENTRY:
    def text_set(self, wid, entry):
        textentry = builder.get_object(wid)
        textentry.set_text(entry)

    # GET DE TEXTO DE WIDGET
    def get_text(self, wid):
        obj = builder.get_object(wid)
        txt = obj.get_text()
        return txt

    # INIT JANELA INICIAL
    def start_inicial(self):
        self.open = builder.get_object("open")
        self.remove = builder.get_object("remove")
        self.new = builder.get_object("new")
        self.lista = builder.get_object("lista")
        self.inicial = builder.get_object("inicial")
        self.inicial.show_all()

    # INIT JANELA CITAÇÃO
    def start_quote(self):
        self.nq_ready = builder.get_object("nq_ready")
        self.nq_cancel = builder.get_object("nq_cancel")
        self.nq_text = builder.get_object("nq_text")
        self.buffer = builder.get_object("buffer")
        self.lista_quotes = builder.get_object("lista_quotes")
        self.quote = builder.get_object("quote")
        self.quote.show_all()

    # RENDERIZADOR DISPLAY JANELA INICIAL
    def renderer_inicial(self, model):
        try:
            self.lista.clear()
            if model:
                for registros in model:
                    self.lista.append(registros)
        except Exception as ex:
            print("Erro na renderização da primeira tabela %s" % ex)

    # RENDERIZADOR DISPLAY JANELA REGISTRO
    def renderer_registro(self, model):
        try:
            self.lista_quotes.clear()
            if model:
                for quote in model:
                    self.lista_quotes.append(quote)
        except Exception as ex:
            print("Erro  na renderização da segunda tabela %s" % ex)

    # MUDANÇA NO CURSOR DO DISPLAY INICIAL
    def on_displaylista_cursor_changed(self, *args):
        try:
            self.num_reg = self.select_reg(args[0].get_selection())
            print("Sucesso no resgate display inicial")
        except Exception as ex:
            print("Error change display 1 cursor %s" % ex)

    #MUDANÇA NO CURSOR DO DISPLAY REGISTRO
    def on_displayquotes_cursor_changed(self, *args):
        try:
            self.num_quote = self.select_reg(args[0].get_selection())
            print("Sucesso no resgate display registro")
        except Exception as ex:
            print("Error change display 2 cursor %s" % ex)  

    def select_reg(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            return model[treeiter][0]

    # VIZUALIZAÇÃO DO REGISTRO
    def on_open_clicked(self, *args):
        try:
            registro = self.get_registro(self.num_reg)
            lista_reg = list(registro[0])

            self.set_display("d_titulo", lista_reg[2])
            self.set_display("d_autor", lista_reg[1])
            self.set_display("d_ano", str(lista_reg[3]))      
            self.set_display("d_editora", lista_reg[4])
            self.set_display("d_anoed", str(lista_reg[5]))
            self.set_display("d_local", str(lista_reg[7]))

            self.set_quote("d_quote", lista_reg[8])

            if lista_reg[6] == "Físico":
                self.set_display("d_pag", "página:")
                self.set_display("d_porcent", "")
            else:
                self.set_display("d_pag", "")
                self.set_display("d_porcent", "%")

            displayer = builder.get_object("displayer")
            displayer.show_all()

        except Exception as ex:
            print("Error resgate do registro %s" % ex)

    # RETORNAR AO INÍCIO
    def on_home_clicked (self, *args):
        display = builder.get_object("displayer")
        display.hide()

    # REMOÇÃO DE REGISTRO
    def on_del_clicked(self, button):
        warn = builder.get_object("warning")
        warn.show_all()

    def on_w_no_clicked(self, button):
        warn = builder.get_object("warning")
        warn.hide()

    def on_w_yes_clicked(self, *args):
        try:
            self.del_reg(self.num_reg)
            self.renderer_inicial(self.search_inicial())
            warn = builder.get_object("warning")
            warn.hide()
        except Exception as ex:
            print("Erro na remoção do registro %s" % ex)        
            self.connectbase.rollback()

    # ABRIR JANELA DE REGISTRO
    def on_new_clicked(self, button):
        global builder
        registro = builder.get_object("registro")
        registro.show_all()
        self.create_quotes()
        self.renderer_registro(self.search_registro())

    # NOVA CITAÇÃO
    def on_new_quote_clicked(self, button):
        self.start_quote()

    def on_nq_cancel_clicked(self, button):
        self.set_quote("nq_text", "")
        nq = builder.get_object("quote")
        nq.hide()

    def on_nq_ready_clicked(self, button):
        textview = builder.get_object("nq_text")
        buffer = textview.get_buffer()
        start_iter, end_iter = buffer.get_bounds()
        text = buffer.get_text(start_iter, end_iter, True)
        print(text)
        
        self.save_quote(text)
        self.renderer_registro(self.search_registro())
        
        nq = builder.get_object("quote")
        nq.hide()

    def on_q_remove_clicked(self, button):
        try:
            self.del_quote(self.num_quote)
            self.renderer_registro(self.search_registro())
        except Exception as ex:
            print("Erro na remoção da citação: %s" % ex)        
            self.connectbase.rollback()

    def on_fis_type_toggled(self, *args):
        self.set_display('l_local', "Página:")

    def on_eb_type_toggled(self, *args):
        self.set_display('l_local', "Porcentagem:")

    # REGISTRO
    def on_reg_in_clicked(self, *args):
        try:
            autor = self.get_text('new_author')
            titulo = self.get_text('new_title')
            ano = self.get_text('new_year')
            editora = self.get_text('new_pubcomp')
            ano_ed = self.get_text('new_yeared')

            fis_type = builder.get_object('fis_type')
            if fis_type.get_active():
                tipo_ed = "Físico"
            else: tipo_ed = "eBook"

            local = self.get_text('t_local')

            quote = self.num_quote

            self.save_registro(autor, titulo, ano, editora, ano_ed, tipo_ed, local, quote)
            self.renderer_inicial(self.search_inicial())
            print("Sucesso no save")
        except Exception as ex:
            print("Erro no save registro %s" % ex)
            self.connectbase.rollback()

    # ENCERRAR REGISTRO
    def on_end_clicked(self, button):
        self.text_set("new_author", "")
        self.text_set("new_title", "")
        self.text_set("new_year", "2000")
        self.text_set('new_pubcomp', "")
        self.text_set("new_yeared", "2000")
        self.text_set("t_local", "")
        self.quotes_drop()
        registro = builder.get_object("registro")
        registro.hide()

    # EDITAR REGISTRO
    def on_d_edit_clicked(self, *args):
        registro = self.get_registro(self.num_reg)
        lista_reg = list(registro[0])

        self.text_set("edit_author", lista_reg[1])
        self.text_set("edit_title", lista_reg[2])
        self.text_set("edit_ypub", str(lista_reg[3]))
        self.text_set("edit_pubcomp", lista_reg[4])
        self.text_set("edit_yed", str(lista_reg[5]))
        self.text_set("edit_local", lista_reg[7])

        self.set_quote("edit_quote", lista_reg[8])

        if lista_reg[6] == "Físico":
            self.set_display("edit_label_local", "Página:")            
        else:
            self.set_display("edit_label_local", "Porcentagem:")

        editw = builder.get_object("editw")
        editw.show_all()

    # SALVAR EDIÇÃO
    def on_edit_update_clicked(self, *args):
        registro = self.get_registro(self.num_reg)
        lista_reg = list(registro[0])

        ud_autor = self.get_text("edit_author")
        ud_titulo = self.get_text("edit_title")
        ud_anopub = self.get_text("edit_ypub")
        ud_editora = self.get_text("edit_pubcomp")
        ud_anoed = self.get_text("edit_yed")
        ud_local = self.get_text("edit_local")

        textview = builder.get_object("edit_quote")
        buffer = textview.get_buffer()
        start_iter, end_iter = buffer.get_bounds()
        ud_quote = buffer.get_text(start_iter, end_iter, True)
        
        self.update_reg(ud_autor, ud_titulo, ud_anopub, ud_editora, ud_anoed, ud_local, ud_quote, lista_reg[0])
        self.renderer_inicial(self.search_inicial())

        editw = builder.get_object("editw")
        editw.hide()
        displayer = builder.get_object("displayer")
        displayer.hide()

    # CANCELAR EDIÇÃO
    def on_edit_cancel_clicked(self, *args):
        editw = builder.get_object("editw")
        editw.hide()

if __name__ == "__main__":
    builder.connect_signals(Handler(Model))
    Gtk.main()