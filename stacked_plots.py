import matplotlib.pyplot as plt


def stack_plots_trakstar(trakstar_df, path=None):
    columns_to_plot = ['PSML_position_x', 'PSML_position_y', 'PSML_position_z',
                       'PSMR_position_x', 'PSMR_position_y', 'PSMR_position_z',
                       'PSML_gripper_angle', 'PSMR_gripper_angle']

    trakstar_df[columns_to_plot].plot(subplots=True, layout=(len(columns_to_plot), 1), figsize=(10, 12), sharex=True,
                                      legend=True)
    plt.xlabel('Relative Frame')
    plt.suptitle('Stacked Plot For Trakstar Dataset')

    if path:
        path = path + "/trakstar_stackplot"
        plt.savefig(path)
        print("Plot saved to " + path)

    plt.show()


def stack_plots_raven(raven_df, path=None):
    columns_to_plot = ['PSML_position_x', 'PSML_position_y', 'PSML_position_z',
                       'PSMR_position_x', 'PSMR_position_y', 'PSMR_position_z',
                       'PSML_gripper_angle', 'PSMR_gripper_angle',
                       'PSML_velocity_x', 'PSML_velocity_y', 'PSML_velocity_z',
                       'PSMR_velocity_x', 'PSMR_velocity_y', 'PSMR_velocity_z']

    raven_df[columns_to_plot].plot(subplots=True, layout=(len(columns_to_plot), 1), figsize=(10, 12), sharex=True,
                                   legend=True)
    plt.xlabel('Frame')
    plt.suptitle('Stacked Plot For Raven Dataset')

    if path:
        path = path + "/raven_stackplot"
        plt.savefig(path)
        print("Plot saved to " + path)

    plt.show()
