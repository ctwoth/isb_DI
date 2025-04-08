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
    """
    Проходимся по тексту.
    Встречая русский строчный/заглавный символ, складываем его номер в алфавите с соответствующим
    номером символа алфавита ключа.

    Достигая конца ключа, начинаем по нему проход сначала.
    """
    key_len = len(key)
    t_list = list(text)
    cur = 0

    for i in range(len(t_list)):
        if (t_list[i] >= 'а') and (t_list[i] <= 'я'):
            int_txt = ord(t_list[i]) - ord('а') # достаём индекс буквы в алфавите
            int_key = ord(key[cur]) - ord('А')

            t_list[i] = chr(ord('а') + (int_txt + int_key + 1) % 32) # складываем индексы

            cur = (cur + 1) % key_len

        elif (t_list[i] >= 'А') and (t_list[i] <= 'Я'):
            int_txt = ord(t_list[i]) - ord('А') # достаём индекс буквы в алфавите
            int_key = ord(key[cur]) - ord('А')
            t_list[i] = chr(ord('А') + (int_txt + int_key + 1) % 32)

            cur = (cur + 1) % key_len

    return ''.join(t_list)


def decode_text(text: str, key: str) -> str:
    """
    Проходимся по тексту.
    Встречая русский строчный/заглавный символ, вычитаем из его номера в алфавите соответствующий
    номер символа алфавита ключа.

    Достигая конца ключа, начинаем по нему проход сначала.
    """
    key_len = len(key)
    t_list = list(text)
    cur = 0

    for i in range(len(t_list)):
        if (t_list[i] >= 'а') and (t_list[i] <= 'я'):
            int_txt = ord(t_list[i]) - ord('а')  # достаём индекс буквы в алфавите
            int_key = ord(key[cur]) - ord('А')

            t_list[i] = chr(ord('а') + (int_txt - int_key - 1) % 32)  # складываем индексы

            cur = (cur + 1) % key_len

        elif (t_list[i] >= 'А') and (t_list[i] <= 'Я'):
            int_txt = ord(t_list[i]) - ord('А')  # достаём индекс буквы в алфавите
            int_key = ord(key[cur]) - ord('А')
            t_list[i] = chr(ord('А') + (int_txt - int_key - 1) % 32)

            cur = (cur + 1) % key_len

    return ''.join(t_list)


def correct_key(key: str) -> str:
    '''возвращает строку только с русскими буквами'''
    cor_key = []
    for x in key:
        if (x >= 'А') and (x <= 'Я'):
            cor_key.append(x)

    return ''.join(cor_key)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Кодирование шифром \"Аббата Тритемиуса\"")
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
        """
        Проверяем ключ на корректность, если всё хорошо - вызываем функцию кодирования, иначе говорим о неправильном ключе.
        Если кодировка произошла результат выводим пользователю и загружаем в файл указанный в ENCODED_TEXT_PATH.
        """
        key = self.key_edit.toPlainText().upper()  # достаём из поля текст и делаем его заглавными буквами
        text = self.enc_txt.toPlainText()

        key = correct_key(key)
        if len(key) == 0:
            self.result.setText("некорректный ключ!")
            return

        encoded_text = encode_text(text, key)
        self.result.setText(encoded_text)

        load_to_txt(encoded_text, ENCODED_TEXT_PATH)


    def decode(self) -> None:
        """
        Проверяем ключ на корректность, если всё хорошо - вызываем функцию кодирования, иначе говорим о неправильном ключе.
        Если кодировка произошла результат выводим пользователю.
        """
        key = self.key_edit.toPlainText().upper()  # достаём из поля текст и делаем его заглавными буквами
        text = self.enc_txt.toPlainText()

        key = correct_key(key)
        if len(key) == 0:
            self.result.setText("некорректный ключ!")
            return

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