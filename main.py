from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from course_getter import get_courses
from PyQt5.QtGui import QDoubleValidator

app = QApplication([])
window = QWidget()

window.resize(500, 500)
window.setWindowTitle("Currency calc")

main_hbl = QHBoxLayout()
left_vbl = QVBoxLayout()
right_vbl = QVBoxLayout()

dollars_hbl = QHBoxLayout()
tenges_hbl = QHBoxLayout()
yens_hbl = QHBoxLayout()
roubles_hbl = QHBoxLayout()

eur_l = QLabel("Введите сумму в евро")
eur_le = QLineEdit()

dollars_img_l = QLabel("$")
dollars_le = QLineEdit()
dollars_le.setReadOnly(True)

tenges_img_l = QLabel("₸")
tenges_le = QLineEdit()
tenges_le.setReadOnly(True)

yens_img_l = QLabel("¥")
yens_le = QLineEdit()
yens_le.setReadOnly(True)

roubles_img_l = QLabel("₽")
roubles_le = QLineEdit()
roubles_le.setReadOnly(True)

currency_btn = QPushButton("Перевести валюту")

# упаковываем виджеты в лейауты
dollars_hbl.addWidget(dollars_img_l)
dollars_hbl.addWidget(dollars_le)

tenges_hbl.addWidget(tenges_img_l)
tenges_hbl.addWidget(tenges_le)

yens_hbl.addWidget(yens_img_l)
yens_hbl.addWidget(yens_le)

roubles_hbl.addWidget(roubles_img_l)
roubles_hbl.addWidget(roubles_le)

left_vbl.addWidget(eur_l, alignment=Qt.AlignHCenter)
left_vbl.addWidget(eur_le, alignment=Qt.AlignHCenter)
left_vbl.addWidget(currency_btn, alignment=Qt.AlignHCenter)
left_vbl.setContentsMargins(0, 200, 0, 200) 

right_vbl.addLayout(dollars_hbl)
right_vbl.addLayout(tenges_hbl)
right_vbl.addLayout(yens_hbl)
right_vbl.addLayout(roubles_hbl)

main_hbl.addLayout(left_vbl)
main_hbl.addLayout(right_vbl)

eur_le.setValidator(QDoubleValidator())

currency_btn.setEnabled(False)
eur_le.textChanged.connect(lambda text: currency_btn.setEnabled(bool(text.strip())))

def currency_convert():
    amount = float(eur_le.text())
    converted_courses = get_courses(amount)
    dollars_le.setText(str(converted_courses["USD"]))
    yens_le.setText(str(converted_courses["JPY"]))
    tenges_le.setText(str(converted_courses["KZT"]))
    roubles_le.setText(str(converted_courses["RUB"]))

currency_btn.clicked.connect(currency_convert)

window.setLayout(main_hbl)
window.show()
app.exec_()