from IPoint import IPoint
from IntersectionManager import *
from sympy import Symbol


def clean_by_x(points: list[IPoint]):
    excluir = set()
    for p_i in points:
        for p_j in points:
            if p_i is p_j or p_j in excluir:
                continue
            elif min(p_i.get_x(), 0) <= p_j.get_x() <= max(p_i.get_x(), 0):
                if p_i.get_y() >= p_j.get_y():
                    excluir.add(p_i)
                    break
    return set(points) - excluir


def clean_by_y(points: list[IPoint], functions):
    excluir = set()
    for p_i in points:
        for f_i in functions:
            if f_i.eval(p_i.get_x()) is None:
                continue
            elif f_i.eval(p_i.get_x()) < p_i.get_y():
                excluir.add(p_i)
    return set(points) - excluir


def get_minor_contour(points: list[IPoint], functions: list):
    intersect = []
    exclude = []
    min_sc = None
    min_fc = None
    for p_i in points:
        if p_i.get_x() == 0:
            exclude.append(p_i)
        elif p_i.get_y() == 0:
            if p_i.get_x() < 0:

                if min_sc is None:
                    min_sc = p_i
                elif p_i.get_x() > min_sc.get_x():
                    exclude.append(min_sc)
                    min_sc = p_i
                elif p_i.get_x() == min_sc.get_x():
                    x = p_i.get_x()
                    fun_p_i = p_i.major_after()
                    fun_sc = min_sc.major_after()
                    if fun_p_i.eval(x + 0.1) > fun_sc.eval(x + 0.1):
                        exclude.append(p_i)
                    else:
                        exclude.append(min_sc)
                        min_sc = p_i
                else:
                    exclude.append(p_i)
            else:

                if min_fc is None:
                    min_fc = p_i
                elif p_i.get_x() < min_fc.get_x():
                    exclude.append(min_fc)
                    min_fc = p_i
                else:
                    exclude.append(p_i)
        else:
            for fun in functions:

                if not (fun is p_i.get_f_1() or fun is p_i.get_f_2()):
                    if isinstance(fun, Function):
                        aux_x = [i * (p_i.get_x()) / 4 for i in range(5)]
                        aux_y = [i * (p_i.get_y()) / 4 for i in range(5)]
                        aux_fun_p = FunctionPoints(aux_x, aux_y, grid=50)
                        intersect = fun_and_point(fun, aux_fun_p, operation='speed')

                    elif isinstance(fun, FunctionPoints):
                        m = round(p_i.get_y()/p_i.get_x(), 5)
                        aux_fun_p = Function(m * Symbol('x'))
                        intersect = fun_and_point(aux_fun_p, fun)

                    if len(intersect) != 0:

                        for i in intersect:
                            if p_i.get_x() < 0 and (i - p_i.get_x() > 0) \
                                    or p_i.get_x() > 0 and (i - p_i.get_x() < 0):
                                exclude.append(p_i)
                                break
    out_aux = list(set(points)-set(exclude))
    out_aux.sort(key=lambda x: x.get_x())
    return out_aux


def get_centroid(points: list[IPoint]):
    x, y = 0, 0
    for point in points:
        x = x + point.get_x()
        y = y + point.get_y()
    return [x/len(points), y/len(points)]


def intersect_functions(fun_array: list, order=True) -> list[IPoint]:
    out_array = []
    # Realiza una intersección de la combinación de todas las funciones
    for fun in fun_array:
        # Define los extremos del sub recorrido
        start = fun_array.index(fun) + 1
        end = len(fun_array)
        # Ciclo para interceptar a la función actual fun con las funciones adelante en el arreglo
        for i in range(start, end):
            # Verifica que fun sea Function
            if isinstance(fun, Function):

                # Verifica que la función i-ésima sea Function para emplear fun_intersection
                if isinstance(fun_array[i], Function):
                    intersect = fun_intersect(fun, fun_array[i])
                    for x_i in intersect:
                        if fun.eval(x_i) is None and fun_array[i].eval(x_i) is None:
                            continue
                        else:
                            fun_eval = fun_array[i].eval(x_i) if fun.eval(x_i) is None else fun.eval(x_i)
                            out_array.append(IPoint(x_i, round(fun_eval, 5), fun, fun_array[i]))

                elif isinstance(fun_array[i], FunctionPoints):
                    intersect = fun_and_point(fun, fun_array[i])
                    for x_i in intersect:
                        out_array.append(IPoint(x_i, round(fun.eval(x_i), 5), fun, fun_array[i]))

            # Verifica que la función i-ésima sea FunctionPoints para emplear fun_and_points
            elif isinstance(fun, FunctionPoints):
                if isinstance(fun_array[i], Function):
                    intersect = fun_and_point(fun_array[i], fun)
                    for x_i in intersect:
                        out_array.append(IPoint(x_i, fun.eval(x_i), fun, fun_array[i]))
                elif isinstance(fun_array[i], FunctionPoints):
                    raise TypeError('There is no support for the intersection between two FunctionPoints.')
    if order:
        out_array.sort(key=lambda x: x.get_x())
    return out_array
