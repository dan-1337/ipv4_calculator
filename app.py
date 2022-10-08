
import sys

from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication, QMainWindow

from classes.calc_ipv4 import CalcIpv4
from design import Ui_MainWindow


class Ipv4(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setFixedSize(350, 360)
        self.networkEdit.setReadOnly(True)
        self.maskEdit.setReadOnly(True)
        self.prefixEdit.setReadOnly(True)
        self.broadcastEdit.setReadOnly(True)
        self.nIpsEdit.setReadOnly(True)

        self.btnCalculate.clicked.connect(self.calculate_ip)
        self.btnClear.clicked.connect(self.clear_fields)

    def calculate_ip(self):
        res = None
        combo_box_index = self.maskOrPrefixComboBox.currentIndex()
        num_ipv4 = self.ipv4Edit.text().strip()

        try:
            if combo_box_index == 0:
                prefix = int(self.maskOrPrefixEdit.text().strip())
                res = CalcIpv4(ip=num_ipv4, prefixo=prefix)
                self.labelValid.setText('IP calculado com sucesso!')
            if combo_box_index == 1:
                mask = self.maskOrPrefixEdit.text().strip()
                res = CalcIpv4(ip=num_ipv4, mascara=mask)
                self.labelValid.setText('IP calculado com sucesso!')

            self.networkEdit.setText(res.rede)
            self.maskEdit.setText(res.mascara)
            self.prefixEdit.setText(str(res.prefixo))
            self.broadcastEdit.setText(res.broadcast)
            self.nIpsEdit.setText(str(res.numero_ips))
        except Exception as e:
            self.labelInvalid.setText(f'Erro! {e}')

        QTest.qWait(5000)
        self.labelValid.setText('')
        self.labelInvalid.setText('')

    def clear_fields(self):
        self.networkEdit.setText('')
        self.maskEdit.setText('')
        self.broadcastEdit.setText('')
        self.prefixEdit.setText('')
        self.nIpsEdit.setText('')
        self.labelValid.setText('')
        self.labelInvalid.setText('')
        self.ipv4Edit.setText('')
        self.maskOrPrefixEdit.setText('')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc_ipv4 = Ipv4()
    calc_ipv4.show()
    qt.exec_()
