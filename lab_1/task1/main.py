import sys
from PyQt6.QtWidgets import QApplication, QTextEdit, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

from constants import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Кодирование шифром \"по книге\"")
        self.setFixedWidth(600)

        # Лейблы (просто надписи)
        self.enc_label = QLabel("Текст:")
        self.keyword_label = QLabel("Ключ:")
        self.result_label = QLabel("Результат:")

        # окна с текстом
        self.enc_txt = QTextEdit()

        self.result = QTextEdit()
        self.result.setReadOnly(True)

        self.key_edit = QTextEdit()
        self.key_edit.setFixedHeight(35) #

        # кнопки
        self.encode_button = QPushButton("Кодировать")
        self.encode_button.clicked.connect(self.encode)
        self.decode_button = QPushButton("Декодировать")
        self.decode_button.clicked.connect(self.decode)

        # собираем все виджеты в окно приложения
        layout = QVBoxLayout()
        layout.addWidget(self.enc_label)
        layout.addWidget(self.enc_txt)
        layout.addWidget(self.keyword_label)
        layout.addWidget(self.key_edit)
        layout.addWidget(self.encode_button)
        layout.addWidget(self.decode_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def encode(self) -> None:
        print()

    def decode(self) -> None:
        print()


def main():
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()