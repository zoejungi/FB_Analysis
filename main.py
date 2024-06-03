# This is a sample main.py how to analyse and plot FB data from D-Flow and Vicon
from subject import *
from GDI import *
from SUS_TLX import *

# GDI

hFB_GDI_path = r'C:\Users\User\Documents\CEFIR_LLUI\Haptic FB\Data\extraction_normalization'
vFB_GDI_path = r'C:\Users\User\Documents\CEFIR_LLUI\Visual FB\Data\extraction_normalization'

#GDI(hFB_GDI_path, "hFB", "ST", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx")
#GDI(hFB_GDI_path, "hFB", "APF", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx")
#GDI(hFB_GDI_path, "hFB", "POF", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx")
#GDI(vFB_GDI_path, "vFB", "ST", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx", excl=["S2_","S3_","S6_","S12_"])
#GDI(vFB_GDI_path, "vFB", "APF", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx", excl=["S2_","S3_","S6_","S12_"])
#GDI(vFB_GDI_path, "vFB", "POF", output_file= r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables.xlsx", excl=["S2_","S3_","S6_","S12_"])

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


#create all subjects and calculate all gait parameters for all
n_hFB = 20
n_vFB = 24
subjects_hFB = {}
subjects_vFB = {}

for i in range(1, n_hFB+1):
    subjects_hFB[f'S{i}'] = Subject(f'S{i}_', "hFB", r'C:\Users\User\Documents\CEFIR_LLUI\Haptic FB\Data')
print('dictionary subjects hFB created')

for i in range(1, n_vFB+1):
    subjects_vFB[f'S{i}'] = Subject(f'S{i}_', "vFB", r'C:\Users\User\Documents\CEFIR_LLUI\Visual FB\Data')
print('dictionary subjects vFB created')

for i in range(1, n_hFB+1)
    subjects_hFB[f'S{i}'].st = subjects_hFB[f'S{i}'].ST()
    subjects_hFB[f'S{i}'].pof = subjects_hFB[f'S{i}'].POF()
    #subjects_hFB[f'S{i}'].apf = subjects_hFB[f'S{i}'].maxAPF()
    subjects_hFB[f'S{i}'].swingtime = subjects_hFB[f'S{i}'].swingTime()
    subjects_hFB[f'S{i}'].steplength = subjects_hFB[f'S{i}'].stepLength()
    subjects_hFB[f'S{i}'].stepheight = subjects_hFB[f'S{i}'].stepHeight()
    subjects_hFB[f'S{i}'].stepwidth = subjects_hFB[f'S{i}'].stepWidth()
    subjects_hFB[f'S{i}'].GRFz = subjects_hFB[f'S{i}'].meanGRFz()
    subjects_hFB[f'S{i}'].kneeflexion = subjects_hFB[f'S{i}'].kneeFlexion()
print('gait parameters calculated for all subjects hFB')

or i in range(1, n_vFB+1)
    if i != 2 or 3 or 4 or 6 or 12:
        subjects_vFB[f'S{i}'].st = subjects_vFB[f'S{i}'].ST()
        subjects_vFB[f'S{i}'].pof = subjects_vFB[f'S{i}'].POF()
        #subjects_vFB[f'S{i}'].apf = subjects_vFB[f'S{i}'].maxAPF()
        subjects_vFB[f'S{i}'].swingtime = subjects_vFB[f'S{i}'].swingTime()
        subjects_vFB[f'S{i}'].steplength = subjects_vFB[f'S{i}'].stepLength()
        subjects_vFB[f'S{i}'].stepheight = subjects_vFB[f'S{i}'].stepHeight()
        subjects_vFB[f'S{i}'].stepwidth = subjects_vFB[f'S{i}'].stepWidth()
        subjects_vFB[f'S{i}'].GRFz = subjects_vFB[f'S{i}'].meanGRFz()
        subjects_vFB[f'S{i}'].kneeflexion = subjects_vFB[f'S{i}'].kneeFlexion()
print('gait parameters calculated for all subjects vFB')

# plot all individuals
for i in range(1, hFB+1):
    # ST
    for j, df in enumerate(subjects_hFB[f'S{i}'].st):
        subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].st[j]['time'], subjects_hFB[f'S{i}'].st[j]['SR_SMA5'], label='SR$_{ST}$')
        subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].st[j]['time'], subjects_hFB[f'S{i}'].st[j]['ST_left'], subjects_hFB[f'S{i}'].st[j]['ST_right'], ylabel='ST [s]')
    # POF
    for j, df in enumerate(subjects_hFB[f'S{i}'].pof):
        subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].pof[j]['time'], subjects_hFB[f'S{i}'].pof[j]['SR_SMA5'], label='SR$_{POF}$')
        subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].pof[j]['time'], subjects_hFB[f'S{i}'].pof[j]['POF_left_SMA5'], subjects_hFB[f'S{i}'].pof[j]['POF_right_SMA5'], ylabel='POF [N]')
    # APF
    #for j, df in enumerate(subjects_hFB[f'S{i}'].apf):
        #subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].apf[j]['time'], subjects_hFB[f'S{i}'].apf[j]['SR_SMA5'], label='SR$_{APF}$')
        #subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].apf[j]['time'], subjects_hFB[f'S{i}'].apf[j]['apf_left'], subjects_hFB[f'S{i}'].apf[j]['apf_right'], ylabel='maxAPF [°]')
    # Swingtime
    for j, df in enumerate(subjects_hFB[f'S{i}'].swingtime):
        subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].swingtime[j]['time'], subjects_hFB[f'S{i}'].swingtime[j]['SR_SMA5'], label='SR$_{Swingtime}$', baseline=False)
        subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].swingtime[j]['time'], subjects_hFB[f'S{i}'].swingtime[j]['swingtime_left_SMA5'], subjects_hFB[f'S{i}'].swingtime[j]['swingtime_right_SMA5'], ylabel='Swingtime [s]')
    # Step Length
    for j, df in enumerate(subjects_hFB[f'S{i}'].steplength):
        subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].steplength[j]['time'], subjects_hFB[f'S{i}'].steplength[j]['SR_SMA5'], label='SR$_{Steplength}$', baseline=False)
        subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].steplength[j]['time'], subjects_hFB[f'S{i}'].steplength[j]['steplength_left_SMA5'], subjects_hFB[f'S{i}'].steplength[j]['steplength_right_SMA5'], ylabel='Steplength [m]')
    # Step Height
    for j, df in enumerate(subjects_hFB[f'S{i}'].stepheight):
        subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].stepheight[j]['time'], subjects_hFB[f'S{i}'].stepheight[j]['SR_SMA5'], label='SR$_{Stepheight}$', baseline=False)
        subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].stepheight[j]['time'], subjects_hFB[f'S{i}'].stepheight[j]['stepheight_left_SMA5'], subjects_hFB[f'S{i}'].stepheight[j]['stepheight_right_SMA5'], ylabel='Stepheight [m]')
    # Step Width
    for j, df in enumerate(subjects_hFB[f'S{i}'].stepwidth):
        subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].stepwidth[j]['time'], subjects_hFB[f'S{i}'].stepwidth[j]['SR_SMA5'], label='SR$_{Stepwidth}$', baseline=False)
        subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].stepwidth[j]['time'], subjects_hFB[f'S{i}'].stepwidth[j]['stepwidth_left_SMA5'], subjects_hFB[f'S{i}'].stepwidth[j]['stepwidth_right_SMA5'], ylabel='Stepwidth [m]')
    # meanGRFz
    for j, df in enumerate(subjects_hFB[f'S{i}'].GRFz):
        subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].GRFz[j]['time'], subjects_hFB[f'S{i}'].GRFz[j]['SR_SMA5'], label='SR$_{meanGRFz}$', baseline=False)
        subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].GRFz[j]['time'], subjects_hFB[f'S{i}'].GRFz[j]['GRFz_left_SMA5'], subjects_hFB[f'S{i}'].GRFz[j]['GRFz_right_SMA5'], ylabel='meanGRFz [N]')
    # max Kneeflexion
    for j, df in enumerate(subjects_hFB[f'S{i}'].kneeflexion):
        subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].kneeflexion[j]['time'], subjects_hFB[f'S{i}'].kneeflexion[j]['SR_SMA5'], label='SR$_{max Kneeflexion}$', baseline=False)
        subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].kneeflexion[j]['time'], subjects_hFB[f'S{i}'].kneeflexion[j]['knee_left_SMA5'], subjects_hFB[f'S{i}'].kneeflexion[j]['knee_right_SMA5'], ylabel='max Kneeflexion [°]')
print('all individual plots done for all subjects hFB')

for i in range(1, vFB+1):
    # ST
    for j, df in enumerate(subjects_vFB[f'S{i}'].st):
        subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].st[j]['time'], subjects_vFB[f'S{i}'].st[j]['SR_SMA5'], label='SR$_{ST}$')
        subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].st[j]['time'], subjects_vFB[f'S{i}'].st[j]['ST_left'], subjects_vFB[f'S{i}'].st[j]['ST_right'], ylabel='ST [s]')
    # POF
    for j, df in enumerate(subjects_vFB[f'S{i}'].pof):
        subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].pof[j]['time'], subjects_vFB[f'S{i}'].pof[j]['SR_SMA5'], label='SR$_{POF}$')
        subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].pof[j]['time'], subjects_vFB[f'S{i}'].pof[j]['POF_left_SMA5'], subjects_vFB[f'S{i}'].pof[j]['POF_right_SMA5'], ylabel='POF [N]')
    # APF
    #for j, df in enumerate(subjects_vFB[f'S{i}'].apf):
        #subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].apf[j]['time'], subjects_vFB[f'S{i}'].apf[j]['SR_SMA5'], label='SR$_{APF}$')
        #subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].apf[j]['time'], subjects_vFB[f'S{i}'].apf[j]['apf_left'], subjects_vFB[f'S{i}'].apf[j]['apf_right'], ylabel='maxAPF [°]')
    # Swingtime
    for j, df in enumerate(subjects_vFB[f'S{i}'].swingtime):
        subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].swingtime[j]['time'], subjects_vFB[f'S{i}'].swingtime[j]['SR_SMA5'], label='SR$_{Swingtime}$', baseline=False)
        subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].swingtime[j]['time'], subjects_vFB[f'S{i}'].swingtime[j]['swingtime_left_SMA5'], subjects_vFB[f'S{i}'].swingtime[j]['swingtime_right_SMA5'], ylabel='Swingtime [s]')
    # Step Length
    for j, df in enumerate(subjects_vFB[f'S{i}'].steplength):
        subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].steplength[j]['time'], subjects_vFB[f'S{i}'].steplength[j]['SR_SMA5'], label='SR$_{Steplength}$', baseline=False)
        subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].steplength[j]['time'], subjects_vFB[f'S{i}'].steplength[j]['steplength_left_SMA5'], subjects_vFB[f'S{i}'].steplength[j]['steplength_right_SMA5'], ylabel='Steplength [m]')
    # Step Height
    for j, df in enumerate(subjects_vFB[f'S{i}'].stepheight):
        subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].stepheight[j]['time'], subjects_vFB[f'S{i}'].stepheight[j]['SR_SMA5'], label='SR$_{Stepheight}$', baseline=False)
        subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].stepheight[j]['time'], subjects_vFB[f'S{i}'].stepheight[j]['stepheight_left_SMA5'], subjects_vFB[f'S{i}'].stepheight[j]['stepheight_right_SMA5'], ylabel='Stepheight [m]')
    # Step Width
    for j, df in enumerate(subjects_vFB[f'S{i}'].stepwidth):
        subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].stepwidth[j]['time'], subjects_vFB[f'S{i}'].stepwidth[j]['SR_SMA5'], label='SR$_{Stepwidth}$', baseline=False)
        subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].stepwidth[j]['time'], subjects_vFB[f'S{i}'].stepwidth[j]['stepwidth_left_SMA5'], subjects_vFB[f'S{i}'].stepwidth[j]['stepwidth_right_SMA5'], ylabel='Stepwidth [m]')
    # meanGRFz
    for j, df in enumerate(subjects_vFB[f'S{i}'].GRFz):
        subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].GRFz[j]['time'], subjects_vFB[f'S{i}'].GRFz[j]['SR_SMA5'], label='SR$_{meanGRFz}$', baseline=False)
        subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].GRFz[j]['time'], subjects_vFB[f'S{i}'].GRFz[j]['GRFz_left_SMA5'], subjects_vFB[f'S{i}'].GRFz[j]['GRFz_right_SMA5'], ylabel='meanGRFz [N]')
    # max Kneeflexion
    for j, df in enumerate(subjects_vFB[f'S{i}'].kneeflexion):
        subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].kneeflexion[j]['time'], subjects_vFB[f'S{i}'].kneeflexion[j]['SR_SMA5'], label='SR$_{max Kneeflexion}$', baseline=False)
        subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].kneeflexion[j]['time'], subjects_vFB[f'S{i}'].kneeflexion[j]['knee_left_SMA5'], subjects_vFB[f'S{i}'].kneeflexion[j]['knee_right_SMA5'], ylabel='max Kneeflexion [°]')
print('all individual plots done for all subjects vFB')

# plot all


