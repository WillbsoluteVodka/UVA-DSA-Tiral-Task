import matplotlib.pyplot as plt

def threeD_side_by_side(raven_df, trakstar_df, x, y, z, title=""):
    x_coords_raven = raven_df[x]
    y_coords_raven = raven_df[y]
    z_coords_raven = raven_df[z]

    x_coords_trakstar = trakstar_df[x]
    y_coords_trakstar = trakstar_df[y]
    z_coords_trakstar = trakstar_df[z]

    plt.subplot(2, 3, 1)
    plt.plot(x_coords_raven, y_coords_raven, color='blue')
    plt.title('Raven Dataset')
    plt.xlabel(x)
    plt.ylabel(y)

    plt.subplot(2, 3, 2)
    plt.plot(x_coords_raven, z_coords_raven, color='blue')
    plt.title('Raven Dataset')
    plt.xlabel(x)
    plt.ylabel(z)

    plt.subplot(2, 3, 3)
    plt.plot(y_coords_raven, z_coords_raven, color='blue')
    plt.title('Raven Dataset')
    plt.xlabel(y)
    plt.ylabel(z)

    plt.subplot(2, 3, 4)
    plt.plot(x_coords_trakstar, y_coords_trakstar, color='green')
    plt.title('TrakStar Dataset')
    plt.xlabel(x)
    plt.ylabel(y)

    plt.subplot(2, 3, 5)
    plt.plot(x_coords_trakstar, z_coords_trakstar, color='green')
    plt.title('TrakStar Dataset')
    plt.xlabel(x)
    plt.ylabel(z)

    plt.subplot(2, 3, 6)
    plt.plot(y_coords_trakstar, z_coords_trakstar, color='green')
    plt.title('TrakStar Dataset')
    plt.xlabel(y)
    plt.ylabel(z)

    plt.suptitle(title)
    plt.show()

def oneD_side_by_side(raven_df, trakstar_df, var, title=""):

    plt.subplot(1, 2, 1)
    plt.plot(raven_df['Frame'],raven_df[var], color = 'blue')
    plt.xlabel("Frame")
    plt.ylabel(var)
    plt.title("Raven Dataset")

    plt.subplot(1, 2, 2)
    plt.plot(trakstar_df['Relative frame #'], trakstar_df[var],color = 'green')
    plt.xlabel("Frame")
    plt.ylabel(var)
    plt.title("Trakstar Dataset")

    plt.suptitle(title+" Comparison")
    plt.show()

def threeD_overlap(raven_df, trakstar_df, x, y, z, title=""):
    x_coords_raven = raven_df[x]
    y_coords_raven = raven_df[y]
    z_coords_raven = raven_df[z]

    x_coords_trakstar = trakstar_df[x]
    y_coords_trakstar = trakstar_df[y]
    z_coords_trakstar = trakstar_df[z]

    plt.subplot(1, 3, 1)
    plt.plot(x_coords_raven, y_coords_raven, label='Raven', color='blue', alpha = 0.5)
    plt.plot(x_coords_trakstar, y_coords_trakstar, label='TrakStar', color='red', alpha = 0.5)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend()

    plt.subplot(1, 3, 2)
    plt.plot(x_coords_raven, z_coords_raven, label='Raven', color='blue', alpha = 0.5)
    plt.plot(x_coords_trakstar, z_coords_trakstar, label='TrakStar', color='red', alpha = 0.5)
    plt.xlabel(x)
    plt.ylabel(z)
    plt.legend()

    plt.subplot(1, 3, 3)
    plt.plot(y_coords_raven, z_coords_raven, label='Raven', color='blue', alpha = 0.5)
    plt.plot(y_coords_trakstar, z_coords_trakstar, label='TrakStar', color='red', alpha = 0.5)
    plt.xlabel(y)
    plt.ylabel(z)
    plt.legend()


    plt.suptitle(title)
    plt.show()


def oneD_overlap(raven_df, trakstar_df, var, title=""):

    plt.plot(raven_df['Frame'],raven_df[var], label='Raven', color='blue', alpha=0.5)
    plt.plot(trakstar_df['Relative frame #'], trakstar_df[var], label='TrakStar', color='red', alpha=0.5)
    plt.xlabel("Frame")
    plt.ylabel(var)
    plt.legend()
    plt.title(var)
    plt.show()