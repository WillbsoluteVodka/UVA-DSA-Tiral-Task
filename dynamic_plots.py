import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def dynamic_plot_demo(raven_df,video_path):
    cap = cv.VideoCapture(video_path)
    total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    print(f"Total number of frames: {total_frames}")

    frame_num = 0
    fig, ax = plt.subplots()
    x_data, y_data = [], []
    line, = ax.plot([], [], 'r-')

    ax.set_xlim(0, total_frames)
    ax.set_ylim(raven_df['PSML_position_x'].min(), raven_df['PSML_position_x'].max())
    ax.set_xlabel('Frame')
    ax.set_ylabel('PSML_position_x')

    def update_plot(frame_num):
        x_data.append(frame_num)
        if frame_num < len(raven_df):
            y_data.append(raven_df.loc[frame_num, 'PSML_position_x'])
        else:
            y_data.append(np.median(raven_df['PSML_position_x']))
        line.set_data(x_data, y_data)
        fig.canvas.draw()
        plt.pause(0.001)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('Video with PSML_position_x Value', gray)

        update_plot(frame_num)
        frame_num += 1

        if cv.waitKey(10) == ord('q'):
            break

        if frame_num >= total_frames:
            break

    cap.release()
    cv.destroyAllWindows()
    plt.close()
