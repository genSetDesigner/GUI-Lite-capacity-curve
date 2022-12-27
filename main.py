import sys
from gui_main import *

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainGUIApp()
    main.show()
    sys.exit(app.exec_())
