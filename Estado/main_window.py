from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from nota import Note
from ui_mainwindow import Ui_MainWindow
import pickle, threading
from time import sleep


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Mis_notas')
        
        #boton de agregar
        self.ui.guardarButton.clicked.connect(self.guardarNota)
        
        self.cargarNota()

        threading.Thread(target=self.respaldo, daemon=True).start()

    @Slot()
    def guardarNota(self):
        self.dbfile = open ('notas', 'wb')

        titulo = self.ui.LEtitulo.text()
        nota = self.ui.textNotas.toPlainText()

        self.nota = Note(titulo,nota)
        pickle.dump(self.nota, self.dbfile)
        self.dbfile.close()

    def cargarNota(self):
        try:
            with open("notas", "rb") as dbfile:
                self.nota = pickle.load(dbfile)
                self.ui.LEtitulo.setText(self.nota.getTitulo())
                self.ui.textNotas.setText(self.nota.getTexto())
                
            dbfile.close()
        except:
            pass

    def respaldo(self):
        while True:
            print("Guardando...")
            self.guardarNota()
            sleep(5)