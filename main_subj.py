from subject import*

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

for i in range(1, n_hFB+1):
    subjects_hFB[f'S{i}'].st = subjects_hFB[f'S{i}'].ST()
    subjects_hFB[f'S{i}'].pof = subjects_hFB[f'S{i}'].POF()
    subjects_hFB[f'S{i}'].apf = subjects_hFB[f'S{i}'].maxAPF()
    #subjects_hFB[f'S{i}'].swingtime = subjects_hFB[f'S{i}'].swingTime()
    #subjects_hFB[f'S{i}'].steplength = subjects_hFB[f'S{i}'].stepLength()
    #subjects_hFB[f'S{i}'].stepheight = subjects_hFB[f'S{i}'].stepHeight()
    #subjects_hFB[f'S{i}'].stepwidth = subjects_hFB[f'S{i}'].stepWidth()
    #subjects_hFB[f'S{i}'].GRFz = subjects_hFB[f'S{i}'].meanGRFz()
    #subjects_hFB[f'S{i}'].kneeflexion = subjects_hFB[f'S{i}'].maxKneeflexion()
print('gait parameters calculated for all subjects hFB')

for i in range(1, n_vFB+1):
    if i != 2 and i != 3 and i != 4 and i != 6 and i !=12: #subjects 2,3,4,6,12 are excluded
        subjects_vFB[f'S{i}'].st = subjects_vFB[f'S{i}'].ST()
        subjects_vFB[f'S{i}'].pof = subjects_vFB[f'S{i}'].POF()
        subjects_vFB[f'S{i}'].apf = subjects_vFB[f'S{i}'].maxAPF()
        #subjects_vFB[f'S{i}'].swingtime = subjects_vFB[f'S{i}'].swingTime()
        #subjects_vFB[f'S{i}'].steplength = subjects_vFB[f'S{i}'].stepLength()
        #subjects_vFB[f'S{i}'].stepheight = subjects_vFB[f'S{i}'].stepHeight()
        #subjects_vFB[f'S{i}'].stepwidth = subjects_vFB[f'S{i}'].stepWidth()
        #subjects_vFB[f'S{i}'].GRFz = subjects_vFB[f'S{i}'].meanGRFz()
        #subjects_vFB[f'S{i}'].kneeflexion = subjects_vFB[f'S{i}'].maxKneeflexion()
print('gait parameters calculated for all subjects vFB')

# plot all individuals
t = [0, 60, 240, 300, 480, 640]
phases = ['NW', 'FB1', 'noFB1', 'FB2', 'noFB2']

for i in range(1, n_hFB+1):

    # write mean per t-phase in excel_file (only during corresponding FB)
    #for j in range(len(phases)):
        #print_in_excel_table(calculate_mean_interval(t_start = t[j], t_end = t[j+1], df = subjects_hFB[f'S{i}'].st[0]), 'Indiv', f'hFB S{i}', f'{phases[j]} (duringST)', r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx")
        #print_in_excel_table(calculate_mean_interval(t_start = t[j], t_end = t[j+1], df = subjects_hFB[f'S{i}'].pof[1]), 'Indiv', f'hFB S{i}', f'{phases[j]} (duringPOF)', r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx")
        #print_in_excel_table(calculate_mean_interval(t_start = t[j], t_end = t[j+1], df = subjects_hFB[f'S{i}'].apf[2]), 'Indiv', f'hFB S{i}', f'{phases[j]} (duringAPF)', r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx")

    # ST
    for j, df in enumerate(subjects_hFB[f'S{i}'].st):
        if j == 0:
            subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].st[j]['time'], subjects_hFB[f'S{i}'].st[j]['SR_SMA5'], label=f'S{i} SR$_{{ST}}$', savingname=f'hFB_S{i}_ST_SR')
            subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].st[j]['time'], subjects_hFB[f'S{i}'].st[j]['ST_left'], subjects_hFB[f'S{i}'].st[j]['ST_right'], ylabel='ST [s]', savingname=f'hFB_S{i}_ST_lr')
        #else:
            #subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].st[j]['time'], subjects_hFB[f'S{i}'].st[j]['SR_SMA5'], label=f'S{i} SR$_{{ST}}$', savingname=f'hFB_S{i}_STduring{j}_SR', target=False)
            #subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].st[j]['time'], subjects_hFB[f'S{i}'].st[j]['ST_left'], subjects_hFB[f'S{i}'].st[j]['ST_right'], ylabel='ST [s]', savingname=f'hFB_S{i}_STduring{j}_lr')

    # POF
    for j, df in enumerate(subjects_hFB[f'S{i}'].pof):
        if j == 1:
            subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].pof[j]['time'], subjects_hFB[f'S{i}'].pof[j]['SR_SMA5'], label=f'S{i} SR$_{{POF}}$', savingname=f'hFB_S{i}_POF_SR')
            subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].pof[j]['time'], subjects_hFB[f'S{i}'].pof[j]['POF_left_SMA5'], subjects_hFB[f'S{i}'].pof[j]['POF_right_SMA5'], ylabel='POF [N]', savingname=f'hFB_S{i}_POF_lr')

        #else:
            #subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].pof[j]['time'], subjects_hFB[f'S{i}'].pof[j]['SR_SMA5'], label=f'S{i} SR$_{{POF}}$', savingname=f'hFB_S{i}_POFduring{j}_SR', target=False)
            #subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].pof[j]['time'], subjects_hFB[f'S{i}'].pof[j]['POF_left_SMA5'], subjects_hFB[f'S{i}'].pof[j]['POF_right_SMA5'], ylabel='POF [N]', savingname=f'hFB_S{i}_POFduring{j}_lr')
    # APF
    for j, df in enumerate(subjects_hFB[f'S{i}'].apf):
        if j == 2:
            subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].apf[j]['time'], subjects_hFB[f'S{i}'].apf[j]['SR_SMA5'], label=f'S{i} SR$_{{APF}}$', savingname=f'hFB_S{i}_APF_SR', yaxis = True)
            subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].apf[j]['time'], subjects_hFB[f'S{i}'].apf[j]['apf_left'], subjects_hFB[f'S{i}'].apf[j]['apf_right'], ylabel='maxAPF [°]', savingname=f'hFB_S{i}_APF_lr')
        #else:
            #subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].apf[j]['time'], subjects_hFB[f'S{i}'].apf[j]['SR_SMA5'], label=f'S{i} SR$_{{APF}}$', savingname=f'hFB_S{i}_APFduring{j}_SR', yaxis = True, target = False)
            #subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].apf[j]['time'], subjects_hFB[f'S{i}'].apf[j]['apf_left'], subjects_hFB[f'S{i}'].apf[j]['apf_right'], ylabel='maxAPF [°]', savingname=f'hFB_S{i}_APFduring{j}_lr')

    # Swingtime
    #for j, df in enumerate(subjects_hFB[f'S{i}'].swingtime):
        #subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].swingtime[j]['time'], subjects_hFB[f'S{i}'].swingtime[j]['SR_SMA5'], label=f'S{i} SR$_{{swingtime}}$', savingname=f'hFB_S{i}_swingtimeduring{j}_SR', yaxis = True, baseline=False, target = False)
        #subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].swingtime[j]['time'], subjects_hFB[f'S{i}'].swingtime[j]['swingtime_left_SMA5'], subjects_hFB[f'S{i}'].swingtime[j]['swingtime_right_SMA5'], ylabel='Swingtime [s]', savingname=f'hFB_S{i}_swingtimeduring{j}_lr')
    # Step Length
    #for j, df in enumerate(subjects_hFB[f'S{i}'].steplength):
        #subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].steplength[j]['time'], subjects_hFB[f'S{i}'].steplength[j]['SR_SMA5'], label=f'S{i} SR$_{{steplength}}$', savingname=f'hFB_S{i}_steplengthduring{j}_SR', yaxis = True, baseline=False, target = False)
        #subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].steplength[j]['time'], subjects_hFB[f'S{i}'].steplength[j]['steplength_left_SMA5'], subjects_hFB[f'S{i}'].steplength[j]['steplength_right_SMA5'], ylabel='Steplength [m]', savingname=f'hFB_S{i}_steplengthduring{j}_lr')
    # Step Height
    #for j, df in enumerate(subjects_hFB[f'S{i}'].stepheight):
        #subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].stepheight[j]['time'], subjects_hFB[f'S{i}'].stepheight[j]['SR_SMA5'], label=f'S{i} SR$_{{stepheight}}$', savingname=f'hFB_S{i}_stepheightduring{j}_SR', yaxis = True, baseline=False, target = False)
        #subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].stepheight[j]['time'], subjects_hFB[f'S{i}'].stepheight[j]['stepheight_left_SMA5'], subjects_hFB[f'S{i}'].stepheight[j]['stepheight_right_SMA5'], ylabel='Stepheight [m]', savingname=f'hFB_S{i}_stepheightduring{j}_lr')
    # Step Width
    #for j, df in enumerate(subjects_hFB[f'S{i}'].stepwidth):
        #subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].stepwidth[j]['time'], subjects_hFB[f'S{i}'].stepwidth[j]['SR_SMA5'], label=f'S{i} SR$_{{stepwidth}}$', savingname=f'hFB_S{i}_stepwidthduring{j}_SR', yaxis = True, baseline=False, target = False)
        #subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].stepwidth[j]['time'], subjects_hFB[f'S{i}'].stepwidth[j]['stepwidth_left_SMA5'], subjects_hFB[f'S{i}'].stepwidth[j]['stepwidth_right_SMA5'], ylabel='Stepwidth [m]', savingname=f'hFB_S{i}_stepwidthduring{j}_lr')
    # meanGRFz
    #for j, df in enumerate(subjects_hFB[f'S{i}'].GRFz):
        #subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].GRFz[j]['time'], subjects_hFB[f'S{i}'].GRFz[j]['SR_SMA5'], label=f'S{i} SR$_{{meanGRFz}}$', savingname=f'hFB_S{i}_meanGRFzduring{j}_SR', yaxis = True, baseline=False, target = False)
        #subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].GRFz[j]['time'], subjects_hFB[f'S{i}'].GRFz[j]['GRFz_left_SMA5'], subjects_hFB[f'S{i}'].GRFz[j]['GRFz_right_SMA5'], ylabel='meanGRFz [N]', savingname=f'hFB_S{i}_meanGRFzduring{j}_lr')
    # max Kneeflexion
    #for j, df in enumerate(subjects_hFB[f'S{i}'].kneeflexion):
        #subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].kneeflexion[j]['time'], subjects_hFB[f'S{i}'].kneeflexion[j]['SR_SMA5'], label=f'S{i} SR$_{{max kneeflexion}}$', savingname=f'hFB_S{i}_kneeflexionduring{j}_SR', yaxis = True, baseline=False, target = False)
        #subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].kneeflexion[j]['time'], subjects_hFB[f'S{i}'].kneeflexion[j]['knee_left_SMA5'], subjects_hFB[f'S{i}'].kneeflexion[j]['knee_right_SMA5'], ylabel='max kneeflexion [°]', yaxis = True, savingname=f'hFB_S{i}_kneeflexionduring{j}_lr')
print('all individual plots done for all subjects hFB')

for i in range(1, n_vFB+1):
    if i != 2 and i != 3 and i != 4 and i != 6 and i != 12:
        # write mean per t-phase in excel_file (only during corresponding FB)
        #for j in range(len(phases)):
            #print_in_excel_table(calculate_mean_interval(t_start=t[j], t_end=t[j + 1], df = subjects_vFB[f'S{i}'].st[0]), 'Indiv', f'vFB S{i}', f'{phases[j]} (duringST)', r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx")
            #print_in_excel_table(calculate_mean_interval(t_start=t[j], t_end=t[j + 1], df = subjects_vFB[f'S{i}'].pof[1]), 'Indiv', f'vFB S{i}', f'{phases[j]} (duringPOF)', r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx")
            #print_in_excel_table(calculate_mean_interval(t_start=t[j], t_end=t[j + 1], df = subjects_vFB[f'S{i}'].apf[2]), 'Indiv', f'vFB S{i}', f'{phases[j]} (duringAPF)', r"C:\\Users\\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx")

        # ST
        for j, df in enumerate(subjects_vFB[f'S{i}'].st):
            if j == 0:
                subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].st[j]['time'], subjects_vFB[f'S{i}'].st[j]['SR_SMA5'], label=f'S{i} SR$_{{ST}}$', savingname=f'vFB_S{i}_ST_SR')
                subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].st[j]['time'], subjects_vFB[f'S{i}'].st[j]['ST_left'], subjects_vFB[f'S{i}'].st[j]['ST_right'], ylabel='ST [s]', savingname=f'vFB_S{i}_ST_lr')
            #else:
                #subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].st[j]['time'], subjects_vFB[f'S{i}'].st[j]['SR_SMA5'], label=f'S{i} SR$_{{ST}}$', savingname=f'vFB_S{i}_STduring{j}_SR', target = False)
                #subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].st[j]['time'], subjects_vFB[f'S{i}'].st[j]['ST_left'], subjects_vFB[f'S{i}'].st[j]['ST_right'], ylabel='ST [s]', savingname=f'vFB_S{i}_STduring{j}_lr')

        # POF
        for j, df in enumerate(subjects_vFB[f'S{i}'].pof):
            if j == 1:
                subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].pof[j]['time'], subjects_vFB[f'S{i}'].pof[j]['SR_SMA5'], label=f'S{i} SR$_{{POF}}$', savingname=f'vFB_S{i}_POF_SR')
                subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].pof[j]['time'], subjects_vFB[f'S{i}'].pof[j]['POF_left_SMA5'], subjects_vFB[f'S{i}'].pof[j]['POF_right_SMA5'], ylabel='POF [N]', savingname=f'vFB_S{i}_POF_lr')
            #else:
                #subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].pof[j]['time'], subjects_vFB[f'S{i}'].pof[j]['SR_SMA5'], label=f'S{i} SR$_{{POF}}$', savingname=f'vFB_S{i}_POFduring{j}_SR', target = False)
                #subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].pof[j]['time'], subjects_vFB[f'S{i}'].pof[j]['POF_left_SMA5'], subjects_vFB[f'S{i}'].pof[j]['POF_right_SMA5'], ylabel='POF [N]', savingname=f'vFB_S{i}_POFduring{j}_lr')

        # APF
        for j, df in enumerate(subjects_vFB[f'S{i}'].apf):
            if j == 2:
                subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].apf[j]['time'], subjects_vFB[f'S{i}'].apf[j]['SR_SMA5'], label=f'S{i} SR$_{{APF}}$', savingname=f'vFB_S{i}_APF_SR', yaxis = True)
                subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].apf[j]['time'], subjects_vFB[f'S{i}'].apf[j]['apf_left'], subjects_vFB[f'S{i}'].apf[j]['apf_right'], ylabel='maxAPF [°]', savingname=f'vFB_S{i}_APF_lr')
            #else:
                #subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].apf[j]['time'], subjects_vFB[f'S{i}'].apf[j]['SR_SMA5'], label=f'S{i} SR$_{{APF}}$', savingname=f'vFB_S{i}_APFduring{j}_SR', yaxis = True, target = False)
                #subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].apf[j]['time'], subjects_vFB[f'S{i}'].apf[j]['apf_left'], subjects_vFB[f'S{i}'].apf[j]['apf_right'], ylabel='maxAPF [°]', savingname=f'vFB_S{i}_APFduring{j}_lr')

        # Swingtime
        #for j, df in enumerate(subjects_vFB[f'S{i}'].swingtime):
            #subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].swingtime[j]['time'], subjects_vFB[f'S{i}'].swingtime[j]['SR_SMA5'], label=f'S{i} SR$_{{swingtime}}$', savingname=f'vFB_S{i}_swingtimeduring{j}_SR', yaxis = True, baseline=False, target = False)
            #subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].swingtime[j]['time'], subjects_vFB[f'S{i}'].swingtime[j]['swingtime_left_SMA5'], subjects_vFB[f'S{i}'].swingtime[j]['swingtime_right_SMA5'], ylabel='Swingtime [s]', savingname=f'vFB_S{i}_swingtimeduring{j}_lr')
        # Step Length
        #for j, df in enumerate(subjects_vFB[f'S{i}'].steplength):
            #subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].steplength[j]['time'], subjects_vFB[f'S{i}'].steplength[j]['SR_SMA5'], label=f'S{i} SR$_{{steplength}}$', savingname=f'vFB_S{i}_steplengthduring{j}_SR', yaxis = True, baseline=False, target = False)
            #subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].steplength[j]['time'], subjects_vFB[f'S{i}'].steplength[j]['steplength_left_SMA5'], subjects_vFB[f'S{i}'].steplength[j]['steplength_right_SMA5'], ylabel='Steplength [m]', savingname=f'vFB_S{i}_steplengthduring{j}_lr')
        # Step Height
        #for j, df in enumerate(subjects_vFB[f'S{i}'].stepheight):
            #subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].stepheight[j]['time'], subjects_vFB[f'S{i}'].stepheight[j]['SR_SMA5'], label=f'S{i} SR$_{{stepheight}}$', savingname=f'vFB_S{i}_stepheightduring{j}_SR', yaxis = True, baseline=False, target = False)
            #subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].stepheight[j]['time'], subjects_vFB[f'S{i}'].stepheight[j]['stepheight_left_SMA5'], subjects_vFB[f'S{i}'].stepheight[j]['stepheight_right_SMA5'], ylabel='Stepheight [m]', savingname=f'vFB_S{i}_stepheightduring{j}_lr')
        # Step Width
        #for j, df in enumerate(subjects_vFB[f'S{i}'].stepwidth):
            #subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].stepwidth[j]['time'], subjects_vFB[f'S{i}'].stepwidth[j]['SR_SMA5'], label=f'S{i} SR$_{{stepwidth}}$', savingname=f'vFB_S{i}_stepwidthduring{j}_SR', yaxis = True, baseline=False, target = False)
            #subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].stepwidth[j]['time'], subjects_vFB[f'S{i}'].stepwidth[j]['stepwidth_left_SMA5'], subjects_vFB[f'S{i}'].stepwidth[j]['stepwidth_right_SMA5'], ylabel='Stepwidth [m]', savingname=f'vFB_S{i}_stepwidthduring{j}_lr')
        # meanGRFz
        #for j, df in enumerate(subjects_vFB[f'S{i}'].GRFz):
            #subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].GRFz[j]['time'], subjects_vFB[f'S{i}'].GRFz[j]['SR_SMA5'], label=f'S{i} SR$_{{meanGRFz}}$', savingname=f'vFB_S{i}_meanGRFzduring{j}_SR', yaxis = True, baseline=False, target = False)
            #subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].GRFz[j]['time'], subjects_vFB[f'S{i}'].GRFz[j]['GRFz_left_SMA5'], subjects_vFB[f'S{i}'].GRFz[j]['GRFz_right_SMA5'], ylabel='meanGRFz [N]', savingname=f'vFB_S{i}_meanGRFzduring{j}_lr')
        # max Kneeflexion
        #for j, df in enumerate(subjects_vFB[f'S{i}'].kneeflexion):
            #subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].kneeflexion[j]['time'], subjects_vFB[f'S{i}'].kneeflexion[j]['SR_SMA5'], label=f'S{i} SR$_{{max kneeflexion}}$', savingname=f'vFB_S{i}_kneeflexionduring{j}_SR', yaxis = True, baseline=False, target = False)
            #subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].kneeflexion[j]['time'], subjects_vFB[f'S{i}'].kneeflexion[j]['knee_left_SMA5'], subjects_vFB[f'S{i}'].kneeflexion[j]['knee_right_SMA5'], ylabel='max Kneeflexion [°]', savingname=f'vFB_S{i}_kneeflexionduring{j}_lr')
print('all individual plots done for all subjects vFB')

# plot all hFB
hFB_st_SR_duringST, hFB_st_SR_std_duringST, hFB_st_t_duringST = calculate_averages(subjects_hFB, FB_mode = 'st', param = 'st')
hFB_st_SR_duringPOF, hFB_st_SR_std_duringPOF, hFB_st_t_duringPOF = calculate_averages(subjects_hFB, FB_mode = 'pof', param ='st')
hFB_st_SR_duringAPF, hFB_st_SR_std_duringAPF, hFB_st_t_duringAPF = calculate_averages(subjects_hFB, FB_mode = 'apf', param='st')

hFB_pof_SR_duringST, hFB_pof_SR_std_duringST, hFB_pof_t_duringST = calculate_averages(subjects_hFB, FB_mode = 'st', param = 'pof')
hFB_pof_SR_duringPOF, hFB_pof_SR_std_duringPOF, hFB_pof_t_duringPOF = calculate_averages(subjects_hFB, FB_mode = 'pof', param ='pof')
hFB_pof_SR_duringAPF, hFB_pof_SR_std_duringAPF, hFB_pof_t_duringAPF = calculate_averages(subjects_hFB, FB_mode = 'apf', param='pof')

hFB_apf_SR_duringST, hFB_apf_SR_std_duringST, hFB_apf_t_duringST = calculate_averages(subjects_hFB, FB_mode = 'st', param = 'apf')
hFB_apf_SR_duringPOF, hFB_apf_SR_std_duringPOF, hFB_apf_t_duringPOF = calculate_averages(subjects_hFB, FB_mode = 'pof', param ='apf')
hFB_apf_SR_duringAPF, hFB_apf_SR_std_duringAPF, hFB_apf_t_duringAPF = calculate_averages(subjects_hFB, FB_mode = 'apf', param='apf')

Plotting.plot_3SR_std(hFB_st_t_duringST, hFB_st_SR_duringST, hFB_st_SR_std_duringST, hFB_st_t_duringPOF, hFB_st_SR_duringPOF, hFB_st_SR_std_duringPOF, hFB_st_t_duringAPF, hFB_st_SR_duringAPF, hFB_st_SR_std_duringAPF, 'ST during ST', 'ST during POF', 'ST during APF', show = True, color=['orchid', get_color('orchid', 0.15), get_color('orchid', 0.3)], savingname='hFB_meanST_SR_all', title = f'hFB, n = {len(subjects_hFB)}')
Plotting.plot_3SR_std(hFB_pof_t_duringST, hFB_pof_SR_duringST, hFB_pof_SR_std_duringST, hFB_pof_t_duringPOF, hFB_pof_SR_duringPOF, hFB_pof_SR_std_duringPOF, hFB_pof_t_duringAPF, hFB_pof_SR_duringAPF, hFB_pof_SR_std_duringAPF, 'POF during ST', 'POF during POF', 'POF during APF', show = True, color=[get_color('burlywood', 0.1), 'burlywood', get_color('burlywood', 0.2)], savingname='hFB_meanPOF_SR_all', title = f'hFB, n = {len(subjects_hFB)}')
Plotting.plot_3SR_std(hFB_apf_t_duringST, hFB_apf_SR_duringST, hFB_apf_SR_std_duringST, hFB_apf_t_duringPOF, hFB_apf_SR_duringPOF, hFB_apf_SR_std_duringPOF, hFB_apf_t_duringAPF, hFB_apf_SR_duringAPF, hFB_apf_SR_std_duringAPF, 'APF during ST', 'APF during POF', 'APF during APF', show = True, color=[get_color('c', 0.1), get_color('c', 0.2), 'c'], yaxis = True, savingname='hFB_meanAPF_SR_all')

Plotting.plot_3SR_std(hFB_st_t_duringST, hFB_st_SR_duringST, hFB_st_SR_std_duringST, hFB_pof_t_duringPOF, hFB_pof_SR_duringPOF, hFB_pof_SR_std_duringPOF, hFB_apf_t_duringAPF, hFB_apf_SR_duringAPF, hFB_apf_SR_std_duringAPF, 'ST during ST', 'POF during POF', 'APF during APF', show = True, color=['orchid', 'burlywood', 'c'], yaxis = True, savingname='hFB_SR_all')

#plot all vFB

vFB_st_SR_duringST, vFB_st_SR_std_duringST, vFB_st_t_duringST = calculate_averages(subjects_vFB, FB_mode = 'st', param = 'st')
vFB_st_SR_duringPOF, vFB_st_SR_std_duringPOF, vFB_st_t_duringPOF = calculate_averages(subjects_vFB, FB_mode = 'pof', param ='st')
vFB_st_SR_duringAPF, vFB_st_SR_std_duringAPF, vFB_st_t_duringAPF = calculate_averages(subjects_vFB, FB_mode = 'apf', param='st')

vFB_pof_SR_duringST, vFB_pof_SR_std_duringST, vFB_pof_t_duringST = calculate_averages(subjects_vFB, FB_mode = 'st', param = 'pof')
vFB_pof_SR_duringPOF, vFB_pof_SR_std_duringPOF, vFB_pof_t_duringPOF = calculate_averages(subjects_vFB, FB_mode = 'pof', param ='pof')
vFB_pof_SR_duringAPF, vFB_pof_SR_std_duringAPF, vFB_pof_t_duringAPF = calculate_averages(subjects_vFB, FB_mode = 'apf', param='pof')

vFB_apf_SR_duringST, vFB_apf_SR_std_duringST, vFB_apf_t_duringST = calculate_averages(subjects_vFB, FB_mode = 'st', param = 'apf')
vFB_apf_SR_duringPOF, vFB_apf_SR_std_duringPOF, vFB_apf_t_duringPOF = calculate_averages(subjects_vFB, FB_mode = 'pof', param ='apf')
vFB_apf_SR_duringAPF, vFB_apf_SR_std_duringAPF, vFB_apf_t_duringAPF = calculate_averages(subjects_vFB, FB_mode = 'apf', param='apf')

Plotting.plot_3SR_std(vFB_st_t_duringST, vFB_st_SR_duringST, vFB_st_SR_std_duringST, vFB_st_t_duringPOF, vFB_st_SR_duringPOF, vFB_st_SR_std_duringPOF, vFB_st_t_duringAPF, vFB_st_SR_duringAPF, vFB_st_SR_std_duringAPF, 'ST during ST', 'ST during POF', 'ST during APF', show = True, color=['orchid', get_color('orchid', 0.15), get_color('orchid', 0.3)], savingname='vFB_meanST_SR_all', title = f'vFB, n = {len(subjects_vFB)-4}')
Plotting.plot_3SR_std(vFB_pof_t_duringST, vFB_pof_SR_duringST, vFB_pof_SR_std_duringST, vFB_pof_t_duringPOF, vFB_pof_SR_duringPOF, vFB_pof_SR_std_duringPOF, vFB_pof_t_duringAPF, vFB_pof_SR_duringAPF, vFB_pof_SR_std_duringAPF, 'POF during ST', 'POF during POF', 'POF during APF', show = True, color=[get_color('burlywood', 0.1), 'burlywood', get_color('burlywood', 0.2)], savingname='vFB_meanPOF_SR_all', title = f'vFB, n = {len(subjects_vFB)-4}')
Plotting.plot_3SR_std(vFB_apf_t_duringST, vFB_apf_SR_duringST, vFB_apf_SR_std_duringST, vFB_apf_t_duringPOF, vFB_apf_SR_duringPOF, vFB_apf_SR_std_duringPOF, vFB_apf_t_duringAPF, vFB_apf_SR_duringAPF, vFB_apf_SR_std_duringAPF, 'APF during ST', 'APF during POF', 'APF during APF', show = True, color=[get_color('c', 0.1), get_color('c', 0.2), 'c'], savingname='vFB_meanAPF_SR_all')

Plotting.plot_3SR_std(vFB_st_t_duringST, vFB_st_SR_duringST, vFB_st_SR_std_duringST, vFB_pof_t_duringPOF, vFB_pof_SR_duringPOF, vFB_pof_SR_std_duringPOF, vFB_apf_t_duringAPF, vFB_apf_SR_duringAPF, vFB_apf_SR_std_duringAPF, 'ST during ST', 'POF during POF', 'APF during APF', show = True, color=['orchid', 'burlywood', 'c'], yaxis = True, savingname='vFB_SR_all')

# comparison plots all
Plotting.plot_2SR_std(hFB_st_t_duringST, hFB_st_SR_duringST, hFB_st_SR_std_duringST, vFB_st_t_duringST, vFB_st_SR_duringST, vFB_st_SR_std_duringST, 'ST during hFB', 'ST during vFB', show = True, savingname='comp_SR_ST')
Plotting.plot_2SR_std(hFB_pof_t_duringPOF, hFB_pof_SR_duringPOF, hFB_pof_SR_std_duringPOF, vFB_pof_t_duringPOF, vFB_pof_SR_duringPOF, vFB_pof_SR_std_duringPOF, 'POF during hFB', 'POF during vFB', show = True, savingname='comp_SR_POF')
Plotting.plot_2SR_std(hFB_apf_t_duringAPF, hFB_apf_SR_duringAPF, hFB_apf_SR_std_duringAPF, vFB_apf_t_duringAPF, vFB_apf_SR_duringAPF, vFB_apf_SR_std_duringAPF, 'APF during hFB', 'APF during vFB', yaxis = True, show = True, savingname='comp_SR_APF')
print("all comparison plots (all subjects) done")

# responders and nonresponder groups
hFB_res_ST = ['S2', 'S3', 'S5', 'S6', 'S7', 'S9', 'S11', 'S15', 'S16', 'S17']
hFB_res_POF = ['S1', 'S3', 'S5', 'S7', 'S8', 'S9', 'S11', 'S14', 'S15', 'S16', 'S17', 'S18']
hFB_res_APF = ['S4', 'S8', 'S9', 'S10', 'S15', 'S16', 'S18']

responders_hFB_ST = {subject: subjects_hFB[subject] for subject in hFB_res_ST if subject in subjects_hFB}
responders_hFB_POF = {subject: subjects_hFB[subject] for subject in hFB_res_POF if subject in subjects_hFB}
responders_hFB_APF = {subject: subjects_hFB[subject] for subject in hFB_res_APF if subject in subjects_hFB}
nonresponders_hFB_ST = {subject: subjects_hFB[subject] for subject in subjects_hFB if not subject in hFB_res_ST}
nonresponders_hFB_POF = {subject: subjects_hFB[subject] for subject in subjects_hFB if not subject in hFB_res_POF}
nonresponders_hFB_APF = {subject: subjects_hFB[subject] for subject in subjects_hFB if not subject in hFB_res_APF}

vFB_res_ST = ['S1', 'S5', 'S7', 'S11', 'S13', 'S14', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24']
vFB_res_POF = ['S1', 'S7', 'S9', 'S10', 'S11', 'S13', 'S14', 'S16','S17', 'S18', 'S19', 'S20', 'S22', 'S23', 'S24']
vFB_res_APF = ['S7', 'S11', 'S14','S17', 'S18', 'S20', 'S24']

responders_vFB_ST = {subject: subjects_vFB[subject] for subject in vFB_res_ST if subject in subjects_vFB}
responders_vFB_POF = {subject: subjects_vFB[subject] for subject in vFB_res_POF if subject in subjects_vFB}
responders_vFB_APF = {subject: subjects_vFB[subject] for subject in vFB_res_APF if subject in subjects_vFB}
nonresponders_vFB_ST = {subject: subjects_vFB[subject] for subject in subjects_vFB if not subject in vFB_res_ST}
nonresponders_vFB_POF = {subject: subjects_vFB[subject] for subject in subjects_vFB if not subject in vFB_res_POF}
nonresponders_vFB_APF = {subject: subjects_vFB[subject] for subject in subjects_vFB if not subject in vFB_res_APF}

# plot all hFBres vs hFBnonres
hFB_st_SR_duringST, hFB_st_SR_std_duringST, hFB_st_t_duringST = calculate_averages(subjects_hFB, FB_mode = 'st', param = 'st')
hFB_pof_SR_duringPOF, hFB_pof_SR_std_duringPOF, hFB_pof_t_duringPOF = calculate_averages(subjects_hFB, FB_mode = 'pof', param ='pof')
hFB_apf_SR_duringAPF, hFB_apf_SR_std_duringAPF, hFB_apf_t_duringAPF = calculate_averages(subjects_hFB, FB_mode = 'apf', param='apf')

hFBres_st_SR_duringST, hFBres_st_SR_std_duringST, hFBres_st_t_duringST = calculate_averages(responders_hFB_ST, FB_mode = 'st', param = 'st')
hFBres_pof_SR_duringPOF, hFBres_pof_SR_std_duringPOF, hFBres_pof_t_duringPOF = calculate_averages(responders_hFB_POF, FB_mode = 'pof', param ='pof')
hFBres_apf_SR_duringAPF, hFBres_apf_SR_std_duringAPF, hFBres_apf_t_duringAPF = calculate_averages(responders_hFB_APF, FB_mode = 'apf', param='apf')
hFBnonres_st_SR_duringST, hFBnonres_st_SR_std_duringST, hFBnonres_st_t_duringST = calculate_averages(nonresponders_hFB_ST, FB_mode = 'st', param = 'st')
hFBnonres_pof_SR_duringPOF, hFBnonres_pof_SR_std_duringPOF, hFBnonres_pof_t_duringPOF = calculate_averages(nonresponders_hFB_POF, FB_mode = 'pof', param ='pof')
hFBnonres_apf_SR_duringAPF, hFBnonres_apf_SR_std_duringAPF, hFBnonres_apf_t_duringAPF = calculate_averages(nonresponders_hFB_APF, FB_mode = 'apf', param='apf')

Plotting.plot_3SR_std(hFB_st_t_duringST, hFB_st_SR_duringST, hFB_st_SR_std_duringST, hFBres_st_t_duringST, hFBres_st_SR_duringST, hFBres_st_SR_std_duringST, hFBnonres_st_t_duringST, hFBnonres_st_SR_duringST, hFBnonres_st_SR_std_duringST, f'all, n = {len(subjects_hFB)}', f'responders, n = {len(responders_hFB_ST)}', f'nonresponders, n = {len(nonresponders_hFB_ST)}', show = True, color=[get_color('orchid', 0.3), 'orchid', get_color('orchid', 0.15)], savingname='hFB_meanST_allresnonres', title = f'hFB ST')
Plotting.plot_3SR_std(hFB_pof_t_duringPOF, hFB_pof_SR_duringPOF, hFB_pof_SR_std_duringPOF, hFBres_pof_t_duringPOF, hFBres_pof_SR_duringPOF, hFBres_pof_SR_std_duringPOF, hFBnonres_pof_t_duringPOF, hFBnonres_pof_SR_duringPOF, hFBnonres_pof_SR_std_duringPOF, f'all, n = {len(subjects_hFB)}', f'responders, n = {len(responders_hFB_POF)}', f'nonresponders, n = {len(nonresponders_hFB_POF)}', show = True, color=[get_color('burlywood', 0.2), 'burlywood', get_color('burlywood', 0.1)], savingname='hFB_meanPOF_allresnonres', title = f'hFB POF')
Plotting.plot_3SR_std(hFB_apf_t_duringAPF, hFB_apf_SR_duringAPF, hFB_apf_SR_std_duringAPF, hFBres_apf_t_duringAPF, hFBres_apf_SR_duringAPF, hFBres_apf_SR_std_duringAPF, hFBnonres_apf_t_duringAPF, hFBnonres_apf_SR_duringAPF, hFBnonres_apf_SR_std_duringAPF, f'all, n = {len(subjects_hFB)}', f'responders, n = {len(responders_hFB_APF)}', f'nonresponders, n = {len(nonresponders_hFB_APF)}', show = True, color=[get_color('c', 0.2), 'c', get_color('c', 0.1)], yaxis = True, title = f'hFB APF', savingname='hFB_meanAPF_allresnonres')

Plotting.plot_3SR_std(hFBres_st_t_duringST, hFBres_st_SR_duringST, hFBres_st_SR_std_duringST, hFBres_pof_t_duringPOF, hFBres_pof_SR_duringPOF, hFBres_pof_SR_std_duringPOF, hFBres_apf_t_duringAPF, hFBres_apf_SR_duringAPF, hFBres_apf_SR_std_duringAPF, 'ST responders', 'POF responders', 'APF responders', show = True, color=['orchid', 'burlywood', 'c'], yaxis = True, savingname='hFB_SR_allresponders')
print("all plots hFB res vs nonres and only res done")

# plot all vFBres vs vFBnonres
vFB_st_SR_duringST, vFB_st_SR_std_duringST, vFB_st_t_duringST = calculate_averages(subjects_vFB, FB_mode = 'st', param = 'st')
vFB_pof_SR_duringPOF, vFB_pof_SR_std_duringPOF, vFB_pof_t_duringPOF = calculate_averages(subjects_vFB, FB_mode = 'pof', param ='pof')
vFB_apf_SR_duringAPF, vFB_apf_SR_std_duringAPF, vFB_apf_t_duringAPF = calculate_averages(subjects_vFB, FB_mode = 'apf', param='apf')

vFBres_st_SR_duringST, vFBres_st_SR_std_duringST, vFBres_st_t_duringST = calculate_averages(responders_vFB_ST, FB_mode = 'st', param = 'st')
vFBres_pof_SR_duringPOF, vFBres_pof_SR_std_duringPOF, vFBres_pof_t_duringPOF = calculate_averages(responders_vFB_POF, FB_mode = 'pof', param ='pof')
vFBres_apf_SR_duringAPF, vFBres_apf_SR_std_duringAPF, vFBres_apf_t_duringAPF = calculate_averages(responders_vFB_APF, FB_mode = 'apf', param='apf')
vFBnonres_st_SR_duringST, vFBnonres_st_SR_std_duringST, vFBnonres_st_t_duringST = calculate_averages(nonresponders_vFB_ST, FB_mode = 'st', param = 'st')
vFBnonres_pof_SR_duringPOF, vFBnonres_pof_SR_std_duringPOF, vFBnonres_pof_t_duringPOF = calculate_averages(nonresponders_vFB_POF, FB_mode = 'pof', param ='pof')
vFBnonres_apf_SR_duringAPF, vFBnonres_apf_SR_std_duringAPF, vFBnonres_apf_t_duringAPF = calculate_averages(nonresponders_vFB_APF, FB_mode = 'apf', param='apf')

Plotting.plot_3SR_std(vFB_st_t_duringST, vFB_st_SR_duringST, vFB_st_SR_std_duringST, vFBres_st_t_duringST, vFBres_st_SR_duringST, vFBres_st_SR_std_duringST, vFBnonres_st_t_duringST, vFBnonres_st_SR_duringST, vFBnonres_st_SR_std_duringST, f'all, n = {len(subjects_vFB)}', f'responders, n = {len(responders_vFB_ST)}', f'nonresponders, n = {len(nonresponders_vFB_ST)}', show = True, color=[get_color('orchid', 0.3), 'orchid', get_color('orchid', 0.15)], savingname='vFB_meanST_allresnonres', title = f'vFB ST')
Plotting.plot_3SR_std(vFB_pof_t_duringPOF, vFB_pof_SR_duringPOF, vFB_pof_SR_std_duringPOF, vFBres_pof_t_duringPOF, vFBres_pof_SR_duringPOF, vFBres_pof_SR_std_duringPOF, vFBnonres_pof_t_duringPOF, vFBnonres_pof_SR_duringPOF, vFBnonres_pof_SR_std_duringPOF, f'all, n = {len(subjects_vFB)}', f'responders, n = {len(responders_vFB_POF)}', f'nonresponders, n = {len(nonresponders_vFB_POF)}', show = True, color=[get_color('burlywood', 0.2), 'burlywood', get_color('burlywood', 0.1)], savingname='vFB_meanPOF_allresnonres', title = f'vFB POF')
Plotting.plot_3SR_std(vFB_apf_t_duringAPF, vFB_apf_SR_duringAPF, vFB_apf_SR_std_duringAPF, vFBres_apf_t_duringAPF, vFBres_apf_SR_duringAPF, vFBres_apf_SR_std_duringAPF, vFBnonres_apf_t_duringAPF, vFBnonres_apf_SR_duringAPF, vFBnonres_apf_SR_std_duringAPF, f'all, n = {len(subjects_vFB)}', f'responders, n = {len(responders_vFB_APF)}', f'nonresponders, n = {len(nonresponders_vFB_APF)}', show = True, color=[get_color('c', 0.2), 'c', get_color('c', 0.1)], yaxis = True, title = f'hFB APF', savingname='vFB_meanAPF_allresnonres')

Plotting.plot_3SR_std(vFBres_st_t_duringST, vFBres_st_SR_duringST, vFBres_st_SR_std_duringST, vFBres_pof_t_duringPOF, vFBres_pof_SR_duringPOF, vFBres_pof_SR_std_duringPOF, vFBres_apf_t_duringAPF, vFBres_apf_SR_duringAPF, vFBres_apf_SR_std_duringAPF, 'ST responders', 'POF responders', 'APF responders', show = True, color=['orchid', 'burlywood', 'c'], yaxis = True, savingname='vFB_SR_allresponders')
print("all plots vFB res vs nonres and only res done")

# comparison plots only res
Plotting.plot_2SR_std(hFBres_st_t_duringST, hFBres_st_SR_duringST, hFBres_st_SR_std_duringST, vFBres_st_t_duringST, vFBres_st_SR_duringST, vFBres_st_SR_std_duringST, 'ST during hFB', 'ST during vFB', show = True, savingname='comp_SR_ST_res')
Plotting.plot_2SR_std(hFBres_pof_t_duringPOF, hFBres_pof_SR_duringPOF, hFBres_pof_SR_std_duringPOF, vFBres_pof_t_duringPOF, vFBres_pof_SR_duringPOF, vFBres_pof_SR_std_duringPOF, 'POF during hFB', 'POF during vFB', show = True, savingname='comp_SR_POF_res')
Plotting.plot_2SR_std(hFBres_apf_t_duringAPF, hFBres_apf_SR_duringAPF, hFBres_apf_SR_std_duringAPF, vFBres_apf_t_duringAPF, vFBres_apf_SR_duringAPF, vFBres_apf_SR_std_duringAPF, 'APF during hFB', 'APF during vFB', yaxis = True, show = True, savingname='comp_SR_APF_res')
print("all plots hFB/vFB res only res done")

# correlation hFB and vFB and save stats files all

correlation_path_hFB = r'C:\Users\User\Documents\CEFIR_LLUI\Haptic FB\correlation.csv'
stats_path_hFB = r'C:\Users\User\Documents\CEFIR_LLUI\Haptic FB'
correlation_path_vFB = r'C:\Users\User\Documents\CEFIR_LLUI\Visual FB\correlation.csv'
stats_path_vFB = r'C:\Users\User\Documents\CEFIR_LLUI\Visual FB'

# Check if the correlation file exists, then normally stats files exist as well.
if not os.path.exists(correlation_path_hFB):
    df_correlation_hFB = []
    df_statsST_hFB = []
    df_statsPOF_hFB = []
    df_statsAPF_hFB = []
    for i in range(1, n_hFB+1):
        subjects_hFB[f'S{i}'].correlation, subjects_hFB[f'S{i}'].statsST, subjects_hFB[f'S{i}'].statsPOF, subjects_hFB[f'S{i}'].statsAPF = subjects_hFB[f'S{i}'].calc_corrandstats()
        df_correlation_hFB.append(subjects_hFB[f'S{i}'].correlation)
        df_statsST_hFB.append(subjects_hFB[f'S{i}'].statsST)
        df_statsPOF_hFB.append(subjects_hFB[f'S{i}'].statsPOF)
        df_statsAPF_hFB.append(subjects_hFB[f'S{i}'].statsAPF)

    save_corrstats(df_correlation_hFB, correlation_path_hFB)
    save_corrstats(df_statsST_hFB, stats_path_hFB, FB = 'ST')
    save_corrstats(df_statsPOF_hFB, stats_path_hFB, FB = 'POF')
    save_corrstats(df_statsAPF_hFB, stats_path_hFB, FB = 'APF')
    print('corr/stats done individually and saved as a group.csv (hFB)')
else:
    df_correlation_hFB = pd.read_csv(correlation_path_hFB)
    print('correlation file hFB read')

# Check if the correlation file exists
if not os.path.exists(correlation_path_vFB):
    df_correlation_vFB = []
    df_statsST_vFB = []
    df_statsPOF_vFB = []
    df_statsAPF_vFB = []
    for i in range(1, n_vFB+1):
        if i != 2 and i != 3 and i != 4 and i != 6 and i != 12:
            subjects_vFB[f'S{i}'].correlation, subjects_vFB[f'S{i}'].statsST, subjects_vFB[f'S{i}'].statsPOF, subjects_vFB[f'S{i}'].statsAPF = subjects_vFB[f'S{i}'].calc_corrandstats()
            df_correlation_vFB.append(subjects_vFB[f'S{i}'].correlation)
            df_statsST_vFB.append(subjects_vFB[f'S{i}'].statsST)
            df_statsPOF_vFB.append(subjects_vFB[f'S{i}'].statsPOF)
            df_statsAPF_vFB.append(subjects_vFB[f'S{i}'].statsAPF)

    save_corrstats(df_correlation_vFB, correlation_path_vFB)
    save_corrstats(df_statsST_vFB, stats_path_vFB, FB = 'ST')
    save_corrstats(df_statsPOF_vFB, stats_path_vFB, FB = 'POF')
    save_corrstats(df_statsAPF_vFB, stats_path_vFB, FB = 'APF')
    print('corr/stats done individually and saved as a group.csv (vFB)')
else:
    df_correlation_vFB = pd.read_csv(correlation_path_vFB)
    print('correlation file vFB read')

calc_corrcoeffs (df_correlation_hFB, 'hFB', r'C:\Users\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx')
Plotting.plot_correlation(df_correlation_hFB, 'hFB', save=True)

calc_corrcoeffs (df_correlation_vFB, 'vFB', r'C:\Users\User\Documents\CEFIR_LLUI\Result_tables_all.xlsx')
Plotting.plot_correlation(df_correlation_vFB, 'vFB', save=True)
print('correlation plotted and printed for hFB/vFB')
