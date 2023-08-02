import sys
import subprocess
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit

class App(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QTextEdit widget to display the output
        self.text_edit = QTextEdit(self)

        # Add the widget to the layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

        # Start the terminal command
        process = subprocess.Popen(["python", "detect2.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        output = stdout.decode('utf-8') + stderr.decode('utf-8')
        self.text_edit.setPlainText(output)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
