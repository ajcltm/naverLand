import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QColor


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUI()

    def setupUI(self):
        self.setGeometry(800,200, 1000, 700)

        tabs1 = QTabWidget()
        tab1 = QTableWidget()
        tab1.resize(400, 500)
        tab2 = QTableWidget()
        tab2.resize(400, 500)
        tabs1.addTab(tab1, 'table1')
        tabs1.addTab(tab2, 'table2')

        table3 = QTableWidget()
        table3.move(100, 0)

        tabs2 = QTabWidget()
        tab4 = QTableWidget()
        tab5 = QTableWidget()
        tabs2.addTab(tab4, 'table4')
        tabs2.addTab(tab5, 'table5')

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(tabs1)

        rightLayout = QVBoxLayout()
        rightLayout.addSpacing(24)
        rightLayout.addWidget(table3)
        rightLayout.addWidget(tabs2)
        

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)

        self.setLayout(layout)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()

    app.exec()