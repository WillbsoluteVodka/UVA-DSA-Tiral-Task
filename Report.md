From the stacked plots of the TrakStar dataset, we can observe that:
1. Both PSML_gripper_angle and PSMR_gripper_angle display similar trends, where the gripper remains in a neutral position for a considerable amount of time with rapid spikes. These spikes likely indicate brief periods of gripping or releasing objects.
2. PSML_position_x shows significant variation, with some relatively flat periods interrupted by sudden changes in position. This suggests the movement is not smooth and exhibits abrupt shifts.
    PSML_position_y and PSML_position_z both exhibit more consistent movement, with smaller fluctuations. However, there are still notable changes, indicating moments where the movements in the Y and Z axes become more pronounced. 
3. Compared to the PSML position data, the PSMR related positions all exhibit rather drastic changes, indicating more movements with the right arm than the left arm.

From the stacked plots of the raven dataset, we can observe that:
1. The trends and observations noted in the TrakStar dataset still hold here. The overall movement patterns in the PSML and PSMR positions are generally similar, with the same fluctuations and shifts occurring across the X, Y, and Z axes.
This consistency suggests a high degree of similarity between the two systems, indicating that the robotic arms are doing generally the same movements as the tracked data.
2. The newly added velocity graphs show clear synchronization with their corresponding position graphs. Increases in velocity coincide with sharp changes in position, as expected.

The side-by-side plots of PSML_Position and PSML_angle, as well as the overlap plots of PSMR_Position and PSMR_angle, consistently indicate that the movements recorded by the two systems (Raven and TrakStar) are highly similar. The coordination between position and angle across both systems shows only minor variations, reinforcing the idea that both systems track movements in a very similar manner.
