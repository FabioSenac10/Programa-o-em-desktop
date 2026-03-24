from PySide6.QtWidgets import QApplication, QMainWindow 
from PySide6.QtUiTools import QUiLoader 
from PySide6.QtCore import QFile 
import sys 
 
class MainWindow(QMainWindow): 
   def __init__(self): 
       super().__init__() 
 
       loader = QUiLoader() 
       ui_file = QFile("tela.ui") 
       ui_file.open(QFile.ReadOnly) 
       self.ui = loader.load(ui_file) 
       ui_file.close() 
 
app = QApplication(sys.argv) 
window = MainWindow() 
window.ui.show() 
sys.exit(app.exec()) 