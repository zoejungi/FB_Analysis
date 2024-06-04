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
    subjects_hFB[f'S{i}'].swingtime = subjects_hFB[f'S{i}'].swingTime()
    subjects_hFB[f'S{i}'].steplength = subjects_hFB[f'S{i}'].stepLength()
    subjects_hFB[f'S{i}'].stepheight = subjects_hFB[f'S{i}'].stepHeight()
    subjects_hFB[f'S{i}'].stepwidth = subjects_hFB[f'S{i}'].stepWidth()
    subjects_hFB[f'S{i}'].GRFz = subjects_hFB[f'S{i}'].meanGRFz()
    subjects_hFB[f'S{i}'].kneeflexion = subjects_hFB[f'S{i}'].maxKneeflexion()
print('gait parameters calculated for all subjects hFB')

for i in range(1, n_vFB+1):
    if i != 2 and i != 3 and i != 4 and i != 6 and i !=12:
        subjects_vFB[f'S{i}'].st = subjects_vFB[f'S{i}'].ST()
        subjects_vFB[f'S{i}'].pof = subjects_vFB[f'S{i}'].POF()
        subjects_vFB[f'S{i}'].apf = subjects_vFB[f'S{i}'].maxAPF()
        subjects_vFB[f'S{i}'].swingtime = subjects_vFB[f'S{i}'].swingTime()
        subjects_vFB[f'S{i}'].steplength = subjects_vFB[f'S{i}'].stepLength()
        subjects_vFB[f'S{i}'].stepheight = subjects_vFB[f'S{i}'].stepHeight()
        subjects_vFB[f'S{i}'].stepwidth = subjects_vFB[f'S{i}'].stepWidth()
        subjects_vFB[f'S{i}'].GRFz = subjects_vFB[f'S{i}'].meanGRFz()
        subjects_vFB[f'S{i}'].kneeflexion = subjects_vFB[f'S{i}'].maxKneeflexion()
print('gait parameters calculated for all subjects vFB')

# plot all individuals
for i in range(1, n_hFB+1):
    # ST
    for j, df in enumerate(subjects_hFB[f'S{i}'].st):
        subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].st[j]['time'], subjects_hFB[f'S{i}'].st[j]['SR_SMA5'], label=f'S{i} SR$_{{ST}}$', savingname=f'hFB_S{i}_ST_SR')
        subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].st[j]['time'], subjects_hFB[f'S{i}'].st[j]['ST_left'], subjects_hFB[f'S{i}'].st[j]['ST_right'], ylabel='ST [s]', savingname=f'hFB_S{i}_ST_lr')
    # POF
    for j, df in enumerate(subjects_hFB[f'S{i}'].pof):
        subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].pof[j]['time'], subjects_hFB[f'S{i}'].pof[j]['SR_SMA5'], label=f'S{i} SR$_{{POF}}$', savingname=f'hFB_S{i}_POF_SR')
        subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].pof[j]['time'], subjects_hFB[f'S{i}'].pof[j]['POF_left_SMA5'], subjects_hFB[f'S{i}'].pof[j]['POF_right_SMA5'], ylabel='POF [N]', savingname=f'hFB_S{i}_POF_lr')
    # APF
    for j, df in enumerate(subjects_hFB[f'S{i}'].apf):
        subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].apf[j]['time'], subjects_hFB[f'S{i}'].apf[j]['SR_SMA5'], label=f'S{i} SR$_{{APF}}$', savingname=f'hFB_S{i}_APF_SR')
        subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].apf[j]['time'], subjects_hFB[f'S{i}'].apf[j]['apf_left'], subjects_hFB[f'S{i}'].apf[j]['apf_right'], ylabel='maxAPF [°]', savingname=f'hFB_S{i}_APF_lr')
    # Swingtime
    for j, df in enumerate(subjects_hFB[f'S{i}'].swingtime):
        subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].swingtime[j]['time'], subjects_hFB[f'S{i}'].swingtime[j]['SR_SMA5'], label=f'S{i} SR$_{{swingtime}}$', savingname=f'hFB_S{i}_swingtime_SR', baseline=False)
        subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].swingtime[j]['time'], subjects_hFB[f'S{i}'].swingtime[j]['swingtime_left_SMA5'], subjects_hFB[f'S{i}'].swingtime[j]['swingtime_right_SMA5'], ylabel='Swingtime [s]', savingname=f'hFB_S{i}_swingtime_lr')
    # Step Length
    for j, df in enumerate(subjects_hFB[f'S{i}'].steplength):
        subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].steplength[j]['time'], subjects_hFB[f'S{i}'].steplength[j]['SR_SMA5'], label=f'S{i} SR$_{{steplength}}$', savingname=f'hFB_S{i}_steplength_SR', baseline=False)
        subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].steplength[j]['time'], subjects_hFB[f'S{i}'].steplength[j]['steplength_left_SMA5'], subjects_hFB[f'S{i}'].steplength[j]['steplength_right_SMA5'], ylabel='Steplength [m]', savingname=f'hFB_S{i}_steplength_lr')
    # Step Height
    for j, df in enumerate(subjects_hFB[f'S{i}'].stepheight):
        subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].stepheight[j]['time'], subjects_hFB[f'S{i}'].stepheight[j]['SR_SMA5'], label=f'S{i} SR$_{{stepheight}}$', savingname=f'hFB_S{i}_stepheight_SR', baseline=False)
        subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].stepheight[j]['time'], subjects_hFB[f'S{i}'].stepheight[j]['stepheight_left_SMA5'], subjects_hFB[f'S{i}'].stepheight[j]['stepheight_right_SMA5'], ylabel='Stepheight [m]', savingname=f'hFB_S{i}_stepheight_lr')
    # Step Width
    for j, df in enumerate(subjects_hFB[f'S{i}'].stepwidth):
        subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].stepwidth[j]['time'], subjects_hFB[f'S{i}'].stepwidth[j]['SR_SMA5'], label=f'S{i} SR$_{{stepwidth}}$', savingname=f'hFB_S{i}_stepwidth_SR', baseline=False)
        subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].stepwidth[j]['time'], subjects_hFB[f'S{i}'].stepwidth[j]['stepwidth_left_SMA5'], subjects_hFB[f'S{i}'].stepwidth[j]['stepwidth_right_SMA5'], ylabel='Stepwidth [m]', savingname=f'hFB_S{i}_stepwidth_lr')
    # meanGRFz
    for j, df in enumerate(subjects_hFB[f'S{i}'].GRFz):
        subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].GRFz[j]['time'], subjects_hFB[f'S{i}'].GRFz[j]['SR_SMA5'], label=f'S{i} SR$_{{meanGRFz}}$', savingname=f'hFB_S{i}_meanGRFz_SR', baseline=False)
        subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].GRFz[j]['time'], subjects_hFB[f'S{i}'].GRFz[j]['GRFz_left_SMA5'], subjects_hFB[f'S{i}'].GRFz[j]['GRFz_right_SMA5'], ylabel='meanGRFz [N]', savingname=f'hFB_S{i}_meanGRFz_lr')
    # max Kneeflexion
    for j, df in enumerate(subjects_hFB[f'S{i}'].kneeflexion):
        subjects_hFB[f'S{i}'].plot_SR(subjects_hFB[f'S{i}'].kneeflexion[j]['time'], subjects_hFB[f'S{i}'].kneeflexion[j]['SR_SMA5'], label=f'S{i} SR$_{{max kneeflexion}}$', savingname=f'hFB_S{i}_kneeflexion_SR', baseline=False)
        subjects_hFB[f'S{i}'].plot_leftvsright(subjects_hFB[f'S{i}'].kneeflexion[j]['time'], subjects_hFB[f'S{i}'].kneeflexion[j]['knee_left_SMA5'], subjects_hFB[f'S{i}'].kneeflexion[j]['knee_right_SMA5'], ylabel='max kneeflexion [°]', savingname=f'hFB_S{i}_kneeflexion_lr')
print('all individual plots done for all subjects hFB')

for i in range(1, n_vFB+1):
    if i != 2 and i != 3 and i != 4 and i != 6 and i != 12:
        # ST
        for j, df in enumerate(subjects_vFB[f'S{i}'].st):
            subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].st[j]['time'], subjects_vFB[f'S{i}'].st[j]['SR_SMA5'], label=f'S{i} SR$_{{ST}}$', savingname=f'vFB_S{i}_ST_SR')
            subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].st[j]['time'], subjects_vFB[f'S{i}'].st[j]['ST_left'], subjects_vFB[f'S{i}'].st[j]['ST_right'], ylabel='ST [s]', savingname=f'vFB_S{i}_ST_lr')
        # POF
        for j, df in enumerate(subjects_vFB[f'S{i}'].pof):
            subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].pof[j]['time'], subjects_vFB[f'S{i}'].pof[j]['SR_SMA5'], label=f'S{i} SR$_{{POF}}$', savingname=f'vFB_S{i}_POF_SR')
            subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].pof[j]['time'], subjects_vFB[f'S{i}'].pof[j]['POF_left_SMA5'], subjects_vFB[f'S{i}'].pof[j]['POF_right_SMA5'], ylabel='POF [N]', savingname=f'vFB_S{i}_POF_lr')
        # APF
        for j, df in enumerate(subjects_vFB[f'S{i}'].apf):
            subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].apf[j]['time'], subjects_vFB[f'S{i}'].apf[j]['SR_SMA5'], label=f'S{i} SR$_{{APF}}$', savingname=f'vFB_S{i}_APF_SR')
            subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].apf[j]['time'], subjects_vFB[f'S{i}'].apf[j]['apf_left'], subjects_vFB[f'S{i}'].apf[j]['apf_right'], ylabel='maxAPF [°]', savingname=f'vFB_S{i}_APF_lr')
        # Swingtime
        for j, df in enumerate(subjects_vFB[f'S{i}'].swingtime):
            subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].swingtime[j]['time'], subjects_vFB[f'S{i}'].swingtime[j]['SR_SMA5'], label=f'S{i} SR$_{{swingtime}}$', savingname=f'vFB_S{i}_swingtime_SR', baseline=False)
            subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].swingtime[j]['time'], subjects_vFB[f'S{i}'].swingtime[j]['swingtime_left_SMA5'], subjects_vFB[f'S{i}'].swingtime[j]['swingtime_right_SMA5'], ylabel='Swingtime [s]', savingname=f'vFB_S{i}_swingtime_lr')
        # Step Length
        for j, df in enumerate(subjects_vFB[f'S{i}'].steplength):
            subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].steplength[j]['time'], subjects_vFB[f'S{i}'].steplength[j]['SR_SMA5'], label=f'S{i} SR$_{{steplength}}$', savingname=f'vFB_S{i}_steplength_SR', baseline=False)
            subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].steplength[j]['time'], subjects_vFB[f'S{i}'].steplength[j]['steplength_left_SMA5'], subjects_vFB[f'S{i}'].steplength[j]['steplength_right_SMA5'], ylabel='Steplength [m]', savingname=f'vFB_S{i}_steplength_lr')
        # Step Height
        for j, df in enumerate(subjects_vFB[f'S{i}'].stepheight):
            subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].stepheight[j]['time'], subjects_vFB[f'S{i}'].stepheight[j]['SR_SMA5'], label=f'S{i} SR$_{{stepheight}}$', savingname=f'vFB_S{i}_stepheight_SR', baseline=False)
            subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].stepheight[j]['time'], subjects_vFB[f'S{i}'].stepheight[j]['stepheight_left_SMA5'], subjects_vFB[f'S{i}'].stepheight[j]['stepheight_right_SMA5'], ylabel='Stepheight [m]', savingname=f'vFB_S{i}_stepheight_lr')
        # Step Width
        for j, df in enumerate(subjects_vFB[f'S{i}'].stepwidth):
            subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].stepwidth[j]['time'], subjects_vFB[f'S{i}'].stepwidth[j]['SR_SMA5'], label=f'S{i} SR$_{{stepwidth}}$', savingname=f'vFB_S{i}_stepwidth_SR', baseline=False)
            subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].stepwidth[j]['time'], subjects_vFB[f'S{i}'].stepwidth[j]['stepwidth_left_SMA5'], subjects_vFB[f'S{i}'].stepwidth[j]['stepwidth_right_SMA5'], ylabel='Stepwidth [m]', savingname=f'vFB_S{i}_stepwidth_lr')
        # meanGRFz
        for j, df in enumerate(subjects_vFB[f'S{i}'].GRFz):
            subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].GRFz[j]['time'], subjects_vFB[f'S{i}'].GRFz[j]['SR_SMA5'], label=f'S{i} SR$_{{meanGRFz}}$', savingname=f'vFB_S{i}_meanGRFz_SR', baseline=False)
            subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].GRFz[j]['time'], subjects_vFB[f'S{i}'].GRFz[j]['GRFz_left_SMA5'], subjects_vFB[f'S{i}'].GRFz[j]['GRFz_right_SMA5'], ylabel='meanGRFz [N]', savingname=f'vFB_S{i}_meanGRFz_lr')
        # max Kneeflexion
        for j, df in enumerate(subjects_vFB[f'S{i}'].kneeflexion):
            subjects_vFB[f'S{i}'].plot_SR(subjects_vFB[f'S{i}'].kneeflexion[j]['time'], subjects_vFB[f'S{i}'].kneeflexion[j]['SR_SMA5'], label=f'S{i} SR$_{{max kneeflexion}}$', savingname=f'vFB_S{i}_kneeflexion_SR', baseline=False)
            subjects_vFB[f'S{i}'].plot_leftvsright(subjects_vFB[f'S{i}'].kneeflexion[j]['time'], subjects_vFB[f'S{i}'].kneeflexion[j]['knee_left_SMA5'], subjects_vFB[f'S{i}'].kneeflexion[j]['knee_right_SMA5'], ylabel='max Kneeflexion [°]', savingname=f'vFB_S{i}_kneeflexion_lr')
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

Plotting.plot_3SR_std(hFB_st_t_duringST, hFB_st_SR_duringST, hFB_st_SR_std_duringST, hFB_st_t_duringPOF, hFB_st_SR_duringPOF, hFB_st_SR_std_duringPOF, hFB_st_t_duringAPF, hFB_st_SR_duringAPF, hFB_st_SR_std_duringAPF, 'ST during ST', 'ST during POF', 'ST during APF', show = True, color=['orchid', get_color('orchid', 0.15), get_color('orchid', 0.3)], savingname='hFB_meanST_SR_all')
Plotting.plot_3SR_std(hFB_pof_t_duringST, hFB_pof_SR_duringST, hFB_pof_SR_std_duringST, hFB_pof_t_duringPOF, hFB_pof_SR_duringPOF, hFB_pof_SR_std_duringPOF, hFB_pof_t_duringAPF, hFB_pof_SR_duringAPF, hFB_pof_SR_std_duringAPF, 'POF during ST', 'POF during POF', 'POF during APF', show = True, color=[get_color('burlywood', 0.15), 'burlywood', get_color('burlywood', 0.3)], savingname='hFB_meanST_SR_all')
Plotting.plot_3SR_std(hFB_apf_t_duringST, hFB_apf_SR_duringST, hFB_apf_SR_std_duringST, hFB_apf_t_duringPOF, hFB_apf_SR_duringPOF, hFB_apf_SR_std_duringPOF, hFB_apf_t_duringAPF, hFB_apf_SR_duringAPF, hFB_apf_SR_std_duringAPF, 'APF during ST', 'APF during POF', 'APF during APF', show = True, color=[get_color('c', 0.15), get_color('c', 0.3), 'c'], savingname='hFB_meanST_SR_all')

Plotting.plot_3SR_std(hFB_st_t_duringST, hFB_st_SR_duringST, hFB_st_SR_std_duringST, hFB_pof_t_duringPOF, hFB_pof_SR_duringPOF, hFB_pof_SR_std_duringPOF, hFB_apf_t_duringAPF, hFB_apf_SR_duringAPF, hFB_apf_SR_std_duringAPF, 'ST during ST', 'POF during POF', 'APF during APF', show = True, color=['orchid', 'burlywood', 'c'], savingname='hFB_SR_all')

vFB_st_SR_duringST, vFB_st_SR_std_duringST, vFB_st_t_duringST = calculate_averages(subjects_vFB, FB_mode = 'st', param = 'st')
vFB_st_SR_duringPOF, vFB_st_SR_std_duringPOF, vFB_st_t_duringPOF = calculate_averages(subjects_vFB, FB_mode = 'pof', param ='st')
vFB_st_SR_duringAPF, vFB_st_SR_std_duringAPF, vFB_st_t_duringAPF = calculate_averages(subjects_vFB, FB_mode = 'apf', param='st')

vFB_pof_SR_duringST, vFB_pof_SR_std_duringST, vFB_pof_t_duringST = calculate_averages(subjects_vFB, FB_mode = 'st', param = 'pof')
vFB_pof_SR_duringPOF, vFB_pof_SR_std_duringPOF, vFB_pof_t_duringPOF = calculate_averages(subjects_vFB, FB_mode = 'pof', param ='pof')
vFB_pof_SR_duringAPF, vFB_pof_SR_std_duringAPF, vFB_pof_t_duringAPF = calculate_averages(subjects_vFB, FB_mode = 'apf', param='pof')

vFB_apf_SR_duringST, vFB_apf_SR_std_duringST, vFB_apf_t_duringST = calculate_averages(subjects_vFB, FB_mode = 'st', param = 'apf')
vFB_apf_SR_duringPOF, vFB_apf_SR_std_duringPOF, vFB_apf_t_duringPOF = calculate_averages(subjects_vFB, FB_mode = 'pof', param ='apf')
vFB_apf_SR_duringAPF, vFB_apf_SR_std_duringAPF, vFB_apf_t_duringAPF = calculate_averages(subjects_vFB, FB_mode = 'apf', param='apf')

Plotting.plot_3SR_std(vFB_st_t_duringST, vFB_st_SR_duringST, vFB_st_SR_std_duringST, vFB_st_t_duringPOF, vFB_st_SR_duringPOF, vFB_st_SR_std_duringPOF, vFB_st_t_duringAPF, vFB_st_SR_duringAPF, vFB_st_SR_std_duringAPF, 'ST during ST', 'ST during POF', 'ST during APF', show = True, color=['orchid', get_color('orchid', 0.15), get_color('orchid', 0.3)], savingname='vFB_meanST_SR_all')
Plotting.plot_3SR_std(vFB_pof_t_duringST, vFB_pof_SR_duringST, vFB_pof_SR_std_duringST, vFB_pof_t_duringPOF, vFB_pof_SR_duringPOF, vFB_pof_SR_std_duringPOF, vFB_pof_t_duringAPF, vFB_pof_SR_duringAPF, vFB_pof_SR_std_duringAPF, 'POF during ST', 'POF during POF', 'POF during APF', show = True, color=[get_color('burlywood', 0.15), 'burlywood', get_color('burlywood', 0.3)], savingname='vFB_meanST_SR_all')
Plotting.plot_3SR_std(vFB_apf_t_duringST, vFB_apf_SR_duringST, vFB_apf_SR_std_duringST, vFB_apf_t_duringPOF, vFB_apf_SR_duringPOF, vFB_apf_SR_std_duringPOF, vFB_apf_t_duringAPF, vFB_apf_SR_duringAPF, vFB_apf_SR_std_duringAPF, 'APF during ST', 'APF during POF', 'APF during APF', show = True, color=[get_color('c', 0.15), get_color('c', 0.3), 'c'], savingname='vFB_meanST_SR_all')

Plotting.plot_3SR_std(vFB_st_t_duringST, vFB_st_SR_duringST, vFB_st_SR_std_duringST, vFB_pof_t_duringPOF, vFB_pof_SR_duringPOF, vFB_pof_SR_std_duringPOF, vFB_apf_t_duringAPF, vFB_apf_SR_duringAPF, vFB_apf_SR_std_duringAPF, 'ST during ST', 'POF during POF', 'APF during APF', show = True, color=['orchid', 'burlywood', 'c'], savingname='vFB_SR_all')

Plotting.plot_2SR_std(hFB_st_t_duringST, hFB_st_SR_duringST, hFB_st_SR_std_duringST, vFB_st_t_duringST, vFB_st_SR_duringST, vFB_st_SR_std_duringST, 'ST during hFB', 'ST during vFB', show = True, savingname='comp_SR_ST')
Plotting.plot_2SR_std(hFB_pof_t_duringPOF, hFB_pof_SR_duringPOF, hFB_pof_SR_std_duringPOF, vFB_pof_t_duringPOF, vFB_pof_SR_duringPOF, vFB_pof_SR_std_duringPOF, 'POF during hFB', 'POF during vFB', show = True, savingname='comp_SR_POF')
Plotting.plot_2SR_std(hFB_apf_t_duringAPF, hFB_apf_SR_duringAPF, hFB_apf_SR_std_duringAPF, vFB_apf_t_duringAPF, vFB_apf_SR_duringAPF, vFB_apf_SR_std_duringAPF, 'APF during hFB', 'APF during vFB', show = True, savingname='comp_SR_APF')


