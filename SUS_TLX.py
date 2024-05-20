#analysis of SUS and TLX questionnaires.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def TLX (df_q, excl = []):
    #input: dataframe with corresponding categories as column header
    #output: angles, values_ST, values_POF, values_APF (data for figures)
    data_ST = {'Category': ['TLX Mental', 'TLX Physical', 'TLX Temporal', 'TLX Performance', 'TLX Effort', 'TLX Frustration'],
               'Value': [df_q['ST TLX Mental'].mean(), df_q['ST TLX Physical'].mean(), df_q['ST TLX Temporal'].mean(), df_q['ST TLX Performance (Poor = 100, Good = 0)'].mean(), df_q['ST TLX Effort'].mean(), df_q['ST TLX Frustration'].mean()]}
    df_ST = pd.DataFrame(data_ST)

    data_POF = {'Category': ['TLX Mental', 'TLX Physical', 'TLX Temporal', 'TLX Performance', 'TLX Effort', 'TLX Frustration'],
                'Value': [df_q['POF TLX Mental'].mean(), df_q['POF TLX Physical'].mean(), df_q['POF TLX Temporal'].mean(), df_q['POF TLX Performance  (Poor = 100, Good = 0)'].mean(), df_q['POF TLX Effort'].mean(), df_q['POF TLX Frustration'].mean()]}
    df_POF = pd.DataFrame(data_POF)

    data_APF = {'Category': ['TLX Mental', 'TLX Physical', 'TLX Temporal', 'TLX Performance', 'TLX Effort', 'TLX Frustration'],
                'Value': [df_q['APF TLX Mental'].mean(), df_q['APF TLX Physical'].mean(), df_q['APF TLX Temporal'].mean(), df_q['APF TLX Performance  (Poor = 100, Good = 0)'].mean(), df_q['APF TLX Effort'].mean(), df_q['APF TLX Frustration'].mean()]}
    df_APF = pd.DataFrame(data_APF)

    # Number of categories (for all three FBs the same)
    num_categories = len(df_ST['Category'])
    # Create an array of angles for each category (for all three FBs the same
    angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
    angles += angles[:1]

    # Close the plot by adding the first data point at the end
    values_ST = df_ST['Value'].tolist()
    values_ST += values_ST[:1]

    values_POF = df_POF['Value'].tolist()
    values_POF += values_POF[:1]

    values_APF = df_APF['Value'].tolist()
    values_APF += values_APF[:1]

    return [angles, values_ST, values_POF, values_APF]

def SUS (df_q, n_questions, FB_mode):
    categories = ['Strongly agree', 'Agree', 'No opinion', 'Disagree', 'Strongly disagree']
    bar_width = 0.25
    x_positions_st = np.arange(len(categories))
    x_positions_pof = x_positions_st + bar_width
    x_positions_apf = x_positions_pof + bar_width

    for i in range(n_questions):  # where points are given as 'Strongly agree' = -2 to 'Strongly disagree' = 2 under the respective header
        values_ST = [df_q[f'ST SUS Q{i + 1}'].value_counts().get(-2, 0),
                     df_q[f'ST SUS Q{i + 1}'].value_counts().get(-1, 0),
                     df_q[f'ST SUS Q{i + 1}'].value_counts().get(0, 0),
                     df_q[f'ST SUS Q{i + 1}'].value_counts().get(1, 0),
                     df_q[f'ST SUS Q{i + 1}'].value_counts().get(2, 0)]
        values_POF = [df_q[f'POF SUS Q{i + 1}'].value_counts().get(-2, 0),
                      df_q[f'POF SUS Q{i + 1}'].value_counts().get(-1, 0),
                      df_q[f'POF SUS Q{i + 1}'].value_counts().get(0, 0),
                      df_q[f'POF SUS Q{i + 1}'].value_counts().get(1, 0),
                      df_q[f'POF SUS Q{i + 1}'].value_counts().get(2, 0)]
        values_APF = [df_q[f'APF SUS Q{i + 1}'].value_counts().get(-2, 0),
                      df_q[f'APF SUS Q{i + 1}'].value_counts().get(-1, 0),
                      df_q[f'APF SUS Q{i + 1}'].value_counts().get(0, 0),
                      df_q[f'APF SUS Q{i + 1}'].value_counts().get(1, 0),
                      df_q[f'APF SUS Q{i + 1}'].value_counts().get(2, 0)]

        plt.bar(x_positions_st, values_ST, width=bar_width, color='skyblue', label='ST')
        plt.bar(x_positions_pof, values_POF, width=bar_width, color='limegreen', label='POF')
        plt.bar(x_positions_apf, values_APF, width=bar_width, color='indigo', label='APF')

        plt.xticks(x_positions_st + bar_width, categories)
        plt.xlabel('Categories')
        plt.ylabel('Values')
        plt.title(f'{FB_mode} SUS Q{i + 1}, n = {len(df_q)}')
        plt.legend()
        plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Questionnaires\{FB_mode}_SUS_Q{i+1}')

        #plt.show()

    # SUS scores per subject, already calculated in csv file -> SUS tot
    # Calculation of total score: 2.5*sum(all_Q_scores_indiv)
    #                   for Q1,Q2,Q3,Q5,Q6,Q8: 5-score -> if score is given out from 0 (strongly agree) to 4 (strongly disagree))
    #                                          5-(score+3) -> if score is given from -2 (storngly agree) to 2 (strongly disagree))
    #                   for Q4,Q7: score-1 -> if score is given out from 0 (strongly agree) to 4 (strongly disagree))
    #                             (score+3)-1 -> if score is given from -2 (storngly agree) to 2 (strongly disagree))


def clean_df (df_q, n, excl = []):
    if excl:
        return df_q[0:n].loc[~df_q[0:n].iloc[:,0].isin(excl)].head(n)
    else:
        return df_q[0:n]

n_hFB = 20 #number of subjects hFB
n_vFB = 24 #number of subjects vFB

hFB_path = r"C:\Users\User\Documents\CEFIR_LLUI\Haptic FB\Data\Questionnaire_subjects.csv"
df_hFB = pd.read_csv(hFB_path, delimiter = ';') #dataframe with all subjects SUS&TLX
df_hFB = clean_df(df_hFB, n_hFB)

vFB_path = r"C:\Users\User\Documents\CEFIR_LLUI\Visual FB\Data\Questionnaire_subjects_vFB.csv"
df_vFB = pd.read_csv(vFB_path, delimiter = ';') #dataframe with all subjects SUS&TLX
df_vFB = clean_df(df_vFB, n_vFB, excl=["S2", "S3", "S6", "S12"])

# SUS (1 bar plot per question -> 8 plots)
SUS_n = 8 #number of questions for SUS

SUS(df_hFB, SUS_n, 'hFB')
SUS(df_vFB, SUS_n, 'vFB')

# TLX (input score for each task and each subject under respective header)
TLX_hFB = TLX(df_hFB)
TLX_vFB = TLX(df_vFB)

# plotting settings TLX

a = 0.8 #transparency of color = alpha
f = 16 #fontsize, ticks and legend
t = 18 #fontsize, title

# Plot ST, POF and APF for hFB and vFB separately
fig, ax = plt.subplots(figsize=(11, 8), subplot_kw=dict(polar=True))
ax.fill(TLX_hFB[0], TLX_hFB[1], color='orchid', alpha=a, label = 'ST' + f", mean = {round(df_vFB['ST TLX raw'].mean())}")
ax.fill(TLX_hFB[0], TLX_hFB[3], color='lightblue', alpha=a, label = 'APF' + f", mean = {round(df_vFB['APF TLX raw'].mean())}")
ax.fill(TLX_hFB[0], TLX_hFB[2], color='burlywood', alpha=a, label = 'POF' + f", mean = {round(df_vFB['POF TLX raw'].mean())}")
plt.title(f"TLX hFB, n = {len(df_hFB)}")
ax.set_xticks(TLX_hFB[0][:-1])
ax.set_xticklabels(['Mental', 'Physical', 'Temporal', 'Performance', 'Effort', 'Frustration'])
plt.xticks(fontsize = f)
plt.yticks(fontsize = f)
plt.legend(loc = (0.88,0.75), fontsize = f)
plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Questionnaires\hFB_TLX_STvsPOFvsAPF')
#plt.show()

fig, ax = plt.subplots(figsize=(11, 8), subplot_kw=dict(polar=True))
ax.fill(TLX_vFB[0], TLX_vFB[1], color='orchid', alpha=a, label = 'ST' + f", mean = {round(df_vFB['ST TLX raw'].mean())}")
ax.fill(TLX_vFB[0], TLX_vFB[3], color='lightblue', alpha=a, label = 'APF' + f", mean = {round(df_vFB['APF TLX raw'].mean())}")
ax.fill(TLX_vFB[0], TLX_vFB[2], color='burlywood', alpha=a, label = 'POF' + f", mean = {round(df_vFB['POF TLX raw'].mean())}")
plt.title(f"TLX vFB, n = {len(df_vFB)}", fontsize = t)
ax.set_xticks(TLX_vFB[0][:-1])
ax.set_xticklabels(['Mental', 'Physical', 'Temporal', 'Performance', 'Effort', 'Frustration'])
plt.xticks(fontsize = f)
plt.yticks(fontsize = f)
plt.legend(loc = (0.88,0.75), fontsize = f)
plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Questionnaires\vFB_TLX_STvsPOFvsAPF')
#plt.show()

# Plot the spiderweb graph ST
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(TLX_hFB[0], TLX_hFB[1], color='orchid', alpha=a, label = 'hFB')
ax.fill(TLX_vFB[0], TLX_vFB[1], color='burlywood', alpha=a, label = 'vFB')
plt.title(f"TLX ST", fontsize = t)
ax.set_xticks(TLX_vFB[0][:-1])
ax.set_xticklabels(['Mental', 'Physical', 'Temporal', 'Performance', 'Effort', 'Frustration'])
plt.xticks(fontsize = f)
plt.yticks(fontsize = f)
plt.legend(loc = (0.88,0.75), fontsize = f)
plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Questionnaires\TLX_ST')
#plt.show()

# Plot the spiderweb graph POF
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(TLX_hFB[0], TLX_hFB[2], color='orchid', alpha=a, label = 'hFB')
ax.fill(TLX_vFB[0], TLX_vFB[2], color='burlywood', alpha=a, label = 'vFB')
plt.title(f"TLX POF", fontsize = t)
ax.set_xticks(TLX_vFB[0][:-1])
ax.set_xticklabels(['Mental', 'Physical', 'Temporal', 'Performance', 'Effort', 'Frustration'])
plt.xticks(fontsize = f)
plt.yticks(fontsize = f)
plt.legend(loc = (0.88,0.75), fontsize = f)
plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Questionnaires\TLX_POF')
#plt.show()

# Plot the spiderweb graph APF
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(TLX_hFB[0], TLX_hFB[3], color='orchid', alpha=a, label = 'hFB')
ax.fill(TLX_vFB[0], TLX_vFB[3], color='burlywood', alpha=a, label = 'vFB')
plt.title(f"TLX APF", fontsize = t)
ax.set_xticks(TLX_vFB[0][:-1])
ax.set_xticklabels(['Mental', 'Physical', 'Temporal', 'Performance', 'Effort', 'Frustration'])
plt.xticks(fontsize = f)
plt.yticks(fontsize = f)
plt.legend(loc = (0.88,0.75), fontsize = f)
plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Questionnaires\TLX_APF')
#plt.show()