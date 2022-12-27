from graficar import *
import matplotlib.pyplot as plt
import matplotlib


matplotlib.use('TkAgg')

if __name__ == '__main__':
    figura = plt.figure()
    # Sn, Vn, Fp, xd, xq, P_motriz, ef, seg_min, seg_prac, text, bar, per_units=False):
    crearpolosaliente(figura,
                      1,
                      1,
                      0.85,
                      1.1,
                      0.7,
                      None,
                      2,
                      0.05,
                      0.1,
                      None,
                      None,
                      per_units=True
                    )
    plt.show()



