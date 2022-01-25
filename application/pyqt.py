import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUI()

    def setupUI(self):
        self.setGeometry(800,200, 1000, 700)

        self.tabs1 = QTabWidget()
        self.tab1 = QTableWidget()
        self.tab1.resize(400, 500)
        self.set_tab1()
        self.tab2 = QTableWidget()
        self.tab2.resize(400, 500)
        self.tabs1.addTab(self.tab1, 'table1')
        self.tabs1.addTab(self.tab2, 'table2')

        self.table3 = QTableWidget()
        self.table3.move(100, 0)

        self.tabs2 = QTabWidget()
        self.tab4 = QTableWidget()
        self.tab5 = QTableWidget()
        self.tabs2.addTab(self.tab4, 'table4')
        self.tabs2.addTab(self.tab5, 'table5')

        self.leftLayout = QVBoxLayout()
        self.leftLayout.addWidget(self.tabs1)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.addSpacing(24)
        self.rightLayout.addWidget(self.table3)
        self.rightLayout.addWidget(self.tabs2)
        

        self.layout = QHBoxLayout()
        self.layout.addLayout(self.leftLayout)
        self.layout.addLayout(self.rightLayout)

        self.setLayout(self.layout)
    
    def set_tab1(self):

        self.tab1.setColumnCount(4)
        self.tab1.setRowCount(5)
        # self.tab1.setStyleSheet("::item {background-color : #f1f2f3;}")
        # self.tab1.setStyleSheet("::section{background-color : #194350;" "color:white;" "border-style : solid;"}")

        cols = ['col1', 'col2', 'col3', 'col4']
        for tuple in enumerate(cols):
            item = QTableWidgetItem(tuple[1])
            item.setBackground(1)
            self.tab1.setHorizontalHeaderItem(tuple[0], item)
        # self.tab1.setHorizontalHeaderLabels()
        self.tab1.horizontalHeaderItem(0).setToolTip('''It's something...''')
        # self.tab1.horizontalHeaderItem(0).setTextAlignment(4) # 0:left 1:left 2:right 3:right 4:centre
        # self.tab1.horizontalHeader().setStyleSheet("::section{background-color : #194350;" "color:white;" "border-style : solid;}")

        

        QComboBox_lst = [QComboBox() for i in range(len(cols))]
        QComboBox_element_dict = {'col1' : ['a', 'b', 'c', 'd'],
                                    'col2' : ['e', 'f', 'g', 'h'],
                                    'col3' : ['i', 'f', 'k', 'l'],
                                    'col4' : ['n', 'm', 'o', 'p'],
                                } 
        for tuple in enumerate(cols):
            QComboBox_lst[tuple[0]].addItems(QComboBox_element_dict.get(tuple[1]))
            self.tab1.setCellWidget(0, tuple[0], QComboBox_lst[tuple[0]])

        for tuple in enumerate(cols): 
            self.tab1.setCellWidget(1, tuple[0], QLineEdit())


        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()

    app.exec()