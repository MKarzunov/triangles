from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class MainWindowClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("main_window")
        self.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        self.sides = ('a', 'b', 'c')

        self.font = QtGui.QFont()
        self.font.setPointSize(12)

        self.add_label('main_label', 'Введите длины сторон треугольника')

        for side_name in self.sides:
            self.add_label(f'side_{side_name}_label', f'Сторона {side_name.upper()}')
            self.add_input(f'side_{side_name}_input')

        self.add_button('commit_button', 'Проверить')

        self.commit_button.clicked.connect(self.check_triangle)

    def add_label(self, label_name: str = 'label', label_text: str = ''):
        label = QtWidgets.QLabel(self)
        label.setFont(self.font)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName(label_name)
        label.setText(label_text)
        setattr(self, label_name, label)
        self.verticalLayout.addWidget(label)

    def add_input(self, input_name: str = 'line_input'):
        line_input = QtWidgets.QLineEdit(self)
        line_input.setFont(self.font)
        line_input.setAlignment(QtCore.Qt.AlignCenter)
        line_input.setObjectName(input_name)
        setattr(self, input_name, line_input)
        self.verticalLayout.addWidget(line_input)

    def add_button(self, button_name: str = 'button', button_text: str = ''):
        button = QtWidgets.QPushButton(self)
        button.setFont(self.font)
        button.setObjectName("commit_button")
        button.setText(button_text)
        setattr(self, button_name, button)
        self.verticalLayout.addWidget(button)

    def check_triangle(self):
        values = [getattr(self, f"side_{side}_input").text().strip() for side in self.sides]
        test_set = set()
        for value in values:
            if value == '':
                result = "Одно или несколько полей остались незаполненными"
                break
            if not value.isdigit() or value == '0':
                result = "В поля допускается вводить только строго положительные целые числа"
                break
            test_set.add(int(value))
        else:
            if len(test_set) == 1:
                result = "Треугольник равносторонний"
            elif len(test_set) == 2:
                if 2 * min(test_set) <= max(test_set):
                    result = "Треугольник с заданными сторонами не существует"
                else:
                    result = "Треугольник равнобедренный"
            else:
                test_list_sorted = sorted(test_set)
                if test_list_sorted[0] + test_list_sorted[1] <= test_list_sorted[2]:
                    result = "Треугольник с заданными сторонами не существует"
                else:
                    result = "Треугольник разносторонний"
        msg = QtWidgets.QMessageBox(text=result)
        msg.setWindowTitle("Результат")
        msg.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindowClass()
    main_window.setWindowTitle("Треугольники")
    main_window.show()
    sys.exit(app.exec_())
