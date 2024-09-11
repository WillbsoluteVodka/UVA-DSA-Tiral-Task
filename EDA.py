import matplotlib.pyplot as plt

def EDA(raven_df, var, title="", path=None):

    plt.plot(raven_df['Frame'],raven_df[var])
    plt.xlabel("Frame")
    plt.ylabel(var)
    plt.legend()
    plt.title(var)

    if path:
        path = path + "/" + var + "_EDA"
        plt.savefig(path)
        print("Plot saved to " + path)

    plt.show()