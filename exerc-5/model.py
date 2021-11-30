import sqlite3
from sqlite3 import Error

class Model():
    def __init__(self, *args):
        self.connectbase = sqlite3.connect("modelo.db")
        self.cursor = self.connectbase.cursor()
        self.create_base()

        self.connectquote = sqlite3.connect("quotes.db")
        self.cursorq = self.connectquote.cursor()
        self.create_quotes()

    # CRIAÇÃO DA BASE DE DADOS
    def create_base(self, *args):
        sqlquery = ("create table if not exists file("
                    "n_num integer primary key autoincrement,"
                    "t_author varchar(100),"
                    "t_title varchar(200),"
                    "n_year integer,"
                    "t_pubcomp varchar(100),"
                    "n_yeared integer,"
                    "t_type varchar(50),"
                    "t_locquote varchar(50),"
                    "t_quote text)")
        self.cursor.execute(sqlquery)
        self.connectbase.commit()
        print("Base criada")

    # TREE VIEW DA JANELA INICIAL
    def search_inicial(self, *args):
        sqlquery = ("select f.n_num, f.t_author, f.t_title, f.t_quote from file f")
        self.cursor.execute(sqlquery)
        return self.cursor.fetchall()

    # RESGATE DO REGISTRO
    def get_registro(self, filecode):
        sqlquery = ("select * from file where n_num = ?")
        sqlargs = [filecode]
        self.cursor.execute(sqlquery, sqlargs)
        return self.cursor.fetchall()

    # SAVE DE NOVO REGISTRO
    def save_registro(self, t_author, t_title, n_year, t_pubcomp, n_yeared, t_type, t_locquote, t_quote):
        sqlquery = ("insert into file"
                    "(t_author, t_title, n_year, t_pubcomp, n_yeared, t_type, t_locquote, t_quote)"
                    "values (?,?,?,?,?,?,?,?)")
        sqlargs = (t_author, t_title, n_year, t_pubcomp, n_yeared, t_type, t_locquote, t_quote)
        self.cursor.execute(sqlquery, sqlargs)
        self.connectbase.commit()

    # REMOÇÃO DE REGISTRO
    def del_reg(self, filecode):
        sqlquery = ("delete from file where n_num = ?")
        sqlargs = [filecode]
        self.cursor.execute(sqlquery, sqlargs)
        self.connectbase.commit()

    # UPDATE DO REGISTRO
    def update_reg(self, t_author, t_title, n_year, t_pubcomp, n_yeared, t_locquote, t_quote, n_num):
        sqlquery = ("update file set "
                    "t_author = ?, "
                    "t_title = ?, " 
                    "n_year = ?, "
                    "t_pubcomp = ?, "
                    "n_yeared = ?, "
                    "t_locquote = ?, "
                    "t_quote = ? "
                    " where n_num = ?")
        sqlargs = (t_author, t_title, n_year, t_pubcomp, n_yeared, t_locquote, t_quote, n_num)
        self.cursor.execute(sqlquery, sqlargs)
        self.connectbase.commit()

    # CRIAÇÃO BASE DE CITAÇÕES
    def create_quotes(self, *args):
        sqlquery = ("create table if not exists fileq("
                    "n_numq integer primary key autoincrement,"
                    "t_new_quote text)")
        self.cursorq.execute(sqlquery)
        self.connectquote.commit()
        print("base quotes criada")

    # TREE VIEW DA JANELA REGISTROS
    def search_registro(self, *args):
        sqlquery = ("select f.t_new_quote from fileq f")
        self.cursorq.execute(sqlquery)
        return self.cursorq.fetchall()

    # SAVE DE NOVA CITAÇÃO
    def save_quote(self, t_new_quote):
        sqlquery = ("insert into fileq"
                    "(t_new_quote)"
                    "values (?)")
        sqlargs = (t_new_quote,)
        self.cursorq.execute(sqlquery, sqlargs)
        self.connectquote.commit()

    # REMOÇÃO DE CITAÇÃO
    def del_quote(self, filecode):
        sqlquery = ("delete from fileq where t_new_quote = ?")
        sqlargs = [filecode]
        self.cursorq.execute(sqlquery, sqlargs)
        self.connectquote.commit()

    # DROP DO BANCO DE CITAÇÕES
    def quotes_drop(self, *args):
        self.cursorq.execute("drop table fileq")