
import time
import graficar
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

if __name__ == '__main__':

    Sn = 1500000
    Vn = 3000
    Fp = 0.8
    Xd = 2
    Xq = 1.5
    P_motriz = 1300000

    # --------------------------------------
    #  esto es para probar con un ef o sin ello
    # --------------------------------------

    try:
        ef = float(input("tension maxima de campo en PU: "))
    except ValueError:
        ef = None

    fig = plt.figure()

    # -----------------------------------------------------------------------------

    t1 = time.time()
    graficar.crear(fig, Sn, Vn, Fp, Xd, P_motriz, ef, 0.05, 0.1)
    t2 = time.time()
    print(t2 - t1)

    plt.show()
