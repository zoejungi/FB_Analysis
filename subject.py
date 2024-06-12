# Class subject
# in: subject id, FB given on ST/APF/POF
import pandas as pd

import Plotting
from helperfunctions import *
from Plotting import *

class Subject (Plotting):
    def __init__(self, sub_id, study, input_data): #if study = "FB" then subject from FB study -> param include df from all three FB trials
        self.ID = sub_id
        self.study = study
        self.datapath = input_data

        df = pd.read_excel(os.path.join(input_data, 'Data_subjects.xlsx'), index_col=None) # Read the Excel file
        filtered_df = df[df.iloc[:, 0] == sub_id[:-1]] # Filter rows for subject specific infos (first column = sub_ids)
        self.infos = filtered_df # Combine headers and filtered rows
    def ST(self):
        # input = self
        # output = array of dfs (during ST, POF and APF FB), headers include cycle_number, stance_duration_p_left, cycle_duration_s_left, stance_duration_p_right
        #           cycle_duration_s_right, ST_left, ST_right, time, SR_raw, SR, SR_SMA5, ST_left_SMA5, ST_right_SMA5
        if self.study == "hFB" or "vFB":
            # datasets with only columns of interest for all three FB modes
            df_res = []
            data_paths = [get_filepath(datapath = self.datapath, sub_id = self.ID, FB = "ST", param = "ST"),
                          get_filepath(datapath = self.datapath, sub_id = self.ID, FB = "POF", param = "ST"),
                          get_filepath(datapath = self.datapath, sub_id = self.ID, FB = "APF", param = "ST")]

            for path in data_paths:
                if '.txt' in path:
                    path = convert_txt_to_csv(path)

            for i, file_path in enumerate(data_paths):
                if file_path:
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

            # Computing metrics: ST left and ST right [s]
            for i, df in enumerate(df_res):
                df_res[i]['ST_left'] = df_res[i]['stance_duration_p_left'] * df_res[i]['cycle_duration_s_left']
                df_res[i]['ST_right'] = df_res[i]['stance_duration_p_right'] * df_res[i]['cycle_duration_s_right']
                df_res[i].reset_index(inplace=True)
                df_res[i]['time'] = df_time[i]["end_frame"] * 0.01  # 0.01 = sampling time of Vicon
                df_res[i].set_index('index', inplace=True, drop=True)

            # SR value computed by dflow during the baseline reported in subinfos
            baseline_sr = np.squeeze(self.infos['BSR ST'])
            for i, df in enumerate(df_res):
                df_res[i]['SR_raw'] = df_res[i]['ST_left'] / df_res[i]['ST_right']  # raw symmetry ratio
                df_res[i]['SR'] = df_res[i]['SR_raw'] / baseline_sr  # SR in proportion of baseline SR
                # Averaging with window = 5, taking SR and not SR_raw
                df_res[i]['SR_SMA5'] = df_res[i]['SR'].rolling(window=5, min_periods=1).mean()
                df_res[i]['ST_left_SMA5'] = df_res[i]['ST_left'].rolling(window=5, min_periods=1).mean()
                df_res[i]['ST_right_SMA5'] = df_res[i]['ST_right'].rolling(window=5, min_periods=1).mean()
        else:
            print(f"Error: not FB study and no other study defined yet or S{self.ID} excluded for ST")
            df_res = []

        return df_res
    def POF(self):
        # input = self
        # output = array of dfs (during ST, POF and APF FB), headers include cycle_number, POF (=left),
        #               time, SR_raw, SR, SR_SMA5, POF_left_SMA5, POF_right_SMA5

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

            # SR value computed by dflow during the baseline reported in subinfos
            baseline_sr = np.squeeze(self.infos['BSR POF'])
            # storing SR in df_left
            for i, df in enumerate(df_left):
                df_left[i]['SR_raw'] = df_left[i]['POF'] / df_right[i]['POF']
                df_left[i]['SR'] = df_left[i]['SR_raw'] / baseline_sr
                # Average with window = 5, using SR not SR_raw
                df_left[i]['SR_SMA5'] = df_left[i]['SR'].rolling(window=5, min_periods=1).mean()
                df_left[i]['POF_left_SMA5'] = df_left[i]['POF'].rolling(window=5, min_periods=1).mean()
                df_left[i]['POF_right_SMA5'] = df_right[i]['POF'].rolling(window=5, min_periods=1).mean()
        else:
            # only one dataset instead of 3
            df_left = []
            print(f"Error: not FB study and no other study defined yet or S{self.ID} excluded for POF")

        return df_left
    def maxAPF(self):
        # input = self
        # output = array of dfs (during ST, POF and APF FB), headers include cycle_number, apf_left, apf_right
        #           time, SR_raw, SR, SR_SMA5, APF_left_SMA5, APF_right_SMA5

        if self.study == "hFB" or "vFB":

            df_apf = []
            data_paths = [get_filepath(datapath = self.datapath, sub_id = self.ID, FB="ST", param="APF"),
                          get_filepath(datapath = self.datapath, sub_id = self.ID, FB="POF", param="APF"),
                          get_filepath(datapath = self.datapath, sub_id = self.ID, FB="APF", param="APF")]
            for i, file_path in enumerate(data_paths):
                if '.txt' in data_paths[i]:
                    print(f'{file_path} from txt to csv')
                    file_path = convert_txt_to_csv(file_path, separator='\t')
                df = pd.read_csv(file_path)
                df = df.apply(pd.to_numeric) # whole dataframe from str to num
                if 'left apf offset' in df.columns:
                    df.rename(columns={'left apf offset': 'LAPF.Offset'}, inplace=True)
                    df.rename(columns={'right apf offset': 'RAPF.Offset'}, inplace=True)
                df['LAPF.Offset'] = - df['LAPF.Offset']
                df['RAPF.Offset'] = - df['RAPF.Offset']
                df['Time_adj'] = df['Time'] - df['Time'][0]

                # correction of events that are somethimes not reset to zero
                df["LHS"] = df["LHS"] - df.iloc[0, :]["LHS"]
                df["RHS"] = df["RHS"] - df.iloc[0, :]["RHS"]
                df["LTO"] = df["LTO"] - df.iloc[0, :]["LTO"]
                df["RTO"] = df["RTO"] - df.iloc[0, :]["RTO"]

                df_apf.append(df)
            print('Step 1 (reading data) complete')
            # Identifying max APF
            maxAPF_path = os.path.join(self.datapath, f'maxAPF_identified_{self.ID}.csv')
            if os.path.exists(maxAPF_path):
                df_apf_final_concat = pd.read_csv(maxAPF_path)
                grouped = df_apf_final_concat.groupby('group_id')
                df_apf_final = [grouped.get_group(group_id).drop(columns='group_id').reset_index(drop=True) for group_id in grouped.groups]
            else:
                df_apf_final = identify_maxAPF(df_apf, self.ID, self.datapath)
            print('Step 2 (identify maxAPF) complete')
            # Getting rid of outliers that are anatomically impossible
            exclude_outliers(df_apf_final)
            print('Step 3 (anatomically impossible values excluded) complete')
            # compute symmetry ratio
            baseline_sr = np.squeeze(self.infos['BSR APF'])
            for j, df in enumerate(df_apf_final):
                if not df_apf_final[j]['apf_right'].isnull().any() and not (df_apf_final[j]['apf_right'] == 0).any() and not df_apf_final[j]['apf_left'].isnull().any():
                    df_apf_final[j]['SR_raw'] = df_apf_final[j]['apf_left']/df_apf_final[j]['apf_right']
                    df_apf_final[j]['SR'] = df_apf_final[j]['SR_raw']/baseline_sr
                    df_apf_final[j]['time_sr'] = df_apf_final[j]['time']
                    df_apf_final[j]['SR_SMA5'] = df_apf_final[j]['SR'].rolling(window=5, min_periods=1).mean()
                    df_apf_final[j]['APF_left_SMA5'] = df_apf_final[j]['apf_left'].rolling(window=5, min_periods=1).mean()
                    df_apf_final[j]['APF_right_SMA5'] = df_apf_final[j]['apf_right'].rolling(window=5, min_periods=1).mean()
        else:
            df_apf_final = []
            print(f"Error: not FB study and no other study defined yet or S{self.ID} excluded for APF")

        return df_apf_final
    def maxKneeflexion(self):
        # input = self
        # output = array of dfs (during ST, POF and APF FB), headers include cycle_number, knee_flexion (=left)
        #           time, SR_raw, SR, SR_SMA5, knee_left_SMA5, knee_right_SMA5

        if self.study == "hFB" or "vFB":

            df_knee_left = []
            df_knee_right = []

            df_left = [get_filepath(self.datapath, self.ID, FB='ST', param='left_knee_angles.Angles.x.Left-normalised'),
                       get_filepath(self.datapath, self.ID, FB='POF', param='left_knee_angles.Angles.x.Left-normalised'),
                       get_filepath(self.datapath, self.ID, FB='APF', param='left_knee_angles.Angles.x.Left-normalised')]
            df_right = [get_filepath(self.datapath, self.ID, FB='ST', param='right_knee_angles.Angles.x.Right-normalised'),
                       get_filepath(self.datapath, self.ID, FB='POF', param='right_knee_angles.Angles.x.Right-normalised'),
                       get_filepath(self.datapath, self.ID, FB='APF', param='right_knee_angles.Angles.x.Right-normalised')]
            for i, file_path in enumerate(df_left):
                df = pd.read_csv(file_path)
                df = df.apply(pd.to_numeric)  # whole dataframe from str to num
                df_knee_left.append(df)
                df_knee_left[i]['time'] = df_knee_left[i]["end_frame"] * 0.01
                df_knee_left[i]['knee_flexion'] = df_knee_left[i]['cycle_number']  # random
                for index, row in df_knee_left[i].iterrows():
                    knee_range = df_knee_left[i].iloc[index, 6:105].apply(pd.to_numeric, errors='coerce')  # Convert to numeric
                    max_index = knee_range.idxmax()
                    max_value = knee_range.max()
                    df_knee_left[i].loc[index, 'knee_flexion'] = max_value
                    df_knee_left[i].loc[index, 'max_knee_flexion_index'] = max_index

            for i, file_path in enumerate(df_right):
                df = pd.read_csv(file_path)
                df = df.apply(pd.to_numeric)  # whole dataframe from str to num
                df_knee_right.append(df)
                df_knee_right[i]['knee_flexion'] = df_knee_right[i]['cycle_number']  # random
                df_knee_right[i]['time'] = df_knee_left[i]["end_frame"] * 0.01
                for index, row in df_knee_right[i].iterrows():
                    knee_range = df_knee_right[i].iloc[index, 6:105].apply(pd.to_numeric, errors='coerce')  # Convert to numeric
                    max_index = knee_range.idxmax()
                    max_value = knee_range.max()
                    df_knee_right[i].loc[index, 'knee_flexion'] = max_value
                    df_knee_right[i].loc[index, 'max_knee_flexion_index'] = max_index

            #calculate df_NW_sr
            df_knee_left_NW = copy.deepcopy(df_knee_left)
            df_knee_right_NW = copy.deepcopy(df_knee_right)
            df_NW_sr = []

            for i in range(len(df_knee_left_NW)):
                df_knee_left_NW[i] = df_knee_left_NW[i][df_knee_left_NW[i]["start_frame"] * 0.01 >= 0]
                df_knee_left_NW[i] = df_knee_left_NW[i][df_knee_left_NW[i]["time"] <= 60]

                df_knee_right_NW[i] = df_knee_right_NW[i][df_knee_right_NW[i]["start_frame"] * 0.01 >= 0]
                df_knee_right_NW[i] = df_knee_right_NW[i][df_knee_right_NW[i]["time"] <= 60]

                df_NW_sr.append(round(np.mean(df_knee_left_NW[i]["knee_flexion"]/df_knee_right_NW[i]["knee_flexion"]), 2))

            df_knee = copy.deepcopy(df_knee_left)
            for i, df in enumerate(df_knee_left):
                df_knee[i]['SR_raw'] = df_knee_left[i]['knee_flexion'] / df_knee_right[i]['knee_flexion']
                df_knee[i]['SR'] = df_knee[i]['SR_raw']/df_NW_sr[i]
                df_knee[i]['SR_SMA5'] = df_knee[i]['SR'].rolling(window=5,min_periods=1).mean()
                df_knee[i]['knee_left_SMA5'] = df_knee_left[i]['knee_flexion'].rolling(window=5,min_periods=1).mean()
                df_knee[i]['knee_right_SMA5'] = df_knee_right[i]['knee_flexion'].rolling(window=5,min_periods=1).mean()
                df_knee[i]['time'] = df_knee_left[i]['time']

        else:
            df_knee = []
            print(f"Error: not FB study and no other study defined yet or S{self.ID} excluded for kneeflexion")

        return df_knee
    def meanGRFz(self):
        # input = self
        # output = array of dfs (during ST, POF and APF FB), headers include cycle_number, mean_GRFz (=left)
        #           time, SR_raw, SR, SR_SMA5, GRFz_left_SMA5, GRFz_right_SMA5

        if self.study == "hFB" or "vFB":

            df_left = [get_filepath(self.datapath, self.ID, FB='ST', param='left_GRF.Forces.z.Left-raw'),
                       get_filepath(self.datapath, self.ID, FB='POF', param='left_GRF.Forces.z.Left-raw'),
                       get_filepath(self.datapath, self.ID, FB='APF', param='left_GRF.Forces.z.Left-raw')]
            df_right = [get_filepath(self.datapath, self.ID, FB='ST', param='right_GRF.Forces.z.Right-raw'),
                        get_filepath(self.datapath, self.ID, FB='POF', param='right_GRF.Forces.z.Right-raw'),
                        get_filepath(self.datapath, self.ID, FB='APF', param='right_GRF.Forces.z.Right-raw')]

            # Datasets only with parameters of interest
            df_GRF_left = []
            df_GRF_right = []

            for i, file_path in enumerate(df_left):
                df = pd.read_csv(file_path)
                df = df.apply(pd.to_numeric)  # whole dataframe from str to num
                df_GRF_left.append(df)
                df_GRF_left[i]['time'] = df_GRF_left[i]["end_frame"] * 0.01

                for index, row in df_GRF_left[i].iterrows():
                    HS = 0
                    TO = int(row["Foot_Off"])
                    # Mean GRF during Stance phase
                    df_GRF_left[i].loc[index, 'meanGRFz'] = df_GRF_left[i].iloc[index, HS + 6:TO + 6].mean()

            for i, file_path in enumerate(df_right):
                df = pd.read_csv(file_path)
                df = df.apply(pd.to_numeric)  # whole dataframe from str to num
                df_GRF_right.append(df)
                df_GRF_right[i]['time'] = df_GRF_left[i]["end_frame"] * 0.01
                for index, row in df_GRF_right[i].iterrows():
                    HS = 0
                    TO = int(row["Foot_Off"])
                    # Mean GRF during Stance phase
                    df_GRF_right[i].loc[index, 'meanGRFz'] = df_GRF_right[i].iloc[index, HS + 6:TO + 6].mean()

            #Calculate SR during NW
            df_GRF_left_NW = copy.deepcopy(df_GRF_left)
            df_GRF_right_NW = copy.deepcopy(df_GRF_right)
            df_NW_sr = []

            for i in range(len(df_GRF_left_NW)):
                df_GRF_left_NW[i] = df_GRF_left_NW[i][df_GRF_left_NW[i]["start_frame"] * 0.01 >= 0]
                df_GRF_left_NW[i] = df_GRF_left_NW[i][df_GRF_left_NW[i]["time"] <= 60]
                df_GRF_right_NW[i] = df_GRF_right_NW[i][df_GRF_right_NW[i]["start_frame"] * 0.01 >= 0]
                df_GRF_right_NW[i] = df_GRF_right_NW[i][df_GRF_right_NW[i]["time"] <= 60]

                df_NW_sr.append(round(df_GRF_left_NW[i]['meanGRFz'] / df_GRF_right_NW[i]['meanGRFz'],2))

            df_GRF = copy.deepcopy(df_GRF_left)
            for i, df in enumerate(df_GRF_left):
                df_GRF[i]['SR_raw'] = df_GRF_left[i]['meanGRFz']/df_GRF_right[i]['meanGRFz']
                df_GRF[i]['SR'] = df_GRF[i]['SR_raw']/df_NW_sr[i]
                df_GRF[i]['SR_SMA5'] = df_GRF[i]['SR'].rolling(window=5, min_periods=1).mean()
                df_GRF[i]['GRFz_left_SMA5'] = df_GRF_left[i]['meanGRFz'].rolling(window=5,min_periods=1).mean()
                df_GRF[i]['GRFz_right_SMA5'] = df_GRF_right[i]['meanGRFz'].rolling(window=5,min_periods=1).mean()
                df_GRF[i]['time'] = df_GRF_left[i]['time']

        else:
            df_GRF = []
            print(f"Error: not FB study and no other study defined yet or S{self.ID} excluded for GRF")

        return df_GRF
    def swingTime(self):
        # input = self
        # output = array of dfs (during ST, POF and APF FB), headers include cycle_number, cycle_duration_s_left, cycle_duration_s_right,
        #           swing_duration_p_left, swing_duration_p_right, swingtime_left, swingtime_right, time, SR_raw, SR, SR_SMA5,
        #           swingtime_left_SMA5, swingtime_right_SMA5

        if self.study == "hFB" or "vFB":
            # datasets with only columns of interest for all three FB modes
            df_swing = []
            data_paths = [get_filepath(datapath=self.datapath, sub_id=self.ID, FB="ST", param="spatiotemp"),
                          get_filepath(datapath=self.datapath, sub_id=self.ID, FB="POF", param="spatiotemp"),
                          get_filepath(datapath=self.datapath, sub_id=self.ID, FB="APF", param="spatiotemp")]

            # used to get the time
            df_time = []
            time_paths = [get_filepath(datapath=self.datapath, sub_id=self.ID, FB="ST", param="left_GRF.Forces.y.Left-normalised"),
                          get_filepath(datapath=self.datapath, sub_id=self.ID, FB="POF", param="left_GRF.Forces.y.Left-normalised"),
                          get_filepath(datapath=self.datapath, sub_id=self.ID, FB="APF", param="left_GRF.Forces.y.Left-normalised")]

            for i, file_path in enumerate(time_paths):
                df = pd.read_csv(file_path)
                df = df.apply(pd.to_numeric)  # whole dataframe from str to num
                df_time.append(df)

            for i, file_path in enumerate(data_paths):
                df = pd.read_csv(file_path)
                df.rename(columns={'Unnamed: 0': 'cycle_number'}, inplace=True)
                df = df.loc[2:,
                     ['cycle_number', 'cycle_duration_s_left', 'cycle_duration_s_right', 'swing_duration_p_left', 'swing_duration_p_right']]  # only parameters of interest
                df = df.apply(pd.to_numeric)  # whole dataframe from str to num
                df_swing.append(df)
                df_swing[i].reset_index(inplace=True)
                df_swing[i]['time'] = df_time[i]["end_frame"] * 0.01
                df_swing[i].set_index('index', inplace=True, drop=True)
                df_swing[i]['swingtime_left'] = df_swing[i]['swing_duration_p_left'] * df_swing[i]['cycle_duration_s_left']
                df_swing[i]['swingtime_right'] = df_swing[i]['swing_duration_p_right'] * df_swing[i]['cycle_duration_s_right']

            # calculate SR during NW
            df_swing_NW = copy.deepcopy(df_swing)
            df_NW_sr = []
            for i in range(len(df_swing_NW)):
                df_swing_NW[i] = df_swing[i][df_swing[i]["time"] >= 0]
                df_swing_NW[i] = df_swing[i][df_swing[i]["time"] <= 60]
                df_NW_sr.append(round(np.mean(df_swing_NW[i]["swingtime_left"] / df_swing_NW[i]["swingtime_right"]), 2))

            for i, df in enumerate(df_swing):
                df_swing[i]['SR_raw'] = df_swing[i]['swingtime_left']/df_swing[i]['swingtime_right']
                df_swing[i]['SR'] = df_swing[i]['SR_raw']/df_NW_sr[i]
                df_swing[i]['SR_SMA5'] = df_swing[i]['SR'].rolling(window=5, min_periods=1).mean()
                df_swing[i]['swingtime_left_SMA5'] = df_swing[i]['swingtime_left'].rolling(window=5, min_periods=1).mean()
                df_swing[i]['swingtime_right_SMA5'] = df_swing[i]['swingtime_right'].rolling(window=5, min_periods=1).mean()

        else:
            df_swing = []
            print(f"Error: not FB study and no other study defined yet or S{self.ID} excluded for swingtime")

        return df_swing
    def stepLength(self):
        # input = self
        # output = array of dfs (during ST, POF and APF FB), headers include cycle_number, step_length_left, step_length_right,
        #           time, SR_raw, SR, SR_SMA5, steplength_left_SMA5, steplength_right_SMA5
        if self.study == "hFB" or "vFB":
            # datasets with only columns of interest for all three FB modes
            df_step = []
            data_paths = [get_filepath(datapath=self.datapath, sub_id=self.ID, FB="ST", param="spatiotemp"),
                          get_filepath(datapath=self.datapath, sub_id=self.ID, FB="POF", param="spatiotemp"),
                          get_filepath(datapath=self.datapath, sub_id=self.ID, FB="APF", param="spatiotemp")]

            # used to get the time
            df_time = []
            time_paths = [get_filepath(datapath=self.datapath, sub_id=self.ID, FB="ST", param="left_GRF.Forces.y.Left-normalised"),
                          get_filepath(datapath=self.datapath, sub_id=self.ID, FB="POF", param="left_GRF.Forces.y.Left-normalised"),
                          get_filepath(datapath=self.datapath, sub_id=self.ID, FB="APF", param="left_GRF.Forces.y.Left-normalised")]

            for i, file_path in enumerate(time_paths):
                df = pd.read_csv(file_path)
                df = df.apply(pd.to_numeric)  # whole dataframe from str to num
                df_time.append(df)

            for i, file_path in enumerate(data_paths):
                df = pd.read_csv(file_path)
                df.rename(columns={'Unnamed: 0': 'cycle_number'}, inplace=True)
                df = df.loc[2:,
                     ['cycle_number', 'step_length_left', 'step_length_right']]  # only parameters of interest
                df = df.apply(pd.to_numeric)  # whole dataframe from str to num
                df_step.append(df)
                df_step[i].reset_index(inplace=True)
                df_step[i]['time'] = df_time[i]["end_frame"] * 0.01
                df_step[i].set_index('index', inplace=True, drop=True)
            # calculate SR during NW
            df_step_NW = copy.deepcopy(df_step)
            df_NW_sr = []
            for i in range(len(df_step_NW)):
                df_step_NW[i] = df_step[i][df_step[i]["time"] >= 0]
                df_step_NW[i] = df_step[i][df_step[i]["time"] <= 60]
                df_NW_sr.append(round(np.mean(df_step_NW[i]["step_length_left"] / df_step_NW[i]["step_length_right"]), 2))

            for i, df in enumerate(df_step):
                df_step[i]['SR_raw'] = df_step[i]['step_length_left']/df_step[i]['step_length_right']
                df_step[i]['SR'] = df_step[i]['SR_raw']/df_NW_sr[i]
                df_step[i]['SR_SMA5'] = df_step[i]['SR'].rolling(window=5, min_periods=1).mean()
                df_step[i]['steplength_left_SMA5'] = df_step[i]['step_length_left'].rolling(window=5, min_periods=1).mean()
                df_step[i]['steplength_right_SMA5'] = df_step[i]['step_length_right'].rolling(window=5, min_periods=1).mean()

        else:
            df_step = []
            print(f"Error: not FB study and no other study defined yet or S{self.ID} excluded for steplength")

        return df_step
    def stepHeight(self):
        # input = self
        # output = array of dfs (during ST, POF and APF FB), headers include cycle_number, step_height_left, step_height_right,
        #           time, SR_raw, SR, SR_SMA5, stepheight_left_SMA5, stepheight_right_SMA5
        if self.study == "hFB" or "vFB":
            # datasets with only columns of interest for all three FB modes
            df_step = []
            data_paths = [get_filepath(datapath=self.datapath, sub_id=self.ID, FB="ST", param="spatiotemp"),
                          get_filepath(datapath=self.datapath, sub_id=self.ID, FB="POF", param="spatiotemp"),
                          get_filepath(datapath=self.datapath, sub_id=self.ID, FB="APF", param="spatiotemp")]

            # used to get the time
            df_time = []
            time_paths = [get_filepath(datapath=self.datapath, sub_id=self.ID, FB="ST", param="left_GRF.Forces.y.Left-normalised"),
                          get_filepath(datapath=self.datapath, sub_id=self.ID, FB="POF", param="left_GRF.Forces.y.Left-normalised"),
                          get_filepath(datapath=self.datapath, sub_id=self.ID, FB="APF", param="left_GRF.Forces.y.Left-normalised")]

            for i, file_path in enumerate(time_paths):
                df = pd.read_csv(file_path)
                df = df.apply(pd.to_numeric)  # whole dataframe from str to num
                df_time.append(df)

            for i, file_path in enumerate(data_paths):
                df = pd.read_csv(file_path)
                df.rename(columns={'Unnamed: 0': 'cycle_number'}, inplace=True)
                df = df.loc[2:,
                     ['cycle_number', 'step_height_left', 'step_height_right']]  # only parameters of interest
                df = df.apply(pd.to_numeric)  # whole dataframe from str to num
                df_step.append(df)
                df_step[i].reset_index(inplace=True)
                df_step[i]['time'] = df_time[i]["end_frame"] * 0.01
                df_step[i].set_index('index', inplace=True, drop=True)

            # calculate SR during NW
            df_step_NW = copy.deepcopy(df_step)
            df_NW_sr = []
            for i in range(len(df_step_NW)):
                df_step_NW[i] = df_step[i][df_step[i]["time"] >= 0]
                df_step_NW[i] = df_step[i][df_step[i]["time"] <= 60]
                df_NW_sr.append(round(np.mean(df_step_NW[i]["step_height_left"] / df_step_NW[i]["step_height_right"]), 2))

            for i, df in enumerate(df_step):
                df_step[i]['SR_raw'] = df_step[i]['step_height_left']/df_step[i]['step_height_right']
                df_step[i]['SR'] = df_step[i]['SR_raw']/df_NW_sr[i]
                df_step[i]['SR_SMA5'] = df_step[i]['SR'].rolling(window=5, min_periods=1).mean()
                df_step[i]['stepheight_left_SMA5'] = df_step[i]['step_height_left'].rolling(window=5, min_periods=1).mean()
                df_step[i]['stepheight_right_SMA5'] = df_step[i]['step_height_right'].rolling(window=5, min_periods=1).mean()

        else:
            df_step = []
            print(f"Error: not FB study and no other study defined yet or S{self.ID} excluded for stepheight")

        return df_step
    def stepWidth(self):
        # input = self
        # output = array of dfs (during ST, POF and APF FB), headers include cycle_number, step_width_left, step_width_right,
        #           time, SR_raw, SR, SR_SMA5, stepwidth_left_SMA5, stepwidth_right_SMA5
        if self.study == "hFB" or "vFB":
            # datasets with only columns of interest for all three FB modes
            df_step = []
            data_paths = [get_filepath(datapath=self.datapath, sub_id=self.ID, FB="ST", param="spatiotemp"),
                          get_filepath(datapath=self.datapath, sub_id=self.ID, FB="POF", param="spatiotemp"),
                          get_filepath(datapath=self.datapath, sub_id=self.ID, FB="APF", param="spatiotemp")]

            # used to get the time
            df_time = []
            time_paths = [get_filepath(datapath=self.datapath, sub_id=self.ID, FB="ST",param="left_GRF.Forces.y.Left-normalised"),
                          get_filepath(datapath=self.datapath, sub_id=self.ID, FB="POF",param="left_GRF.Forces.y.Left-normalised"),
                          get_filepath(datapath=self.datapath, sub_id=self.ID, FB="APF",param="left_GRF.Forces.y.Left-normalised")]

            for i, file_path in enumerate(time_paths):
                df = pd.read_csv(file_path)
                df = df.apply(pd.to_numeric)  # whole dataframe from str to num
                df_time.append(df)

            for i, file_path in enumerate(data_paths):
                df = pd.read_csv(file_path)
                df.rename(columns={'Unnamed: 0': 'cycle_number'}, inplace=True)
                df = df.loc[2:,
                     ['cycle_number', 'step_width_left', 'step_width_right']]  # only parameters of interest
                df = df.apply(pd.to_numeric)  # whole dataframe from str to num
                df_step.append(df)
                df_step[i].reset_index(inplace=True)
                df_step[i]['time'] = df_time[i]["end_frame"] * 0.01
                df_step[i].set_index('index', inplace=True, drop=True)

            # calculate SR during NW
            df_step_NW = copy.deepcopy(df_step)
            df_NW_sr = []
            for i in range(len(df_step_NW)):
                df_step_NW[i] = df_step[i][df_step[i]["time"] >= 0]
                df_step_NW[i] = df_step[i][df_step[i]["time"] <= 60]
                df_NW_sr.append(round(np.mean(df_step_NW[i]["step_width_left"] / df_step_NW[i]["step_width_right"]), 2))

            for i, df in enumerate(df_step):
                df_step[i]['SR_raw'] = df_step[i]['step_width_left']/df_step[i]['step_width_right']
                df_step[i]['SR'] = df_step[i]['SR_raw']/df_NW_sr[i]
                df_step[i]['SR_SMA5'] = df_step[i]['SR'].rolling(window=5, min_periods=1).mean()
                df_step[i]['stepwidth_left_SMA5'] = df_step[i]['step_width_left'].rolling(window=5, min_periods=1).mean()
                df_step[i]['stepwidth_right_SMA5'] = df_step[i]['step_width_right'].rolling(window=5, min_periods=1).mean()

        else:
            df_step = []
            print(f"Error: not FB study and no other study defined yet or S{self.ID} excluded for stepwidth")

        return df_step

    def calc_corrandstats(self):
        # make df for correlation and for stats. -> row headers = condition (NW, duringST, during APF, during POF)
        #  -> column headers = subject ID, cycle number, SR_raw of all gait params.

        df_ST = pd.concat([group_data(self, 'ST', self.ID[:-1], 'st'), group_data(self, 'POF', self.ID[:-1], 'st'),
                           group_data(self, 'APF', self.ID[:-1], 'st')], ignore_index=True)
        df_ST = df_ST.rename(columns={'SR_raw': 'SR_ST'})

        df_POF = pd.concat([group_data(self, 'ST', self.ID[:-1], 'pof'), group_data(self, 'POF', self.ID[:-1], 'pof'),
                            group_data(self, 'APF', self.ID[:-1], 'pof')], ignore_index=True)
        df_POF = df_POF.rename(columns={'SR_raw': 'SR_POF'})

        df_APF = pd.concat([group_data(self, 'ST', self.ID[:-1], 'apf'), group_data(self, 'POF', self.ID[:-1], 'apf'),
                            group_data(self, 'APF', self.ID[:-1], 'apf')], ignore_index=True)
        df_APF = df_APF.rename(columns={'SR_raw': 'SR_APF'})
        df_APF = df_APF.rename(columns={'gait_cycle_left': 'cycle_number'})

        df_swingtime = pd.concat(
            [group_data(self, 'ST', self.ID[:-1], 'swingtime'), group_data(self, 'POF', self.ID[:-1], 'swingtime'),
             group_data(self, 'APF', self.ID[:-1], 'swingtime')], ignore_index=True)
        df_swingtime = df_swingtime.rename(columns={'SR_raw': 'SR_swingtime'})

        df_steplength = pd.concat(
            [group_data(self, 'ST', self.ID[:-1], 'steplength'), group_data(self, 'POF', self.ID[:-1], 'steplength'),
             group_data(self, 'APF', self.ID[:-1], 'steplength')], ignore_index=True)
        df_steplength = df_steplength.rename(columns={'SR_raw': 'SR_steplength'})

        df_stepwidth = pd.concat(
            [group_data(self, 'ST', self.ID[:-1], 'stepwidth'), group_data(self, 'POF', self.ID[:-1], 'stepwidth'),
             group_data(self, 'APF', self.ID[:-1], 'stepwidth')], ignore_index=True)
        df_stepwidth = df_stepwidth.rename(columns={'SR_raw': 'SR_stepwidth'})

        df_stepheight = pd.concat(
            [group_data(self, 'ST', self.ID[:-1], 'stepheight'), group_data(self, 'POF', self.ID[:-1], 'stepheight'),
             group_data(self, 'APF', self.ID[:-1], 'stepheight')], ignore_index=True)
        df_stepheight = df_stepheight.rename(columns={'SR_raw': 'SR_stepheight'})

        df_meanGRFz = pd.concat([group_data(self, 'ST', self.ID[:-1], 'GRFz'), group_data(self, 'POF', self.ID[:-1], 'GRFz'),
                                 group_data(self, 'APF', self.ID[:-1], 'GRFz')], ignore_index=True)
        df_meanGRFz = df_meanGRFz.rename(columns={'SR_raw': 'SR_meanGRFz'})

        df_kneeflexion = pd.concat(
            [group_data(self, 'ST', self.ID[:-1], 'kneeflexion'), group_data(self, 'POF', self.ID[:-1], 'kneeflexion'),
             group_data(self, 'APF', self.ID[:-1], 'kneeflexion')], ignore_index=True)
        df_kneeflexion = df_kneeflexion.rename(columns={'SR_raw': 'SR_kneeflexion'})

        df_correlation = pd.merge(df_ST, df_POF, on=["condition", "subject_ID", "cycle_number"])
        df_correlation = pd.merge(df_correlation, df_APF, on=["condition", "subject_ID", "cycle_number"])
        df_correlation = pd.merge(df_correlation, df_swingtime, on=["condition", "subject_ID", "cycle_number"])
        df_correlation = pd.merge(df_correlation, df_steplength, on=["condition", "subject_ID", "cycle_number"])
        df_correlation = pd.merge(df_correlation, df_stepheight, on=["condition", "subject_ID", "cycle_number"])
        df_correlation = pd.merge(df_correlation, df_stepwidth, on=["condition", "subject_ID", "cycle_number"])
        df_correlation = pd.merge(df_correlation, df_meanGRFz, on=["condition", "subject_ID", "cycle_number"])
        df_correlation = pd.merge(df_correlation, df_kneeflexion, on=["condition", "subject_ID", "cycle_number"])

        df_correlation.replace([np.inf, -np.inf], np.nan, inplace=True)
        df_correlation.dropna(inplace=True)
        # Rearrange the column headers to put 'subject_ID' and 'condition' to the front
        columns = df_correlation.columns.tolist()
        df_correlation = df_correlation[['subject_ID', 'condition'] + [col for col in columns if col not in ['subject_ID', 'condition']]]

        # take the mean of the 10 last values of FB2 phase for statistical analysis
        mean_stats_ST = calc_stats(df_correlation, 'duringST')
        mean_stats_POF = calc_stats(df_correlation, 'duringPOF')
        mean_stats_APF = calc_stats(df_correlation, 'duringAPF')

        return df_correlation, mean_stats_ST, mean_stats_POF, mean_stats_APF



# Assuming correlation_file is the path to the correlation file
correlation_path = r'C:\Users\User\Documents\CEFIR_LLUI\Haptic FB\correlation.csv'
stats_path = r'C:\Users\User\Documents\CEFIR_LLUI\Haptic FB'

# Check if the correlation file exists
if not os.path.exists(correlation_path):
    # create all subjects and calculate all gait parameters for all
    n_hFB = 3
    subjects_hFB = {}

    for i in range(1, n_hFB + 1):
        subjects_hFB[f'S{i}'] = Subject(f'S{i}_', "hFB", r'C:\Users\User\Documents\CEFIR_LLUI\Haptic FB\Data')
    print('dictionary subjects hFB created')

    for i in range(1, n_hFB + 1):
        subjects_hFB[f'S{i}'].st = subjects_hFB[f'S{i}'].ST()
        subjects_hFB[f'S{i}'].pof = subjects_hFB[f'S{i}'].POF()
        subjects_hFB[f'S{i}'].apf = subjects_hFB[f'S{i}'].maxAPF()
        subjects_hFB[f'S{i}'].swingtime = subjects_hFB[f'S{i}'].swingTime()
        subjects_hFB[f'S{i}'].steplength = subjects_hFB[f'S{i}'].stepLength()
        subjects_hFB[f'S{i}'].stepheight = subjects_hFB[f'S{i}'].stepHeight()
        subjects_hFB[f'S{i}'].stepwidth = subjects_hFB[f'S{i}'].stepWidth()
        subjects_hFB[f'S{i}'].GRFz = subjects_hFB[f'S{i}'].meanGRFz()
        subjects_hFB[f'S{i}'].kneeflexion = subjects_hFB[f'S{i}'].maxKneeflexion()
    print('gait parameters calculated for all subjects hFB')

    df_correlation = []
    df_statsST = []
    df_statsPOF = []
    df_statsAPF = []

    for i in range(1, n_hFB+1):
        subjects_hFB[f'S{i}'].correlation, subjects_hFB[f'S{i}'].statsST, subjects_hFB[f'S{i}'].statsPOF, subjects_hFB[f'S{i}'].statsAPF = subjects_hFB[f'S{i}'].calc_corrandstats()
        df_correlation.append(subjects_hFB[f'S{i}'].correlation)
        df_statsST.append(subjects_hFB[f'S{i}'].statsST)
        df_statsPOF.append(subjects_hFB[f'S{i}'].statsPOF)
        df_statsAPF.append(subjects_hFB[f'S{i}'].statsAPF)

    save_corrstats(df_correlation, correlation_path)
    save_corrstats(df_statsST, stats_path, FB = 'ST')
    save_corrstats(df_statsPOF, stats_path, FB = 'POF')
    save_corrstats(df_statsAPF, stats_path, FB = 'APF')
    print('corr/stats done individually and saved as a group.csv')
else:
    df_correlation = pd.read_csv(correlation_path)

calc_corrcoeffs (df_correlation, 'hFB', r'C:\Users\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx')
Plotting.plot_correlation(df_correlation,show=True)



