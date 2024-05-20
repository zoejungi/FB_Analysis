import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import copy
import helperfunctions

def maxAPF(sub_id, FB, exclusion = True): # max_APF = array of APF_l, t_l, APF_r, t_r -> same number and anatomically impossible values excluded


    return max_apf

def POF(sub_id, FB, exclusion = True):

    return pof

def ST(sub_id, FB):
    #take files: S2_st_spatiotemp.csv and S2_HFB_st-left_GRF.Forces.y.Left-normalised.csv
    st_paths = []
    st_paths.append(get_file (sub_id, FB, param = st)) #return path
    time_paths = []
    time_paths.append(get_file(sub_id, FB, param = time)) #return path

    df = pd.read_csv(st_path)
    df.rename(columns={'Unnamed: 0': 'cycle_number'}, inplace=True)
    df = df.loc[2:, ['cycle_number', 'stance_duration_p_left', 'cycle_duration_s_left', 'stance_duration_p_right', 'cycle_duration_s_right']]  # only parameters of interest
    df = df.apply(pd.to_numeric)  # whole dataframe from str to num

    df_time = pd.read_csv(time_path)
    df_time.apply(pd.to_numeric) #whole dataframe from str to num

    #compute ST left and right [s] and add timepoint
    df['ST_left'] = df['stance_duration_p_left']*df['cycle_duration_s_left']
    df['ST_right'] = df['stance_duration_p_right'] * df['cycle_duration_s_right']
    df.reset_index(inplace=True)
    df['time'] = df_time["end_frame"]*0.01 #0.01 == sampling time vicon

    return df

def max_kneeflexion = maxKneeflexion(sub_id, FB, exclusion = True):\

    return maxKneeflexion

def meanGRFz(sub_id, FB, exclusion = True):

    return mean_grfz

def stepLength(sub_id, FB, exclusion = True):

    return step_length

def stepHeight(sub_id, FB, exclusion = True):

    return step_height

def stepWidth(sub_id, FB, exclusion = True):

    return step_width

def swingTime(sub_id, FB, exclusion = True):

    return swing_time
