import sys
from PyQt6.QtWidgets import QApplication, QTextEdit, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

from constants import *


def load_from_txt(path: str)  -> str:
    """загрузка текста из файла"""
    with open(path, 'r', encoding="utf-8") as file:
        text = file.read()

    return text


def decode_text(text:str, alphabet: str, key: str) -> str:
    return ''


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Декодирование частотным анализем")
        self.setFixedWidth(600)

        # Лейблы (просто надписи)
        self.enc_label = QLabel("Кодированный текст:")
        self.alph_label = QLabel("Алфавит")
        self.key_label = QLabel("Ключ")
        self.result_label = QLabel("Результат:")

        # окна с текстом
        self.enc_txt = QTextEdit()
        self.enc_txt.setText(load_from_txt(TEXT_PATH))

        self.alphabet = QTextEdit()
        self.alphabet.setFixedHeight(35)

        self.key = QTextEdit()
        self.key.setFixedHeight(35)

        self.result = QTextEdit()
        self.result.setReadOnly(True)

        # кнопка
        self.stat_button = QPushButton("Статистика текста")
        self.stat_button.clicked.connect(self.stat)
        self.decode_button = QPushButton("Декодировать по алфавиту и ключу")
        self.decode_button.clicked.connect(self.decode)

        # собираем все виджеты в окно приложения
        layout = QVBoxLayout()
        layout.addWidget(self.enc_label)
        layout.addWidget(self.enc_txt)
        layout.addWidget(self.alph_label)
        layout.addWidget(self.alphabet)
        layout.addWidget(self.key_label)
        layout.addWidget(self.key)

        layout.addWidget(self.stat_button)
        layout.addWidget(self.decode_button)

        layout.addWidget(self.result_label)
        layout.addWidget(self.result)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def stat(self):
        print()


    def decode(self):
        alphabet = self.alphabet.toPlainText()
        key = self.key.toPlainText()
        text = self.enc_txt.toPlainText()

        decode_text = decode_text(text, alphabet, key)
        self.result.setText(decode_text)


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