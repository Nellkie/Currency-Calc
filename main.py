from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

app = QApplication([])
window = QWidget()

window.resize(1000, 600)
window.setWindowTitle("Currency calc")

main_hbl = QHBoxLayout()
left_vbl = QVBoxLayout()
right_vbl = QVBoxLayout()

dollars_hbl = QHBoxLayout()
tenges_hbl = QHBoxLayout()
yens_hbl = QHBoxLayout()
roubles_hbl = QHBoxLayout()

eur_l = QLabel("Введите сумму")
eur_le = QLineEdit()

dollars_img_l = QLabel("$")
dollars_le = QLineEdit()

tenges_img_l = QLabel("₸")
tenges_le = QLineEdit()

yens_img_l = QLabel("¥")
yens_le = QLineEdit()

roubles_img_l = QLabel("₽")
roubles_le = QLineEdit()
