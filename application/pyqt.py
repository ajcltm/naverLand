import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

sys.path.append('C:/Users/ajcltm/PycharmProjects/naverLand')
import dataclass


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
        dcs = dataclass.ComplexDCs()

        self.tab1.setColumnCount(6)
        self.tab1.setRowCount(len(dcs.data))
        # self.tab1.setStyleSheet("::item {background-color : #f1f2f3;}")
        # self.tab1.setStyleSheet("::section{background-color : #194350;" "color:white;" "border-style : solid;"}")

        cols = ['name', 'address', 'type', 'count', 'hFloor', 'Ymd']
        for tuple in enumerate(cols):
            item = QTableWidgetItem(tuple[1])
            self.tab1.setHorizontalHeaderItem(tuple[0], item)
        # self.tab1.setHorizontalHeaderLabels()
        self.tab1.horizontalHeaderItem(0).setToolTip('''It's something...''')
        # self.tab1.horizontalHeaderItem(0).setTextAlignment(4) # 0:left 1:left 2:right 3:right 4:centre
        self.tab1.horizontalHeader().setStyleSheet("::section{background-color : #194350;" "color:white;" "border-style : solid;}")

        QComboBox_lst = [QComboBox() for i in range(len(cols))]
        QComboBox_element_dict = {'name' : list(set([dc.name for dc in dcs.data])),
                                    'address' : list(set([dc.cortarAddress for dc in dcs.data])),
                                    'type' : list(set([dc.realEstateTypeCode for dc in dcs.data])),
                                    'count' : list(set([str(dc.totalHouseholdCount) for dc in dcs.data])),
                                    'hFloor' : list(set([str(dc.highFloor) for dc in dcs.data])),
                                    'Ymd' : list(set([dc.useApproveYmd for dc in dcs.data]))
                                }
        for tuple in enumerate(cols):
            QComboBox_lst[tuple[0]].addItems(QComboBox_element_dict.get(tuple[1]))
            self.tab1.setCellWidget(0, tuple[0], QComboBox_lst[tuple[0]])

        for tuple in enumerate(cols): 
            self.tab1.setCellWidget(1, tuple[0], QLineEdit())

        for tuple in enumerate(dcs.data) :
            self.tab1.setItem(tuple[0]+2, 0, QTableWidgetItem(tuple[1].name))
            self.tab1.setItem(tuple[0]+2, 1, QTableWidgetItem(tuple[1].cortarAddress))
            self.tab1.setItem(tuple[0]+2, 2, QTableWidgetItem(tuple[1].realEstateTypeCode))
            self.tab1.setItem(tuple[0]+2, 3, QTableWidgetItem(str(tuple[1].totalHouseholdCount)))
            self.tab1.setItem(tuple[0]+2, 4, QTableWidgetItem(str(tuple[1].highFloor)))
            self.tab1.setItem(tuple[0]+2, 5, QTableWidgetItem(tuple[1].useApproveYmd))

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()

    app.exec()