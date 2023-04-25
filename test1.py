import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton,
                             QLabel, QStackedWidget, QLineEdit, QCalendarWidget,
                             QSplashScreen, QMainWindow, QMessageBox, QDateTimeEdit, QScrollArea)
from PyQt6.QtGui import QIcon, QFont, QFontDatabase, QPixmap, QColor, QPalette
from PyQt6.QtCore import Qt

class Page1(QWidget):
    def __init__(self):
        super().__init__()

        bg1 = QWidget(self)
        # self.setCentralWidget(bg1)

        # bg1.setStyleSheet("background-color: #F1F6F9;")
        # bg1.setGeometry(0,0, 850, 500)

        label1 = QLabel("Task Mate", self)
        label1.move(400, 20)

        # Font Size
        font1 = QFont()
        font1.setBold(True)
        font1.setPointSize(20)

        # Font Color


        label1.setFont(font1)
        label1.setStyleSheet("color: black")


        # Create Event
        label2 = QLabel("Event Name", self)
        label2.move(50, 100)
        label2.setStyleSheet("color: black")

        # Textbox for Event Name
        textBox2 = QLineEdit(self)
        textBox2.move(50, 120)
        textBox2.setFixedWidth(200)
        textBox2.setFixedHeight(35)

        # Date and Time
        label_date = QLabel("MM/DD/YY", self)
        label_date.move(50, 180)
        date_time_edit = QDateTimeEdit(self)
        date_time_edit.move(50, 200)



        # Descriptions
        label3 = QLabel("Notes or Descriptions", self)
        label3.move(50, 250)
        label3.setStyleSheet("color: black")

        # Textbox for Note and Description
        textBox3 = QLineEdit(self)
        textBox3.move(50, 270)
        textBox3.setFixedWidth(300)
        textBox3.setFixedHeight(150)

        btn1 = QPushButton("Submit", self)
        btn1.clicked.connect(lambda: self.go_to_page2(textBox2))
        btn1.move(50, 440)

        # Set app background
        # self.setStyleSheet("background-image: url('app_bg.jpg');")
        # self.setStyleSheet("background-color: #FEE8B0;")

        # Set developer notes
        btn0 = QPushButton("?", self)
        btn0.clicked.connect(lambda: QMessageBox.information(None, '', 'Version 1.0 (March 7th, 2023)'
                                                                       '\n'
                                                                       '\n- Task creation page developed with limited UI elements'
                                                             '\n- User input validation'
                                                             '\n- Multiple task creation capabilities added'
                                                             '\n- Checkbox integration for days of the week'
                                                             '\n- Console log output for task management for the time being'))
        btn0.move(800, 460)

    def go_to_page2(self, textBox2):
        stacked_widget.setCurrentWidget(page2)
        text = textBox2.text()
        print(text)

# Pop up window


# Page 2
class Page2(QWidget):
    def __init__(self):
        super().__init__()

        label4 = QLabel("Choose Your Schedule", self)
        label4.move(350, 20)

        label0 = QLabel("Need algorithm here", self)
        label0.move(350, 150)

        # Font

        font1 = QFont()
        font1.setBold(True)
        font1.setPointSize(20)

        # Set Font
        label4.setFont(font1)

        button = QPushButton("next", self)
        button.move(50, 400)
        button.clicked.connect(self.go_to_page3)

    def go_to_page3(self):
        stacked_widget.setCurrentWidget(page3)

class Page3(QWidget):
    def __init__(self):
        super().__init__()

        label4 = QLabel("Your Schedule", self)
        label4.move(400,20)

        # Font

        font1 = QFont()
        font1.setBold(True)
        font1.setPointSize(20)

        # Set Font
        label4.setFont(font1)

        # Calendar View
        cal = QCalendarWidget(self)

        cal.setSelectedDate(cal.selectedDate())
        label5 = QLabel()
        label5.setText("Selected Date: " + cal.selectedDate().toString())
        cal.move(250, 150)

        button = QPushButton("Back", self)
        button.move(50, 400)
        button.clicked.connect(self.go_to_page1)



    def go_to_page1(self):
        stacked_widget.setCurrentWidget(page1)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the pages
    page1 = Page1()
    page2 = Page2()
    page3 = Page3()

    # Create the stacked widget and add the pages to it
    stacked_widget = QStackedWidget()
    stacked_widget.addWidget(page1)
    stacked_widget.addWidget(page2)
    stacked_widget.addWidget(page3)
    stacked_widget.setCurrentWidget(page1)

    stacked_widget.setGeometry(300, 300, 850, 500)

    # Show the stacked widget

    stacked_widget.show()

    sys.exit(app.exec())
