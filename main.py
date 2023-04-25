import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel


class PopupWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Popup Window')

        layout = QVBoxLayout()
        label = QLabel('This is a popup window.')
        layout.addWidget(label)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')

        button = QPushButton('Show Popup', self)
        button.clicked.connect(self.show_popup)



    def show_popup(self):
        popup = PopupWindow(self)
        popup.open()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
