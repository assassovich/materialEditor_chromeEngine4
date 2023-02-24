# coding: utf8
# GUI для создания текстового файла конфигурации материала для Chrome Engine 4

import sys, os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QLabel, QLineEdit, QPushButton, QFrame, QVBoxLayout, \
    QHBoxLayout, QComboBox, QCheckBox

from PyQt6.QtGui import QDragEnterEvent, QDropEvent

Border = "---------------------------------------------------------------------------------"


class DragDropLabel(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)

        # установка стиля
        self.setStyleSheet('''
            background-color: white;
            color: blue;
            border: 2px solid blue;
            padding: 4px;
        ''')

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent) -> None:
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            self.setText(file_name)

class SliderWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.input_field_1 = None
        self.setWindowTitle("Material editor for Chrome engine 4")
        self.initUI()

    def initUI(self):
        self.setFixedSize(440, 660)  # Set fixed window size
        self.label_1 = QLabel("This utility can help create more material \nconfiguration files in Chrome Engine 4")

        self.input_field_label_1 = QLabel("enter *.mat file name")
        self.input_field_1 = QLineEdit(self)
        self.drop_label_1 = QLabel("or drop *.mat file name")
        self.drop_field_1 = DragDropLabel(self)


        self.input_field_label_2 = QLabel("s_clr = ")
        self.input_field_2 = QLineEdit()
        self.input_field_label_3 = QLabel("s_nrm = ")
        self.input_field_3 = QLineEdit()
        self.input_field_label_4 = QLabel("s_shn = ")
        self.input_field_4 = QLineEdit()
        self.input_field_label_5 = QLabel("s_dye = ")
        self.input_field_5 = QLineEdit()
        self.input_field_label_11 = QLabel("set surfase type")
        self.ComboBox_1 = QComboBox()
        self.input_field_label_6 = QLabel("s_clr_srf = ")
        self.input_field_6 = QLineEdit()
        self.input_field_label_7 = QLabel("s_nrm_srf = ")
        self.input_field_7 = QLineEdit()
        self.input_field_label_8 = QLabel("commented parameters = ")
        self.input_field_8 = QLineEdit()

        self.input_field_label_9 = QLabel("b_dye_level_color_on = ", self)
        self.checkbox_1 = QCheckBox("TRUE or FALSE", self)
        self.input_field_label_10 = QLabel("b_clr_usr_on = ", self)
        self.checkbox_2 = QCheckBox("TRUE or FALSE", self)
        self.checkbox_2.setChecked(True)
        # значения

        self.ComboBox_1.addItems(
            ['No Value', 'SRF_UNKNOWN', 'SRF_FLEXIBLE', 'SRF_FIRE', 'SRF_WATER', 'SRF_SNOW', 'SRF_GRASS', 'SRF_GROUND',
             'SRF_MUD', 'SRF_GRAVEL', 'SRF_FLESH', 'SRF_RUBBER', 'SRF_WOOD', 'SRF_PLASTIC', 'SRF_PLEXIGLASS',
             'SRF_GLASS', 'SRF_ICE', 'SRF_METAL', 'SRF_STONE'])

        # слайдеры
        self.slider_1 = QSlider(Qt.Orientation.Horizontal)
        self.slider_1.setMinimum(0)
        self.slider_1.setMaximum(1500)
        self.slider_1.setValue(500)

        self.slider_4 = QSlider(Qt.Orientation.Horizontal)
        self.slider_4.setMinimum(-400)
        self.slider_4.setMaximum(400)
        self.slider_4.setValue(170)

        self.slider_2 = QSlider(Qt.Orientation.Horizontal)
        self.slider_2.setMinimum(-500)
        self.slider_2.setMaximum(500)
        self.slider_2.setValue(-100)

        self.slider_3 = QSlider(Qt.Orientation.Horizontal)
        self.slider_3.setMinimum(0)
        self.slider_3.setMaximum(400)
        self.slider_3.setValue(200)

        self.Border_1 = QLabel(Border, self)
        self.Border_2 = QLabel(Border, self)
        self.Border_3 = QLabel(Border, self)
        self.Border_4 = QLabel(Border, self)

        self.fixed_text_3 = QLabel("f_srf_uv_scale = ", self)
        self.label_2 = QLabel("5.0")
        self.fixed_text_6 = QLabel("f_nrm_srf_scale = ", self)
        self.label_5 = QLabel("1.7")
        self.fixed_text_4 = QLabel("f_shn_factor = ", self)
        self.label_3 = QLabel("-1.0")
        self.fixed_text_5 = QLabel("f_nrm_factor = ", self)
        self.label_4 = QLabel("2.0")
        self.save_button = QPushButton("Save")

        self.restart_button = QPushButton('Restart', self)
        self.restart_button.clicked.connect(self.reset_fields)

        layout = QVBoxLayout()
        layout.addWidget(self.label_1)

        hbox_1 = QHBoxLayout()  #
        hbox_1.addWidget(self.input_field_label_1)
        hbox_1.addWidget(self.input_field_1)
        layout.addLayout(hbox_1)

        hbox_16 = QHBoxLayout()  #
        hbox_16.addWidget(self.drop_label_1)
        hbox_16.addWidget(self.drop_field_1)
        layout.addLayout(hbox_16)

        hbox_2 = QHBoxLayout()  #
        hbox_2.addWidget(self.input_field_label_2)
        hbox_2.addWidget(self.input_field_2)
        layout.addLayout(hbox_2)

        hbox_3 = QHBoxLayout()  #
        hbox_3.addWidget(self.input_field_label_3)
        hbox_3.addWidget(self.input_field_3)
        layout.addLayout(hbox_3)

        hbox_4 = QHBoxLayout()  #
        hbox_4.addWidget(self.input_field_label_4)
        hbox_4.addWidget(self.input_field_4)
        layout.addLayout(hbox_4)

        hbox_5 = QHBoxLayout()  #
        hbox_5.addWidget(self.input_field_label_5)
        hbox_5.addWidget(self.input_field_5)
        layout.addLayout(hbox_5)

        layout.addWidget(self.Border_1)
        hbox_14 = QHBoxLayout()
        hbox_14.addWidget(self.input_field_label_11)
        hbox_14.addWidget(self.ComboBox_1)
        layout.addLayout(hbox_14)
        layout.addWidget(self.Border_4)

        hbox_6 = QHBoxLayout()  #
        hbox_6.addWidget(self.input_field_label_6)
        hbox_6.addWidget(self.input_field_6)
        layout.addLayout(hbox_6)

        hbox_7 = QHBoxLayout()  #
        hbox_7.addWidget(self.input_field_label_7)
        hbox_7.addWidget(self.input_field_7)
        layout.addLayout(hbox_7)

        hbox_8 = QHBoxLayout()  #
        hbox_8.addWidget(self.input_field_label_8)
        hbox_8.addWidget(self.input_field_8)
        layout.addLayout(hbox_8)

        layout.addWidget(self.Border_2)

        hbox_9 = QHBoxLayout()  #
        hbox_9.addWidget(self.input_field_label_9)
        hbox_9.addWidget(self.checkbox_1)
        layout.addLayout(hbox_9)

        hbox_10 = QHBoxLayout()  #
        hbox_10.addWidget(self.input_field_label_10)
        hbox_10.addWidget(self.checkbox_2)
        layout.addLayout(hbox_10)

        layout.addWidget(self.Border_3)

        hbox_11 = QHBoxLayout()  #
        hbox_11.addWidget(self.fixed_text_3)
        hbox_11.addWidget(self.slider_1)
        hbox_11.addWidget(self.label_2)
        layout.addLayout(hbox_11)

        hbox_15 = QHBoxLayout()
        hbox_15.addWidget(self.fixed_text_6)
        hbox_15.addWidget(self.slider_4)
        hbox_15.addWidget(self.label_5)
        layout.addLayout(hbox_15)

        hbox_12 = QHBoxLayout()  #
        hbox_12.addWidget(self.fixed_text_4)
        hbox_12.addWidget(self.slider_2)
        hbox_12.addWidget(self.label_3)
        layout.addLayout(hbox_12)

        hbox_13 = QHBoxLayout()  #
        hbox_13.addWidget(self.fixed_text_5)
        hbox_13.addWidget(self.slider_3)
        hbox_13.addWidget(self.label_4)
        layout.addLayout(hbox_13)

        layout.addWidget(self.save_button)
        layout.addWidget(self.restart_button)

        self.slider_1.valueChanged.connect(lambda: self.label_2.setText(str(self.slider_1.value() / 100)))
        self.slider_2.valueChanged.connect(lambda: self.label_3.setText(str(self.slider_2.value() / 100)))
        self.slider_3.valueChanged.connect(lambda: self.label_4.setText(str(self.slider_3.value() / 100)))
        self.slider_4.valueChanged.connect(lambda: self.label_5.setText(str(self.slider_4.value() / 100)))
        self.save_button.clicked.connect(self.save_values)

        self.setLayout(layout)

        # Сохраняем исходные значения полей
        self.input1_default = self.input_field_1.text()
        self.input2_default = self.input_field_2.text()
        self.input3_default = self.input_field_3.text()
        self.input4_default = self.input_field_4.text()
        self.input5_default = self.input_field_5.text()
        self.input6_default = self.input_field_6.text()
        self.input7_default = self.input_field_7.text()
        self.input8_default = self.input_field_8.text()
        self.slider1_default = self.slider_1.value()
        self.slider2_default = self.slider_2.value()
        self.slider3_default = self.slider_3.value()
        self.checkbox1_default = self.checkbox_1.isChecked()
        self.checkbox2_default = self.checkbox_2.isChecked()
        self.ComboBox_1.setCurrentIndex(12)


    def reset_fields(self):
        # Сбросить значения полей на исходные
        self.input_field_1.setText("")
        self.drop_field_1.setText("")
        self.input_field_2.setText("")
        self.input_field_3.setText("")
        self.input_field_4.setText("")
        self.input_field_5.setText("")
        self.input_field_6.setText("")
        self.input_field_7.setText("")
        self.input_field_8.setText("")
        self.slider_1.setValue(self.slider1_default)
        self.slider_2.setValue(self.slider2_default)
        self.slider_3.setValue(self.slider3_default)
        self.checkbox_1.setChecked(self.checkbox1_default)
        self.checkbox_2.setChecked(self.checkbox2_default)
        self.ComboBox_1.setCurrentIndex(12)

    def save_values(self):

        fi_2 = self.input_field_2.text()
        add_2 = "//" if fi_2 == "" else ""
        fi_3 = self.input_field_3.text()
        add_3 = "//" if fi_3 == "" else ""
        fi_4 = self.input_field_4.text()
        add_4 = "//" if fi_4 == "" else ""
        fi_5 = self.input_field_5.text()
        add_5 = "//" if fi_5 == "" else ""
        fi_6 = self.input_field_6.text()
        add_6 = "//" if fi_6 == "" else ""
        fi_7 = self.input_field_7.text()
        add_7 = "//" if fi_7 == "" else ""

        CB_1text = self.ComboBox_1.currentText()
        add_8 = "//" if CB_1text == "No Value" else ""

        x1 = str(self.checkbox_1.isChecked())
        x2 = str(self.checkbox_2.isChecked())

        if self.input_field_1.text() == "":
            file_name_1 = self.drop_field_1.text()
            print(self.drop_field_1.text())
            print(self.input_field_1.text())
            print(file_name_1)
            print(1)
        else:
            file_name_1 = self.input_field_1.text()
            print(self.drop_field_1.text())
            print(self.input_field_1.text())
            print(file_name_1)
            print(2)
        if file_name_1 != "":
            with open(file_name_1 + '.mat', "w") as f:
                f.write('import "templates.mtt"\n\nsub material()\n{\n    use mtt_objects(\n        ')
                f.write(add_2 + 's_clr = "' + self.input_field_2.text() + '.dds",\n        ')
                f.write(add_3 + 's_nrm = "' + self.input_field_3.text() + '.dds",\n        ')
                f.write(add_4 + 's_shn = "' + self.input_field_4.text() + '.dds",\n        ')
                f.write(add_5 + 's_dye = "' + self.input_field_5.text() + '.dds",\n\n        ')
                f.write(add_6 + 's_clr_srf = "' + self.input_field_6.text() + '.dds",\n        ')
                f.write(add_7 + 's_nrm_srf = "' + fi_7 + '.dds",\n\n        ')

                f.write('// ' + self.input_field_8.text() + ',\n\n        ')
                f.write(add_8 + 'e_srf_id = ' + CB_1text + ',\n\n        ')

                f.write('b_dye_level_color_on = ' + x1.upper() + ',\n        ')
                f.write('b_clr_usr_on = ' + x2.upper() + ',\n\n        ')

                f.write('f_srf_uv_scale = ' + str(self.slider_1.value() / 100) + ',\n        ')
                f.write('f_nrm_srf_scale = ' + str(self.slider_4.value()/100) + ',\n        ')
                f.write('f_shn_factor = ' + str(self.slider_2.value() / 100) + ',\n        ')
                f.write('f_nrm_factor = ' + str(self.slider_3.value() / 100) + ');\n}\n')
        else:
            print("error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SliderWindow()
    window.show()
    sys.exit(app.exec())
