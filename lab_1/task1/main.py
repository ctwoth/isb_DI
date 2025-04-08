import sys
from PyQt6.QtWidgets import QApplication, QTextEdit, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

from constants import *


def load_from_txt(path: str)  -> str:
    """загрузка текста из файла"""
    with open(path, 'r', encoding="utf-8") as file:
        text = file.read()

    return text


def load_to_txt(text: str, path: str) -> None:
    """загрузка текста в файл"""
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)


def encode_text(text: str, key: str) -> str:
    return ''


def decode_text(text: str, key: str) -> str:
    return ''


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
        self.enc_txt.setText(load_from_txt(TEXT_PATH))

        self.result = QTextEdit()
        self.result.setReadOnly(True)

        self.key_edit = QTextEdit()
        self.key_edit.setText(load_from_txt(KEY_PATH))
        self.key_edit.setFixedHeight(35)

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
        key = self.key_edit.toPlainText().upper()  # достаём из поля текст и делаем его заглавными буквами
        text = self.enc_txt.toPlainText()

        encoded_text = encode_text(text, key)
        self.result.setText(encoded_text)

        load_to_txt(encoded_text, ENCODED_TEXT_PATH)


    def decode(self) -> None:
        key = self.key_edit.toPlainText().upper()  # достаём из поля текст и делаем его заглавными буквами
        text = self.enc_txt.toPlainText()

        decoded_text = decode_text(text, key)
        self.result.setText(decoded_text)


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