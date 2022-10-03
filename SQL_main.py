from fileinput import filename
from tkinter import dialog
import sql_ing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(609, 402)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(20, 80, 81, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(100, 80, 111, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(210, 80, 101, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(290, 80, 131, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 260, 81, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_6.setGeometry(QtCore.QRect(120, 260, 81, 16))
        self.checkBox_6.setObjectName("checkBox_6")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 230, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 230, 151, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 110, 431, 71))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(20, 290, 431, 91))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 210, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 210, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(330, 210, 131, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 230, 121, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 40, 431, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(490, 30, 91, 83))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.label_4.setObjectName("label_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(490, 205, 91, 83))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(490, 360, 89, 23))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.reset)
        self.checkBox.clicked.connect(self.set_opt)
        self.checkBox_2.clicked.connect(self.set_opt2)
        self.checkBox_3.clicked.connect(self.set_opt3)
        self.checkBox_4.clicked.connect(self.set_opt4)
        self.pushButton_4.clicked.connect(self.start2)
        self.pushButton_5.clicked.connect(self.reset2)
        self.pushButton_6.clicked.connect(self.save2)
        self.checkBox_5.clicked.connect(self.set_opt5)
        self.checkBox_6.clicked.connect(self.set_opt6)
        self.check_scan= [0,0,0,0]
        self.check_scan2= [0,0]
        self.result1 = ""
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    btn_state = []    
    def start(self):
        text = self.lineEdit_4.text()
        sql_ing.set_cookie(text)
        if self.check_scan[0] == 1:
            clc = sql_ing.Columncount()
            self.plainTextEdit.setPlainText("ANSWER테이블의 컬럼 개수 "+str(clc))
            self.result1 += "ANSWER테이블의 컬럼 개수 "+ str(clc) +"\n"
        elif self.check_scan[1] == 1:
            Column_text_length = sql_ing.Column_text_length()
            self.plainTextEdit.setPlainText("ANSWER테이블의 컬럼 문자열 범위 "+str(Column_text_length))
            self.result1 += "ANSWER테이블의 컬럼 문자열 범위 "+ str(Column_text_length) +"\n"
        elif self.check_scan[2] == 1:
            columnname = sql_ing.Columnname()
            self.plainTextEdit.setPlainText("ANSWER테이블의 컬럼 "+str(columnname))
            self.result1 += "ANSWER테이블의 컬럼 "+ str(columnname) +"\n"
        elif self.check_scan[3] == 1:
            All_find_Column_data_length = sql_ing.All_find_Column_data_length()
            self.plainTextEdit.setPlainText("ANSWER테이블의 컬럼별 데이터 개수 "+str(All_find_Column_data_length))
            self.result1 += "ANSWER테이블의 컬럼별 데이터 개수 "+str(All_find_Column_data_length) +"\n"
    
    def start2(self):
        text = self.lineEdit_4.text()
        sql_ing.set_cookie(text)
        if self.check_scan2[0] == 1:
            name = list(map(str, self.lineEdit.text().split(', ')))
            data_length = list(map(int, self.lineEdit_2.text().split(', ')))
            all_data_length = sql_ing.Data_length(name, data_length)
            self.plainTextEdit_2.setPlainText("ANSWER테이블의 컬럼별 데이터 길이 "+str(all_data_length))
            self.result1 += "ANSWER테이블의 컬럼별 데이터 길이 "+str(all_data_length) +"\n"
        elif self.check_scan2[1] == 1:
            name = list(map(str, self.lineEdit.text().split(', ')))
            data_length = list(map(int, self.lineEdit_2.text().split(', ')))
            all_data_length = list(map(int, self.lineEdit_3.text().split(', ')))
            data = sql_ing.Data_name(name, data_length, all_data_length)
            self.plainTextEdit_2.setPlainText("ANSWER테이블의 컬럼의 전체 데이터 "+str(data))
            self.result1 += "ANSWER테이블의 컬럼의 전체 데이터 "+ str(data) +"\n"
    
    def reset(self):
        self.lineEdit_4.setText("")
        self.plainTextEdit.setPlainText("")
        self.checkBox.setChecked(0)
        self.checkBox_2.setChecked(0)
        self.checkBox_3.setChecked(0)
        self.checkBox_4.setChecked(0)
        self.checkBox.setEnabled(True)
        self.checkBox_2.setEnabled(True)
        self.checkBox_3.setEnabled(True)
        self.checkBox_4.setEnabled(True)
        self.result1 = ""
        
    def reset2(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit.setEnabled(True)
        self.checkBox.setEnabled(True)
        self.checkBox_2.setEnabled(True)
        self.checkBox_3.setEnabled(True)
        self.checkBox_4.setEnabled(True)
        self.checkBox_5.setChecked(0)
        self.checkBox_6.setChecked(0)
        self.lineEdit_3.setEnabled(True)
        self.checkBox_5.setEnabled(True)
        self.checkBox_6.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.result1 = ""
        
    def save2(self):
        file_name = QFileDialog.getSaveFileName(None, 'Save file', './',"text files(*.txt)")
        if file_name[0]:
            with open(file_name[0],'w',encoding='UTF-8') as f:
                f.write(str(self.result1))
    
    def set_opt(self):
        if self.checkBox.checkState() == 2:
            self.checkBox_2.setEnabled(False)
            self.checkBox_3.setEnabled(False)
            self.checkBox_4.setEnabled(False)
            self.check_scan[0] = 1
            
        elif self.checkBox.checkState() == 0:
            self.checkBox_2.setEnabled(True)
            self.checkBox_3.setEnabled(True)
            self.checkBox_4.setEnabled(True)
            self.check_scan[0] = 0
                
    def set_opt2(self):
        if self.checkBox_2.checkState() == 2:
            self.checkBox.setEnabled(False)
            self.checkBox_3.setEnabled(False)
            self.checkBox_4.setEnabled(False)
            self.check_scan[1] = 1
            
        elif self.checkBox_2.checkState() == 0:
            self.checkBox.setEnabled(True)
            self.checkBox_3.setEnabled(True)
            self.checkBox_4.setEnabled(True)
            self.check_scan[1] = 0            
            
    def set_opt3(self):
        if self.checkBox_3.checkState() == 2:
            self.checkBox_2.setEnabled(False)
            self.checkBox.setEnabled(False)
            self.checkBox_4.setEnabled(False)
            self.check_scan[2] = 1
            
        elif self.checkBox_3.checkState() == 0:
            self.checkBox_2.setEnabled(True)
            self.checkBox.setEnabled(True)
            self.checkBox_4.setEnabled(True)
            self.check_scan[2] = 0
    def set_opt4(self):
        if self.checkBox_4.checkState() == 2:
            self.checkBox_2.setEnabled(False)
            self.checkBox_3.setEnabled(False)
            self.checkBox.setEnabled(False)
            self.check_scan[3] = 1
            
        elif self.checkBox_4.checkState() == 0:
            self.checkBox_2.setEnabled(True)
            self.checkBox_3.setEnabled(True)
            self.checkBox.setEnabled(True)
            self.check_scan[3] = 0
            
    def set_opt5(self):
        if self.checkBox_5.checkState() == 2:
            self.checkBox_2.setEnabled(False)
            self.checkBox_3.setEnabled(False)
            self.checkBox_4.setEnabled(False)
            self.checkBox_6.setEnabled(False)
            self.checkBox.setEnabled(False)
            self.plainTextEdit.setEnabled(False)
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(False)
            self.lineEdit_3.setEnabled(False)
            self.check_scan2[0] = 1
            
        elif self.checkBox_5.checkState() == 0:
            self.checkBox_2.setEnabled(True)
            self.checkBox_3.setEnabled(True)
            self.checkBox_4.setEnabled(True)
            self.checkBox_6.setEnabled(True)
            self.checkBox.setEnabled(True)
            self.plainTextEdit.setEnabled(True)
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.check_scan2[0] = 0
            
    def set_opt6(self):
        if self.checkBox_6.checkState() == 2:
            self.checkBox_2.setEnabled(False)
            self.checkBox_3.setEnabled(False)
            self.checkBox_4.setEnabled(False)
            self.checkBox_5.setEnabled(False)
            self.checkBox.setEnabled(False)
            self.plainTextEdit.setEnabled(False)
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(False)
            self.check_scan2[1] = 1
            
        elif self.checkBox_6.checkState() == 0:
            self.checkBox_2.setEnabled(True)
            self.checkBox_3.setEnabled(True)
            self.checkBox_4.setEnabled(True)
            self.checkBox_5.setEnabled(True)
            self.checkBox.setEnabled(True)
            self.plainTextEdit.setEnabled(True)
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.check_scan2[1] = 0
            
            

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowIcon(QIcon('hacker.png'))
        Dialog.setWindowTitle(_translate("Dialog", "SQL Injection"))
        self.checkBox.setText(_translate("Dialog", "컬럼 개수"))
        self.checkBox_2.setText(_translate("Dialog", "컬럼 이름 길이"))
        self.checkBox_3.setText(_translate("Dialog", "컬럼 이름"))
        self.checkBox_4.setText(_translate("Dialog", "컬럼 데이터 길이"))
        self.checkBox_5.setText(_translate("Dialog", "데이터 길이"))
        self.checkBox_6.setText(_translate("Dialog", "데이터 추출"))
        self.label.setText(_translate("Dialog", "컬럼 이름 입력"))
        self.label_2.setText(_translate("Dialog", "컬럼 데이터 길이 입력"))
        self.label_3.setText(_translate("Dialog", "데이터 길이 입력"))
        self.pushButton.setText(_translate("Dialog", "실행"))
        self.pushButton_2.setText(_translate("Dialog", "초기화"))
        self.label_4.setText(_translate("Dialog", "쿠키 값 입력"))
        self.pushButton_4.setText(_translate("Dialog", "실행"))
        self.pushButton_5.setText(_translate("Dialog", "초기화"))
        self.pushButton_6.setText(_translate("Dialog", "저장"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
