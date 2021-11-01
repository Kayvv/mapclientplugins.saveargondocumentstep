# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(570, 341)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label0)

        self.lineEditIdentifier = QLineEdit(self.configGroupBox)
        self.lineEditIdentifier.setObjectName(u"lineEditIdentifier")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditIdentifier)

        self.labelConsolidateResources = QLabel(self.configGroupBox)
        self.labelConsolidateResources.setObjectName(u"labelConsolidateResources")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelConsolidateResources)

        self.checkBoxConsolidateResources = QCheckBox(self.configGroupBox)
        self.checkBoxConsolidateResources.setObjectName(u"checkBoxConsolidateResources")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.checkBoxConsolidateResources)

        self.label1 = QLabel(self.configGroupBox)
        self.label1.setObjectName(u"label1")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEditOutputDirectory = QLineEdit(self.configGroupBox)
        self.lineEditOutputDirectory.setObjectName(u"lineEditOutputDirectory")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditOutputDirectory.sizePolicy().hasHeightForWidth())
        self.lineEditOutputDirectory.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lineEditOutputDirectory)

        self.pushButtonDIrectoryChooser = QPushButton(self.configGroupBox)
        self.pushButtonDIrectoryChooser.setObjectName(u"pushButtonDIrectoryChooser")

        self.horizontalLayout.addWidget(self.pushButtonDIrectoryChooser)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout)


        self.gridLayout.addWidget(self.configGroupBox, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        QWidget.setTabOrder(self.lineEditIdentifier, self.checkBoxConsolidateResources)
        QWidget.setTabOrder(self.checkBoxConsolidateResources, self.lineEditOutputDirectory)
        QWidget.setTabOrder(self.lineEditOutputDirectory, self.pushButtonDIrectoryChooser)

        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Step", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("ConfigureDialog", u"Identifier:  ", None))
        self.labelConsolidateResources.setText(QCoreApplication.translate("ConfigureDialog", u"Consolidate Resources:  ", None))
        self.checkBoxConsolidateResources.setText("")
        self.label1.setText(QCoreApplication.translate("ConfigureDialog", u"Output Directory:", None))
        self.pushButtonDIrectoryChooser.setText(QCoreApplication.translate("ConfigureDialog", u"...", None))
    # retranslateUi

