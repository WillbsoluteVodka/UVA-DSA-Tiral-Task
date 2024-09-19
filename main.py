from load_data import *
from stacked_plots import *
from comparision_plots import *
from dynamic_plots import *
from EDA import *

######## LOAD DATA
raven_df, trakstar_df = load_all_data('Peg_Transfer_SKay_T2_27-01-2023_16-11-31/Peg_Transfer_S01_T02.csv',
                                      'Peg_Transfer_SKay_T2_27-01-2023_16-11-31/Peg_Transfer_S01_T02_trakStar_final.csv')

# ######## STACK PLOTS
# stack_plots_trakstar(trakstar_df, 'Peg_Transfer_SKay_T2_27-01-2023_16-11-31')
# stack_plots_raven(raven_df, "Peg_Transfer_SKay_T2_27-01-2023_16-11-31")

######## SIDE BY SIDE PLOTS
# threeD_side_by_side(raven_df, trakstar_df, 'PSML_position_x', 'PSML_position_y', 'PSML_position_z', 'PSML_position')
# oneD_side_by_side(raven_df, trakstar_df, 'PSML_gripper_angle', 'PSML_gripper_angle')
#
# ######## OVERLAP PLOTS
threeD_overlap(raven_df, trakstar_df, 'PSMR_position_x', 'PSMR_position_y', 'PSMR_position_z', 'PSMR_position')
# oneD_overlap(raven_df, trakstar_df, 'PSMR_gripper_angle', 'PSMR_gripper_angle')
#
# ######## VARIABLE EDA
# # Since most of them have been visualized in other parts, this part would only draw out the velocity variables
# EDA(raven_df, 'PSML_velocity_x', 'PSML_velocity_x to Frame', 'Peg_Transfer_SKay_T2_27-01-2023_16-11-31')
# EDA(raven_df, 'PSML_velocity_y', 'PSML_velocity_x to Frame', 'Peg_Transfer_SKay_T2_27-01-2023_16-11-31')
# EDA(raven_df, 'PSML_velocity_z', 'PSML_velocity_x to Frame', 'Peg_Transfer_SKay_T2_27-01-2023_16-11-31')
# EDA(raven_df, 'PSMR_velocity_x', 'PSML_velocity_x to Frame', 'Peg_Transfer_SKay_T2_27-01-2023_16-11-31')
# EDA(raven_df, 'PSMR_velocity_y', 'PSML_velocity_x to Frame', 'Peg_Transfer_SKay_T2_27-01-2023_16-11-31')
# EDA(raven_df, 'PSMR_velocity_z', 'PSML_velocity_x to Frame', 'Peg_Transfer_SKay_T2_27-01-2023_16-11-31')
#
# ######## PLAY DYNAMIC PLOT WITH VIDEO
# dynamic_plot_demo(raven_df,'Peg_Transfer_SKay_T2_27-01-2023_16-11-31/Peg_Transfer_SKay_T2_27-01-2023_16-11-31_video.mp4')
#
