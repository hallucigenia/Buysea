# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

__author__ = 'fansly'


from PyQt5 import QtCore, QtGui, QtWidgets

import main_menu   #导入该对象所在文件
Ui_MainWindow = main_menu.Ui_MainWindow#指定Ui_MainWindow 为main_menu文件下的Ui_MainWindow对象。


class Ui_QUICreator(object):
    def setupUi(self, QUICreator):
        QUICreator.setObjectName("QUICreator")
        QUICreator.resize(958, 708)
        self.centralwidget = QtWidgets.QWidget(QUICreator)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_7.addWidget(self.progressBar, 6, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_7.addWidget(self.lineEdit, 0, 0, 1, 3)
        self.frameColor = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameColor.sizePolicy().hasHeightForWidth())
        self.frameColor.setSizePolicy(sizePolicy)
        self.frameColor.setMinimumSize(QtCore.QSize(220, 0))
        self.frameColor.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frameColor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameColor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameColor.setObjectName("frameColor")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frameColor)
        self.gridLayout_3.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ck2 = QtWidgets.QCheckBox(self.frameColor)
        self.ck2.setChecked(False)
        self.ck2.setObjectName("ck2")
        self.gridLayout_3.addWidget(self.ck2, 5, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frameColor)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_3.addWidget(self.radioButton_2, 12, 0, 1, 2)
        self.checkBox = QtWidgets.QCheckBox(self.frameColor)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 3, 1, 1, 1)
        self.ck3 = QtWidgets.QCheckBox(self.frameColor)
        self.ck3.setObjectName("ck3")
        self.gridLayout_3.addWidget(self.ck3, 1, 2, 1, 1)
        self.ck1 = QtWidgets.QCheckBox(self.frameColor)
        self.ck1.setObjectName("ck1")
        self.gridLayout_3.addWidget(self.ck1, 1, 1, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.frameColor)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_3.addWidget(self.radioButton_3, 11, 0, 1, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frameColor)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 10, 0, 1, 3)
        self.radioButton_5 = QtWidgets.QRadioButton(self.frameColor)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_3.addWidget(self.radioButton_5, 13, 0, 1, 1)
        self.btnNew = QtWidgets.QPushButton(self.frameColor)
        self.btnNew.setObjectName("btnNew")
        self.gridLayout_3.addWidget(self.btnNew, 12, 2, 1, 1)
        self.btnSave = QtWidgets.QPushButton(self.frameColor)
        self.btnSave.setObjectName("btnSave")
        self.gridLayout_3.addWidget(self.btnSave, 13, 2, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frameColor)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_3.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.frameColor)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_3.addWidget(self.checkBox_3, 3, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.frameColor)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_3.addWidget(self.checkBox_4, 5, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frameColor, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_7.addLayout(self.horizontalLayout, 4, 0, 2, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_7.addWidget(self.pushButton, 6, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 712, 620))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_7.addWidget(self.scrollArea, 3, 1, 3, 2)
        QUICreator.setCentralWidget(self.centralwidget)

        self.retranslateUi(QUICreator)
        QtCore.QMetaObject.connectSlotsByName(QUICreator)

    def retranslateUi(self, QUICreator):
        _translate = QtCore.QCoreApplication.translate
        QUICreator.setWindowTitle(_translate("QUICreator", "MainWindow"))
        self.lineEdit.setText(_translate("QUICreator", "商品名称在此输入"))
        self.ck2.setText(_translate("QUICreator", "自营"))
        self.radioButton_2.setText(_translate("QUICreator", "价格优先"))
        self.checkBox.setText(_translate("QUICreator", "旗舰店"))
        self.ck3.setText(_translate("QUICreator", "金牌卖家"))
        self.ck1.setText(_translate("QUICreator", "包邮"))
        self.radioButton_3.setText(_translate("QUICreator", "评级权重 ( 默认 )"))
        self.lineEdit_2.setText(_translate("QUICreator", "价格区间"))
        self.radioButton_5.setText(_translate("QUICreator", "销量优先"))
        self.btnNew.setText(_translate("QUICreator", "新建"))
        self.btnSave.setText(_translate("QUICreator", "保存规则"))
        self.checkBox_2.setText(_translate("QUICreator", "淘宝"))
        self.checkBox_3.setText(_translate("QUICreator", "天猫"))
        self.checkBox_4.setText(_translate("QUICreator", "京东"))
        self.pushButton.setText(_translate("QUICreator", "关于我"))


class CoperQt(QtWidgets.QMainWindow,Ui_MainWindow):#创建一个Qt对象
#这里的第一个变量是你该窗口的类型，第二个是该窗口对象。
#这里是主窗口类型。所以设置成当QtWidgets.QMainWindow。
#你的窗口是一个会话框时你需要设置成:QtWidgets.QDialog
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)  # 创建主界面对象
        Ui_MainWindow.__init__(self)#主界面对象初始化
        self.setupUi(self)  #配置主界面对象

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CoperQt()#创建QT对象
    window.show()#QT对象显示
    sys.exit(app.exec_())
