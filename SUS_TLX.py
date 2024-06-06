#analysis of SUS and TLX questionnaires.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from helperfunctions import print_in_excel_table
from helperfunctions import weighted_std_mean

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

def SUS (df_q, n_questions, FB_mode, show = False, save = False):
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

        for j in range(len(categories)): # = number of categories
            print_in_excel_table(values_POF[j], 'SUS', f'{FB_mode} POF Q{i+1}', f'{categories[j]}', r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx")
            print_in_excel_table(values_APF[j], 'SUS', f'{FB_mode} APF Q{i+1}', f'{categories[j]}', r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx")
            print_in_excel_table(values_ST[j], 'SUS', f'{FB_mode} ST Q{i+1}', f'{categories[j]}', r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx")

        #mean_ST = (values_ST[0]*4 + values_ST[1]*3 + values_ST[2]*2 + values_ST[3]*1) / np.sum(values_ST[:])
        #mean_POF = (values_POF[0]*4 + values_POF[1]*3 + values_POF[2]*2 + values_POF[3]*1) / np.sum(values_POF[:])
        #mean_APF = (values_APF[0]*4 + values_APF[1]*3 + values_APF[2]*2 + values_APF[3]*1)/np.sum(values_APF[:])
        w = [4, 3, 2, 1, 0]
        std_ST, mean_ST = weighted_std_mean(w, values_ST)
        std_POF, mean_POF = weighted_std_mean(w, values_POF)
        std_APF, mean_APF = weighted_std_mean(w, values_APF)

        print_in_excel_table(np.round(mean_ST,2), 'SUS', f'{FB_mode} ST Q{i+1}', 'Mean', r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx")
        print_in_excel_table(np.round(mean_POF,2), 'SUS', f'{FB_mode} POF Q{i + 1}', 'Mean', r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx")
        print_in_excel_table(np.round(mean_APF,2), 'SUS', f'{FB_mode} APF Q{i + 1}', 'Mean', r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx")

        print_in_excel_table(np.round(std_ST, 2), 'SUS', f'{FB_mode} ST Q{i + 1}', 'STD',r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx")
        print_in_excel_table(np.round(std_POF, 2), 'SUS', f'{FB_mode} POF Q{i + 1}', 'STD', r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx")
        print_in_excel_table(np.round(std_APF, 2), 'SUS', f'{FB_mode} APF Q{i + 1}', 'STD', r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx")

        plt.bar(x_positions_st, values_ST, width=bar_width, color='skyblue', label='ST')
        plt.bar(x_positions_pof, values_POF, width=bar_width, color='limegreen', label='POF')
        plt.bar(x_positions_apf, values_APF, width=bar_width, color='indigo', label='APF')

        plt.xticks(x_positions_st + bar_width, categories)
        plt.ylabel('Number of subjects', fontsize = 16)
        plt.title(f'{FB_mode} SUS Q{i + 1}, n = {len(df_q)}')
        plt.legend()
        if save:
            plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Questionnaires\{FB_mode}_SUS_Q{i+1}')
        if show:
            plt.show()
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

def plot_singleTLX(FB_mode, TLX, q, save=False, show=False):
    a = 0.8  # transparency of color = alpha
    f = 16  # fontsize, ticks and legend
    t = 18  # fontsize, title

    fig, ax = plt.subplots(figsize=(11, 8), subplot_kw=dict(polar=True))
    ax.fill(TLX[0], TLX[1], color='orchid', alpha=a, label='ST' + f", mean = {round(q['ST TLX raw'].mean())}")
    ax.fill(TLX[0], TLX[3], color='lightblue', alpha=a, label='APF' + f", mean = {round(q['APF TLX raw'].mean())}")
    ax.fill(TLX[0], TLX[2], color='burlywood', alpha=a, label='POF' + f", mean = {round(q['POF TLX raw'].mean())}")
    plt.title(f"TLX {FB_mode}, n = {len(q)}")
    ax.set_xticks(TLX[0][:-1])
    ax.set_xticklabels(['Mental', 'Physical', 'Temporal', 'Performance', 'Effort', 'Frustration'])
    plt.xticks(fontsize=f)
    plt.yticks(fontsize=f)
    plt.legend(loc=(0.88, 0.75), fontsize=f)
    if save:
        plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Questionnaires\{FB_mode}_TLX_STvsPOFvsAPF')
    if show:
        plt.show()
def plot_comparisonTLX(FB_param, TLX_h, TLX_v, save=False, show=False):
    a = 0.8  # transparency of color = alpha
    f = 16  # fontsize, ticks and legend
    t = 18  # fontsize, title
    if FB_param == 'ST':
        index = 1
    elif FB_param == 'POF':
        index = 2
    elif FB_param == 'APF':
        index = 3
    else:
        print('Error: FB param not known')

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.fill(TLX_h[0], TLX_h[index], color='orchid', alpha=a, label='hFB')
    ax.fill(TLX_v[0], TLX_v[index], color='burlywood', alpha=a, label='vFB')
    plt.title(f"TLX {FB_param}", fontsize=t)
    ax.set_xticks(TLX_v[0][:-1])
    ax.set_xticklabels(['Mental', 'Physical', 'Temporal', 'Performance', 'Effort', 'Frustration'])
    plt.xticks(fontsize=f)
    plt.yticks(fontsize=f)
    plt.legend(loc=(0.88, 0.75), fontsize=f)
    if save:
        plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Questionnaires\TLX_{FB_param}')
    if show:
        plt.show()

