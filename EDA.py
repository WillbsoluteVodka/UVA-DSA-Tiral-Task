import matplotlib.pyplot as plt
import pandas as pd

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

def EDA_diff_box(raven_df, trakstar_df):
    # Calculate the differences between the two columns

    plt.figure(figsize=(16, 9))


    plt.subplot(2, 3, 1)
    position_x_diff = raven_df['PSML_position_x'] - trakstar_df['PSML_position_x']
    plt.boxplot(position_x_diff.dropna(), vert=False)  # Drop any NaN values
    plt.title(f'Box Plot of PSML_position_x differences')
    plt.xlabel('Difference')

    plt.subplot(2, 3, 2)
    position_y_diff = raven_df['PSML_position_y'] - trakstar_df['PSML_position_y']
    plt.boxplot(position_y_diff.dropna(), vert=False)  # Drop any NaN values
    plt.title(f'Box Plot of PSML_position_y differences')
    plt.xlabel('Difference')

    plt.subplot(2, 3, 3)
    position_z_diff = raven_df['PSML_position_z'] - trakstar_df['PSML_position_z']
    plt.boxplot(position_z_diff.dropna(), vert=False)  # Drop any NaN values
    plt.title(f'Box Plot of PSML_position_z differences')
    plt.xlabel('Difference')

    plt.subplot(2, 3, 4)
    position_x_diff = raven_df['PSMR_position_x'] - trakstar_df['PSMR_position_x']
    plt.boxplot(position_x_diff.dropna(), vert=False)  # Drop any NaN values
    plt.title(f'Box Plot of PSMR_position_x differences')
    plt.xlabel('Difference')

    plt.subplot(2, 3, 5)
    position_y_diff = raven_df['PSMR_position_y'] - trakstar_df['PSMR_position_y']
    plt.boxplot(position_y_diff.dropna(), vert=False)  # Drop any NaN values
    plt.title(f'Box Plot of PSMR_position_y differences')
    plt.xlabel('Difference')

    plt.subplot(2, 3, 6)
    position_z_diff = raven_df['PSMR_position_z'] - trakstar_df['PSMR_position_z']
    plt.boxplot(position_z_diff.dropna(), vert=False)  # Drop any NaN values
    plt.title(f'Box Plot of PSMR_position_z differences')
    plt.xlabel('Difference')


    plt.show()