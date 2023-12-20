# hello.py

"""Simple Hello, World example with PyQt6."""

import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
# hello.py
# ...

# 2. Create an instance of QApplication
app = QApplication([])
# hello.py
# ...

# 3. Create your application's GUI
window = QWidget()
window.setWindowTitle("BHAGYASHREE APP")
window.setGeometry(200, 200, 580, 580)
helloMsg = QLabel("<h1>WELCOME, TO BTECH!</h1>", parent=window)
helloMsg.move(100, 100)
# hello.py
# ...

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec())
