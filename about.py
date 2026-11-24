from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class AboutWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("About")
        self.setGeometry(550, 150, 340, 380)

        self.title_label = QLabel("Grade Corrector")
        self.title_label.setObjectName("title")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.image_label = QLabel()
        pixmap = QPixmap("profile.jpeg")
        self.image_label.setPixmap(pixmap.scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.image_label.setAlignment(Qt.AlignCenter)

        self.name_label = QLabel("Created by: Talya Eitan")
        self.name_label.setAlignment(Qt.AlignCenter)
        
        self.email_label = QLabel("Email: talya1eitan@gmail.com")
        self.email_label.setAlignment(Qt.AlignCenter)
        
        self.linkedin_label = QLabel('<a href="https://www.linkedin.com/in/talya-eitan-112372229/">LinkedIn</a>')
        self.linkedin_label.setAlignment(Qt.AlignCenter)
        self.linkedin_label.setOpenExternalLinks(True)

        self.github_label = QLabel('<a href="https://github.com/talyaeitan/ice-cream.git">Github repository</a>')
        self.github_label.setAlignment(Qt.AlignCenter)
        self.github_label.setOpenExternalLinks(True)

        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.image_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.email_label)
        layout.addWidget(self.linkedin_label)
        layout.addWidget(self.github_label)
        layout.addStretch()
        layout.addWidget(self.close_button)

        self.setLayout(layout)

    def close_clicked(self):
        self.hide()