#!usr/bin/env python
#-*-coding:utf-8-*-

import pygtk
pygtk.require("2.0")
import gtk
from analise import *
from calc import *

class CalculadoraApp(object):

    validate = True

    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("forms/calculadora.glade")

        self.window = builder.get_object("window1")
        self.window.show()

        # widgets
        self.entry_expressao = builder.get_object("entry_expressao")
        self.label_error = builder.get_object("label_error")

        # signals
        builder.connect_signals({
            "gtk_main_quit": gtk.main_quit,
            "on_btn_clicked": self.button_clicked,
            "on_btn_resultado_clicked": self.resultado_clicked,
            "on_entry_expressao_insert_text": self.insert_text,
        })

    def insert_text(self, widget, new_text, new_text_length, position):
        expressao = widget.get_text() + new_text
        try:
            Analise.lexica(expressao)
            self.label_error.set_text("")
        except LexicaError as error:
            self.label_error.set_text(error.message)

    def button_clicked(self, widget):
        number = widget.get_label()
        if self.validate:
            text = self.entry_expressao.get_text()
            self.entry_expressao.set_text(text + number)
        else:
            self.entry_expressao.set_text(number)
            self.validate = True

        expressao = self.entry_expressao.get_text()
        try:
            Analise.lexica(expressao)
            self.label_error.set_text("")
        except LexicaError as error:
            self.label_error.set_text(error.message)

    def resultado_clicked(self, widget):
        expressao = self.entry_expressao.get_text()
        try:
            Analise.sintatica(expressao)
            resultado = str(Calc.calcula(expressao))
            self.entry_expressao.set_text(resultado)
            self.validate = False
            self.label_error.set_text("")
        except SintaticaError as error:
            self.label_error.set_text(error.message)

if __name__ == "__main__":
    app = CalculadoraApp()
    gtk.main()
