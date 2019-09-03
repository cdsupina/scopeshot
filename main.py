from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from screenshot import take_screenshot
import sys


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Oscilloscope Screenshot'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 600
        self.image_data = None
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.screenshot_image = QLabel(self)
        self.screenshot_image.resize(800,512)

        self.info_label = QLabel(self)
        self.info_label.setText('Take a screenshot of your oscilloscope.')
        self.info_label.move(20,550)
        self.info_label.resize(450,20)

        self.save_screenshot_button = QPushButton('Save Screenshot', self)
        self.save_screenshot_button.move(550,550)

        self.take_screenshot_button = QPushButton('Take Screenshot', self)
        self.take_screenshot_button.move(680,550)

        self.take_screenshot_button.clicked.connect(self.on_click_screenshot)
        self.save_screenshot_button.clicked.connect(self.on_click_save)
        self.show()
    
    @pyqtSlot()
    def on_click_screenshot(self):
        self.image_data = take_screenshot()
        if self.image_data != None:
            pixmap = QPixmap()
            pixmap.loadFromData(self.image_data, "PNG")
            self.screenshot_image.setPixmap(pixmap)
            self.info_label.setText('Screenshot taken. Take another screenshot or save this one.')
        else:
            self.info_label.setText('Resource not found.')

    @pyqtSlot()
    def on_click_save(self):
        if self.image_data is not None:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', '.png')
            output_file = open(filename, 'wb')
            output_file.write(self.image_data)
            output_file.close()
            self.info_label.setText('Screenshot saved to ' + filename + '.')
        else:
            self.info_label.setText('You must take a screenshot before saving.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
