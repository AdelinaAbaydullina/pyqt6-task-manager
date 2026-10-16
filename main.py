import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QRadioButton, QCheckBox, QTextEdit, QPushButton,
    QVBoxLayout, QHBoxLayout
)

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Task Manager")
window.resize(600, 700)

central_widget = QWidget()
window.setCentralWidget(central_widget)

layout = QVBoxLayout()
central_widget.setLayout(layout)

layout.addWidget(QLabel("Create task"))

layout.addWidget(QLabel("Task:"))
task_name = QLineEdit()
layout.addWidget(task_name)

layout.addWidget(QLabel("Description:"))
description = QTextEdit()
layout.addWidget(description)

layout.addWidget(QLabel("Priority:"))

row = QHBoxLayout()
low = QRadioButton("Low")
medium = QRadioButton("Medium")
high = QRadioButton("High")
medium.setChecked(True)

row.addWidget(low)
row.addWidget(medium)
row.addWidget(high)
layout.addLayout(row)

important = QCheckBox("Important")
notification = QCheckBox("Send notification")
layout.addWidget(important)
layout.addWidget(notification)

def create_task():
    if not task_name.text().strip():
        result.setPlainText("Please enter a task name.")
        return

    if low.isChecked():
        priority = "Low"
    elif high.isChecked():
        priority = "High"
    else:
        priority = "Medium"

    text = (
        f"Task: {task_name.text()}\n"
        f"Priority: {priority}\n"
        f"Important: {important.isChecked()}\n"
        f"Send notification: {notification.isChecked()}\n\n"
        f"Description:\n{description.toPlainText()}"
    )

    result.setPlainText(text)
    status.setText("Status: Task created")
    print(text)

button = QPushButton("Create task")
button.clicked.connect(create_task)
layout.addWidget(button)

layout.addWidget(QLabel("Result:"))
result = QTextEdit()
result.setReadOnly(True)
layout.addWidget(result)

def clear_form():
    task_name.clear()
    description.clear()
    medium.setChecked(True)
    important.setChecked(False)
    notification.setChecked(False)
    result.clear()
    status.setText("Status: Ready")

clear_button = QPushButton("Clear")
clear_button.clicked.connect(clear_form)
layout.addWidget(clear_button)

status = QLabel("Status: Ready")
layout.addWidget(status)

window.show()
sys.exit(app.exec())