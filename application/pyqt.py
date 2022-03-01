import sqlite3
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtGui, QtCore

import pandas as pd

from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.ticker as ticker

import plotly.express as px
import numpy as np
import math

sys.path.append('C:/Users/ajcltm/PycharmProjects/naverLand')
import dataclass
import sqlQuery
import whereClause
from formatting import formatting


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.tab1_init_data = sqlQuery.Tab1_table().get_data()
        self.tab1_data = self.tab1_init_data
        self.tab1_currentRowCount = 0
        self.tab1_maxRowCount = 100
        self.where = whereClause.tab1_WhereHandler().set_where_dict()
        self.label_data = {}
        self.tab4_data = None

        self.setupUI()

    def setupUI(self):
        self.setGeometry(200, 200, 1400, 700)

        self.tabs1 = QTabWidget()

        self.tab1 = QTableWidget()
        self.tab1.verticalScrollBar().valueChanged.connect(self.scrolled)
        self.tab1.resize(400, 500)
        self.set_tab1()
        self.searchGroupBox = QGroupBox('Search')
        self.searchLineEdit = QLineEdit()
        self.searchLineEdit.returnPressed.connect(self.search_LineEditClicked)
        searchGoupBox_vlayout = QVBoxLayout()
        searchGoupBox_vlayout.addWidget(self.searchLineEdit)
        self.searchGroupBox.setLayout(searchGoupBox_vlayout)

        tab1_vlayout = QVBoxLayout()
        tab1_vlayout.addWidget(self.searchGroupBox)
        tab1_vlayout.addWidget(self.tab1)
        self.tab1_widget = QWidget()
        self.tab1_widget.setLayout(tab1_vlayout)


        self.tab2 = QTableWidget()
        self.tab2.resize(400, 500)
        # self.set_tab2()


        self.tabs1.addTab(self.tab1_widget, 'table1')
        self.tabs1.addTab(self.tab2, 'table2')


        self.set_mainGroupBox()
        self.set_mainGroupBox_label()
        self.set_mainGroupBox_layout()

        self.set_detailGroupBox()
        self.set_detailGroupBox_label()
        self.set_detailGroupBox_layout()

        self.set_brokerGroupBox()
        self.set_brokerGroupBox_label()
        self.set_brokerGroupBox_layout()

        self.tabs2 = QTabWidget()
        self.tab3 = QWidget()
        # tab3_vlayout = QVBoxLayout()
        tab3_layout = QHBoxLayout()

        tab3_plot_vlayout = QVBoxLayout()
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        # self.fig = plt.Figure(figsize=(3,2))
        # self.tab3_plot = FigureCanvas(self.fig)
        tab3_plot_vlayout.addWidget(self.browser)

        tab3_table_vlayout = QVBoxLayout()
        self.tab3_table = QTableWidget()       

        tab3_table_vlayout.addSpacing(7)
        tab3_table_vlayout.addWidget(self.tab3_table)

        tab3_layout.addLayout(tab3_plot_vlayout, 6)
        tab3_layout.addLayout(tab3_table_vlayout, 4)
        # tab3_layout.addWidget(self.tab3_table)
        # tab3_vlayout.addLayout(tab3_layout)
        self.tab3.setLayout(tab3_layout)

        self.tab4 = QWidget()
        tab4_layout = QHBoxLayout()
        self.tab4.setLayout(tab4_layout)
        
        self.tab4 = QTableWidget()
        # setFrameStyle(QtGui.QFrame)
        self.tabs2.addTab(self.tab3, 'tab3')
        self.tabs2.addTab(self.tab4, 'tab4')


        self.leftLayout = QVBoxLayout()
        self.leftLayout.addWidget(self.tabs1)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.addSpacing(24)
        self.rightLayout.addWidget(self.mainGroupBox)
        self.rightLayout.addWidget(self.detailGroupBox)
        self.rightLayout.addWidget(self.brokerGroupBox)
        self.rightLayout.addWidget(self.tabs2)
        
        self.layout = QHBoxLayout()
        self.layout.addLayout(self.leftLayout, 9)
        self.layout.addLayout(self.rightLayout, 7)

        self.setLayout(self.layout)


    def search_LineEditClicked(self):

        text = self.searchLineEdit.text()

        if len(text) > 0 :
            where_content = whereClause.tab1_WhereHandler().handle_searchLideEdit(text)
        else :
            where_content = None

        dic = {key : value for key, value in self.where.items()}
        dic['search'] = where_content
        where_clause = whereClause.tab1_WhereHandler().get_where_clause(dic)
        response = sqlQuery.Tab1_table().get_data(where=where_clause)
        if response :
            self.tab1_data = response
            self.where = dic
        else:
            self.Warning_event()
        self.tab1_currentRowCount=0
        self.tab1_maxRowCount=100
        self.set_tab1_contents()

    

    def set_tab1(self):
        
        cols = ['city', 'gu', 'dong', 'complex', 'articleName', 'articleNo', 'dealPrice', 'realPrice', 'allWarrant','hhCount',  'ApproveYmd', 'exposeYMD', 'estateType','tradeType']
        self.tab1.setColumnCount(len(cols))
        self.tab1.setRowCount(len(self.tab1_data))
        
        self.tab1.setHorizontalHeaderLabels(cols)
        self.tab1.horizontalHeader().setStyleSheet("::section{background-color : #05111b;" "color:white;" "border-style : solid;}")

        # create table data

        self.set_tab1_contents()

        # create line Editers
    
        self.set_cell_lineEdit()

        self.tab1.clicked.connect(self.tab1Clicked)
    
    def set_tab1_contents(self):
        if self.tab1_maxRowCount + 100 > len(self.tab1_data) :
            if len(self.tab1_data) == 0:
                self.tab1.setRowCount(1)                    
            else:
                self.tab1.setRowCount(len(self.tab1_data))
        else :
            self.tab1.setRowCount(self.tab1_maxRowCount)
        db_cols = ['cityName', 'gu', 'dong', 'complex', 'articleName', 'articleNo',
                     'dealPrice', 'price', 'allWarrantPrice',  
                    'householdCountByPtp','aptUseApproveYmd', 'exposeStartYMD',
                    'realestateTypeCode', 'tradeTypeName']
        width_cols = {
                'cityName': 55, 'gu': 55, 'dong': 55, 'complex': 120, 'articleName': 160, 'articleNo': 90,
                     'dealPrice': 80, 'price': 80, 'allWarrantPrice': 80,  
                    'householdCountByPtp': 80, 'aptUseApproveYmd': 80, 'exposeStartYMD': 80,
                    'realestateTypeCode': 80, 'tradeTypeName': 80
        }

        numeric_cols = ['dealPrice', 'price', 'allWarrantPrice', 'householdCountByPtp']

        for row_tuple in enumerate(self.tab1_data) :  # rows
            
            if row_tuple[0]+1 > self.tab1_maxRowCount:
                self.tab1_currentRowCount = self.tab1_maxRowCount
                break
            if row_tuple[0]+1 >= self.tab1_currentRowCount :
                for col_tuple in enumerate(db_cols) : #cols
                    self.tab1.setColumnWidth(col_tuple[0], width_cols.get(col_tuple[1]))
                    value = row_tuple[1].get(col_tuple[1])
                    value = formatting(value)
                    item = QTableWidgetItem(value)
                    item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    if col_tuple[1] in numeric_cols: 
                        item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                    self.tab1.setItem(row_tuple[0]+1, col_tuple[0], item)
                    

        self.tab1.setEditTriggers(QTableWidget.NoEditTriggers)

    def scrolled(self, value):
        if value == self.tab1.verticalScrollBar().maximum():
            if self.tab1_maxRowCount + 100 > len(self.tab1_data) :
                self.tab1_maxRowCount = len(self.tab1_data)
            else:
                self.tab1_maxRowCount += 100
            self.set_tab1_contents()

    def tab1Clicked(self):

        row = self.tab1.currentIndex().row()-1

        articleNo = self.tab1_data[row].get('articleNo')

        where = whereClause.label_WhereHandler().get_where_clause(articleNo)

        self.label_data = sqlQuery.Tab1_table().get_data(where=where)[0]
        self.set_mainGroupBox_label(update=True)
        self.set_detailGroupBox_label(update=True)
        self.set_brokerGroupBox_label(update=True)

        complexNo = self.tab1_data[row].get('complexNo')
        ptpNo = self.tab1_data[row].get('ptpNo')

        where = whereClause.tab4_WhereHandler().get_where_clause(complexNo, ptpNo)

        self.tab4_data = sqlQuery.Tab4_table().get_data(where=where)
        self.set_tab3_table()

        self.set_tab3_plot()


    def set_cell_lineEdit(self):
        self.city_le = QLineEdit()
        self.tab1.setCellWidget(0, 0, self.city_le)
        self.city_le.returnPressed.connect(self.city_cellLineEditClicked)

        self.gu_le = QLineEdit()
        self.tab1.setCellWidget(0, 1, self.gu_le)
        self.gu_le.returnPressed.connect(self.gu_cellLineEditClicked)

        self.dong_le = QLineEdit()
        self.tab1.setCellWidget(0, 2, self.dong_le)
        self.dong_le.returnPressed.connect(self.dong_cellLineEditClicked)

        self.complex_le = QLineEdit()
        self.tab1.setCellWidget(0, 3, self.complex_le)
        self.complex_le.returnPressed.connect(self.complex_cellLineEditClicked)

        self.articleName_le = QLineEdit()
        self.tab1.setCellWidget(0, 4, self.articleName_le)
        self.articleName_le.returnPressed.connect(self.articleName_cellLineEditClicked)

        self.articleNo_le = QLineEdit()
        self.tab1.setCellWidget(0, 5, self.articleNo_le)
        self.articleNo_le.returnPressed.connect(self.articleNo_cellLineEditClicked)

        self.dealPrice_le = QLineEdit()
        self.tab1.setCellWidget(0, 6, self.dealPrice_le)
        self.dealPrice_le.returnPressed.connect(self.dealPrice_cellLineEditClicked)

        self.realPrice_le = QLineEdit()
        self.tab1.setCellWidget(0, 7, self.realPrice_le)
        self.realPrice_le.returnPressed.connect(self.realPrice_cellLineEditClicked)

        self.allWarrantPrice_le = QLineEdit()
        self.tab1.setCellWidget(0, 8, self.allWarrantPrice_le)
        self.allWarrantPrice_le.returnPressed.connect(self.allWarrantPrice_cellLineEditClicked)

        self.hhCount_le = QLineEdit()
        self.tab1.setCellWidget(0, 9, self.hhCount_le)
        self.hhCount_le.returnPressed.connect(self.hhCount_cellLineEditClicked)

        self.aptUseYMD_le = QLineEdit()
        self.tab1.setCellWidget(0, 10, self.aptUseYMD_le)
        self.aptUseYMD_le.returnPressed.connect(self.aptUseYMD_cellLineEditClicked)

        self.exposeStartYMD_le = QLineEdit()
        self.tab1.setCellWidget(0, 11, self.exposeStartYMD_le)
        self.exposeStartYMD_le.returnPressed.connect(self.exposeStartYMD_cellLineEditClicked)

        self.estateType_le = QLineEdit()
        self.tab1.setCellWidget(0, 12, self.estateType_le)
        self.estateType_le.returnPressed.connect(self.estateType_cellLineEditClicked)

        self.tradeTypeName_le = QLineEdit()
        self.tab1.setCellWidget(0, 13, self.tradeTypeName_le)
        self.tradeTypeName_le.returnPressed.connect(self.tradeTypeName_cellLineEditClicked)

    def city_cellLineEditClicked(self):
        text = self.city_le.text()
        target_col = 'city_info.cityName'
        if len(text) > 0 :
            where_content = whereClause.tab1_WhereHandler().handle_comma(text, target_col)
        else :
            where_content = None

        dic = {key : value for key, value in self.where.items()}
        dic['cityName'] = where_content
        
        where_clause = whereClause.tab1_WhereHandler().get_where_clause(dic)
        response = sqlQuery.Tab1_table().get_data(where=where_clause)
        if response :
            self.tab1_data = response
            self.where = dic
        else:
            self.Warning_event()
        self.tab1_currentRowCount=0
        self.tab1_maxRowCount=100
        self.set_tab1_contents()

    def gu_cellLineEditClicked(self):
        text = self.gu_le.text()
        target_col = 'gu'
        if len(text) > 0 :
            where_content = whereClause.tab1_WhereHandler().handle_comma(text, target_col)
        else :
            where_content = None

        dic = {key : value for key, value in self.where.items()}
        dic['gu'] = where_content
        where_clause = whereClause.tab1_WhereHandler().get_where_clause(dic)
        response = sqlQuery.Tab1_table().get_data(where=where_clause)
        if response :
            self.tab1_data = response
            self.where = dic
        else:
            self.Warning_event()
        self.tab1_currentRowCount=0
        self.tab1_maxRowCount=100
        self.set_tab1_contents()

    def dong_cellLineEditClicked(self):
        text = self.dong_le.text()
        target_col = 'dong'
        if len(text) > 0 :
            where_content = whereClause.tab1_WhereHandler().handle_comma(text, target_col)
        else :
            where_content = None

        dic = {key : value for key, value in self.where.items()}
        dic['dong'] = where_content
        where_clause = whereClause.tab1_WhereHandler().get_where_clause(dic)
        response = sqlQuery.Tab1_table().get_data(where=where_clause)
        if response :
            self.tab1_data = response
            self.where = dic
        else:
            self.Warning_event()
        self.tab1_currentRowCount=0
        self.tab1_maxRowCount=100
        self.set_tab1_contents()

    def complex_cellLineEditClicked(self):
        text = self.complex_le.text()
        target_col = 'complex'
        if len(text) > 0 :
            where_content = whereClause.tab1_WhereHandler().handle_comma(text, target_col)
        else :
            where_content = None

        dic = {key : value for key, value in self.where.items()}
        dic['complex'] = where_content
        where_clause = whereClause.tab1_WhereHandler().get_where_clause(dic)
        response = sqlQuery.Tab1_table().get_data(where=where_clause)
        if response :
            self.tab1_data = response
            self.where = dic
        else:
            self.Warning_event()
        self.tab1_currentRowCount=0
        self.tab1_maxRowCount=100
        self.set_tab1_contents()

    def articleName_cellLineEditClicked(self):
        text = self.articleName_le.text()
        target_col = 'article_info.articleName'
        if len(text) > 0 :
            where_content = whereClause.tab1_WhereHandler().handle_comma(text, target_col)
        else :
            where_content = None

        dic = {key : value for key, value in self.where.items()}
        dic['articleName'] = where_content
        where_clause = whereClause.tab1_WhereHandler().get_where_clause(dic)
        response = sqlQuery.Tab1_table().get_data(where=where_clause)
        if response :
            self.tab1_data = response
            self.where = dic
        else:
            self.Warning_event()
        self.tab1_currentRowCount=0
        self.tab1_maxRowCount=100
        self.set_tab1_contents()

    def articleNo_cellLineEditClicked(self):
        text = self.articleNo_le.text()
        target_col = 'article_info.articleNo'
        if len(text) > 0 :
            where_content = whereClause.tab1_WhereHandler().handle_comma(text, target_col)
        else :
            where_content = None

        dic = {key : value for key, value in self.where.items()}
        dic['articleNo'] = where_content
        where_clause = whereClause.tab1_WhereHandler().get_where_clause(dic)
        response = sqlQuery.Tab1_table().get_data(where=where_clause)
        if response :
            self.tab1_data = response
            self.where = dic
        else:
            self.Warning_event()
        self.tab1_currentRowCount=0
        self.tab1_maxRowCount=100
        self.set_tab1_contents()

    def dealPrice_cellLineEditClicked(self):
        text = self.dealPrice_le.text()

        target_col = 'article_info.dealPrice'
        if len(text) > 0 :
            where_content = whereClause.tab1_WhereHandler().handle_comma_numeric(text, target_col)
        else :
            where_content = None

        dic = {key : value for key, value in self.where.items()}
        dic['dealPrice'] = where_content
        where_clause = whereClause.tab1_WhereHandler().get_where_clause(dic)
        response = sqlQuery.Tab1_table().get_data(where=where_clause)
        if response :
            self.tab1_data = response
            self.where = dic
        else:
            self.Warning_event()
        self.tab1_currentRowCount=0
        self.tab1_maxRowCount=100
        self.set_tab1_contents()

    def realPrice_cellLineEditClicked(self):
        text = self.realPrice_le.text()

        target_col = 'v.price'
        if len(text) > 0 :
            where_content = whereClause.tab1_WhereHandler().handle_comma_numeric(text, target_col)
        else :
            where_content = None

        dic = {key : value for key, value in self.where.items()}
        dic['realPrice'] = where_content
        where_clause = whereClause.tab1_WhereHandler().get_where_clause(dic)
        response = sqlQuery.Tab1_table().get_data(where=where_clause)
        if response :
            self.tab1_data = response
            self.where = dic
        else:
            self.Warning_event()
        self.tab1_currentRowCount=0
        self.tab1_maxRowCount=100   
        self.set_tab1_contents()

    def allWarrantPrice_cellLineEditClicked(self):
        text = self.allWarrantPrice_le.text()

        target_col = 'allWarrantPrice'
        if len(text) > 0 :
            where_content = whereClause.tab1_WhereHandler().handle_comma_numeric(text, target_col)
        else :
            where_content = None

        dic = {key : value for key, value in self.where.items()}
        dic['allWarrantPrice'] = where_content
        where_clause = whereClause.tab1_WhereHandler().get_where_clause(dic)
        response = sqlQuery.Tab1_table().get_data(where=where_clause)
        if response :
            self.tab1_data = response
            self.where = dic
        else:
            self.Warning_event()
        self.tab1_currentRowCount=0
        self.tab1_maxRowCount=100
        self.set_tab1_contents()

    def hhCount_cellLineEditClicked(self):
        text = self.hhCount_le.text()

        target_col = 'householdCountByPtp'
        if len(text) > 0 :
            where_content = whereClause.tab1_WhereHandler().handle_comma_numeric(text, target_col)
        else :
            where_content = None

        dic = {key : value for key, value in self.where.items()}
        dic['householdCountByPtp'] = where_content
        where_clause = whereClause.tab1_WhereHandler().get_where_clause(dic)
        response = sqlQuery.Tab1_table().get_data(where=where_clause)
        if response :
            self.tab1_data = response
            self.where = dic
        else:
            self.Warning_event()
        self.tab1_currentRowCount=0
        self.tab1_maxRowCount=100
        self.set_tab1_contents()

    def aptUseYMD_cellLineEditClicked(self):
        text = self.aptUseYMD_le.text()

        target_col = 'aptUseApproveYmd'
        if len(text) > 0 :
            where_content = whereClause.tab1_WhereHandler().handle_comma_numeric(text, target_col)
        else :
            where_content = None

        dic = {key : value for key, value in self.where.items()}
        dic['aptUseApproveYmd'] = where_content
        where_clause = whereClause.tab1_WhereHandler().get_where_clause(dic)
        response = sqlQuery.Tab1_table().get_data(where=where_clause)
        if response :
            self.tab1_data = response
            self.where = dic
        else:
            self.Warning_event()
        self.tab1_currentRowCount=0
        self.tab1_maxRowCount=100
        self.set_tab1_contents()
    
    def exposeStartYMD_cellLineEditClicked(self):
        text = self.exposeStartYMD_le.text()

        target_col = 'exposeStartYMD'
        if len(text) > 0 :
            where_content = whereClause.tab1_WhereHandler().handle_comma_numeric(text, target_col)
        else :
            where_content = None

        dic = {key : value for key, value in self.where.items()}
        dic['exposeStartYMD'] = where_content
        where_clause = whereClause.tab1_WhereHandler().get_where_clause(dic)
        response = sqlQuery.Tab1_table().get_data(where=where_clause)
        if response :
            self.tab1_data = response
            self.where = dic
        else:
            self.Warning_event()
        self.tab1_currentRowCount=0
        self.tab1_maxRowCount=100
        self.set_tab1_contents()

    def estateType_cellLineEditClicked(self):
        text = self.estateType_le.text()
        target_col = 'article_info.realestateTypeCode'
        if len(text) > 0 :
            where_content = whereClause.tab1_WhereHandler().handle_comma(text, target_col)
        else :
            where_content = None

        dic = {key : value for key, value in self.where.items()}
        dic['realestateTypeCode'] = where_content
        where_clause = whereClause.tab1_WhereHandler().get_where_clause(dic)
        response = sqlQuery.Tab1_table().get_data(where=where_clause)
        if response :
            self.tab1_data = response
            self.where = dic
        else:
            self.Warning_event()
        self.tab1_currentRowCount=0
        self.tab1_maxRowCount=100
        self.set_tab1_contents()
    
    def tradeTypeName_cellLineEditClicked(self):
        text = self.tradeTypeName_le.text()
        target_col = 'article_info.tradeTypeName'
        if len(text) > 0 :
            where_content = whereClause.tab1_WhereHandler().handle_comma(text, target_col)
        else :
            where_content = None

        dic = {key : value for key, value in self.where.items()}
        dic['tradeTypeName'] = where_content
        where_clause = whereClause.tab1_WhereHandler().get_where_clause(dic)
        response = sqlQuery.Tab1_table().get_data(where=where_clause)
        if response :
            self.tab1_data = response
            self.where = dic
        else:
            self.Warning_event()
        self.tab1_currentRowCount=0
        self.tab1_maxRowCount=100
        self.set_tab1_contents()

    def set_mainGroupBox(self):

        self.mainGroupBox = QGroupBox('Main Information')
        

    def set_mainGroupBox_label(self, update=False):  

        if update == False :
            self.ql_articleName = QLabel()
        i = self.label_data.get('articleName')
        i = formatting(i)
        self.ql_articleName.setText(f'article name : {i}')
        self.ql_articleName.repaint()

        if update == False :
            self.ql_aptUseApproveYmd = QLabel()
        i = self.label_data.get('aptUseApproveYmd')
        i = formatting(i)
        self.ql_aptUseApproveYmd.setText(f'approve date : {i}')
        self.ql_aptUseApproveYmd.repaint()

        if update == False :
            self.ql_fullAddress = QLabel()
        i = self.label_data.get('fullAddress')
        i = formatting(i)
        self.ql_fullAddress.setText(f'address : {i}')
        self.ql_fullAddress.repaint()

        if update == False :
            self.ql_dealPrice = QLabel()
        i = self.label_data.get('dealPrice')
        i = formatting(i)
        self.ql_dealPrice.setText(f'deal price : {i}')
        self.ql_dealPrice.repaint()

        if update == False :
            self.ql_price = QLabel()
        i = self.label_data.get('price')
        i = formatting(i)
        self.ql_price.setText(f'real price : {i}')
        self.ql_price.repaint()

        if update == False :
            self.ql_allWarrantPrice = QLabel()
        i = self.label_data.get('allWarrantPrice')
        i = formatting(i)
        self.ql_allWarrantPrice.setText(f'all warrant price : {i}')
        self.ql_allWarrantPrice.repaint()

        if update == False :
            self.ql_financePrice = QLabel()
        i = self.label_data.get('financePrice')
        i = formatting(i)
        self.ql_financePrice.setText(f'finance price : {i}')
        self.ql_financePrice.repaint()

        if update == False :
            self.ql_supplySpace = QLabel()
        i = self.label_data.get('supplySpace')
        i = formatting(i)
        self.ql_supplySpace.setText(f'supply space : {i}')
        self.ql_supplySpace.repaint()

        if update == False :
            self.ql_exclusiveSpace = QLabel()
        i = self.label_data.get('exclusiveSpace')
        i = formatting(i)
        self.ql_exclusiveSpace.setText(f'exclusive space : {i}')
        self.ql_exclusiveSpace.repaint()

        if update == False :
            self.ql_exclusiveRate = QLabel()
        i = self.label_data.get('exclusiveRate')
        i = formatting(i)
        self.ql_exclusiveRate.setText(f'exclusive rate : {i}')
        self.ql_exclusiveRate.repaint()

        if update == False :
            self.ql_walkingTimeToNearSubway = QLabel()
        i = self.label_data.get('walkingTimeToNearSubway')
        i = formatting(i)
        self.ql_walkingTimeToNearSubway.setText(f'time to subway : {i}')
        self.ql_walkingTimeToNearSubway.repaint()

        if update == False :
            self.ql_totalDongCount = QLabel()
        i = self.label_data.get('totalDongCount')
        i = formatting(i)
        self.ql_totalDongCount.setText(f'dong count : {i}')
        self.ql_totalDongCount.repaint()

        if update == False :
            self.ql_aptHouseholdCount = QLabel()
        i = self.label_data.get('aptHouseholdCount')
        i = formatting(i)
        self.ql_aptHouseholdCount.setText(f'house count : {i}')
        self.ql_aptHouseholdCount.repaint()

        if update == False :
            self.ql_floorInfo = QLabel()
        i = self.label_data.get('floorInfo')
        i = formatting(i)
        self.ql_floorInfo.setText(f'floor info : {i}')
        self.ql_floorInfo.repaint()

        if update == False :
            self.ql_entranceTypeName = QLabel()
        i = self.label_data.get('entranceTypeName')
        i = formatting(i)
        self.ql_entranceTypeName.setText(f'entrance type : {i}')
        self.ql_entranceTypeName.repaint()


    def set_mainGroupBox_layout(self):
        labelVBox = QVBoxLayout()

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_articleName)
        labelHBox.addWidget(self.ql_aptUseApproveYmd)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_fullAddress)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_dealPrice)
        labelHBox.addWidget(self.ql_price)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_allWarrantPrice)
        labelHBox.addWidget(self.ql_financePrice)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_supplySpace)
        labelHBox.addWidget(self.ql_exclusiveSpace)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_exclusiveRate)
        labelHBox.addWidget(self.ql_walkingTimeToNearSubway)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_totalDongCount)
        labelHBox.addWidget(self.ql_aptHouseholdCount)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_floorInfo)
        labelHBox.addWidget(self.ql_entranceTypeName)
        labelVBox.addLayout(labelHBox)

        self.mainGroupBox.setLayout(labelVBox)

    def set_detailGroupBox(self):

        self.detailGroupBox = QGroupBox('detail Information')


    def set_detailGroupBox_label(self, update=False):  

        if update == False :
            self.ql_aptConstructionCompanyName = QLabel()
        i = self.label_data.get('aptConstructionCompanyName')
        i = formatting(i)
        self.ql_aptConstructionCompanyName.setText(f'construction firm : {i}')
        self.ql_aptConstructionCompanyName.repaint()

        if update == False :
            self.ql_exposeStartYMD = QLabel()
        i = self.label_data.get('exposeStartYMD')
        i = formatting(i)
        self.ql_exposeStartYMD.setText(f'expose start date : {i}')
        self.ql_exposeStartYMD.repaint()

        if update == False :
            self.ql_exposeEndYMD = QLabel()
        i = self.label_data.get('exposeEndYMD')
        i = formatting(i)
        self.ql_exposeEndYMD.setText(f'expose end date : {i}')
        self.ql_exposeEndYMD.repaint()

        if update == False :
            self.ql_roomCount = QLabel()
        i = self.label_data.get('roomCount')
        i = formatting(i)
        self.ql_roomCount.setText(f'room count : {i}')
        self.ql_roomCount.repaint()

        if update == False :
            self.ql_bathroomCount = QLabel()
        i = self.label_data.get('bathroomCount')
        i = formatting(i)
        self.ql_bathroomCount.setText(f'bathroom count : {i}')
        self.ql_bathroomCount.repaint()

        if update == False :
            self.ql_monthlyManagementCost = QLabel()
        i = self.label_data.get('monthlyManagementCost')
        i = formatting(i)
        self.ql_monthlyManagementCost.setText(f'management cost : {i}')
        self.ql_monthlyManagementCost.repaint()

        if update == False :
            self.ql_monthlyManagementCostInclusdeItemName = QLabel()
        i = self.label_data.get('monthlyManagementCostInclusdeItemName')
        i = formatting(i)
        self.ql_monthlyManagementCostInclusdeItemName.setText(f'include item : {i}')
        self.ql_monthlyManagementCostInclusdeItemName.repaint()

        if update == False :
            self.ql_direction = QLabel()
        i = self.label_data.get('direction')
        i = formatting(i)
        self.ql_direction.setText(f'direction : {i}')
        self.ql_direction.repaint()

        if update == False :
            self.ql_articleFeatureDescription = QLabel()
        i = self.label_data.get('articleFeatureDescription')
        i = formatting(i)
        self.ql_articleFeatureDescription.setText(f'description : {i}')
        self.ql_articleFeatureDescription.repaint()


    def set_detailGroupBox_layout(self):
        labelVBox = QVBoxLayout()

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_aptConstructionCompanyName)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_exposeStartYMD)
        labelHBox.addWidget(self.ql_exposeEndYMD)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_roomCount)
        labelHBox.addWidget(self.ql_bathroomCount)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_monthlyManagementCost)
        labelHBox.addWidget(self.ql_monthlyManagementCostInclusdeItemName)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_direction)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_articleFeatureDescription)
        labelVBox.addLayout(labelHBox)

        self.detailGroupBox.setLayout(labelVBox)


    def set_brokerGroupBox(self):

        self.brokerGroupBox = QGroupBox('broker Information')


    def set_brokerGroupBox_label(self, update=False):  

        if update == False :
            self.ql_realtorName = QLabel()
        i = self.label_data.get('realtorName')
        i = formatting(i)
        self.ql_realtorName.setText(f'broker name : {i}')
        self.ql_realtorName.repaint()

        if update == False :
            self.ql_representativeName = QLabel()
        i = self.label_data.get('representativeName')      
        i = formatting(i)
        self.ql_representativeName.setText(f'representative : {i}')
        self.ql_representativeName.repaint()

        if update == False :
            self.ql_address = QLabel()
        i = self.label_data.get('address')
        i = formatting(i)
        self.ql_address.setText(f'broker address : {i}')
        self.ql_address.repaint()

        if update == False :
            self.ql_representiveTelNo = QLabel()
        i = self.label_data.get('telephon')
        i = formatting(i)
        self.ql_representiveTelNo.setText(f'telephon : {i}')
        self.ql_representiveTelNo.repaint()

        if update == False :
            self.ql_cellPhoneNo = QLabel()
        i = self.label_data.get('cellPhoneNo')
        i = formatting(i)
        self.ql_cellPhoneNo.setText(f'cell phone : {i}')
        self.ql_cellPhoneNo.repaint()


    def set_brokerGroupBox_layout(self):
        labelVBox = QVBoxLayout()

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_realtorName)
        labelHBox.addWidget(self.ql_representativeName)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_address)
        labelVBox.addLayout(labelHBox)

        labelHBox = QHBoxLayout()
        labelHBox.addWidget(self.ql_representiveTelNo)
        labelHBox.addWidget(self.ql_cellPhoneNo)
        labelVBox.addLayout(labelHBox)

        self.brokerGroupBox.setLayout(labelVBox)


    def set_tab3_table(self):
        
        cols = ['date', 'real price']
        self.tab3_table.setColumnCount(len(cols))
        self.tab3_table.setRowCount(len(self.tab4_data))

        self.tab3_table.setColumnWidth(0, 90)
        self.tab3_table.setColumnWidth(1, 80)        
        self.tab3_table.setHorizontalHeaderLabels(cols)
        self.tab3_table.horizontalHeader().setStyleSheet("::section{background-color : #05111b;" "color:white;" "border-style : solid;}")

        # create table data

        self.set_tab3_table_contents()
    
    def set_tab3_table_contents(self):
        db_cols = ['date', 'price']
        for row_tuple in enumerate(self.tab4_data) :  # rows
            for col_tuple in enumerate(db_cols) : #cols
                value = row_tuple[1].get(col_tuple[1])
                value = formatting(value)
                item = QTableWidgetItem(value)
                item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                if col_tuple[1] == 'price': 
                    item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                self.tab3_table.setItem(row_tuple[0], col_tuple[0], item)

        self.tab3_table.setEditTriggers(QTableWidget.NoEditTriggers)
        

    def set_tab3_plot(self):
        
        date = [self.tab4_data[i].get('date') for i in range(len(self.tab4_data))]
        if date[0] == None:
            date_datetime = date
        else:
            date_datetime = [datetime.strptime(i,'%Y-%m-%d') for i in date]

        
        price = [self.tab4_data[i].get('price') for i in range(len(self.tab4_data))]
        if price[0] ==None:
            price = price
        else:
            price = [self.tab4_data[i].get('price')/10000 for i in range(len(self.tab4_data))]

        df = pd.DataFrame({'date': date_datetime, 'price': price})

        fig = px.scatter(df, x="date", y="price")
        # fig.update_traces(quartilemethod="inclusive") # or "inclusive", or "linear" by default

        fig.update_layout(
            autosize=False,
            width=300,
            height=200,
            margin=dict(
                l=6,
                r=8,
                b=6,
                t=8,
                pad=0
            ),
            paper_bgcolor="LightSteelBlue"
        )
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_title=None, yaxis_title=None)
        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def Warning_event(self) : 
        QMessageBox.warning(self,'ERROR','Failed to query the data.')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()

    app.exec()
   