import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
def print_in_excel_table(value, sheet_name, row_header, column_header, output_file):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(output_file, sheet_name=sheet_name, index_col=0)
    # Find the row and column index based on the row and column headers
    try:
        row_index = df.index.get_loc(row_header)
    except KeyError:
        print(f"Row header '{row_header}' not found.")
        return
    try:
        column_index = df.columns.get_loc(column_header)
    except KeyError:
        print(f"Column header '{column_header}' not found.")
        return

    # Set value in specific cell
    df.iloc[row_index, column_index] = value

    # Write DataFrame back to Excel file
    df.to_excel(output_file, sheet_name=sheet_name)
def get_data(data_use, FB_param, input_path, excl=[]):
    if data_use == "GDI":
        parameters_subpaths = [
            "left_pelvis_angles.Angles.x.Left-normalised", "right_pelvis_angles.Angles.x.Right-normalised",
            "left_pelvis_angles.Angles.y.Left-normalised", "right_pelvis_angles.Angles.y.Right-normalised",
            "left_pelvis_angles.Angles.z.Left-normalised", "right_pelvis_angles.Angles.z.Right-normalised",
            "left_hip_angles.Angles.x.Left-normalised", "right_hip_angles.Angles.x.Right-normalised",
            "left_hip_angles.Angles.y.Left-normalised", "right_hip_angles.Angles.y.Right-normalised",
            "left_hip_angles.Angles.z.Left-normalised", "right_hip_angles.Angles.z.Right-normalised",
            "left_knee_angles.Angles.x.Left-normalised", "right_knee_angles.Angles.x.Right-normalised",
            "left_ankle_angles.Angles.x.Left-normalised", "right_ankle_angles.Angles.x.Right-normalised",
            "left_foot_progression_angles.Angles.x.Left-normalised", "right_foot_progression_angles.Angles.x.Right-normalised"]

        df_left_pelvis_tilt = []
        df_left_pelvis_obl = []
        df_left_pelvis_rot = []
        df_left_hip_flexion = []
        df_left_hip_ad = []
        df_left_hip_rot = []
        df_left_knee_flexion = []
        df_left_ankle_plantarflexion = []
        df_left_foot_progression = []

        df_right_pelvis_tilt = []
        df_right_pelvis_obl = []
        df_right_pelvis_rot = []
        df_right_hip_flexion = []
        df_right_hip_ad = []
        df_right_hip_rot = []
        df_right_knee_flexion = []
        df_right_ankle_plantarflexion = []
        df_right_foot_progression = []

        for subject_folder in os.listdir(input_path):
            exclude_folder = False
            for subject in excl:
                if subject in subject_folder:
                    exclude_folder = True
                    print(subject)
                    break
            if exclude_folder:
                # Subject folder name contains one of the subjects from excl
                continue  # Skip processing this folder
            subject_path = os.path.join(input_path, subject_folder)
            for folder in os.listdir(subject_path):
                if FB_param.lower() in folder.lower():
                    param_path = os.path.join(subject_path, folder)
                    break
            # Check if out directory exists for the subject
            if os.path.exists(param_path) and os.path.isdir(param_path):
                files_in_param_path = [os.path.join(param_path, f) for f in os.listdir(param_path) if any(param_subpath in f for param_subpath in parameters_subpaths)]
                for file_path in files_in_param_path:
                    if "left_pelvis_angles.Angles.x.Left-normalised" in file_path:
                        df_left_pelvis_tilt.append(pd.read_csv(file_path).apply(pd.to_numeric))
                    elif "left_pelvis_angles.Angles.y.Left-normalised" in file_path:
                        df_left_pelvis_obl.append(pd.read_csv(file_path).apply(pd.to_numeric))
                    elif "left_pelvis_angles.Angles.z.Left-normalised" in file_path:
                        df_left_pelvis_rot.append(pd.read_csv(file_path).apply(pd.to_numeric))
                    elif "left_hip_angles.Angles.x.Left-normalised" in file_path:
                        df_left_hip_flexion.append(pd.read_csv(file_path).apply(pd.to_numeric))
                    elif "left_hip_angles.Angles.y.Left-normalised" in file_path:
                        df_left_hip_ad.append(pd.read_csv(file_path).apply(pd.to_numeric))
                    elif "left_hip_angles.Angles.z.Left-normalised" in file_path:
                        df_left_hip_rot.append(pd.read_csv(file_path).apply(pd.to_numeric))
                    elif "left_knee_angles.Angles.x.Left-normalised" in file_path:
                        df_left_knee_flexion.append(pd.read_csv(file_path).apply(pd.to_numeric))
                    elif "left_ankle_angles.Angles.x.Left-normalised" in file_path:
                        df_left_ankle_plantarflexion.append(pd.read_csv(file_path).apply(pd.to_numeric))
                    elif "left_foot_progression_angles.Angles.x.Left-normalised" in file_path:
                        df_left_foot_progression.append(pd.read_csv(file_path).apply(pd.to_numeric))
                    if "right_pelvis_angles.Angles.x.Right-normalised" in file_path:
                        df_right_pelvis_tilt.append(pd.read_csv(file_path).apply(pd.to_numeric))
                    elif "right_pelvis_angles.Angles.y.Right-normalised" in file_path:
                        df_right_pelvis_obl.append(pd.read_csv(file_path).apply(pd.to_numeric))
                    elif "right_pelvis_angles.Angles.z.Right-normalised" in file_path:
                        df_right_pelvis_rot.append(pd.read_csv(file_path).apply(pd.to_numeric))
                    elif "right_hip_angles.Angles.x.Right-normalised" in file_path:
                        df_right_hip_flexion.append(pd.read_csv(file_path).apply(pd.to_numeric))
                    elif "right_hip_angles.Angles.y.Right-normalised" in file_path:
                        df_right_hip_ad.append(pd.read_csv(file_path).apply(pd.to_numeric))
                    elif "right_hip_angles.Angles.z.Right-normalised" in file_path:
                        df_right_hip_rot.append(pd.read_csv(file_path).apply(pd.to_numeric))
                    elif "right_knee_angles.Angles.x.Right-normalised" in file_path:
                        df_right_knee_flexion.append(pd.read_csv(file_path).apply(pd.to_numeric))
                    elif "right_ankle_angles.Angles.x.Right-normalised" in file_path:
                        df_right_ankle_plantarflexion.append(pd.read_csv(file_path).apply(pd.to_numeric))
                    elif "right_foot_progression_angles.Angles.x.Right-normalised" in file_path:
                        df_right_foot_progression.append(pd.read_csv(file_path).apply(pd.to_numeric))
            else:
                raise ValueError('out_FBparam does not exist')

        return df_left_pelvis_tilt, df_left_pelvis_obl, df_left_pelvis_rot, df_left_hip_flexion, df_left_hip_ad, df_left_hip_rot, df_left_knee_flexion, df_left_ankle_plantarflexion, df_left_foot_progression, \
            df_right_pelvis_tilt, df_right_pelvis_obl, df_right_pelvis_rot, df_right_hip_flexion, df_right_hip_ad, df_right_hip_rot, df_right_knee_flexion, df_right_ankle_plantarflexion, df_right_foot_progression
def calculate_g(use, df_left_hip_ad, df_left_pelvis_tilt, df_left_pelvis_obl, df_left_pelvis_rot, df_left_hip_flexion,
                df_left_hip_rot, df_left_knee_flexion, df_left_ankle_plantarflexion, df_left_foot_progression,
                df_right_pelvis_tilt, df_right_pelvis_obl, df_right_pelvis_rot, df_right_hip_flexion, df_right_hip_ad,
                df_right_hip_rot, df_right_knee_flexion, df_right_ankle_plantarflexion, df_right_foot_progression, mid = [], point = [], left = True, right = True, n_gaitcycles = 0):
    if use == "midpoints":
        Q = []
        for i in range(len(df_left_hip_ad)):
            for m in mid:
                # left
                g = []
                for df in [df_left_pelvis_tilt, df_left_pelvis_obl, df_left_pelvis_rot, df_left_hip_flexion,
                           df_left_hip_ad, df_left_hip_rot, df_left_knee_flexion, df_left_ankle_plantarflexion,
                           df_left_foot_progression]:
                    gaitcycle = df[i][df[i]["start_frame"] >= m].iloc[0]  # first gait cycle after midpoint
                    next_gaitcycle = df[i][df[i]["start_frame"] >= m].iloc[1]
                    gaitcycle["100"] = next_gaitcycle["0"]  # add final value of gaitcycle = first one of next gaitcycle (to have 51 points)
                    gaitcycle_vector = gaitcycle[6:107:2]  # 2% step
                    g.append(gaitcycle_vector)
                g = np.concatenate(g, axis=0)
                Q.append(g)

                # right
                g = []
                for df in [df_right_pelvis_tilt, df_right_pelvis_obl, df_right_pelvis_rot, df_right_hip_flexion,
                           df_right_hip_ad, df_right_hip_rot, df_right_knee_flexion, df_right_ankle_plantarflexion,
                           df_right_foot_progression]:
                    gaitcycle = df[i][df[i]["start_frame"] >= m].iloc[0]
                    next_gaitcycle = df[i][df[i]["start_frame"] >= m].iloc[1]
                    gaitcycle["100"] = next_gaitcycle[
                        "0"]  # add final value of gaitcycle = first one of next gaitcycle (to have 51 points)
                    gaitcycle_vector = gaitcycle[6:107:2]  # 2% step

                    g.append(gaitcycle_vector)
                g = np.concatenate(g, axis=0)
                Q.append(g)
        return Q
    elif use == "G":
        G = []
        for i in range(len(df_left_hip_ad)):
            # left
            if left:
                g = []
                for df in [df_left_pelvis_tilt, df_left_pelvis_obl, df_left_pelvis_rot, df_left_hip_flexion, df_left_hip_ad,
                           df_left_hip_rot, df_left_knee_flexion, df_left_ankle_plantarflexion, df_left_foot_progression]:
                    picked_cycle_number = df[i][df[i]["start_frame"] >= point].iloc[0]["cycle_number"] - n_gaitcycles  # n gait cycles before middle point
                    gaitcycle = df[i][df[i]["cycle_number"] == picked_cycle_number].iloc[0]
                    next_gait_cycle = df[i][df[i]["cycle_number"] == picked_cycle_number + 1].iloc[0]
                    gaitcycle["100"] = next_gait_cycle["0"]  # add the final value of the gait cycle, which is the first one of next gait cycle (to have 51 points)
                    gaitcycle_vector = gaitcycle[6:107:2]

                    g.append(gaitcycle_vector)

                g = np.concatenate(g, axis=0)
                G.append(g)
            if right:
                # right
                g = []
                for df in [df_right_pelvis_tilt, df_right_pelvis_obl, df_right_pelvis_rot, df_right_hip_flexion,
                           df_right_hip_ad, df_right_hip_rot, df_right_knee_flexion, df_right_ankle_plantarflexion,
                           df_right_foot_progression]:
                    picked_cycle_number = df[i][df[i]["start_frame"] >= point].iloc[0]["cycle_number"] - n_gaitcycles  # n gait cycles befiore middle point
                    gaitcycle = df[i][df[i]["cycle_number"] == picked_cycle_number].iloc[0]
                    next_gait_cycle = df[i][df[i]["cycle_number"] == picked_cycle_number + 1].iloc[0]
                    gaitcycle["100"] = next_gait_cycle["0"]  # add the final value of the gait cycle, wich is the first one of next gait cycle (to have 51 points)
                    gaitcycle_vector = gaitcycle[6:107:2]

                    g.append(gaitcycle_vector)

                g = np.concatenate(g, axis=0)
                G.append(g)
        return np.array(G)
def GDI (input_path, FB_mode, FB_param, output_file, excl=[], plot = False):

# input:    input_path to extraction_normalization files, where we have out_st, out_apf, out_pof
#           excl = list of excl subjects; e.g. ["S1", "S4"]
#           FB_mode = hFB or vFB (used for plot titles)
#           FB_param = APF, ST or POF

# output:   plots the GDI of each subject individually (NW to FB2 evolution)
#           prints values in given document for GDI left and right. (all in same document)

    # get all the param data
    df_left_pelvis_tilt, df_left_pelvis_obl, df_left_pelvis_rot, df_left_hip_flexion, df_left_hip_ad, \
        df_left_hip_rot, df_left_knee_flexion, df_left_ankle_plantarflexion, df_left_foot_progression,\
        df_right_pelvis_tilt, df_right_pelvis_obl, df_right_pelvis_rot, df_right_hip_flexion, df_right_hip_ad, \
        df_right_hip_rot, df_right_knee_flexion, df_right_ankle_plantarflexion, df_right_foot_progression = get_data("GDI", FB_param, input_path, excl)

    t_intervals = [(0, 60), (60, 240), (240, 300), (300, 480)]  # start and end time of the phases except washout
    f = 100 #vicon frequency
    f_intervals = [(start * f, end * f) for start, end in t_intervals]  # start and end frames of the phases

    # pick one gait cycle in the middle of each phase except washout (NW, FB1, noFB, FB2), L and R
    midpoints = [(round((start + end) / 2)) for start, end in f_intervals]

    Q = calculate_g(use = "midpoints", df_left_hip_ad = df_left_hip_ad, df_left_pelvis_tilt = df_left_pelvis_tilt, df_left_pelvis_obl = df_left_pelvis_obl, df_left_pelvis_rot = df_left_pelvis_rot, df_left_hip_flexion = df_left_hip_flexion,
                df_left_hip_rot = df_left_hip_rot, df_left_knee_flexion = df_left_knee_flexion, df_left_ankle_plantarflexion = df_left_ankle_plantarflexion, df_left_foot_progression = df_left_foot_progression,
                df_right_pelvis_tilt = df_right_pelvis_tilt, df_right_pelvis_obl = df_right_pelvis_obl, df_right_pelvis_rot = df_right_pelvis_rot, df_right_hip_flexion = df_right_hip_flexion,df_right_hip_ad = df_right_hip_ad,
                df_right_hip_rot = df_right_hip_rot, df_right_knee_flexion = df_right_knee_flexion, df_right_ankle_plantarflexion = df_right_ankle_plantarflexion, df_right_foot_progression = df_right_foot_progression, mid = midpoints)
    Q = np.array(Q).T

    # SVD
    U, S, V = np.linalg.svd(Q, full_matrices=True)

    # Compute features components for control group = natural walking   # L and R
    # take one gait cycle in natural walking for each subject, different from the one used for G. Should not really matter
    # -> middle point - 10 gaitcycles

    point_control = (f_intervals[0][1] - f_intervals[0][0]) / 2
    # note: G is transposed compared to the paper
    G_control = calculate_g(use = "G", df_left_hip_ad = df_left_hip_ad, df_left_pelvis_tilt = df_left_pelvis_tilt, df_left_pelvis_obl = df_left_pelvis_obl, df_left_pelvis_rot = df_left_pelvis_rot, df_left_hip_flexion = df_left_hip_flexion,
                df_left_hip_rot = df_left_hip_rot, df_left_knee_flexion = df_left_knee_flexion, df_left_ankle_plantarflexion = df_left_ankle_plantarflexion, df_left_foot_progression = df_left_foot_progression,
                df_right_pelvis_tilt = df_right_pelvis_tilt, df_right_pelvis_obl = df_right_pelvis_obl, df_right_pelvis_rot = df_right_pelvis_rot, df_right_hip_flexion = df_right_hip_flexion,df_right_hip_ad = df_right_hip_ad,
                df_right_hip_rot = df_right_hip_rot, df_right_knee_flexion = df_right_knee_flexion, df_right_ankle_plantarflexion = df_right_ankle_plantarflexion, df_right_foot_progression = df_right_foot_progression, point = point_control, n_gaitcycles=10)

    c = np.dot(G_control, U).T
    c_control = np.mean(c, axis=1)  # cTD, mean control
    c_control_matrix = c_control[:, np.newaxis]  # to have a matrix shape, to ba able to substract it from c later

    GPS_control = np.linalg.norm(c - c_control_matrix, axis=0)
    GDI_raw_control = np.log(GPS_control)

    point_NW = (f_intervals[0][1] - f_intervals[0][0]) / 2
    G_NW = calculate_g(use = "G", df_left_hip_ad = df_left_hip_ad, df_left_pelvis_tilt = df_left_pelvis_tilt, df_left_pelvis_obl = df_left_pelvis_obl, df_left_pelvis_rot = df_left_pelvis_rot, df_left_hip_flexion = df_left_hip_flexion,
                df_left_hip_rot = df_left_hip_rot, df_left_knee_flexion = df_left_knee_flexion, df_left_ankle_plantarflexion = df_left_ankle_plantarflexion, df_left_foot_progression = df_left_foot_progression,
                df_right_pelvis_tilt = df_right_pelvis_tilt, df_right_pelvis_obl = df_right_pelvis_obl, df_right_pelvis_rot = df_right_pelvis_rot, df_right_hip_flexion = df_right_hip_flexion,df_right_hip_ad = df_right_hip_ad,
                df_right_hip_rot = df_right_hip_rot, df_right_knee_flexion = df_right_knee_flexion, df_right_ankle_plantarflexion = df_right_ankle_plantarflexion, df_right_foot_progression = df_right_foot_progression, point = point_NW, n_gaitcycles=5, right=False)

    c_NW = np.dot(G_NW, U).T
    GPS_NW = np.linalg.norm(c_NW - c_control_matrix, axis=0) # distance au control
    GDI_raw_NW = np.log(GPS_NW)

    point_FB2 = f_intervals[3][1]
    G_FB2_left = calculate_g(use = "G", df_left_hip_ad = df_left_hip_ad, df_left_pelvis_tilt = df_left_pelvis_tilt, df_left_pelvis_obl = df_left_pelvis_obl, df_left_pelvis_rot = df_left_pelvis_rot, df_left_hip_flexion = df_left_hip_flexion,
                df_left_hip_rot = df_left_hip_rot, df_left_knee_flexion = df_left_knee_flexion, df_left_ankle_plantarflexion = df_left_ankle_plantarflexion, df_left_foot_progression = df_left_foot_progression,
                df_right_pelvis_tilt = df_right_pelvis_tilt, df_right_pelvis_obl = df_right_pelvis_obl, df_right_pelvis_rot = df_right_pelvis_rot, df_right_hip_flexion = df_right_hip_flexion,df_right_hip_ad = df_right_hip_ad,
                df_right_hip_rot = df_right_hip_rot, df_right_knee_flexion = df_right_knee_flexion, df_right_ankle_plantarflexion = df_right_ankle_plantarflexion, df_right_foot_progression = df_right_foot_progression, point = point_FB2, n_gaitcycles=15, right = False)

    c_FB2_left = np.dot(G_FB2_left, U).T
    GPS_FB2_left = np.linalg.norm(c_FB2_left - c_control_matrix, axis=0)  # distance to control
    GDI_raw_FB2_left = np.log(GPS_FB2_left)

    G_FB2_right = calculate_g(use = "G", df_left_hip_ad = df_left_hip_ad, df_left_pelvis_tilt = df_left_pelvis_tilt, df_left_pelvis_obl = df_left_pelvis_obl, df_left_pelvis_rot = df_left_pelvis_rot, df_left_hip_flexion = df_left_hip_flexion,
                df_left_hip_rot = df_left_hip_rot, df_left_knee_flexion = df_left_knee_flexion, df_left_ankle_plantarflexion = df_left_ankle_plantarflexion, df_left_foot_progression = df_left_foot_progression,
                df_right_pelvis_tilt = df_right_pelvis_tilt, df_right_pelvis_obl = df_right_pelvis_obl, df_right_pelvis_rot = df_right_pelvis_rot, df_right_hip_flexion = df_right_hip_flexion,df_right_hip_ad = df_right_hip_ad,
                df_right_hip_rot = df_right_hip_rot, df_right_knee_flexion = df_right_knee_flexion, df_right_ankle_plantarflexion = df_right_ankle_plantarflexion, df_right_foot_progression = df_right_foot_progression, point = point_FB2, n_gaitcycles=15, left = False)

    c_FB2_right = np.dot(G_FB2_right, U).T
    GPS_FB2_right = np.linalg.norm(c_FB2_right - c_control_matrix, axis=0)  # distance to control
    GDI_raw_FB2_right = np.log(GPS_FB2_right)

    GDI_mean = np.mean(GDI_raw_control)
    GDI_std = np.std(GDI_raw_control)

    # NW
    z_NW = (GDI_raw_NW-GDI_mean)/GDI_std
    GDI_scaled_NW = 100 - 10 * z_NW
    print_in_excel_table(GDI_scaled_NW.mean(), "GDI", FB_mode + " NW", FB_param, output_file)

    # FB2 left
    z_FB2_left = (GDI_raw_FB2_left-GDI_mean)/GDI_std
    GDI_scaled_FB2_left = 100 - 10 * z_FB2_left
    print_in_excel_table(GDI_scaled_FB2_left.mean(), "GDI", FB_mode + " FB2 left", FB_param, output_file)

    # FB2 right
    z_FB2_right = (GDI_raw_FB2_right-GDI_mean)/GDI_std
    GDI_scaled_FB2_right = 100 - 10 * z_FB2_right
    print_in_excel_table(GDI_scaled_FB2_right.mean(), "GDI", FB_mode + " FB2 right", FB_param, output_file)

    if plot:
        #Plotting:
        plt.figure(figsize=(8,8))
        for i in range(min(len(GDI_scaled_NW), len(GDI_scaled_FB2_left))):
            plt.plot([1, 3], [GDI_scaled_NW[i], GDI_scaled_FB2_left[i]], linestyle='-')
        plt.axhline(y=100, color='grey', linestyle='--', linewidth=1)
        ax = plt.subplot()
        #ax.set_xlim(df_res[i]['time'].iloc[1], df_res[i]['time'].iloc[-1])
        xticks = [1, 3]
        ax.set_xticks(xticks)
        for tick in xticks:
            ax.axvline(x=tick, color='lightgray', linestyle='dotted', alpha=0.7)
        ax.set_xticklabels(('NW', 'FB2'))
        plt.ylabel(f'GDI {FB_param}', fontsize = 18)
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)
        plt.title(f'{FB_mode}', fontsize = 20)
        plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\GDI\{FB_mode}_{FB_param}.png')
        plt.show()

hFB_path = r'C:\Users\User\Documents\CEFIR_LLUI\Haptic FB\Data\extraction_normalization'
vFB_path = r'C:\Users\User\Documents\CEFIR_LLUI\Visual FB\Data\extraction_normalization'

GDI(hFB_path, "hFB", "ST", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx")
GDI(hFB_path, "hFB", "APF", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx")
GDI(hFB_path, "hFB", "POF", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx")
GDI(vFB_path, "vFB", "ST", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx", excl=["S2_","S3_","S6_","S12_"])
GDI(vFB_path, "vFB", "APF", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx", excl=["S2_","S3_","S6_","S12_"])
GDI(vFB_path, "vFB", "POF", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx", excl=["S2_","S3_","S6_","S12_"])
