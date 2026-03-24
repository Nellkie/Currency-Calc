from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

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



window.setLayout(main_hbl)
window.show()
app.exec_()