import matplotlib
from PyQt5 import QtCore, QtGui, QtWidgets
matplotlib.use('Qt5Agg')


class Ui_MainWindow(object):

    def __init__(self):
        self.sc = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 650)
        MainWindow.setMinimumSize(QtCore.QSize(750, 650))
        MainWindow.setStyleSheet("background-color:rgb(22, 35, 51)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.paginador = QtWidgets.QStackedWidget(self.centralwidget)
        self.paginador.setObjectName("paginador")
        self.inicio = QtWidgets.QWidget()
        self.inicio.setObjectName("inicio")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.inicio)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cont_inicio = QtWidgets.QFrame(self.inicio)
        self.cont_inicio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cont_inicio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cont_inicio.setObjectName("cont_inicio")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.cont_inicio)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titulo_inicio = QtWidgets.QLabel(self.cont_inicio)
        self.titulo_inicio.setMinimumSize(QtCore.QSize(660, 60))
        self.titulo_inicio.setMaximumSize(QtCore.QSize(16777215, 80))
        self.titulo_inicio.setStyleSheet("QLabel{\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "font-weight: bold;\n"
                                         "font-size: 22px;\n"
                                         "}")
        self.titulo_inicio.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.titulo_inicio.setObjectName("titulo_inicio")
        self.verticalLayout_2.addWidget(self.titulo_inicio)
        self.cont_ini_buts = QtWidgets.QFrame(self.cont_inicio)
        self.cont_ini_buts.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cont_ini_buts.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cont_ini_buts.setObjectName("cont_ini_buts")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.cont_ini_buts)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ini_polo_liso = QtWidgets.QToolButton(self.cont_ini_buts)
        self.ini_polo_liso.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ini_polo_liso.setFont(font)
        self.ini_polo_liso.setStyleSheet("QToolButton{\n"
                                         "background-color: rgb(194, 221, 245);\n"
                                         "border-radius: 15px;\n"
                                         "border-style: solid;\n"
                                         "border-width: 2px;\n"
                                         "border-color: black;\n"
                                         "padding: 10px;\n"
                                         "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/Polo liso.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ini_polo_liso.setIcon(icon)
        self.ini_polo_liso.setIconSize(QtCore.QSize(200, 200))
        self.ini_polo_liso.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ini_polo_liso.setObjectName("ini_polo_liso")
        self.horizontalLayout.addWidget(self.ini_polo_liso)
        self.ini_polo_saliente = QtWidgets.QToolButton(self.cont_ini_buts)
        self.ini_polo_saliente.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ini_polo_saliente.setFont(font)
        self.ini_polo_saliente.setStyleSheet("QToolButton{\n"
                                             "background-color: rgb(194, 221, 245);\n"
                                             "border-radius: 15px;\n"
                                             "border-style: solid;\n"
                                             "border-width: 2px;\n"
                                             "border-color: black;\n"
                                             "padding: 10px;\n"
                                             "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./img/Polo saliente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ini_polo_saliente.setIcon(icon1)
        self.ini_polo_saliente.setIconSize(QtCore.QSize(200, 200))
        self.ini_polo_saliente.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ini_polo_saliente.setObjectName("ini_polo_saliente")
        self.horizontalLayout.addWidget(self.ini_polo_saliente)
        self.verticalLayout_2.addWidget(self.cont_ini_buts)
        self.verticalLayout.addWidget(self.cont_inicio)
        self.paginador.addWidget(self.inicio)
        self.polo_liso = QtWidgets.QWidget()
        self.polo_liso.setObjectName("polo_liso")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.polo_liso)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cont_liso = QtWidgets.QFrame(self.polo_liso)
        self.cont_liso.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cont_liso.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cont_liso.setObjectName("cont_liso")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.cont_liso)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.liso_titulo_1 = QtWidgets.QLabel(self.cont_liso)
        self.liso_titulo_1.setMinimumSize(QtCore.QSize(0, 30))
        self.liso_titulo_1.setMaximumSize(QtCore.QSize(16777215, 60))
        self.liso_titulo_1.setStyleSheet("QLabel{\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "font-weight: bold;\n"
                                         "font-size: 24px;\n"
                                         "}")
        self.liso_titulo_1.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.liso_titulo_1.setObjectName("liso_titulo_1")
        self.verticalLayout_5.addWidget(self.liso_titulo_1)
        self.liso_titulo_2 = QtWidgets.QLabel(self.cont_liso)
        self.liso_titulo_2.setMinimumSize(QtCore.QSize(0, 30))
        self.liso_titulo_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.liso_titulo_2.setStyleSheet("QLabel{\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "font-size: 16px;\n"
                                         "}")
        self.liso_titulo_2.setAlignment(QtCore.Qt.AlignCenter)
        self.liso_titulo_2.setObjectName("liso_titulo_2")
        self.verticalLayout_5.addWidget(self.liso_titulo_2)
        self.liso_inputs = QtWidgets.QFrame(self.cont_liso)
        self.liso_inputs.setStyleSheet("")
        self.liso_inputs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.liso_inputs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.liso_inputs.setObjectName("liso_inputs")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.liso_inputs)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.liso_input_content = QtWidgets.QFrame(self.liso_inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liso_input_content.sizePolicy().hasHeightForWidth())
        self.liso_input_content.setSizePolicy(sizePolicy)
        self.liso_input_content.setMinimumSize(QtCore.QSize(700, 350))
        self.liso_input_content.setMaximumSize(QtCore.QSize(900, 420))
        self.liso_input_content.setStyleSheet("QFrame{\n"
                                              "background-color: rgb(217, 217, 217);\n"
                                              "border-radius: 10px;\n"
                                              "border-style: solid;\n"
                                              "border-color: black;\n"
                                              "border-width: 2px;\n"
                                              "}")
        self.liso_input_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.liso_input_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.liso_input_content.setObjectName("liso_input_content")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.liso_input_content)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.input_left = QtWidgets.QFrame(self.liso_input_content)
        self.input_left.setStyleSheet("QFrame{\n"
                                      "background-color: rgb(217, 217, 217);\n"
                                      "border-style: none;\n"
                                      "}")
        self.input_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_left.setObjectName("input_left")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.input_left)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_19 = QtWidgets.QFrame(self.input_left)
        self.frame_19.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.liso_p_aparente = QtWidgets.QLineEdit(self.frame_19)
        self.liso_p_aparente.setMaximumSize(QtCore.QSize(100, 16777215))
        self.liso_p_aparente.setStyleSheet("QLineEdit{\n"
                                           "background-color: rgb(243, 238, 238);\n"
                                           "border-radius: 2px;\n"
                                           "border: 1px solid gray;\n"
                                           "}")
        self.liso_p_aparente.setObjectName("liso_p_aparente")
        self.horizontalLayout_11.addWidget(self.liso_p_aparente)
        self.liso_p_aparente_label = QtWidgets.QLabel(self.frame_19)
        self.liso_p_aparente_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.liso_p_aparente_label.setStyleSheet("QLabel{\n"
                                                 "color: rgb(53, 53, 53);\n"
                                                 "font-weight: bold;\n"
                                                 "font-size: 14px;\n"
                                                 "}")
        self.liso_p_aparente_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.liso_p_aparente_label.setObjectName("liso_p_aparente_label")
        self.horizontalLayout_11.addWidget(self.liso_p_aparente_label)
        self.verticalLayout_10.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.input_left)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.liso_f_p = QtWidgets.QLineEdit(self.frame_20)
        self.liso_f_p.setMaximumSize(QtCore.QSize(100, 16777215))
        self.liso_f_p.setStyleSheet("QLineEdit{\n"
                                    "background-color: rgb(243, 238, 238);\n"
                                    "border-radius: 2px;\n"
                                    "border: 1px solid gray;\n"
                                    "}")
        self.liso_f_p.setObjectName("liso_f_p")
        self.horizontalLayout_12.addWidget(self.liso_f_p)
        self.liso_f_p_label = QtWidgets.QLabel(self.frame_20)
        self.liso_f_p_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.liso_f_p_label.setStyleSheet("QLabel{\n"
                                          "color: rgb(53, 53, 53);\n"
                                          "font-weight: bold;\n"
                                          "font-size: 14px;\n"
                                          "}")
        self.liso_f_p_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.liso_f_p_label.setObjectName("liso_f_p_label")
        self.horizontalLayout_12.addWidget(self.liso_f_p_label)
        self.verticalLayout_10.addWidget(self.frame_20)
        self.frame_21 = QtWidgets.QFrame(self.input_left)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.liso_t_m_c = QtWidgets.QLineEdit(self.frame_21)
        self.liso_t_m_c.setMaximumSize(QtCore.QSize(100, 16777215))
        self.liso_t_m_c.setStyleSheet("QLineEdit{\n"
                                      "background-color: rgb(243, 238, 238);\n"
                                      "border-radius: 2px;\n"
                                      "border: 1px solid gray;\n"
                                      "}")
        self.liso_t_m_c.setObjectName("liso_t_m_c")
        self.horizontalLayout_13.addWidget(self.liso_t_m_c)
        self.liso_t_m_c_label = QtWidgets.QLabel(self.frame_21)
        self.liso_t_m_c_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.liso_t_m_c_label.setStyleSheet("QLabel{\n"
                                            "color: rgb(53, 53, 53);\n"
                                            "font-weight: bold;\n"
                                            "font-size: 14px;\n"
                                            "}")
        self.liso_t_m_c_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.liso_t_m_c_label.setObjectName("liso_t_m_c_label")
        self.horizontalLayout_13.addWidget(self.liso_t_m_c_label)
        self.verticalLayout_10.addWidget(self.frame_21)
        self.frame_23 = QtWidgets.QFrame(self.input_left)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.liso_estabilidad_practica = QtWidgets.QLineEdit(self.frame_23)
        self.liso_estabilidad_practica.setMaximumSize(QtCore.QSize(100, 16777215))
        self.liso_estabilidad_practica.setStyleSheet("QLineEdit{\n"
                                                     "background-color: rgb(243, 238, 238);\n"
                                                     "border-radius: 2px;\n"
                                                     "border: 1px solid gray;\n"
                                                     "}")
        self.liso_estabilidad_practica.setObjectName("liso_estabilidad_practica")
        self.horizontalLayout_14.addWidget(self.liso_estabilidad_practica)
        self.liso_estabilidad_practica_label = QtWidgets.QLabel(self.frame_23)
        self.liso_estabilidad_practica_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.liso_estabilidad_practica_label.setStyleSheet("QLabel{\n"
                                                           "color: rgb(53, 53, 53);\n"
                                                           "font-weight: bold;\n"
                                                           "font-size: 14px;\n"
                                                           "}")
        self.liso_estabilidad_practica_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.liso_estabilidad_practica_label.setObjectName("liso_estabilidad_practica_label")
        self.horizontalLayout_14.addWidget(self.liso_estabilidad_practica_label)
        self.verticalLayout_10.addWidget(self.frame_23)
        self.frame_22 = QtWidgets.QFrame(self.input_left)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_10.addWidget(self.frame_22)
        self.horizontalLayout_5.addWidget(self.input_left)
        self.input_right = QtWidgets.QFrame(self.liso_input_content)
        self.input_right.setStyleSheet("QFrame{\n"
                                       "background-color: rgb(217, 217, 217);\n"
                                       "border-style: none;\n"
                                       "}")
        self.input_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_right.setObjectName("input_right")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.input_right)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.cont_voltaje_nom = QtWidgets.QFrame(self.input_right)
        self.cont_voltaje_nom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cont_voltaje_nom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cont_voltaje_nom.setObjectName("cont_voltaje_nom")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.cont_voltaje_nom)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.voltaje_nominal = QtWidgets.QComboBox(self.cont_voltaje_nom)
        self.voltaje_nominal.setMinimumSize(QtCore.QSize(101, 0))
        self.voltaje_nominal.setMaximumSize(QtCore.QSize(100, 16777215))
        self.voltaje_nominal.setStyleSheet("QComboBox{\n"
                                           "background-color: rgb(243, 238, 238);\n"
                                           "border: 1px solid gray;\n"
                                           "border-radius: 3px;\n"
                                           "padding: 1px 18px 1px 3px;\n"
                                           "min-width: 6em;\n"
                                           "}\n"
                                           "QComboBox:editable {\n"
                                           "    background: white;\n"
                                           "}\n"
                                           "QScrollBar:vertical {          \n"
                                           "    border: none;\n"
                                           "    background: rgb(44, 71, 103);\n"
                                           "    width:10px;\n"
                                           "    border-radius: 2px;\n"
                                           "}")
        self.voltaje_nominal.setObjectName("voltaje_nominal")
        self.voltaje_nominal.addItem("")
        self.voltaje_nominal.addItem("")
        self.voltaje_nominal.addItem("")
        self.voltaje_nominal.addItem("")
        self.voltaje_nominal.addItem("")
        self.voltaje_nominal.addItem("")
        self.voltaje_nominal.addItem("")
        self.voltaje_nominal.addItem("")
        self.voltaje_nominal.addItem("")
        self.voltaje_nominal.addItem("")
        self.voltaje_nominal.addItem("")
        self.voltaje_nominal.addItem("")
        self.horizontalLayout_6.addWidget(self.voltaje_nominal)
        self.liso_v_n_label = QtWidgets.QLabel(self.cont_voltaje_nom)
        self.liso_v_n_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.liso_v_n_label.setStyleSheet("QLabel{\n"
                                          "color: rgb(53, 53, 53);\n"
                                          "font-weight: bold;\n"
                                          "font-size: 14px;\n"
                                          "}")
        self.liso_v_n_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.liso_v_n_label.setObjectName("liso_v_n_label")
        self.horizontalLayout_6.addWidget(self.liso_v_n_label)
        self.verticalLayout_9.addWidget(self.cont_voltaje_nom)
        self.cont_r_s = QtWidgets.QFrame(self.input_right)
        self.cont_r_s.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cont_r_s.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cont_r_s.setObjectName("cont_r_s")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.cont_r_s)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.liso_r_s = QtWidgets.QLineEdit(self.cont_r_s)
        self.liso_r_s.setMaximumSize(QtCore.QSize(100, 16777215))
        self.liso_r_s.setStyleSheet("QLineEdit{\n"
                                    "background-color: rgb(243, 238, 238);\n"
                                    "border-radius: 2px;\n"
                                    "border: 1px solid gray;\n"
                                    "}")
        self.liso_r_s.setObjectName("liso_r_s")
        self.horizontalLayout_7.addWidget(self.liso_r_s)
        self.liso_r_s_label = QtWidgets.QLabel(self.cont_r_s)
        self.liso_r_s_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.liso_r_s_label.setStyleSheet("QLabel{\n"
                                          "color: rgb(53, 53, 53);\n"
                                          "font-weight: bold;\n"
                                          "font-size: 14px;\n"
                                          "}")
        self.liso_r_s_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.liso_r_s_label.setObjectName("liso_r_s_label")
        self.horizontalLayout_7.addWidget(self.liso_r_s_label)
        self.verticalLayout_9.addWidget(self.cont_r_s)
        self.cont_p_m = QtWidgets.QFrame(self.input_right)
        self.cont_p_m.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cont_p_m.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cont_p_m.setObjectName("cont_p_m")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.cont_p_m)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.liso_p_m = QtWidgets.QLineEdit(self.cont_p_m)
        self.liso_p_m.setMaximumSize(QtCore.QSize(100, 16777215))
        self.liso_p_m.setStyleSheet("QLineEdit{\n"
                                    "background-color: rgb(243, 238, 238);\n"
                                    "border-radius: 2px;\n"
                                    "border: 1px solid gray;\n"
                                    "}")
        self.liso_p_m.setObjectName("liso_p_m")
        self.horizontalLayout_3.addWidget(self.liso_p_m)
        self.liso_p_m_label = QtWidgets.QLabel(self.cont_p_m)
        self.liso_p_m_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.liso_p_m_label.setStyleSheet("QLabel{\n"
                                          "color: rgb(53, 53, 53);\n"
                                          "font-weight: bold;\n"
                                          "font-size: 14px;\n"
                                          "}")
        self.liso_p_m_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.liso_p_m_label.setObjectName("liso_p_m_label")
        self.horizontalLayout_3.addWidget(self.liso_p_m_label)
        self.verticalLayout_9.addWidget(self.cont_p_m)
        self.cont_seg_max = QtWidgets.QFrame(self.input_right)
        self.cont_seg_max.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cont_seg_max.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cont_seg_max.setObjectName("cont_seg_max")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.cont_seg_max)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.liso_porcentaje_seg = QtWidgets.QComboBox(self.cont_seg_max)
        self.liso_porcentaje_seg.setMinimumSize(QtCore.QSize(101, 0))
        self.liso_porcentaje_seg.setMaximumSize(QtCore.QSize(100, 16777215))
        self.liso_porcentaje_seg.setStyleSheet("QComboBox{\n"
                                               "background-color: rgb(243, 238, 238);\n"
                                               "border: 1px solid gray;\n"
                                               "border-radius: 3px;\n"
                                               "padding: 1px 18px 1px 3px;\n"
                                               "min-width: 6em;\n"
                                               "}\n"
                                               "QComboBox:editable {\n"
                                               "    background: white;\n"
                                               "}")
        self.liso_porcentaje_seg.setObjectName("liso_porcentaje_seg")
        self.liso_porcentaje_seg.addItem("")
        self.liso_porcentaje_seg.addItem("")
        self.horizontalLayout_8.addWidget(self.liso_porcentaje_seg)
        self.liso_porcentaj_seg_label = QtWidgets.QLabel(self.cont_seg_max)
        self.liso_porcentaj_seg_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.liso_porcentaj_seg_label.setStyleSheet("QLabel{\n"
                                                    "color: rgb(53, 53, 53);\n"
                                                    "font-weight: bold;\n"
                                                    "font-size: 14px;\n"
                                                    "}")
        self.liso_porcentaj_seg_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.liso_porcentaj_seg_label.setObjectName("liso_porcentaj_seg_label")
        self.horizontalLayout_8.addWidget(self.liso_porcentaj_seg_label)
        self.verticalLayout_9.addWidget(self.cont_seg_max)
        self.cont_seg_min = QtWidgets.QFrame(self.input_right)
        self.cont_seg_min.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cont_seg_min.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cont_seg_min.setObjectName("cont_seg_min")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.cont_seg_min)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.liso_exitacion_min = QtWidgets.QComboBox(self.cont_seg_min)
        self.liso_exitacion_min.setMinimumSize(QtCore.QSize(101, 0))
        self.liso_exitacion_min.setMaximumSize(QtCore.QSize(100, 16777215))
        self.liso_exitacion_min.setStyleSheet("QComboBox{\n"
                                              "background-color: rgb(243, 238, 238);\n"
                                              "border: 1px solid gray;\n"
                                              "border-radius: 3px;\n"
                                              "padding: 1px 18px 1px 3px;\n"
                                              "min-width: 6em;\n"
                                              "}\n"
                                              "QComboBox:editable {\n"
                                              "    background: white;\n"
                                              "}")
        self.liso_exitacion_min.setObjectName("liso_exitacion_min")
        self.liso_exitacion_min.addItem("")
        self.horizontalLayout_9.addWidget(self.liso_exitacion_min)
        self.liso_exitacion_min_label = QtWidgets.QLabel(self.cont_seg_min)
        self.liso_exitacion_min_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.liso_exitacion_min_label.setStyleSheet("QLabel{\n"
                                                    "color: rgb(53, 53, 53);\n"
                                                    "font-weight: bold;\n"
                                                    "font-size: 14px;\n"
                                                    "}")
        self.liso_exitacion_min_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.liso_exitacion_min_label.setObjectName("liso_exitacion_min_label")
        self.horizontalLayout_9.addWidget(self.liso_exitacion_min_label)
        self.verticalLayout_9.addWidget(self.cont_seg_min)
        self.horizontalLayout_5.addWidget(self.input_right)
        self.horizontalLayout_4.addWidget(self.liso_input_content)
        self.verticalLayout_5.addWidget(self.liso_inputs)
        self.liso_campos = QtWidgets.QLabel(self.cont_liso)
        self.liso_campos.setMinimumSize(QtCore.QSize(0, 30))
        self.liso_campos.setMaximumSize(QtCore.QSize(16777215, 25))
        self.liso_campos.setStyleSheet("QLabel{\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font-size: 14px;\n"
                                       "}")
        self.liso_campos.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.liso_campos.setObjectName("liso_campos")
        self.verticalLayout_5.addWidget(self.liso_campos)
        self.liso_error_mess = QtWidgets.QLabel(self.cont_liso)
        self.liso_error_mess.setMinimumSize(QtCore.QSize(0, 30))
        self.liso_error_mess.setMaximumSize(QtCore.QSize(16777215, 25))
        self.liso_error_mess.setStyleSheet("QLabel{\n"
                                           "color: red;\n"
                                           "}")
        self.liso_error_mess.setAlignment(QtCore.Qt.AlignCenter)
        self.liso_error_mess.setObjectName("liso_error_mess")
        self.verticalLayout_5.addWidget(self.liso_error_mess)
        self.liso_content_but = QtWidgets.QFrame(self.cont_liso)
        self.liso_content_but.setMinimumSize(QtCore.QSize(0, 50))
        self.liso_content_but.setMaximumSize(QtCore.QSize(16777215, 50))
        self.liso_content_but.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.liso_content_but.setFrameShadow(QtWidgets.QFrame.Raised)
        self.liso_content_but.setObjectName("liso_content_but")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.liso_content_but)
        self.horizontalLayout_2.setContentsMargins(40, 0, 40, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.liso_graficar = QtWidgets.QPushButton(self.liso_content_but)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.liso_graficar.setFont(font)
        self.liso_graficar.setStyleSheet("QPushButton{\n"
                                         "background-color: rgb(194, 221, 245);\n"
                                         "border-radius: 5px;\n"
                                         "border-style: solid;\n"
                                         "border-width: 1px;\n"
                                         "border-color: black;\n"
                                         "padding: 5px;\n"
                                         "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./img/derecha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.liso_graficar.setIcon(icon2)
        self.liso_graficar.setIconSize(QtCore.QSize(14, 14))
        self.liso_graficar.setObjectName("liso_graficar")
        self.horizontalLayout_2.addWidget(self.liso_graficar)
        spacerItem = QtWidgets.QSpacerItem(470, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.liso_anterior = QtWidgets.QPushButton(self.liso_content_but)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.liso_anterior.setFont(font)
        self.liso_anterior.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.liso_anterior.setStyleSheet("QPushButton{\n"
                                         "background-color: rgb(194, 221, 245);\n"
                                         "border-radius: 5px;\n"
                                         "border-style: solid;\n"
                                         "border-width: 1px;\n"
                                         "border-color: black;\n"
                                         "padding: 5px;\n"
                                         "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./img/izquierda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.liso_anterior.setIcon(icon3)
        self.liso_anterior.setIconSize(QtCore.QSize(14, 14))
        self.liso_anterior.setObjectName("liso_anterior")
        self.horizontalLayout_2.addWidget(self.liso_anterior)
        self.verticalLayout_5.addWidget(self.liso_content_but)
        self.verticalLayout_4.addWidget(self.cont_liso)
        self.paginador.addWidget(self.polo_liso)
        self.curva = QtWidgets.QWidget()
        self.curva.setObjectName("curva")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.curva)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.curva_content = QtWidgets.QFrame(self.curva)
        self.curva_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.curva_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.curva_content.setObjectName("curva_content")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.curva_content)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.curva_content)
        self.label.setMaximumSize(QtCore.QSize(16777215, 80))
        self.label.setStyleSheet("QLabel{\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "font-weight: bold;\n"
                                 "font-size: 24px;\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.plot_content = QtWidgets.QFrame(self.curva_content)
        self.plot_content.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.plot_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plot_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plot_content.setObjectName("plot_content")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.plot_content)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.plot_canvas = QtWidgets.QWidget(self.plot_content)
        self.plot_canvas.setStyleSheet("QWidget{\n"
                                       "background-color: rgb(255, 255, 255);\n"
                                       "\n"
                                       "}")
        self.plot_canvas.setObjectName("plot_canvas")
        self.canvas_layout = QtWidgets.QVBoxLayout(self.plot_canvas)
        self.canvas_layout.setObjectName("canvas_layout")
        self.horizontalLayout_17.addWidget(self.plot_canvas)
        self.verticalLayout_3.addWidget(self.plot_content)
        self.curva_butt_content = QtWidgets.QFrame(self.curva_content)
        self.curva_butt_content.setMaximumSize(QtCore.QSize(16777215, 50))
        self.curva_butt_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.curva_butt_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.curva_butt_content.setObjectName("curva_butt_content")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.curva_butt_content)
        self.horizontalLayout_15.setContentsMargins(40, 0, 40, 5)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.inicio_plot = QtWidgets.QPushButton(self.curva_butt_content)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.inicio_plot.setFont(font)
        self.inicio_plot.setStyleSheet("QPushButton{\n"
                                       "background-color: rgb(194, 221, 245);\n"
                                       "border-radius: 5px;\n"
                                       "border-style: solid;\n"
                                       "border-width: 1px;\n"
                                       "border-color: black;\n"
                                       "padding: 5px;\n"
                                       "}")
        self.inicio_plot.setIcon(icon2)
        self.inicio_plot.setObjectName("inicio_plot")
        self.horizontalLayout_15.addWidget(self.inicio_plot)
        spacerItem1 = QtWidgets.QSpacerItem(489, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.anterior_plot = QtWidgets.QPushButton(self.curva_butt_content)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.anterior_plot.setFont(font)
        self.anterior_plot.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.anterior_plot.setStyleSheet("QPushButton{\n"
                                         "background-color: rgb(194, 221, 245);\n"
                                         "border-radius: 5px;\n"
                                         "border-style: solid;\n"
                                         "border-width: 1px;\n"
                                         "border-color: black;\n"
                                         "padding: 5px;\n"
                                         "}")
        self.anterior_plot.setIcon(icon3)
        self.anterior_plot.setIconSize(QtCore.QSize(14, 14))
        self.anterior_plot.setObjectName("anterior_plot")
        self.horizontalLayout_15.addWidget(self.anterior_plot)
        self.verticalLayout_3.addWidget(self.curva_butt_content)
        self.verticalLayout_6.addWidget(self.curva_content)
        self.paginador.addWidget(self.curva)
        self.horizontalLayout_10.addWidget(self.paginador)

        """
        # Accesibilidad de los botones
        self.paginador.setCurrentWidget(self.inicio)
        # Ir hacia la página para ingresar los datos de un generador de polos lisos
        self.ini_polo_liso.clicked.connect(lambda: self.paginador.setCurrentWidget(self.polo_liso))
        # Regresar desde la página de polos lisos a la página de inicio
        self.liso_anterior.clicked.connect(lambda: self.paginador.setCurrentWidget(self.inicio))
        # Ir hacia la vista para graficar desde los datos de un generador de polos lisos
        self.liso_graficar.clicked.connect(self.mirar)
        # Ir hacia el inicio desde la vista para graficar
        self.inicio_plot.clicked.connect(lambda: self.paginador.setCurrentWidget(self.inicio))
        # Ir hacia la vista de parámetros de polos lisos desde la vista para graficar
        self.anterior_plot.clicked.connect(lambda: self.paginador.setCurrentWidget(self.polo_liso))
        """

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.paginador.setCurrentWidget(self.inicio)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    """
    def mirar(self):
        self.canvas_layout.removeWidget(self.sc)
        self.sc = MyStaticMplCanvas(self.plot_canvas, width=5, height=4, dpi=100)
        self.canvas_layout.addWidget(self.sc)
        self.paginador.setCurrentWidget(self.curva)
    """

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo_inicio.setText(
            _translate("MainWindow", "Graficar curva de capacidad - Seleccione el tipo de generador"))
        self.ini_polo_liso.setText(_translate("MainWindow", "Polos lisos"))
        self.ini_polo_saliente.setText(_translate("MainWindow", "Polos salientes"))
        self.liso_titulo_1.setText(_translate("MainWindow", "Graficar curva de capacidad "))
        self.liso_titulo_2.setText(_translate("MainWindow", "Ingrese datos para un generador de polos lisos"))
        self.liso_p_aparente_label.setText(_translate("MainWindow", "Potencia aparente**"))
        self.liso_f_p_label.setText(_translate("MainWindow", "Factor de potencia**"))
        self.liso_t_m_c_label.setText(_translate("MainWindow", "Tensión de campo máxima"))
        self.liso_estabilidad_practica_label.setText(_translate("MainWindow", "Estabilidad práctica**"))
        self.voltaje_nominal.setItemText(0, _translate("MainWindow", "240"))
        self.voltaje_nominal.setItemText(1, _translate("MainWindow", "480"))
        self.voltaje_nominal.setItemText(2, _translate("MainWindow", "600"))
        self.voltaje_nominal.setItemText(3, _translate("MainWindow", "2400"))
        self.voltaje_nominal.setItemText(4, _translate("MainWindow", "4160"))
        self.voltaje_nominal.setItemText(5, _translate("MainWindow", "4800"))
        self.voltaje_nominal.setItemText(6, _translate("MainWindow", "6900"))
        self.voltaje_nominal.setItemText(7, _translate("MainWindow", "13800"))
        self.voltaje_nominal.setItemText(8, _translate("MainWindow", "23000"))
        self.voltaje_nominal.setItemText(9, _translate("MainWindow", "34500"))
        self.voltaje_nominal.setItemText(10, _translate("MainWindow", "46000"))
        self.voltaje_nominal.setItemText(11, _translate("MainWindow", "69000"))
        self.liso_v_n_label.setText(_translate("MainWindow", "Voltaje nominal**"))
        self.liso_r_s_label.setText(_translate("MainWindow", "Reactancia sincrónica**"))
        self.liso_p_m_label.setText(_translate("MainWindow", "Potencia motriz máxima"))
        self.liso_porcentaje_seg.setItemText(0, _translate("MainWindow", "10"))
        self.liso_porcentaje_seg.setItemText(1, _translate("MainWindow", "15"))
        self.liso_porcentaj_seg_label.setText(_translate("MainWindow", "Porcentaje de seguridad**"))
        self.liso_exitacion_min.setItemText(0, _translate("MainWindow", "0"))
        self.liso_exitacion_min_label.setText(_translate("MainWindow", "Exitación mínima**"))
        self.liso_campos.setText(_translate("MainWindow", "Los campos indicados con ** son obligatorios."))
        self.liso_error_mess.setText(_translate("MainWindow", "Hola"))
        self.liso_graficar.setText(_translate("MainWindow", "Graficar"))
        self.liso_anterior.setText(_translate("MainWindow", "Anterior"))
        self.label.setText(_translate("MainWindow", "Graficar curva de capacidad - Generador de polos lisos "))
        self.inicio_plot.setText(_translate("MainWindow", "Inicio"))
        self.anterior_plot.setText(_translate("MainWindow", "Anterior"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
