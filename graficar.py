from sympy import Symbol, sqrt, Eq, cos, sin, nsolve
import numpy as np
import RegionManager
from Function import Function
from FunctionPoints import FunctionPoints
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import cmath as c
import IntersectionManager
import time


def circle(x, r, h):
    return np.sqrt(r ** 2 - (x - h) ** 2)


def circles(x, r, h):
    return sqrt(r ** 2 - (x - h) ** 2)


def rectas(angle_power, origen, x):
    m = abs(c.tan(angle_power))
    return m * (x - origen)


def crear(fig, Sn, Vn, Fp, Xs, P_motriz, ef, seg_min, seg_prac, text, bar, per_units=False):
    if seg_min < 0.05: seg_min = 0.05
    if seg_prac < 0.1: seg_prac = 0.1
    if P_motriz == 0.0: P_motriz = Sn

    if not per_units:
        Zbase = ((Vn) ** 2) / (Sn)
        Vn, Sn, Xs, P_motriz = (Vn / Vn), (Sn / Sn), (Xs / Zbase), (P_motriz / Sn)

    if ef == None:
        fp = abs(c.acos(Fp))
        Ef = c.rect(Vn, 0) + (c.rect(Xs, c.pi / 2) * c.rect(1, -fp))
        Ef = abs(Ef)
    else:
        Ef = ef
    if P_motriz == 1: P_motriz = P_motriz + 0.0000001
    if seg_min == 0: seg_min = 0.02
    x = Symbol('x')
    ax = fig.add_subplot(111)
    eje = (-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1)
    # fig.xticks(eje)
    # fig.title("Curva de capacidad generador Polo liso")

    # --------------Aqui empieza-----------------------
    text.setText('Calculando parámetros en PU.')
    radio = (Ef * Vn) / Xs
    radio_min = radio * 0.1 + radio * seg_min
    centro = -(Vn ** 2) / Xs
    o1 = centro
    limit_armadura = Function(sqrt(Vn - x ** 2))
    Limit_excitacion = Function(circles(x, radio, centro))
    Pmeca = Function(P_motriz)
    Limit_exci_min = Function(circles(x, radio_min, centro))
    Values_x = []
    Values_y = []
    bar.setValue(10)
    time.sleep(0.01)
    # --------------------------------------------------------------------
    # -------------------- aqui se calcula F_practic----------------------
    # --------------------------------------------------------------------
    text.setText("Calculando la estabilidad práctica.")
    rango = [z / 10 for z in range(10, 0, -1)]
    for i in rango:
        rect = Function((radio * i) - (radio * seg_prac))
        f_x = Function(circles(x, radio * i, centro))
        if ((radio * i) - (radio * seg_prac)) <= 0: rect = (Function(0.1))
        Intersections = IntersectionManager.num_intersect(rect, f_x, (centro, centro + (radio * i) - 0.00001))

        if i == rango[-1]:
            Values_x.append(Intersections - 0.00001)
            Values_y.append((radio * i) - (radio * seg_prac) - 0.0001)

        else:
            Values_x.append(Intersections)
            Values_y.append((radio * i) - (radio * seg_prac))
        bar.setValue(bar.value() + 3)
    print(bar.value())
    text.setText("Generando contorno... ")
    F_practic = FunctionPoints(Values_x, Values_y, grid=500)

    text.setText("Generando contorno: intersectando contornos de la izquierda.")
    out_izquierda = RegionManager.intersect_functions([limit_armadura, Limit_exci_min, F_practic, Pmeca])

    text.setText("Generando contorno: obteniendo puntos del menor contorno a la izquierda.")
    puntos_izquierda = RegionManager.get_minor_contour(out_izquierda,
                                                       [limit_armadura, Limit_exci_min, F_practic, Pmeca])

    text.setText("Generando contorno: intersectando contornos de la derecha.")
    out_derecha = RegionManager.intersect_functions([limit_armadura, Limit_excitacion, Pmeca])

    text.setText("Generando contorno: obteniendo puntos del menor contorno a la derecha.")
    puntos_derecha = RegionManager.get_minor_contour(out_derecha, [limit_armadura, Limit_excitacion, Pmeca])
    bar.setValue(50)
    time.sleep(0.01)

    puntos_izquierda = list(filter(lambda x: x.get_x() < 0, puntos_izquierda))
    puntos_derecha = list(filter(lambda x: x.get_x() > 0, puntos_derecha))

    # ------------------------------------------------------------------------
    # ----------------- graficar funciones------------------------------
    # --------------------solo plots------------------------------------
    text.setText("Graficando contornos: límite de estabilidad teórica.")
    ax.plot((centro, centro), (0, radio), color='blue', label='limite de estabilidad teorica')

    text.setText("Graficando contornos: límite de estabilidad práctica.")
    x2 = list(np.linspace(Values_x[0] - 0.00000001, Values_x[-1] + 0.00000001, 25))
    ax.plot(x2, F_practic.eval_an_array(x2), color='red', label='limite de estabilidad practica')

    text.setText("Graficando contornos: límite de armadura.")
    x3 = list(np.linspace(-1 + 0.00001, 1 - 0.00001, 500))
    ax.plot(x3, limit_armadura.eval_an_array(x3), color='green', label='limite de armadura')
    bar.setValue(60)

    text.setText("Graficando contornos: límite de excitación mínima.")
    x4 = list(np.linspace(centro - 0.00001, centro + radio_min - 0.00001, 30))
    ax.plot(x4, Limit_exci_min.eval_an_array(x4), label='limite de excitacion minima')

    text.setText("Graficando contornos: límite de excitación.")
    x5 = list(np.linspace(centro, centro + radio - 0.00001, 50))
    ax.plot(x5, Limit_excitacion.eval_an_array(x5), label='limite de excitacion')

    # ----------------------------------------------------------------------------
    # ----------------------------------------------------------------------------
    # -----------------  puntos de interseccion-----------------------------------
    text.setText("Puntos de intersección del contorno menor.")
    inter_exi_arma = IntersectionManager.fun_intersect(limit_armadura, Limit_exci_min, solution_domain=1)
    inter_arma_Pmec = IntersectionManager.fun_intersect(limit_armadura, Pmeca, solution_domain=1)
    inter_arm_stab = IntersectionManager.fun_and_point(limit_armadura, F_practic)
    inter_exitante_arm = IntersectionManager.fun_intersect(limit_armadura, Limit_excitacion, solution_domain=1)
    bar.setValue(80)
    time.sleep(0.01)
    # -------------------------------------------------
    # ------ Puntos de la izquierda-------------------
    # -------------relleno-----------------------------
    text.setText("Rellenando región del menor contorno: lado izquierdo.")
    if abs(centro) > 1:

        if P_motriz > 1:
            if len(puntos_izquierda)==0:
                pass
            elif puntos_izquierda[0].get_x() < -1:
                puntos_izquierda.pop(0)

            if len(inter_exi_arma) == 0:

                if len(inter_arm_stab) == 0:
                    a1 = list(np.linspace(-1, 0, 50))
                    ax.fill_between(a1, 0, limit_armadura.eval_an_array(a1), color='yellow', alpha=0.2)
                    print('1')

                else:
                    a1 = list(np.linspace(-1, puntos_izquierda[0].get_x(), 10))
                    ax.fill_between(a1, 0, limit_armadura.eval_an_array(a1), color='yellow', alpha=0.2)
                    a2 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 10))
                    ax.fill_between(a2, 0, F_practic.eval_an_array(a2), color='yellow', alpha=0.2)
                    a3 = list(np.linspace(puntos_izquierda[1].get_x(), 0, 50))
                    ax.fill_between(a3, 0, limit_armadura.eval_an_array(a3), color='yellow', alpha=0.2)
                    print('2')

            else:
                if len(puntos_izquierda) == 1 and len(inter_arm_stab) == 0:
                    a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 50))
                    ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1),
                                    color='yellow', alpha=0.2)
                    a2 = list(np.linspace(centro + radio_min - 0.00001, 0, 50))
                    ax.fill_between(a2, 0, limit_armadura.eval_an_array(a2), color='yellow', alpha=0.2)
                    print('3')

                elif len(puntos_izquierda) == 2 and inter_arm_stab[-1] > (centro + radio_min):
                    a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.000001, 10))
                    ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), F_practic.eval_an_array(a1), color='yellow',
                                    alpha=0.2)
                    a2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 40))
                    ax.fill_between(a2, 0, F_practic.eval_an_array(a2), color='yellow', alpha=0.2)
                    a3 = list(np.linspace(puntos_izquierda[1].get_x(), 0, 10))
                    ax.fill_between(a3, 0, limit_armadura.eval_an_array(a3), color='yellow', alpha=0.2)
                    print('4')

                elif len(puntos_izquierda) == 2 and inter_arm_stab[-1] < (centro + radio_min):
                    a1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 10))
                    ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), F_practic.eval_an_array(a1), color='yellow',
                                    alpha=0.2)
                    a2 = list(np.linspace(puntos_izquierda[1].get_x(), centro + radio_min - 0.00001, 20))
                    ax.fill_between(a2, Limit_exci_min.eval_an_array(a2), limit_armadura.eval_an_array(a2),
                                    color='yellow', alpha=0.2)
                    a3 = list(np.linspace(centro + radio_min - 0.00001, 0, 30))
                    ax.fill_between(a3, 0, limit_armadura.eval_an_array(a3), color='yellow', alpha=0.2)
                    print('5')

                elif len(puntos_izquierda) == 3 and inter_arm_stab[0] < (centro + radio_min) and inter_arm_stab[-1] > (
                        centro + radio_min):
                    a1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 10))
                    ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1),
                                    color='yellow', alpha=0.2)
                    a2 = list(np.linspace(puntos_izquierda[1].get_x(), centro + radio_min - 0.00001, 40))
                    ax.fill_between(a2, Limit_exci_min.eval_an_array(a2), F_practic.eval_an_array(a2), color='yellow',
                                    alpha=0.2)
                    a3 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[2].get_x(), 30))
                    ax.fill_between(a3, 0, F_practic.eval_an_array(a3), color='yellow', alpha=0.2)
                    a4 = list(np.linspace(puntos_izquierda[2].get_x(), 0, 30))
                    ax.fill_between(a4, 0, limit_armadura.eval_an_array(a4), color='yellow', alpha=0.2)
                    print('6')

                elif len(puntos_izquierda) == 3 and inter_arm_stab[0] > (centro + radio_min):
                    a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 30))
                    ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1),
                                    color='yellow', alpha=0.2)
                    a2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 30))
                    ax.fill_between(a2, 0, limit_armadura.eval_an_array(a2), color='yellow', alpha=0.2)
                    a3 = list(np.linspace(puntos_izquierda[1].get_x(), puntos_izquierda[2].get_x(), 30))
                    ax.fill_between(a3, 0, F_practic.eval_an_array(a3), color='yellow', alpha=0.2)
                    a4 = list(np.linspace(puntos_izquierda[2].get_x(), 0, 30))
                    ax.fill_between(a4, 0, limit_armadura.eval_an_array(a4), color='yellow', alpha=0.2)
                    print('7')

                elif len(puntos_izquierda) == 3 and inter_arm_stab[0] < (centro + radio_min) and inter_arm_stab[-1] < (
                        centro + radio_min):
                    a1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 30))
                    ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1),
                                    color='yellow', alpha=0.2)
                    a2 = list(np.linspace(puntos_izquierda[1].get_x(), puntos_izquierda[2].get_x(), 30))
                    ax.fill_between(a2, Limit_exci_min.eval_an_array(a2), F_practic.eval_an_array(a2), color='yellow',
                                    alpha=0.2)
                    a3 = list(np.linspace(puntos_izquierda[2].get_x(), centro + radio_min - 0.00001, 30))
                    ax.fill_between(a3, Limit_exci_min.eval_an_array(a3), limit_armadura.eval_an_array(a3),
                                    color='yellow', alpha=0.2)
                    a4 = list(np.linspace(centro + radio_min - 0.00001, 0, 30))
                    ax.fill_between(a4, 0, limit_armadura.eval_an_array(a4), color='yellow', alpha=0.2)
                    print('8')

        else:
            if len(puntos_izquierda) == 0:
                pass
            elif puntos_izquierda[0].get_x() < -1:
                puntos_izquierda.pop(0)

            pm = list(np.linspace(o1, o1 + radio, 10))
            ax.plot(pm, Pmeca.eval_an_array(pm), label='Limite de Potencia')
            if len(inter_exi_arma) == 0:
                if len(inter_arm_stab) == 0:
                    a1 = list(np.linspace(-1, puntos_izquierda[-1].get_x(), 30))
                    ax.fill_between(a1, 0, limit_armadura.eval_an_array(a1), color='yellow', alpha=0.2)
                    a2 = list(np.linspace(puntos_izquierda[-1].get_x(), 0, 50))
                    ax.fill_between(a2, 0, Pmeca.eval_an_array(a2), color='yellow', alpha=0.2)
                    print('1')
                else:
                    if len(puntos_izquierda) == 2:
                        a1 = list(np.linspace(-1, puntos_izquierda[0].get_x(), 30))
                        ax.fill_between(a1, 0, limit_armadura.eval_an_array(a1), color='yellow', alpha=0.2)
                        a2 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 30))
                        ax.fill_between(a2, 0, F_practic.eval_an_array(a2), color='yellow', alpha=0.2)
                        a3 = list(np.linspace(puntos_izquierda[1].get_x(), 0, 30))
                        ax.fill_between(a3, 0, Pmeca.eval_an_array(a3), color='yellow', alpha=0.2)
                        print('2')
                    elif len(puntos_izquierda) == 3:
                        a1 = list(np.linspace(-1, puntos_izquierda[0].get_x(), 30))
                        ax.fill_between(a1, 0, limit_armadura.eval_an_array(a1), color='yellow', alpha=0.2)
                        a2 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 30))
                        ax.fill_between(a2, 0, F_practic.eval_an_array(a2), color='yellow', alpha=0.2)
                        a3 = list(np.linspace(puntos_izquierda[1].get_x(), puntos_izquierda[2].get_x(), 30))
                        ax.fill_between(a3, 0, limit_armadura.eval_an_array(a3), color='yellow', alpha=0.2)
                        a4 = list(np.linspace(puntos_izquierda[2].get_x(), 0, 30))
                        ax.fill_between(a4, 0, Pmeca.eval_an_array(a1), color='yellow', alpha=0.2)
                        print('3')
            else:
                if len(puntos_izquierda) == 2 and inter_arma_Pmec[0] > centro + radio_min and len(inter_arm_stab) == 0:
                    a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 30))
                    ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1),
                                    color='yellow', alpha=0.2)
                    a2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 30))
                    ax.fill_between(a2, 0, limit_armadura.eval_an_array(a2), color='yellow', alpha=0.2)
                    a3 = list(np.linspace(puntos_izquierda[1].get_x(), 0, 30))
                    ax.fill_between(a3, 0, Pmeca.eval_an_array(a3), color='yellow', alpha=0.2)
                    print('4')
                elif len(puntos_izquierda) == 2 and len(inter_arm_stab) != 0:
                    a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 30))
                    ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), F_practic.eval_an_array(a1), color='yellow',
                                    alpha=0.2)
                    a2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 30))
                    ax.fill_between(a2, 0, F_practic.eval_an_array(a2), color='yellow', alpha=0.2)
                    a3 = list(np.linspace(puntos_izquierda[1].get_x(), 0, 30))
                    ax.fill_between(a3, 0, Pmeca.eval_an_array(a3), color='yellow', alpha=0.2)
                    print('4.')

                elif len(puntos_izquierda) == 1:
                    a1 = list(np.linspace(centro + radio_min + 0.00001, puntos_izquierda[0].get_x(), 50))
                    ax.fill_between(a1, 0, F_practic.eval_an_array(a1), color='yellow', alpha=0.2)
                    a2 = list(np.linspace(puntos_izquierda[0].get_x(), 0, 50))
                    ax.fill_between(a2, 0, Pmeca.eval_an_array(a2), color='yellow', alpha=0.2)

                elif len(puntos_izquierda) == 2 and inter_arma_Pmec[0] < centro + radio_min:
                    a1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 30))
                    ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1),
                                    color='yellow', alpha=0.2)
                    a2 = list(np.linspace(puntos_izquierda[1].get_x(), centro + radio_min - 0.00001, 30))
                    ax.fill_between(a2, Limit_exci_min.eval_an_array(a2), Pmeca.eval_an_array(a2), color='yellow',
                                    alpha=0.2)
                    a3 = list(np.linspace(centro + radio_min - 0.00001, 0, 30))
                    ax.fill_between(a3, 0, Pmeca.eval_an_array(a3), color='yellow', alpha=0.2)
                    print('5')

                elif len(puntos_izquierda) == 3 and inter_arm_stab[-1] < inter_arma_Pmec[0]:
                    a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 30))
                    ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), F_practic.eval_an_array(a1), color='yellow',
                                    alpha=0.2)
                    a2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 30))
                    ax.fill_between(a2, 0, F_practic.eval_an_array(a2), color='yellow', alpha=0.2)
                    a3 = list(np.linspace(puntos_izquierda[1].get_x(), puntos_izquierda[2].get_x(), 30))
                    ax.fill_between(a3, 0, limit_armadura.eval_an_array(a3), color='yellow', alpha=0.2)
                    a4 = list(np.linspace(puntos_izquierda[2].get_x(), 0, 30))
                    ax.fill_between(a4, 0, Pmeca.eval_an_array(a4), color='yellow', alpha=0.2)
                    print('6')

                elif len(puntos_izquierda) == 3 and inter_arm_stab[-1] > inter_arma_Pmec[0] and inter_arm_stab[
                    0] < centro + radio_min:
                    a1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 30))
                    ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1),
                                    color='yellow', alpha=0.2)
                    a2 = list(np.linspace(puntos_izquierda[1].get_x(), centro + radio_min - 0.00001, 30))
                    ax.fill_between(a2, Limit_exci_min.eval_an_array(a2), F_practic.eval_an_array(a2), color='yellow',
                                    alpha=0.2)
                    a3 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[2].get_x(), 30))
                    ax.fill_between(a3, 0, F_practic.eval_an_array(a3), color='yellow', alpha=0.2)
                    a4 = list(np.linspace(puntos_izquierda[2].get_x(), 0, 30))
                    ax.fill_between(a4, 0, Pmeca.eval_an_array(a4), color='yellow', alpha=0.2)
                    print('7')

                elif len(puntos_izquierda) == 3 and inter_arm_stab[-1] > inter_arma_Pmec[0] and inter_arm_stab[
                    0] > centro + radio_min:
                    a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 30))
                    ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1),
                                    color='yellow', alpha=0.2)
                    a2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 30))
                    ax.fill_between(a2, 0, limit_armadura.eval_an_array(a2), color='yellow', alpha=0.2)
                    a3 = list(np.linspace(puntos_izquierda[1].get_x(), puntos_izquierda[2].get_x(), 30))
                    ax.fill_between(a3, 0, F_practic.eval_an_array(a3), color='yellow', alpha=0.2)
                    a4 = list(np.linspace(puntos_izquierda[2].get_x(), 0, 30))
                    ax.fill_between(a4, 0, Pmeca.eval_an_array(a4), color='yellow', alpha=0.2)
                    print('8')

                elif len(puntos_izquierda) == 4 and inter_arm_stab[0] < centro + radio_min:
                    a1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 30))
                    ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1),
                                    color='yellow', alpha=0.2)
                    a2 = list(np.linspace(puntos_izquierda[1].get_x(), centro + radio_min - 0.00001, 30))
                    ax.fill_between(a2, Limit_exci_min.eval_an_array(a2), F_practic.eval_an_array(a2), color='yellow',
                                    alpha=0.2)
                    a3 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[2].get_x(), 30))
                    ax.fill_between(a3, 0, F_practic.eval_an_array(a3), color='yellow', alpha=0.2)
                    a4 = list(np.linspace(puntos_izquierda[2].get_x(), puntos_izquierda[3].get_x(), 30))
                    ax.fill_between(a4, 0, limit_armadura.eval_an_array(a4), color='yellow', alpha=0.2)
                    a5 = list(np.linspace(puntos_izquierda[3].get_x(), 0, 30))
                    ax.fill_between(a5, 0, Pmeca.eval_an_array(a5), color='yellow', alpha=0.2)
                    print('9')

                elif len(puntos_izquierda) == 4 and inter_arm_stab[0] > centro + radio_min:
                    a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 30))
                    ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1),
                                    color='yellow', alpha=0.2)
                    a2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 30))
                    ax.fill_between(a2, 0, limit_armadura.eval_an_array(a2), color='yellow', alpha=0.2)
                    a3 = list(np.linspace(puntos_izquierda[1].get_x(), puntos_izquierda[2].get_x(), 30))
                    ax.fill_between(a3, 0, F_practic.eval_an_array(a3), color='yellow', alpha=0.2)
                    a4 = list(np.linspace(puntos_izquierda[2].get_x(), puntos_izquierda[3].get_x(), 30))
                    ax.fill_between(a4, 0, limit_armadura.eval_an_array(a4), color='yellow', alpha=0.2)
                    a5 = list(np.linspace(puntos_izquierda[3].get_x(), 0, 30))
                    ax.fill_between(a5, 0, Pmeca.eval_an_array(a5), color='yellow', alpha=0.2)
    else:
        if P_motriz > 1:
            if limit_armadura.eval(centro) > radio_min:
                if inter_arm_stab[-1] > centro + radio_min:
                    a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 50))
                    ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), F_practic.eval_an_array(a1), color='yellow',
                                    alpha=0.2)
                    a2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 50))
                    ax.fill_between(a2, 0, F_practic.eval_an_array(a2), color='yellow', alpha=0.2)
                    a3 = list(np.linspace(puntos_izquierda[1].get_x(), 0, 50))
                    ax.fill_between(a3, 0, limit_armadura.eval_an_array(a3), color='yellow', alpha=0.2)
                    print('1')
                else:
                    x1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 50))
                    ax.fill_between(x1, Limit_exci_min.eval_an_array(x1), F_practic.eval_an_array(x1), color='yellow',
                                    alpha=0.2)
                    x2 = list(np.linspace(puntos_izquierda[1].get_x(), centro + radio_min - 0.00001, 50))
                    ax.fill_between(x2, Limit_exci_min.eval_an_array(x2), limit_armadura.eval_an_array(x2),
                                    color='yellow', alpha=0.2)
                    x3 = list(np.linspace(centro + radio_min - 0.00001, 0, 50))
                    ax.fill_between(x3, 0, limit_armadura.eval_an_array(x3), color='yellow', alpha=0.2)
                    print('2')
            else:
                if len(inter_arm_stab) == 0:
                    x1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 50))
                    ax.fill_between(x1, Limit_exci_min.eval_an_array(x1), limit_armadura.eval_an_array(x1),
                                    color='yellow', alpha=0.2)
                    x2 = list(np.linspace(centro + radio_min - 0.00001, 0, 50))
                    ax.fill_between(x2, 0, limit_armadura.eval_an_array(x2), color='yellow', alpha=0.2)
                    print('3')
                else:
                    if inter_arm_stab[-1] > centro + radio_min:
                        x1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 50))
                        ax.fill_between(x1, Limit_exci_min.eval_an_array(x1), F_practic.eval_an_array(x1),
                                        color='yellow', alpha=0.2)
                        x2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 50))
                        ax.fill_between(x2, 0, F_practic.eval_an_array(x2), color='yellow', alpha=0.2)
                        x3 = list(np.linspace(puntos_izquierda[1].get_x(), 0, 50))
                        ax.fill_between(x3, 0, limit_armadura.eval_an_array(x3), color='yellow', alpha=0.2)
                        print('4')
                    else:
                        x1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 50))
                        ax.fill_between(x1, Limit_exci_min.eval_an_array(x1), F_practic.eval_an_array(x1),
                                        color='yellow', alpha=0.2)
                        x2 = list(np.linspace(puntos_izquierda[1].get_x(), centro + radio_min - 0.00001, 50))
                        ax.fill_between(x2, Limit_exci_min.eval_an_array(x2), limit_armadura.eval_an_array(x2),
                                        color='yellow', alpha=0.2)
                        x3 = list(np.linspace(centro + radio_min - 0.00001, 0, 50))
                        ax.fill_between(x3, 0, limit_armadura.eval_an_array(x3), color='yellow', alpha=0.2)
                        print('5')
        else:
            pm = list(np.linspace(o1, o1 + radio, 10))
            ax.plot(pm, Pmeca.eval_an_array(pm), label='Limite de Potencia')

            if limit_armadura.eval(centro) > radio_min:
                if len(puntos_izquierda) == 1:
                    x1 = list(np.linspace(centro + radio_min + 0.00001, puntos_izquierda[-1].get_x(), 50))
                    ax.fill_between(x1, 0, F_practic.eval_an_array(x1), color='yellow', alpha=0.2)
                    x2 = list(np.linspace(puntos_izquierda[-1].get_x(), 0, 50))
                    ax.fill_between(x2, 0, Pmeca.eval_an_array(x2), color='yellow', alpha=0.2)

                if len(puntos_izquierda) == 2:
                    if puntos_izquierda[-1].get_x() > centro + radio_min:
                        x1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 50))
                        ax.fill_between(x1, Limit_exci_min.eval_an_array(x1), F_practic.eval_an_array(x1),
                                        color='yellow', alpha=0.2)
                        x2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 50))
                        ax.fill_between(x2, 0, F_practic.eval_an_array(x2), color='yellow', alpha=0.2)
                        x3 = list(np.linspace(puntos_izquierda[1].get_x(), 0, 50))
                        ax.fill_between(x3, 0, Pmeca.eval_an_array(x3), color='yellow', alpha=0.2)

                    else:
                        x1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 50))
                        ax.fill_between(x1, Limit_exci_min.eval_an_array(x1), F_practic.eval_an_array(x1),
                                        color='yellow', alpha=0.2)
                        x2 = list(np.linspace(puntos_izquierda[1].get_x(), centro + radio_min - 0.00001, 50))
                        ax.fill_between(x2, Limit_exci_min.eval_an_array(x2), Pmeca.eval_an_array(x2), color='yellow',
                                        alpha=0.2)
                        x3 = list(np.linspace(centro + radio_min - 0.00001, 0, 50))
                        ax.fill_between(x3, 0, Pmeca.eval_an_array(x3), color='yellow', alpha=0.2)

                elif len(puntos_izquierda) == 3:
                    if puntos_izquierda[1].get_x() > centro + radio_min:
                        x1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 50))
                        ax.fill_between(x1, Limit_exci_min.eval_an_array(x1), F_practic.eval_an_array(x1),
                                        color='yellow', alpha=0.2)
                        x2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 50))
                        ax.fill_between(x2, 0, F_practic.eval_an_array(x2), color='yellow', alpha=0.2)
                        x3 = list(np.linspace(puntos_izquierda[1].get_x(), puntos_izquierda[2].get_x(), 50))
                        ax.fill_between(x3, 0, limit_armadura.eval_an_array(x3), color='yellow', alpha=0.2)
                        x4 = list(np.linspace(puntos_izquierda[2].get_x(), 0, 50))
                        ax.fill_between(x4, 0, Pmeca.eval_an_array(x4), color='yellow', alpha=0.2)

                    else:
                        x1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 50))
                        ax.fill_between(x1, Limit_exci_min.eval_an_array(x1), F_practic.eval_an_array(x1),
                                        color='yellow', alpha=0.2)
                        x2 = list(np.linspace(puntos_izquierda[1].get_x(), centro + radio_min - 0.00001, 50))
                        ax.fill_between(x2, Limit_exci_min.eval_an_array(x2), limit_armadura.eval_an_array(x2),
                                        color='yellow', alpha=0.2)
                        x3 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[2].get_x(), 50))
                        ax.fill_between(x3, 0, limit_armadura.eval_an_array(x3), color='yellow', alpha=0.2)
                        x4 = list(np.linspace(puntos_izquierda[2].get_x(), 0, 50))
                        ax.fill_between(x4, 0, Pmeca.eval_an_array(x4), color='yellow', alpha=0.2)
            else:
                if len(inter_arm_stab) == 0:
                    x1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 50))
                    ax.fill_between(x1, Limit_exci_min.eval_an_array(x1), limit_armadura.eval_an_array(x1),
                                    color='yellow', alpha=0.2)
                    x2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[0].get_x(), 50))
                    ax.fill_between(x2, 0, limit_armadura.eval_an_array(x2), color='yellow', alpha=0.2)
                    x3 = list(np.linspace(puntos_izquierda[0].get_x(), 0, 50))
                    ax.fill_between(x3, 0, Pmeca.eval_an_array(x3), color='yellow', alpha=0.2)
                else:
                    if len(puntos_izquierda) == 2:
                        if puntos_izquierda[-1].get_x() > centro + radio_min:
                            x1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 50))
                            ax.fill_between(x1, Limit_exci_min.eval_an_array(x1), F_practic.eval_an_array(x1),
                                            color='yellow', alpha=0.2)
                            x2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 50))
                            ax.fill_between(x2, 0, F_practic.eval_an_array(x2), color='yellow', alpha=0.2)
                            x3 = list(np.linspace(puntos_izquierda[1].get_x(), 0, 50))
                            ax.fill_between(x3, 0, Pmeca.eval_an_array(x3), color='yellow', alpha=0.2)

                        else:
                            x1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 50))
                            ax.fill_between(x1, Limit_exci_min.eval_an_array(x1), F_practic.eval_an_array(x1),
                                            color='yellow', alpha=0.2)
                            x2 = list(np.linspace(puntos_izquierda[1].get_x(), centro + radio_min - 0.00001, 50))
                            ax.fill_between(x2, Limit_exci_min.eval_an_array(x2), Pmeca.eval_an_array(x2),
                                            color='yellow', alpha=0.2)
                            x3 = list(np.linspace(centro + radio_min - 0.00001, 0, 50))
                            ax.fill_between(x3, 0, Pmeca.eval_an_array(x3), color='yellow', alpha=0.2)
                    if len(puntos_izquierda) == 3:
                        if puntos_izquierda[1].get_x() > centro + radio_min:
                            x1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 50))
                            ax.fill_between(x1, Limit_exci_min.eval_an_array(x1), F_practic.eval_an_array(x1),
                                            color='yellow', alpha=0.2)
                            x2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 50))
                            ax.fill_between(x2, 0, F_practic.eval_an_array(x2), color='yellow', alpha=0.2)
                            x3 = list(np.linspace(puntos_izquierda[1].get_x(), puntos_izquierda[2].get_x(), 50))
                            ax.fill_between(x3, 0, limit_armadura.eval_an_array(x3), color='yellow', alpha=0.2)
                            x4 = list(np.linspace(puntos_izquierda[2].get_x(), 0, 50))
                            ax.fill_between(x4, 0, Pmeca.eval_an_array(x4), color='yellow', alpha=0.2)

                        else:
                            x1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 50))
                            ax.fill_between(x1, Limit_exci_min.eval_an_array(x1), F_practic.eval_an_array(x1),
                                            color='yellow', alpha=0.2)
                            x2 = list(np.linspace(puntos_izquierda[1].get_x(), centro + radio_min - 0.00001, 50))
                            ax.fill_between(x2, Limit_exci_min.eval_an_array(x2), limit_armadura.eval_an_array(x2),
                                            color='yellow', alpha=0.2)
                            x3 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[2].get_x(), 50))
                            ax.fill_between(x3, 0, limit_armadura.eval_an_array(x3), color='yellow', alpha=0.2)
                            x4 = list(np.linspace(puntos_izquierda[2].get_x(), 0, 50))
                            ax.fill_between(x4, 0, Pmeca.eval_an_array(x4), color='yellow', alpha=0.2)
    bar.setValue(90)
    # -----------------------------------------------------------
    # ------------puntos de la derecha---------------------------
    # ------------------relleno----------------------------------
    # -----------------------------------------------------------
    text.setText("Rellenando región del menor contorno: lado derecho.")
    if P_motriz > 1:
        if len(inter_exitante_arm) == 0:
            b1 = list(np.linspace(0, 1, 50))
            ax.fill_between(b1, 0, limit_armadura.eval_an_array(b1), color='yellow', alpha=0.2)
        else:
            b1 = list(np.linspace(0, puntos_derecha[0].get_x(), 50))
            ax.fill_between(b1, 0, limit_armadura.eval_an_array(b1), color='yellow', alpha=0.2)
            b2 = list(np.linspace(puntos_derecha[0].get_x(), o1 + radio - 0.00001, 50))
            ax.fill_between(b2, 0, Limit_excitacion.eval_an_array(b2), color='yellow', alpha=0.2)
    else:
        if len(inter_exitante_arm) == 0:
            b1 = list(np.linspace(0, puntos_derecha[0].get_x(), 50))
            ax.fill_between(b1, 0, Pmeca.eval_an_array(b1), color='yellow', alpha=0.2)
            b2 = list(np.linspace(puntos_derecha[0].get_x(), 1, 50))
            ax.fill_between(b2, 0, limit_armadura.eval_an_array(b2), color='yellow', alpha=0.2)

        else:
            if inter_exitante_arm[0] > inter_arma_Pmec[-1]:
                b1 = list(np.linspace(0, puntos_derecha[0].get_x(), 50))
                ax.fill_between(b1, 0, Pmeca.eval_an_array(b1), color='yellow', alpha=0.2)
                b2 = list(np.linspace(puntos_derecha[0].get_x(), puntos_derecha[1].get_x(), 50))
                ax.fill_between(b2, 0, limit_armadura.eval_an_array(b2), color='yellow', alpha=0.2)
                b3 = list(np.linspace(puntos_derecha[1].get_x(), o1 + radio - 0.00001, 50))
                ax.fill_between(b3, 0, Limit_excitacion.eval_an_array(b3), color='yellow', alpha=0.2)

            else:
                b1 = list(np.linspace(0, puntos_derecha[0].get_x(), 50))
                ax.fill_between(b1, 0, Pmeca.eval_an_array(b1), color='yellow', alpha=0.2)
                b2 = list(np.linspace(puntos_derecha[0].get_x(), o1 + radio - 0.00001, 50))
                ax.fill_between(b2, 0, Limit_excitacion.eval_an_array(b2), color='yellow', alpha=0.2)
    bar.setValue(100)

    ax.set_xlabel('Potencia Reactiva')
    ax.set_ylabel('Potencia Activa')
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)
    # ax.legend(loc='upper right', borderaxespad=0.)


# ---------------------------Polos salientes-------------------------------

def crearpolosaliente(fig, Sn, Vn, Fp, xd, xq, P_motriz, ef, seg_min, seg_prac, text, bar, per_units=False):
    if P_motriz == 0.0: P_motriz = Sn
    if seg_min < 0.05: seg_min = 0.05
    if seg_prac < 0.1: seg_prac = 0.1
    if not per_units:
        text.setText('Calculando parámetros en PU.')
        Zbase = ((Vn) ** 2) / (Sn)
        Vn, Sn, xd, xq, P_motriz = (Vn / Vn), (Sn / Sn), (xd / Zbase), (xq / Zbase), (P_motriz / Sn)

    ax = fig.add_subplot(111)

    if ef == None:
        fp = abs(c.acos(Fp))
        E1 = c.rect(Vn, 0) + (c.rect(xq, c.pi / 2) * c.rect(1, -fp))
        Id = abs(c.sin(fp + c.phase(E1)))
        Ef = abs(E1) + ((xd - xq) * Id)
    else:
        Ef = ef
    if P_motriz == 1: P_motriz = P_motriz + 1
    bar.setValue(5)
    time.sleep(0.01)
    o1, o2, radio = -((Vn ** 2) / xd), -((1 / xq) - (1 / xd)), (Ef * Vn) / xd
    origen = o1 + o2
    x = Symbol('x')
    rango = [z * c.pi / 180 for z in (0.0000001, 10, 15, 25, 45, 75, 89.99)]

    text.setText('Calculando centros.')
    radio_circulito = abs(o2 / 2)
    centro = (o1 + (o2 / 2))
    radio_min = radio_circulito + (radio * seg_min)
    circulito = Function(circles(x, radio_circulito, centro))
    Limit_exci_min = Function(circles(x, radio_min, centro))
    Pmeca = Function(P_motriz)
    bar.setValue(10)
    time.sleep(0.01)
    # ---------------------------------------------------------
    # ---------------------- conseguir puntos para------------------
    # -------------F_practic ,  teorico y exitacion----------------

    teoric_x, teoric_y, practic_x, practic_y, values_x, values_y = [], [], [], [], [], []
    text.setText('Calculando puntos para: estabilidad práctica, teórica y exitación.')
    for j in (1, 0.75, 0.5, 0.25, 0.15, 0.1, 0):

        inter = nsolve(cos(2 * x) * (xd - xq) / (xd * xq) + ((Ef * j / xd) * cos(x)), (0, c.pi / 2), solver='bisect')
        # -----------------------------------------------------------------
        # tengo que verificar que el angulo sea menor a 90:

        if inter < c.pi / 2 > 0:
            punto_de_estabilidad = Function(rectas(inter, origen, x))
        else:
            punto_de_estabilidad = Function(rectas(c.pi / 2, origen, x))

        for i in rango:

            suma = (radio * j)
            rectica = Function(rectas(i, origen, x))

            if i == rango[0]:
                puntosdeintersect = centro + radio_circulito
                values_y.append(suma * abs(c.sin(i)))
            elif i == rango[-1]:
                puntosdeintersect = centro - radio_circulito + 0.00001
                values_y.append(suma * abs(c.sin(i)) + 0.00001)
            else:
                puntosdeintersect = IntersectionManager.num_intersect(rectica, circulito, (
                    centro - radio_circulito + 0.001, centro + radio_circulito - 0.001))
                values_y.append(circulito.eval(puntosdeintersect) + suma * abs(c.sin(i)))
            values_x.append(puntosdeintersect + suma * abs(c.cos(i)))

        if j == 1:

            excitante = FunctionPoints(values_x, values_y, grid=500)
            interpol = list(np.linspace(values_x[0] - 0.00000001, values_x[-1] + 0.00000001, 500))
            ax.plot(interpol, excitante.eval_an_array(interpol), color='black', label='Limite de excitacion')
            Limit_excitacion = excitante

        else:
            excitante = FunctionPoints(values_x, values_y, grid=500)

        sta_teoric = IntersectionManager.num_fun_points(punto_de_estabilidad, excitante)

        if j == 1: inicial = punto_de_estabilidad.eval(sta_teoric[-1])

        teoric_x.append(sta_teoric[-1])
        teoric_y.append(punto_de_estabilidad.eval(sta_teoric[-1]))
        recta_prac = Function(teoric_y[-1] - (inicial * seg_prac))

        if recta_prac.eval(0) <= 0:
            practic_x.append(centro + radio_circulito)
            practic_y.append((0))
        else:
            sta_prac = IntersectionManager.num_fun_points(recta_prac, excitante)
            practic_x.append(sta_prac[-1])
            practic_y.append(recta_prac.eval(sta_prac[-1]))

        values_x.clear()
        values_y.clear()
    bar.setValue(30)
    time.sleep(0.01)
    F_practic = FunctionPoints(practic_x, practic_y, grid=500)
    F_teoric = FunctionPoints(teoric_x, teoric_y, grid=500)
    limit_armadura = Function(sqrt(Vn - x ** 2))
    text.setText('Graficando exitación.')
    # ---------------grafica de circulito--------------------------------

    x5 = list(np.linspace(origen + 0.00001, o1 - 0.000001, 500))
    ax.plot(x5, circulito.eval_an_array(x5), linestyle='--')
    bar.setValue(35)
    time.sleep(0.01)
    # ----> Proceso 3
    text.setText('Calculando puntos de intersección.')
    # -------------------------- puntos de inter para usar get minor contour--------------

    out_izquierda = RegionManager.intersect_functions([limit_armadura, Limit_exci_min, F_practic, Pmeca])
    puntos_izquierda = RegionManager.get_minor_contour(out_izquierda,
                                                       [limit_armadura, Limit_exci_min, F_practic, Pmeca])
    out_derecha = RegionManager.intersect_functions([limit_armadura, Limit_excitacion, Pmeca])
    puntos_derecha = RegionManager.get_minor_contour(out_derecha, [limit_armadura, Limit_excitacion, Pmeca])
    puntos_izquierda = list(filter(lambda x: x.get_x() < 0, puntos_izquierda))
    puntos_derecha = list(filter(lambda x: x.get_x() > 0, puntos_derecha))
    bar.setValue(55)
    time.sleep(0.01)
    # ----> Proceso 4
    # ---------------------------------------------------------------------------------
    # -----------------  puntos de interseccion----------------------------------
    inter_exi_arma = IntersectionManager.fun_intersect(limit_armadura, Limit_exci_min, solution_domain=1)
    inter_arma_Pmec = IntersectionManager.fun_intersect(limit_armadura, Pmeca, solution_domain=1)
    inter_arm_stab = IntersectionManager.fun_and_point(limit_armadura, F_practic)
    inter_exitante_arm = IntersectionManager.fun_and_point(limit_armadura, Limit_excitacion)
    bar.setValue(70)
    time.sleep(0.01)
    # ----> Proceso 5
    # ------------------------------------------------------------------------
    # ----------------- graficar funciones------------------------------
    # --------------------solo plots------------------------------------
    text.setText('Graficando funciones.')
    x1 = list(np.linspace(teoric_x[0] - 0.00000001, teoric_x[-1] + 0.00000001, 25))
    ax.plot(x1, F_teoric.eval_an_array(x1), color='blue', label='limite de estabilidad teorica')

    x2 = list(np.linspace(practic_x[0] - 0.00000001, practic_x[-1] + 0.00000001, 25))
    ax.plot(x2, F_practic.eval_an_array(x2), color='red', label='limite de estabilidad practica')

    x3 = list(np.linspace(-Vn + 0.00001, Vn - 0.00001, 500))
    ax.plot(x3, limit_armadura.eval_an_array(x3), color='green', label='limite de armadura')

    x4 = list(np.linspace(centro + 0.000001, centro + radio_min - 0.000001, 500))
    ax.plot(x4, Limit_exci_min.eval_an_array(x4), label='limite de excitacion minima')
    bar.setValue(80)
    time.sleep(0.01)
    # ----> Proceso 6
    # -------------------------------------------------------------------
    # ------ Puntos de la izquierda-------------------
    # -------------relleno-----------------------------
    text.setText('Rellenando cuadrante izquierdo de la gráfica.')
    if P_motriz > 1:
        if len(puntos_izquierda) == 0:
            pass
        elif puntos_izquierda[0].get_x() < -1:
            puntos_izquierda.pop(0)

        if len(inter_exi_arma) == 0:
            if len(inter_arm_stab) == 0:
                a1 = list(np.linspace(-1, 0, 50))
                ax.fill_between(a1, 0, limit_armadura.eval_an_array(a1), color='yellow', alpha=0.2)
                print('1')

            elif centro > -1:
                #a1 = list(np.linspace(-1, puntos_izquierda[0].get_x(), 10))
                #ax.fill_between(a1, 0, limit_armadura.eval_an_array(a1), color='yellow', alpha=0.2)
                a2 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 10))
                ax.fill_between(a2, 0, F_practic.eval_an_array(a2), color='yellow', alpha=0.2)
                a3 = list(np.linspace(puntos_izquierda[1].get_x(), 0, 50))
                ax.fill_between(a3, 0, limit_armadura.eval_an_array(a3), color='yellow', alpha=0.2)
                print('2')

            else:
                a1 = list(np.linspace(-1, puntos_izquierda[0].get_x(), 10))
                ax.fill_between(a1, 0, limit_armadura.eval_an_array(a1), color='yellow', alpha=0.2)
                a2 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 10))
                ax.fill_between(a2, 0, F_practic.eval_an_array(a2), color='yellow', alpha=0.2)
                a3 = list(np.linspace(puntos_izquierda[1].get_x(), 0, 50))
                ax.fill_between(a3, 0, limit_armadura.eval_an_array(a3), color='yellow', alpha=0.2)
                print('2')


        else:
            if len(puntos_izquierda) == 1:
                a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 50))
                ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1), color='yellow',
                                alpha=0.2)
                a2 = list(np.linspace(centro + radio_min - 0.00001, 0, 50))
                ax.fill_between(a2, 0, limit_armadura.eval_an_array(a2), color='yellow', alpha=0.2)
                print('3')

            elif len(puntos_izquierda) == 2 and inter_arm_stab[-1] > (centro + radio_min):
                a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.000001, 10))
                ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), F_practic.eval_an_array(a1), color='yellow',
                                alpha=0.2)
                a2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 40))
                ax.fill_between(a2, 0, F_practic.eval_an_array(a2), color='yellow', alpha=0.2)
                a3 = list(np.linspace(puntos_izquierda[1].get_x(), 0, 10))
                ax.fill_between(a3, 0, limit_armadura.eval_an_array(a3), color='yellow', alpha=0.2)
                print('4')

            elif len(puntos_izquierda) == 2 and inter_arm_stab[-1] < (centro + radio_min):
                a1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 10))
                ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), F_practic.eval_an_array(a1), color='yellow',
                                alpha=0.2)
                a2 = list(np.linspace(puntos_izquierda[1].get_x(), centro + radio_min - 0.00001, 20))
                ax.fill_between(a2, Limit_exci_min.eval_an_array(a2), limit_armadura.eval_an_array(a2), color='yellow',
                                alpha=0.2)
                a3 = list(np.linspace(centro + radio_min - 0.00001, 0, 30))
                ax.fill_between(a3, 0, limit_armadura.eval_an_array(a3), color='yellow', alpha=0.2)
                print('5')

            elif len(puntos_izquierda) == 3 and inter_arm_stab[0] < (centro + radio_min) and inter_arm_stab[-1] > (
                    centro + radio_min):
                a1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 10))
                ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1), color='yellow',
                                alpha=0.2)
                a2 = list(np.linspace(puntos_izquierda[1].get_x(), centro + radio_min - 0.00001, 40))
                ax.fill_between(a2, Limit_exci_min.eval_an_array(a2), F_practic.eval_an_array(a2), color='yellow',
                                alpha=0.2)
                a3 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[2].get_x(), 30))
                ax.fill_between(a3, 0, F_practic.eval_an_array(a3), color='yellow', alpha=0.2)
                a4 = list(np.linspace(puntos_izquierda[2].get_x(), 0, 30))
                ax.fill_between(a4, 0, limit_armadura.eval_an_array(a4), color='yellow', alpha=0.2)
                print('6')

            elif len(puntos_izquierda) == 3 and inter_arm_stab[0] > (centro + radio_min):
                a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 30))
                ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1), color='yellow',
                                alpha=0.2)
                a2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 30))
                ax.fill_between(a2, 0, limit_armadura.eval_an_array(a2), color='yellow', alpha=0.2)
                a3 = list(np.linspace(puntos_izquierda[1].get_x(), puntos_izquierda[2].get_x(), 30))
                ax.fill_between(a3, 0, F_practic.eval_an_array(a3), color='yellow', alpha=0.2)
                a4 = list(np.linspace(puntos_izquierda[2].get_x(), 0, 30))
                ax.fill_between(a4, 0, limit_armadura.eval_an_array(a4), color='yellow', alpha=0.2)
                print('7')

            elif len(puntos_izquierda) == 3 and inter_arm_stab[0] < (centro + radio_min) and inter_arm_stab[-1] < (
                    centro + radio_min):
                a1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 30))
                ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1), color='yellow',
                                alpha=0.2)
                a2 = list(np.linspace(puntos_izquierda[1].get_x(), puntos_izquierda[2].get_x(), 30))
                ax.fill_between(a2, Limit_exci_min.eval_an_array(a2), F_practic.eval_an_array(a2), color='yellow',
                                alpha=0.2)
                a3 = list(np.linspace(puntos_izquierda[2].get_x(), centro + radio_min - 0.00001, 30))
                ax.fill_between(a3, Limit_exci_min.eval_an_array(a3), limit_armadura.eval_an_array(a3), color='yellow',
                                alpha=0.2)
                a4 = list(np.linspace(centro + radio_min - 0.00001, 0, 30))
                ax.fill_between(a4, 0, limit_armadura.eval_an_array(a4), color='yellow', alpha=0.2)
                print('8')
    else:
        if len(puntos_izquierda) == 0:
            pass
        elif puntos_izquierda[0].get_x() < -1:
            puntos_izquierda.pop(0)

        pm = list(np.linspace(o1, o1 + radio, 10))
        ax.plot(pm, Pmeca.eval_an_array(pm), label='Limite de Potencia')
        if len(inter_exi_arma) == 0:
            if len(inter_arm_stab) == 0:
                a1 = list(np.linspace(-1, puntos_izquierda[-1].get_x(), 30))
                ax.fill_between(a1, 0, limit_armadura.eval_an_array(a1), color='yellow', alpha=0.2)
                a2 = list(np.linspace(puntos_izquierda[-1].get_x(), 0, 50))
                ax.fill_between(a2, 0, Pmeca.eval_an_array(a2), color='yellow', alpha=0.2)
                print('1')
            else:
                if len(puntos_izquierda) == 2 and centro < -1:
                    a1 = list(np.linspace(-1, puntos_izquierda[0].get_x(), 30))
                    ax.fill_between(a1, 0, limit_armadura.eval_an_array(a1), color='yellow', alpha=0.2)
                    a2 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 30))
                    ax.fill_between(a2, 0, F_practic.eval_an_array(a2), color='yellow', alpha=0.2)
                    a3 = list(np.linspace(puntos_izquierda[1].get_x(), 0, 30))
                    ax.fill_between(a3, 0, Pmeca.eval_an_array(a3), color='yellow', alpha=0.2)
                    print('2')
                elif len(puntos_izquierda) == 2 and centro > -1:
                    a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 30))
                    ax.fill_between(a1, 0, F_practic.eval_an_array(a1), color='yellow', alpha=0.2)
                    a2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 30))
                    ax.fill_between(a2, 0, F_practic.eval_an_array(a2), color='yellow', alpha=0.2)
                    a3 = list(np.linspace(puntos_izquierda[1].get_x(), 0, 30))
                    ax.fill_between(a3, 0, Pmeca.eval_an_array(a3), color='yellow', alpha=0.2)
                    print('2')

                elif len(puntos_izquierda) == 3:
                    a1 = list(np.linspace(-1, puntos_izquierda[0].get_x(), 30))
                    ax.fill_between(a1, 0, limit_armadura.eval_an_array(a1), color='yellow', alpha=0.2)
                    a2 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 30))
                    ax.fill_between(a2, 0, F_practic.eval_an_array(a2), color='yellow', alpha=0.2)
                    a3 = list(np.linspace(puntos_izquierda[1].get_x(), puntos_izquierda[2].get_x(), 30))
                    ax.fill_between(a3, 0, limit_armadura.eval_an_array(a3), color='yellow', alpha=0.2)
                    a4 = list(np.linspace(puntos_izquierda[2].get_x(), 0, 30))
                    ax.fill_between(a4, 0, Pmeca.eval_an_array(a1), color='yellow', alpha=0.2)
                    print('3')
        else:
            if len(puntos_izquierda) == 2 and centro < -1 and len(inter_arm_stab) != 0:
                a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 30))
                ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), F_practic.eval_an_array(a1), color='yellow',
                                alpha=0.2)
                a2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 30))
                ax.fill_between(a2, 0, F_practic.eval_an_array(a2), color='yellow', alpha=0.2)
                a3 = list(np.linspace(puntos_izquierda[1].get_x(), 0, 30))
                ax.fill_between(a3, 0, Pmeca.eval_an_array(a3), color='yellow', alpha=0.2)
                print('4')
            elif len(puntos_izquierda) == 2 and centro < -1 and len(inter_arm_stab) == 0 and inter_arma_Pmec[
                0] > centro + radio_min:
                a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 30))
                ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1), color='yellow',
                                alpha=0.2)
                a2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 30))
                ax.fill_between(a2, 0, limit_armadura.eval_an_array(a2), color='yellow', alpha=0.2)
                a3 = list(np.linspace(puntos_izquierda[1].get_x(), 0, 30))
                ax.fill_between(a3, 0, Pmeca.eval_an_array(a3), color='yellow', alpha=0.2)
                print('5')
            elif len(puntos_izquierda) == 2 and centro < -1 and len(inter_arm_stab) == 0 and inter_arma_Pmec[
                0] < centro + radio_min:
                a1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 30))
                ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1), color='yellow',
                                alpha=0.2)
                a2 = list(np.linspace(puntos_izquierda[1].get_x(), centro + radio_min - 0.00001, 30))
                ax.fill_between(a2, 0, Pmeca.eval_an_array(a2), color='yellow', alpha=0.2)
                a3 = list(np.linspace(centro + radio_min - 0.00001, 0, 30))
                ax.fill_between(a3, 0, Pmeca.eval_an_array(a3), color='yellow', alpha=0.2)
            elif len(puntos_izquierda) == 2 and centro > -1:
                a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.0001, 30))
                ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), F_practic.eval_an_array(a1), color='yellow',
                                alpha=0.2)
                a2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 30))
                ax.fill_between(a2, 0, F_practic.eval_an_array(a2), color='yellow', alpha=0.2)
                a3 = list(np.linspace(puntos_izquierda[1].get_x(), 0, 30))
                ax.fill_between(a3, 0, Pmeca.eval_an_array(a3), color='yellow', alpha=0.2)
                print('5')
            elif len(puntos_izquierda) == 3 and inter_arm_stab[-1] < inter_arma_Pmec[0]:
                a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 30))
                ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), F_practic.eval_an_array(a1), color='yellow',
                                alpha=0.2)
                a2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 30))
                ax.fill_between(a2, 0, F_practic.eval_an_array(a2), color='yellow', alpha=0.2)
                a3 = list(np.linspace(puntos_izquierda[1].get_x(), puntos_izquierda[2].get_x(), 30))
                ax.fill_between(a3, 0, limit_armadura.eval_an_array(a3), color='yellow', alpha=0.2)
                a4 = list(np.linspace(puntos_izquierda[2].get_x(), 0, 30))
                ax.fill_between(a4, 0, Pmeca.eval_an_array(a4), color='yellow', alpha=0.2)
                print('6')
            elif len(puntos_izquierda) == 3 and inter_arm_stab[-1] > inter_arma_Pmec[0] and inter_arm_stab[
                0] < centro + radio_min:
                a1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 30))
                ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1), color='yellow',
                                alpha=0.2)
                a2 = list(np.linspace(puntos_izquierda[1].get_x(), centro + radio_min - 0.00001, 30))
                ax.fill_between(a2, Limit_exci_min.eval_an_array(a2), F_practic.eval_an_array(a2), color='yellow',
                                alpha=0.2)
                a3 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[2].get_x(), 30))
                ax.fill_between(a3, 0, F_practic.eval_an_array(a3), color='yellow', alpha=0.2)
                a4 = list(np.linspace(puntos_izquierda[2].get_x(), 0, 30))
                ax.fill_between(a4, 0, Pmeca.eval_an_array(a4), color='yellow', alpha=0.2)
                print('7')
            elif len(puntos_izquierda) == 3 and inter_arm_stab[-1] > inter_arma_Pmec[0] and inter_arm_stab[
                0] > centro + radio_min:
                a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 30))
                ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1), color='yellow',
                                alpha=0.2)
                a2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 30))
                ax.fill_between(a2, 0, limit_armadura.eval_an_array(a2), color='yellow', alpha=0.2)
                a3 = list(np.linspace(puntos_izquierda[1].get_x(), puntos_izquierda[2].get_x(), 30))
                ax.fill_between(a3, 0, F_practic.eval_an_array(a3), color='yellow', alpha=0.2)
                a4 = list(np.linspace(puntos_izquierda[2].get_x(), 0, 30))
                ax.fill_between(a4, 0, Pmeca.eval_an_array(a4), color='yellow', alpha=0.2)
                print('8')
            elif len(puntos_izquierda) == 4 and inter_arm_stab[0] < centro + radio_min:
                a1 = list(np.linspace(puntos_izquierda[0].get_x(), puntos_izquierda[1].get_x(), 30))
                ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1), color='yellow',
                                alpha=0.2)
                a2 = list(np.linspace(puntos_izquierda[1].get_x(), centro + radio_min - 0.00001, 30))
                ax.fill_between(a2, Limit_exci_min.eval_an_array(a2), F_practic.eval_an_array(a2), color='yellow',
                                alpha=0.2)
                a3 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[2].get_x(), 30))
                ax.fill_between(a3, 0, F_practic.eval_an_array(a3), color='yellow', alpha=0.2)
                a4 = list(np.linspace(puntos_izquierda[2].get_x(), puntos_izquierda[3].get_x(), 30))
                ax.fill_between(a4, 0, limit_armadura.eval_an_array(a4), color='yellow', alpha=0.2)
                a5 = list(np.linspace(puntos_izquierda[3].get_x(), 0, 30))
                ax.fill_between(a5, 0, Pmeca.eval_an_array(a5), color='yellow', alpha=0.2)
                print('9')
            elif len(puntos_izquierda) == 4 and inter_arm_stab[0] > centro + radio_min:
                a1 = list(np.linspace(puntos_izquierda[0].get_x(), centro + radio_min - 0.00001, 30))
                ax.fill_between(a1, Limit_exci_min.eval_an_array(a1), limit_armadura.eval_an_array(a1), color='yellow',
                                alpha=0.2)
                a2 = list(np.linspace(centro + radio_min - 0.00001, puntos_izquierda[1].get_x(), 30))
                ax.fill_between(a2, 0, limit_armadura.eval_an_array(a2), color='yellow', alpha=0.2)
                a3 = list(np.linspace(puntos_izquierda[1].get_x(), puntos_izquierda[2].get_x(), 30))
                ax.fill_between(a3, 0, F_practic.eval_an_array(a3), color='yellow', alpha=0.2)
                a4 = list(np.linspace(puntos_izquierda[2].get_x(), puntos_izquierda[3].get_x(), 30))
                ax.fill_between(a4, 0, limit_armadura.eval_an_array(a4), color='yellow', alpha=0.2)
                a5 = list(np.linspace(puntos_izquierda[3].get_x(), 0, 30))
                ax.fill_between(a5, 0, Pmeca.eval_an_array(a5), color='yellow', alpha=0.2)
    bar.setValue(90)
    time.sleep(0.01)
    # ----> Proceso 7
    # ---------------------------------------------------------------------------------------------------
    # --------------------Puntos de la derecha---------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------
    text.setText('Rellenando cuadrante derecho del gráfico')
    if P_motriz > 1:
        if len(inter_exitante_arm) == 0:
            b1 = list(np.linspace(0, 1, 50))
            ax.fill_between(b1, 0, limit_armadura.eval_an_array(b1), color='yellow', alpha=0.2)
        else:
            b1 = list(np.linspace(0, puntos_derecha[0].get_x(), 50))
            ax.fill_between(b1, 0, limit_armadura.eval_an_array(b1), color='yellow', alpha=0.2)
            b2 = list(np.linspace(puntos_derecha[0].get_x(), o1 + radio - 0.00001, 50))
            ax.fill_between(b2, 0, Limit_excitacion.eval_an_array(b2), color='yellow', alpha=0.2)
    else:
        if len(inter_exitante_arm) == 0:
            b1 = list(np.linspace(0, puntos_derecha[0].get_x(), 50))
            ax.fill_between(b1, 0, Pmeca.eval_an_array(b1), color='yellow', alpha=0.2)
            b2 = list(np.linspace(puntos_derecha[0].get_x(), 1, 50))
            ax.fill_between(b2, 0, limit_armadura.eval_an_array(b2), color='yellow', alpha=0.2)

        else:
            if inter_exitante_arm[0] > inter_arma_Pmec[-1]:
                b1 = list(np.linspace(0, puntos_derecha[0].get_x(), 50))
                ax.fill_between(b1, 0, Pmeca.eval_an_array(b1), color='yellow', alpha=0.2)
                b2 = list(np.linspace(puntos_derecha[0].get_x(), puntos_derecha[1].get_x(), 50))
                ax.fill_between(b2, 0, limit_armadura.eval_an_array(b2), color='yellow', alpha=0.2)
                b3 = list(np.linspace(puntos_derecha[1].get_x(), o1 + radio - 0.00001, 50))
                ax.fill_between(b3, 0, Limit_excitacion.eval_an_array(b3), color='yellow', alpha=0.2)

            else:
                b1 = list(np.linspace(0, puntos_derecha[0].get_x(), 50))
                ax.fill_between(b1, 0, Pmeca.eval_an_array(b1), color='yellow', alpha=0.2)
                b2 = list(np.linspace(puntos_derecha[0].get_x(), o1 + radio - 0.00001, 50))
                ax.fill_between(b2, 0, Limit_excitacion.eval_an_array(b2), color='yellow', alpha=0.2)
    bar.setValue(100)
    ax.set_xlabel('Potencia Reactiva')
    ax.set_ylabel('Potencia Activa')
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)
