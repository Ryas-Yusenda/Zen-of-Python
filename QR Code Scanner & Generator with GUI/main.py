import cv2
import qrcode
import sys
import os

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore


class MyGUI(QMainWindow):

    def __init__(self):
        self.path = sys.argv[0][:sys.argv[0].rfind('/')]

        super(MyGUI, self).__init__()
        uic.loadUi(self.path + "/design.ui", self)
        
        self.show()

        self.current_file = ""
        self.actionLoad.triggered.connect(self.load_image)
        self.actionSave.triggered.connect(self.save_image)
        self.actionQuit.triggered.connect(self.close)
        self.textEdit.textChanged.connect(self.generate_qr)

    def load_image(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Image Files (*.png *.jpg)", options=options)

        try:
            self.current_file = filename
            pixmap = QtGui.QPixmap(self.current_file)
            pixmap = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(pixmap)
            self.read_qr()
        except:
            print("No File Selected")

    def save_image(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Image Files (*.png *.jpg)", options=options)

        try:
            img = self.label.pixmap().toImage()
            img.save(filename, "PNG")
        except:
            print("No File Selected")

    def generate_qr(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=2,
        )
        qr.add_data(self.textEdit.toPlainText())
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(self.path + "/QR.png")
        pixmap = QtGui.QPixmap(self.path + "/QR.png")
        pixmap = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)

    def read_qr(self):
        img = cv2.imread(self.current_file)
        detector = cv2.QRCodeDetector()
        data, bbox, straight_qrcode = detector.detectAndDecode(img)
        if bbox is not None:
            self.textEdit.setText(data)
        else:
            self.textEdit.setText("No QR Code Found")

    def close(self):
        if os.path.exists(self.path + "/QR.png"):
            os.remove(self.path + "/QR.png")
        sys.exit()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            if os.path.exists(self.path + "/QR.png"):
                os.remove(self.path + "/QR.png")
            print('Window closed')
        else:
            event.ignore()


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()


if __name__ == "__main__":
    main()
