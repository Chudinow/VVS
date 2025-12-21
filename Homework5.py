import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QScrollBar, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt


class SEOAnalyzerWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()

    def setup_ui(self) -> None:
        self.setWindowTitle("SEO анализ")

        layout = QVBoxLayout(self)
        layout.setSpacing(10)


        text = QTextEdit()
        text.setFixedHeight(120)
        text.setPlaceholderText("Введите текст для анализа...")

        scroll = QScrollBar(Qt.Orientation.Vertical)
        scroll.setFixedHeight(120)

        top_layout = QHBoxLayout()
        top_layout.addWidget(text)
        top_layout.addWidget(scroll)
        layout.addLayout(top_layout)


        button = QPushButton("Анализ")
        layout.addWidget(button)


        self.result_label = QLabel("")
        layout.addWidget(self.result_label)


        button.clicked.connect(self.on_analyze_clicked)

    def on_analyze_clicked(self) -> None:
        self.result_label.setText("Результат: SEO анализ текста")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SEOAnalyzerWindow()
    window.show()
    sys.exit(app.exec())
