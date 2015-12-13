import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def label(event):
        ind = event.ind
        print('onpick3 scatter:', ind, npy.take(x, ind), npy.take(y, ind))


def plot_actual(G, edges):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = []
    y = []
    z = []
    for sensor in G.sensors:
        x.append(sensor.actualPos.x)
        y.append(sensor.actualPos.y)
        z.append(sensor.actualPos.z)
    if edges:
        for i in range(G.V):
            for j in range(G.V):
                if G.is_adj[i][j]:
                    ax.plot([x[i], x[j]], [y[i], y[j]], [z[i], z[j]], c='k')
                else:
                    print(str(G.is_adj[i][j]))

    ax.scatter(x, y, z, c='k')
    plt.show()



