import asyncio

from PyQt5 import QtWidgets
from main_ui import *
import sys

def main():
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        ui = Ui_MainWindow()
        ui.show()
        sys.exit(app.exec_())
main()
# if __name__ == "__main__":
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(main())
#     loop.close()

# group not in list
# delete all accoutns from flood