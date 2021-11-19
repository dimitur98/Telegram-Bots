import asyncio

from PyQt5 import QtWidgets
from main_ui import *
import sys

def main():
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.setMaximumSize(940,700)
        MainWindow.show()
        sys.exit(app.exec_())
# main()
if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)    
    loop.run_until_complete(main())
    loop.close()