import asyncio

from PyQt5 import QtWidgets
from main_ui import *
import sys

def main():
    try:
        if __name__ == "__main__":
            app = QtWidgets.QApplication(sys.argv)
            ui = Ui_MainWindow()
            ui.show()
            sys.exit(app.exec_())
    except Error as e:
         result = QMessageBox.question(app,
                      "Error occured!",
                      e,
                      QMessageBox.Ok)

         if result == QMessageBox.Ok:
            ui.hide()
# main()
if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.close()

# group not in list
# delete all accoutns from flood