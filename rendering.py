from PyQt6.QtWidgets import QWidget, QGridLayout,QPushButton,QApplication,QLabel
from PyQt6.QtGui import QFont,QIcon
from functools import partial

from models.calculator import Calculator
import config as c

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(c.WINDOW_TITLE)
        #self.setWindowIcon(QIcon("myicon.jpg"))

        self.setFixedWidth(600)
        self.setFixedHeight(400)
        self.setGeometry(600,400,100,100)

        self.calculator = Calculator()
        
        grid = QGridLayout()

        key_dict = {"0": (4,0), "1": (3,0), "2": (3,1), "3": (3,2), "4": (2,0), "5": (2,1),
                    "6": (2,2), "7": (1,0), "8": (1,1), "9": (1,2), "+": (1,3), "-": (2,3),
                    "*": (3,3), "/": (4,3), "=": (4,2), ".": (4,1), "C": (0,3)
                     }

        button_set = [(QPushButton(symbol),symbol) for symbol in key_dict]
        self.display=QLabel("0",self)

        def to_enter(symbol):
            self.calculator.entry(symbol)
            self.display.setText(self.calculator.display_current_state())

        grid.addWidget(self.display,0,0,1,3)
 
        for el in button_set:
            grid.addWidget(el[0],key_dict[el[1]][0],key_dict[el[1]][1])
            el[0].clicked.connect(partial(to_enter,el[1]))
            el[0].setFont(QFont(c.KEY_FONT,c.KEY_FONT_SIZE))
             
        self.display.setFont(QFont(c.DISPLAY_FONT,c.DISPLAY_FONT_SIZE))
        self.setLayout(grid)
        
app = QApplication([])
window = Window()
window.show()
app.exec()

