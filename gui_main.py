import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from layer_pu import *
from concurrent.futures import ThreadPoolExecutor
from graficar import crear, crearpolosaliente

matplotlib.use('Qt5Agg')
global text_progress
global bar


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=15, height=10, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class MainGUIApp(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Parámetros indispensables para comunicar la GUI con el resto de la aplicación
        self._liso_param = {}
        self._saliente_param = {}

        # Pool de threads para el manejo de procesos paralelos
        self.pool = ThreadPoolExecutor(max_workers=2)

        # Preparación del área de dibujo
        self.w_canvas = self.ui.plot_canvas
        self.c_layout = self.ui.canvas_layout
        self.static_graph = None

        # Preparación de la barra de progreso
        global bar
        bar = self.ui.barra_espera
        global text_progress
        text_progress = self.ui.mensaje_progreso
        bar.setMinimum(0)
        bar.setMaximum(100)

        # Accesibilidad de los botones
        self.ui.paginador.setCurrentWidget(self.ui.inicio)
        # Ir hacia la página para ingresar los datos de un generador de polos lisos
        self.ui.ini_polo_liso.clicked.connect(lambda: self.ui.paginador.setCurrentWidget(self.ui.polo_liso))
        # Regresar desde la página de polos lisos a la página de inicio
        self.ui.liso_anterior.clicked.connect(lambda: self.ui.paginador.setCurrentWidget(self.ui.inicio))
        # Ir hacia la vista para graficar desde los datos de un generador de polos lisos
        self.ui.liso_graficar.clicked.connect(self.comprobar_liso)
        # Ir hacia el inicio desde la vista para graficar
        self.ui.inicio_plot.clicked.connect(lambda: self.ui.paginador.setCurrentWidget(self.ui.inicio))
        # Ir hacia la vista de parámetros de polos lisos desde la vista para graficar
        self.ui.anterior_plot.clicked.connect(self.atrasCanvas)

        # Ir hacia la página para ingresar los datos de un generador de polos salientes
        self.ui.ini_polo_saliente.clicked.connect(lambda: self.ui.paginador.setCurrentWidget(self.ui.polos_salientes))
        # Regresar desde la página de polos salientes a la página de inicio
        self.ui.saliente_anterior.clicked.connect(lambda: self.ui.paginador.setCurrentWidget(self.ui.inicio))
        # Ir hacia la vista para graficar desde los datos de un generador de polos salientes
        self.ui.saliente_graficar.clicked.connect(self.comprobar_saliente)
        # Valores en unidades o en PU
        self.liso_pu = False
        self.saliente_pu = False
        self.ui.saliente_pu_check.toggled.connect(self.onClicked)
        self.ui.liso_pu_check.toggled.connect(self.onClicked)

    def atrasCanvas(self):
        if self.ui.label.text() == "Graficar curva de capacidad - Generador de polos lisos ":
            self.ui.paginador.setCurrentWidget(self.ui.polo_liso)
        else:
            self.ui.paginador.setCurrentWidget(self.ui.polos_salientes)

    # Función para el manejo de valores en PU de una máquina de polos salientes
    def onClicked(self):
        if not self.ui.saliente_pu_check.isChecked():
            self.saliente_pu = False
            self.ui.voltaje_nominal_sal.setVisible(True)
            self.ui.sal_v_nom_pu.setVisible(False)
            self.ui.sal_p_aparente.setEnabled(True)
            self.ui.sal_p_aparente.setText("")
            self.ui.sal_r_q_label.setText("Reactancia cuadratura**(Ω)")
            self.ui.sal_v_n_label.setText("Voltaje nominal**(V)")
            self.ui.sal_r_d_label.setText("Reactancia directa**(Ω)")
            self.ui.sal_p_m_label.setText("Potencia motriz máxima(W)")
            self.ui.sal_p_aparente_label.setText("Potencia aparente**(V)")
        elif self.ui.saliente_pu_check.isChecked():
            self.saliente_pu = True
            self.ui.voltaje_nominal_sal.setVisible(False)
            self.ui.sal_v_nom_pu.setVisible(True)
            self.ui.sal_p_aparente.setText("1")
            self.ui.sal_p_aparente.setEnabled(False)
            self.ui.sal_r_q_label.setText("Reactancia cuadratura**(PU)")
            self.ui.sal_v_n_label.setText("Voltaje nominal**(PU)")
            self.ui.sal_r_d_label.setText("Reactancia directa**(PU)")
            self.ui.sal_p_m_label.setText("Potencia motriz máxima(PU)")
            self.ui.sal_p_aparente_label.setText("Potencia aparente**(PU)")

        if not self.ui.liso_pu_check.isChecked():
            self.liso_pu = False
            self.ui.voltaje_nominal.setVisible(True)
            self.ui.liso_v_nom_pu.setVisible(False)
            self.ui.liso_p_aparente.setEnabled(True)
            self.ui.liso_p_aparente.setText("")
            self.ui.liso_v_n_label.setText("Voltaje nominal**(V)")
            self.ui.liso_r_s_label.setText("Reactancia sincrónica**(Ω)")
            self.ui.liso_p_m_label.setText("Potencia motriz máxima(W)")
            self.ui.liso_p_aparente_label.setText("Potencia aparente**(VA)")
        elif self.ui.liso_pu_check.isChecked():
            self.liso_pu = True
            self.ui.voltaje_nominal.setVisible(False)
            self.ui.liso_v_nom_pu.setVisible(True)
            self.ui.liso_p_aparente.setText("1")
            self.ui.liso_p_aparente.setEnabled(False)
            self.ui.liso_v_n_label.setText("Voltaje nominal**(PU)")
            self.ui.liso_r_s_label.setText("Reactancia sincrónica**(PU)")
            self.ui.liso_p_m_label.setText("Potencia motriz máxima(PU)")
            self.ui.liso_p_aparente_label.setText("Potencia aparente**(PU)")

    # Función para comprobar que los datos de un GSPL sean correctos
    def comprobar_liso(self):
        self.ui.liso_error_mess.setText('')
        r = self.ui.liso_r_s.text()
        p = self.ui.liso_p_m.text()
        p_s = self.ui.liso_p_aparente.text()
        f_p = self.ui.liso_f_p.text()
        t_c_max = self.ui.liso_t_m_c.text()
        e_p = int(self.ui.liso_estabilidad_practica.currentText())
        v_n = int(self.ui.voltaje_nominal.currentText()) if not self.liso_pu else self.ui.liso_v_nom_pu.text()
        p_seg = int(self.ui.liso_porcentaje_seg.currentText())

        try:
            # Comprueba que los campos no estén vacíos
            if len(r) == 0 or len(p_s) == 0 or len(f_p) == 0:
                self.ui.liso_error_mess.setText('Uno o más campos están vacíos.')
                return
            v_n = float(v_n)
            r = float(r)
            p = 0.0 if len(p) == 0 or p == '0' else float(p)
            p_seg = p_seg / 100.0
            p_s = float(p_s)
            f_p = float(f_p)
            t_c_max = None if len(t_c_max) == 0 or t_c_max == '0' or t_c_max == '0.0' else float(t_c_max)
            e_p = e_p / 100.0
        except ValueError:
            self.ui.liso_error_mess.setText('Solo puedes ingresar dígitos en los campos.')
            return

        # Convierte a todos los valores a números positivos
        r = abs(r)
        p = abs(p)
        p_s = abs(p_s)
        f_p = abs(f_p)
        t_c_max = abs(t_c_max) if t_c_max is not None else None
        v_n = abs(v_n)

        # Actualiza los valores en los campos luego de aplicar valor absoluto
        self.ui.liso_r_s.setText(str(r))
        self.ui.liso_p_m.setText(str(p))
        self.ui.liso_p_aparente.setText(str(p_s))
        self.ui.liso_f_p.setText(str(f_p))
        if self.liso_pu:
            self.ui.liso_v_nom_pu.setText(str(v_n))
        if t_c_max is not None:
            self.ui.liso_t_m_c.setText(str(t_c_max))

        # Comprueba que el Factor de potencia sea correcto
        if f_p >= 1 or f_p <= 0:
            self.ui.liso_error_mess.setText('Ingrese un factor de potencia válido para la máquina.')
        # Comprueba que, si la p_motriz es distinta de cero, no sea menor que la potencia aparente
        elif p != 0 and p_s < p:
            self.ui.liso_error_mess.setText('La potencia motriz y aparente ingresadas no son correctas.')
        elif r == 0:
            self.ui.liso_error_mess.setText('La reactancia síncrona debe ser un número mayor a cero.')
        elif p_s == 0:
            self.ui.liso_error_mess.setText('La potencia aparente debe ser un número mayor a cero.')
        else:
            self._liso_param['voltaje'] = v_n
            self._liso_param['reactancia'] = r
            self._liso_param['potencia_motriz'] = p
            self._liso_param['porcentaje_seg'] = p_seg
            self._liso_param['potencia_aparente'] = p_s
            self._liso_param['factor_potencia'] = f_p
            self._liso_param['tension_campo'] = t_c_max
            self._liso_param['estabilidad_pract'] = e_p
            self.c_layout.removeWidget(self.static_graph)
            self.static_graph = MyMplCanvas(self.w_canvas)
            self.c_layout.addWidget(self.static_graph)
            self.ui.paginador.setCurrentWidget(self.ui.espera)
            self.ui.label.setText("Graficar curva de capacidad - Generador de polos lisos ")
            self.pool.submit(self.generate_polo_liso)

    # Función para construir la curva de capacidad
    def generate_polo_liso(self):
        print(self._liso_param)
        fig = self.static_graph.fig
        global text_progress
        global bar
        crear(fig,
              self._liso_param['potencia_aparente'],
              self._liso_param['voltaje'],
              self._liso_param['factor_potencia'],
              self._liso_param['reactancia'],
              self._liso_param['potencia_motriz'],
              self._liso_param['tension_campo'],
              self._liso_param['porcentaje_seg'],
              self._liso_param['estabilidad_pract'],
              text_progress,
              bar,
              per_units=self.liso_pu
              )
        self.ui.paginador.setCurrentWidget(self.ui.curva)

    # Función para comprobar que los datos de un GSPS sean correctos
    def comprobar_saliente(self):
        self.ui.saliente_error_mess.setText('')
        r_d = self.ui.sal_r_d.text()  # Reactancia de eje directo
        r_q = self.ui.sal_r_q.text()  # Reactancia de eje de cuadratura
        p = self.ui.sal_p_m.text()  # Potencia motriz
        p_s = self.ui.sal_p_aparente.text()  # Potencia aparente
        f_p = self.ui.sal_f_p.text()  # Factor de potencia
        t_c_max = self.ui.sal_t_m_c.text()  # Tension máxima de campo
        e_p = int(self.ui.sal_estabilidad_practica.currentText())  # Porcentaje de estabilidad práctica
        v_n = int(self.ui.voltaje_nominal_sal.currentText()) if not self.saliente_pu else self.ui.sal_v_nom_pu.text()
        p_seg = int(self.ui.sal_porcentaje_seg.currentText())

        try:
            if len(r_q) == 0 or len(r_d) == 0 or len(p_s) == 0 or len(f_p) == 0:
                self.ui.saliente_error_mess.setText('Uno o más campos están vacíos.')
                return
            v_n = float(v_n)
            r_d = float(r_d)
            r_q = float(r_q)
            p = 0.0 if len(p) == 0 or p == '0' else float(p)
            p_seg = p_seg / 100.0
            p_s = float(p_s)
            f_p = float(f_p)
            t_c_max = None if len(t_c_max) == 0 or t_c_max == '0' or t_c_max == '0.0' else float(t_c_max)
            e_p = e_p / 100.0
        except ValueError:
            self.ui.liso_error_mess.setText('Solo puedes ingresar dígitos en los campos.')
            return

        # Convierte a todos los valores a números positivos
        r_d = abs(r_d)
        r_q = abs(r_q)
        p = abs(p)
        p_s = abs(p_s)
        f_p = abs(f_p)
        t_c_max = abs(t_c_max) if t_c_max is not None else None
        v_n = abs(v_n)

        # Actualiza los valores en los campos luego de aplicar valor absoluto
        self.ui.sal_r_d.setText(str(r_d))
        self.ui.sal_r_q.setText(str(r_q))
        self.ui.sal_p_m.setText(str(p))
        self.ui.sal_p_aparente.setText(str(p_s))
        self.ui.sal_f_p.setText(str(f_p))
        if self.saliente_pu:
            self.ui.sal_v_nom_pu.setText(str(v_n))
        if t_c_max is not None:
            self.ui.sal_t_m_c.setText(str(t_c_max))

        # Comprueba que el Factor de potencia sea correcto
        if f_p >= 1 or f_p <= 0:
            self.ui.sal_estabilidad_practica.setText('Ingrese un factor de potencia válido para la máquina.')
        # Comprueba que, si la p_motriz es distinta de cero, no sea menor que la potencia aparente
        elif p != 0 and p_s < p:
            self.ui.sal_estabilidad_practica.setText('La potencia motriz y aparente ingresadas no son correctas.')
        elif r_d == 0:
            self.ui.sal_estabilidad_practica.setText('La reactancia de eje directo debe ser un número mayor a cero.')
        elif r_q == 0:
            self.ui.sal_estabilidad_practica.setText('La reactancia de cuadratura debe ser un número mayor a cero.')
        elif p_s == 0:
            self.ui.sal_estabilidad_practica.setText('La potencia aparente debe ser un número mayor a cero.')
        else:
            self._saliente_param['voltaje'] = v_n
            self._saliente_param['reactancia_directa'] = r_d
            self._saliente_param['reactancia_cuadratura'] = r_q
            self._saliente_param['potencia_motriz'] = p
            self._saliente_param['porcentaje_seg'] = p_seg
            self._saliente_param['potencia_aparente'] = p_s
            self._saliente_param['factor_potencia'] = f_p
            self._saliente_param['tension_campo'] = t_c_max
            self._saliente_param['estabilidad_pract'] = e_p
            self.c_layout.removeWidget(self.static_graph)
            self.static_graph = MyMplCanvas(self.w_canvas)
            self.c_layout.addWidget(self.static_graph)
            self.ui.paginador.setCurrentWidget(self.ui.espera)
            self.ui.label.setText("Graficar curva de capacidad - Generador de polos salientes")
            self.pool.submit(self.generate_polo_saliente)

    # Función para construir la curva de capacidad para generador de polos salientes
    def generate_polo_saliente(self):
        fig = self.static_graph.fig
        global text_progress
        global bar
        crearpolosaliente(
            fig,
            self._saliente_param['potencia_aparente'],
            self._saliente_param['voltaje'],
            self._saliente_param['factor_potencia'],
            self._saliente_param['reactancia_directa'],
            self._saliente_param['reactancia_cuadratura'],
            self._saliente_param['potencia_motriz'],
            self._saliente_param['tension_campo'],
            self._saliente_param['porcentaje_seg'],
            self._saliente_param['estabilidad_pract'],
            text_progress,
            bar,
            per_units=self.saliente_pu
        )
        self.ui.paginador.setCurrentWidget(self.ui.curva)
