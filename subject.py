# Class subject
# in: subject id, FB given on ST/APF/POF


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import copy
from helperfunctions import *

class Plotting:
    def __init__(self):
        t = 18 #fontsize, title
        a = 0.8 #transparency of color = alpha
        f = 16 #fontsize, ticks and legend
class Subject (Plotting):
    def __init__(self, sub_id, study, input_data): #if study = "FB" then subject from FB study -> param include df from all three FB trials
        self.ID = sub_id
        self.study = study
        self.datapath = input_data

        df = pd.read_excel(os.path.join(input_data, 'Data_subjects.xlsx'), index_col=None) # Read the Excel file
        filtered_df = df[df.iloc[:, 0].str.contains(sub_id, na=False)] # Filter rows for subject specific infos (first column = sub_ids)
        self.infos = pd.concat([df.iloc[:1], filtered_df]) # Combine headers and filtered rows

    def ST(self):
        # input = self
        # output = array of dfs (during ST, POF and APF FB), headers include cycle_number, stance_duration_p_left/right,
        #           cycle_duration_s_left/right,
        if self.study == "hFB" or "vFB":
            # datasets with only columns of interest for all three FB modes
            df_res = []
            data_paths = [get_filepath(datapath = self.datapath, sub_id = self.ID, FB = "ST", param = "ST"), get_filepath(datapath = self.datapath, sub_id = self.ID, FB = "POF", param = "ST"), get_filepath(datapath = self.datapath, sub_id = self.ID, FB = "APF", param = "ST")]
            for path in data_paths:
                if '.txt' in path:
                    path = convert_txt_to_csv(path)

            for i, file_path in enumerate(data_paths):
                df = pd.read_csv(file_path)
                df.rename(columns={'Unnamed: 0':'cycle_number'}, inplace=True )
                df = df.loc[2:, ['cycle_number', 'stance_duration_p_left', 'cycle_duration_s_left', 'stance_duration_p_right', 'cycle_duration_s_right']]  # only parameters of interest
                df = df.apply(pd.to_numeric)  # whole dataframe from str to num
                df_res.append(df)

            # used to get the time
            df_time = []
            time_paths = [get_filepath(datapath = self.datapath, sub_id = self.ID, FB="ST", param="left_GRF.Forces.y.Left-normalised"),
                          get_filepath(datapath = self.datapath, sub_id = self.ID, FB="POF", param="left_GRF.Forces.y.Left-normalised"),
                          get_filepath(datapath = self.datapath, sub_id = self.ID, FB="APF", param="left_GRF.Forces.y.Left-normalised")]

            for i, file_path in enumerate(time_paths):
                df = pd.read_csv(file_path)
                df = df.apply(pd.to_numeric)  # whole dataframe from str to num
                df_time.append(df)
        else:
            # only one dataset instead of 3
            print("Error: not FB study and no other study defined yet")

        # Computing metrics: ST left and ST right [s]
        for i, df in enumerate(df_res):
            df_res[i]['ST_left'] = df_res[i]['stance_duration_p_left']*df_res[i]['cycle_duration_s_left']
            df_res[i]['ST_right'] = df_res[i]['stance_duration_p_right']*df_res[i]['cycle_duration_s_right']

        #time
        for i, df in enumerate(df_res):
            df_res[i].reset_index(inplace=True)
            df_res[i]['time'] = df_time[i]["end_frame"] * 0.01 # 0.01 = sampling time of Vicon
            df_res[i].set_index('index', inplace=True, drop=True)

        # SR value computed by dflow during the baseline reported in subinfos
        baseline_sr = self.infos['BSR ST']
        print(baseline_sr)
        for i, df in enumerate(df_res):
            df_res[i]['SR_raw'] = df_res[i]['ST_left']/df_res[i]['ST_right'] # raw symmetry ratio
            df_res[i]['SR'] = df_res[i]['SR_raw']/baseline_sr # SR in proportion of baseline SR
            print(df_res[i]['ST_right'].isna().any())
            # Averaging with window = 5, taking SR and not SR_raw
            df_res[i]['SR_SMA5'] = df_res[i]['SR'].rolling(window=5,min_periods=1).mean()
            df_res[i]['ST_left_SMA5'] = df_res[i]['ST_left'].rolling(window=5,min_periods=1).mean()
            df_res[i]['ST_right_SMA5'] = df_res[i]['ST_right'].rolling(window=5,min_periods=1).mean()

        return df_res

    def POF(self):
        if self.study == "hFB" or "vFB":
            # datasets with only columns of interest for all three FB modes

            data_paths_left = [get_filepath(datapath = self.datapath, sub_id = self.ID, FB="ST", param="left_GRF.Forces.y.Left-normalised"),
                          get_filepath(datapath = self.datapath, sub_id = self.ID, FB="POF", param="left_GRF.Forces.y.Left-normalised"),
                          get_filepath(datapath = self.datapath, sub_id = self.ID, FB="APF", param="left_GRF.Forces.y.Left-normalised")]
            data_paths_right = [get_filepath(datapath = self.datapath, sub_id = self.ID, FB="ST", param="right_GRF.Forces.y.Right-normalised"),
                          get_filepath(datapath = self.datapath, sub_id = self.ID, FB="POF", param="right_GRF.Forces.y.Right-normalised"),
                          get_filepath(datapath = self.datapath, sub_id = self.ID, FB="APF", param="right_GRF.Forces.y.Right-normalised")]

            df_left = []
            df_right = []

            for i, file_path in enumerate(data_paths_left):
                df = pd.read_csv(file_path)
                df = df.apply(pd.to_numeric)  # whole dataframe from str to num
                # creating new column and store POF in it
                df['POF'] = df['cycle_number']
                for index, row in df.iterrows():
                    POF_value = df.iloc[index,6:105].min()  # Min y-GRF in each row (per cycle) # index 6:105 correspond to the columns with the pof values along the gait cycle
                    df.loc[index,'POF'] = abs(POF_value)  # positive value of pof
                # creating new column and store time in it (using left time for both legs)
                df['time'] = df["end_frame"] * 0.01  # 0.01 = vicon sampling time

                df_left.append(df)

            for i, file_path in enumerate(data_paths_right):
                df = pd.read_csv(file_path)
                df = df.apply(pd.to_numeric)  # whole dataframe from str to num
                # creating new column and store POF in it
                df['POF'] = df['cycle_number']
                for index, row in df.iterrows():
                    POF_value = df.iloc[index,6:105].min()  # Min y-GRF in each row (per cycle) # index 6:105 correspond to the columns with the pof values along the gait cycle
                    df.loc[index, 'POF'] = abs(POF_value)  # positive value of pof
                # creating new column and store time in it (using left time for both legs)
                df['time'] = df_left[i]["end_frame"] * 0.01  # 0.01 = vicon sampling time

                df_right.append(df)
        else:
            # only one dataset instead of 3
            print("Error: not FB study and no other study defined yet")
        # SR value computed by dflow during the baseline reported in subinfos
        baseline_sr = self.infos['BSR POF']
        print(baseline_sr)
        # storing SR in df_left
        for i, df in enumerate(df_left):
            df_left[i]['SR_raw'] = df_left[i]['POF']/df_right[i]['POF']
            df_left[i]['SR'] = df_left[i]['SR_raw']/baseline_sr
            # Average with window = 5, using SR not SR_raw
            df_left[i]['SR_SMA5'] = df_left[i]['SR'].rolling(window=5,min_periods=1).mean()
            df_left[i]['POF_left_SMA5'] = df_left[i]['POF'].rolling(window=5,min_periods=1).mean()
            df_left[i]['POF_right_SMA5'] = df_right[i]['POF'].rolling(window=5,min_periods=1).mean()
        return df_left

    def maxAPF(self):
        if self.study == "hFB" or "vFB":

            df_apf = []
            data_paths = [get_filepath(datapath = self.datapath, sub_id = self.ID, FB="ST", param="APF"),
                          get_filepath(datapath = self.datapath, sub_id = self.ID, FB="POF", param="APF"),
                          get_filepath(datapath = self.datapath, sub_id = self.ID, FB="APF", param="APF")]

            for i, file_path in enumerate(dataset_paths):
                df = pd.read_csv(file_path)
                df = df.apply(pd.to_numeric) # whole dataframe froms str to num
                if 'left apf offset' in df.columns:
                    df.rename(columns={'left apf offset': LAPF.Offset}, inplace=True)
                    df.rename(columns={'right apf offset': RAPF.Offset}, inplace=True)
                df['LAPF.Offset'] = - df['LAPF.Offset']
                df['RAPF.Offset'] = - df['RAPF.Offset']
                df['Time_adj'] = df['Time'] - df['Time'][0]

                # correction of events that are somethimes not reset to zero
                df["LHS"] = df["LHS"] - df.iloc[0, :]["LHS"]
                df["RHS"] = df["RHS"] - df.iloc[0, :]["RHS"]
                df["LTO"] = df["LTO"] - df.iloc[0, :]["LTO"]
                df["RTO"] = df["RTO"] - df.iloc[0, :]["RTO"]

                df_apf.append(df)

            # Identifying max APF
            df_apf_final = identify_maxAPF(df_apf)
            # only continue if both sides have the same amount of events
            if check_cycles(df_apf_final):
                # Getting rid of outliers that are anatomically impossible
                exclude_outliers(df_apf_final)
                if check_cycles(df_apf_final):
                    # compute symmetry ratio
                    baseline_sr = self.infos['BSR APF']
                    for i, df in enumerate(df_apf_final):
                        if df_apf_final[i]['apf_right'] != 0 and df_apf_final[i]['apf_right'] != None and df_apf_final[i]['apf_left'] != None:
                            df_apf_final[i]['SR_raw'] = df_apf_final[i]['apf_left']/df_apf_final[i]['apf_right']
                            df_apf_final[i]['SR'] = df_apf_final[i]['SR_raw']/baseline_sr
                            df_apf_final[i]['time_sr'] = df_apf_final[i]['time']
                            df_apf_final[i]['SR_SMA5'] = df_apf_final[i]['SR'].rolling(window=5, min_periods=1).mean()

                   #ratio_series = pd.Series(symmetry_ratios)
                else:
                    print("Error: there's at least one event missing in either foot after excluding the ouliers")
            else:
                print("Error: there's at least one event missing in either foot")

        return df_apf_final

#create all subjects and calculate all gait parameters for all
n_hFB = 20
n_vFB = 24
subjects_hFB = {}
subjects_vFB = {}

for i in range(1, n_hFB+1):
    subjects_hFB[f'S{i}'] = Subject(f'S{i}_', "hFB", r'C:\Users\User\Documents\CEFIR_LLUI\Haptic FB\Data')
print('dictionary subjects hFB created')

subjects_hFB['S1'].st = subjects_hFB['S1'].ST()
print(subjects_hFB['S1'].st[1]['SR_raw'])
# plot ST SR individually
for i, df in enumerate(subjects_hFB['S1'].st):
    plt.figure()
    #plt.plot(df_res[i]['time'][1:], df_res[i]['symmetry ratio_SMA5'][1:], marker='', markersize=4, linewidth=1, linestyle='-', color='m', label='SR [SMA5]')
    plt.plot(subjects_hFB['S1'].st[i]['time'], subjects_hFB['S1'].st[i]['SR_SMA5'], marker='', markersize=4, linewidth=1, linestyle='-', color='m', label='SR$_{ST}$')
    #plt.plot(df_res[i]['time'][1:], df_res[i]['symmetry ratio'][1:], alpha=0.2, label='raw') # raw
    #plt.axhline(y=target_sr[i], color='g', linestyle='-', label='Target Value')
    #plt.axhspan(target_sr[i]-0.05, target_sr[i]+0.05, facecolor='palegreen', alpha=0.5, label='Green Zone')
    plt.axhline(y=0.8, color='g', linestyle='--', linewidth=1, label='Target Value')
    plt.axhline(y=1, color='lightgrey', linestyle='-', linewidth=1)
    plt.axhspan(0.75, 0.85, facecolor='palegreen', alpha=0.2, label='Margin')
    ax = plt.subplot()
    ax.set_yticks([0.7, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00, 1.05, 1.1])
    ax.set_yticklabels(('70', '75', '80', '85', '90', '95', '100', '105', '110'))
    ax.set_xlim(subjects_hFB['S1'].st[i]['time'].iloc[1], subjects_hFB['S1'].st[i]['time'].iloc[-1])
    ax.set_ylim(0.7,1.1)
    xticks = [subjects_hFB['S1'].st[i]['time'].iloc[1], 60, 240, 300, 480]
    ax.set_xticks([subjects_hFB['S1'].st[i]['time'].iloc[1], 60, 240, 300, 480])
    for tick in xticks:
        ax.axvline(x=tick, color='lightgray', linestyle='dotted', alpha=0.7)
    ax.set_xticklabels(('          NW', '                           FB1', '          No FB1', '                           FB2', '                            No FB2'))
    #plt.ylabel('Symmetry Ratio [$ST_{left}/ST_{right}$]')
    plt.ylabel('Baseline SR [%]', fontsize = 14)
    plt.xticks(fontsize = 12)
    plt.yticks(fontsize = 12)
    plt.legend(loc='upper right', fontsize = 12)
    #plt.title(f'Evolution of ST SR - S{i + 1}')
    #plt.savefig(rf'C:\Users\zoe.jungi\Documents\LLUI\HapticFeedback\Results\Study & ProofOfConcept\Plots\ST_SR_S{i+1}')
    plt.show()
# Evolution of the pof value for the left vs right
#for i, df in enumerate (subjects_hFB['S1'].pof):
    #plt.figure()
    #plt.plot(subjects_hFB['S1'].pof[i]['time'], subjects_hFB['S1'].pof[i]['POF_left_SMA5'], label='Left', linewidth=1,
    #         linestyle='-', color='red')
    #plt.plot(subjects_hFB['S1'].pof[i]['time'], subjects_hFB['S1'].pof[i]['POF_right_SMA5'], label='Right', linewidth=1,
    #         linestyle='-', color='royalblue')
    #ax = plt.subplot()
    #ax.set_xlim(subjects_hFB['S1'].pof[i]['time'].iloc[1], subjects_hFB['S1'].pof[i]['time'].iloc[-1])
    #xticks = [subjects_hFB['S1'].pof[i]['time'].iloc[1], 60, 240, 300, 480]
    #ax.set_xticks([subjects_hFB['S1'].pof[i]['time'].iloc[1], 60, 240, 300, 480])
    #for tick in xticks:
     #   ax.axvline(x=tick, color='lightgray', linestyle='dotted', alpha=0.7)
    #ax.set_xticklabels(('          NW', '                           FB1', '          No FB1',
     #                   '                           FB2', '                            No FB2'))
    #plt.ylabel('Push Off Force [N]', fontsize=14)
    #plt.xticks(fontsize=12)
    #plt.yticks(fontsize=12)
    #plt.legend(loc='upper right', fontsize=12)
    # plt.title(f'Evolution of POF - S{i + 1}')
    # plt.savefig(rf'C:\Users\zoe.jungi\Documents\LLUI\HapticFeedback\Results\Study & ProofOfConcept\Plots\POF_lr_S{i+1}')
    # plt.show()

#f'S{i}'.max_apf = maxAPF() # max_APF = array of APF_l, t_l, APF_r, t_r -> same number and anatomically impossible values excluded
    #subjects_hFB[f'S{i}'].pof = subjects_hFB[f'S{i}'].POF()
    #subjects_hFB[f'S{i}'].st = ST()
    #f'S{i}'.max_kneeflexion = maxKneeflexion(exclusion = True)
    #f'S{i}'.mean_grfz = meanGRFz(exclusion = True)
    #f'S{i}'.step_length = stepLength(exclusion = True)
    #f'S{i}'.step_height = stepHeight(exclusion = True)
    #f'S{i}'.step_width = stepWidth(exclusion = True)
    #f'S{i}'.swingtime = swingTime(exclusion = True)

for i in range(1, n_vFB+1):
    subjects_vFB[f'S{i}'] = Subject(f'S{i}_', "vFB", r'C:\Users\User\Documents\CEFIR_LLUI\Visual FB\Data')
    #f'S{i}'.max_apf = maxAPF() # max_APF = array of APF_l, t_l, APF_r, t_r -> same number and anatomically impossible values excluded
    #subjects_vFB[f'S{i}'].pof = POF()
    #subjects_vFB[f'S{i}'].st = ST()
    #f'S{i}'.max_kneeflexion = maxKneeflexion(exclusion = True)
    #f'S{i}'.mean_grfz = meanGRFz(exclusion = True)
    #f'S{i}'.step_length = stepLength(exclusion = True)
    #f'S{i}'.step_height = stepHeight(exclusion = True)
    #f'S{i}'.step_width = stepWidth(exclusion = True)
    #f'S{i}'.swingtime = swingTime(exclusion = True)

# plot individuals

# calculate means

# plot all


