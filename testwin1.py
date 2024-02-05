import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)
trayIcon = QSystemTrayIcon(QIcon('icon.png'), parent=app)
trayIcon.setToolTip('Проверка трей-иконки')
trayIcon.show()

menu = QMenu()
helpAction = menu.addAction('Помощь')
exitAction = menu.addAction('Выход')
exitAction.triggered.connect(app.quit)


trayIcon.setContextMenu(menu)

sys.exit(app.exec_())
