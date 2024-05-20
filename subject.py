# Class subject
# in: subject id, FB given on ST/APF/POF


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import copy
import functions

class Subject ():
    def __init__(self, ID): #if FB = True then subject from FB study -> param include df from all three FB trials
        FB = FB
        sub_infos = pd.read_excel("C:\\Users\\User\Documents\CEFIR_LLUI\Haptic FB\Data\Study\Data_subjects.xlsx", index_col = None,

    max_apf = maxAPF(sub_id, FB, exclusion = True) # max_APF = array of APF_l, t_l, APF_r, t_r -> same number and anatomically impossible values excluded
    pof = POF(sub_id, FB, exclusion = True)
    st = ST(sub_id, FB)
    max_kneeflexion = maxKneeflexion(sub_id, FB, exclusion = True)
    mean_grfz = meanGRFz(sub_id, FB, exclusion = True)
    step_length = stepLength(sub_id, FB, exclusion = True)
    step_height = stepHeight(sub_id, FB, exclusion = True)
    step_width = stepWidth(sub_id, FB, exclusion = True)
    swingtime = swingTime(sub_id, FB, exclusion = True)

