# This is a sample main.py how to analyse and plot FB data from D-Flow and Vicon
from GDI import *
from SUS_TLX import *

# GDI

#hFB_GDI_path = r'C:\Users\User\Documents\CEFIR_LLUI\Haptic FB\Data\extraction_normalization'
#vFB_GDI_path = r'C:\Users\User\Documents\CEFIR_LLUI\Visual FB\Data\extraction_normalization'

#GDI(hFB_GDI_path, "hFB", "ST", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx", save=True)
#GDI(hFB_GDI_path, "hFB", "APF", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx", save = True)
#GDI(hFB_GDI_path, "hFB", "POF", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx", save = True)
#GDI(vFB_GDI_path, "vFB", "ST", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx", excl=["S2_","S3_","S6_","S12_"], save = True)
#GDI(vFB_GDI_path, "vFB", "APF", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx", excl=["S2_","S3_","S6_","S12_"], save = True)
#GDI(vFB_GDI_path, "vFB", "POF", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx", excl=["S2_","S3_","S6_","S12_"], save = True)
#print('GDI calculated for all')
# SUS_TLX

n_hFB = 20 #number of subjects hFB
n_vFB = 24 #number of subjects vFB

hFB_Q_path = r"C:\Users\User\Documents\CEFIR_LLUI\Haptic FB\Data\Questionnaire_subjects.csv"
q_hFB = clean_df(pd.read_csv(hFB_Q_path, delimiter = ';'), n_hFB) #dataframe with all subjects SUS&TLX
vFB_Q_path = r"C:\Users\User\Documents\CEFIR_LLUI\Visual FB\Data\Questionnaire_subjects_vFB.csv"
q_vFB = clean_df(pd.read_csv(vFB_Q_path, delimiter = ';'), n_vFB, excl=["S2", "S3", "S6", "S12"]) #dataframe with all subjects SUS&TLX

## SUS (1 bar plot per question -> 8 plots)
SUS_n = 8 #number of questions for SUS
SUS(q_hFB, SUS_n, 'hFB')
SUS(q_vFB, SUS_n, 'vFB')

## TLX (input score for each task and each subject under respective header)
TLX_hFB = TLX(q_hFB)
TLX_vFB = TLX(q_vFB)

plot_singleTLX('hFB', TLX_hFB, q_hFB)
plot_singleTLX('vFB', TLX_vFB, q_vFB)
plot_comparisonTLX('ST', TLX_hFB, TLX_vFB)
plot_comparisonTLX('POF', TLX_hFB, TLX_vFB)
plot_comparisonTLX('APF', TLX_hFB, TLX_vFB)


