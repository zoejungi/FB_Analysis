Subject class, where kinematic, kinetic and spatiotemporal gait parameters are calculated per gait cycle for left and right for 1 subject.
The gait parameters include:
  - maximal ankle plantarflexion at push off (self.apf = self.maxAPF()), maximal kneeflexion during swing phase (self.kneeflexion = self.Kneeflexion())
  - push off force (self.pof = self.POF()), mean vertical GRF (ground reaction force)(self.GRFz = self.meanGRFz())
  - stance time (self.st = self.ST()), swing time (self.swingtime = self.Swingtime()), step width, step height, step length (the spatiotemporal parameters need to be taken with a grain of salt, as the spatiotemp. files are not accurately calculated
The column headers in each dataframe (= for each param) include at least:
  - 'param_left_SMA5'
  - 'param_right_SMA5'
  - 'SR_raw': param_left/param_right
  - 'SR': SR_raw/baseline_SR for ST, APF and POF, SR_raw/NW_SR for all other params
  - 'SR_SMA5':
  - 'time': time for each SR
Correlation and Statistical analysis dataframe can be saved as well within this class.

Plotting class, where all plots are made for the gait parameter analysis and correlation:
  - plot_leftvsright: left and right values are plotted together
  - plot_SR: 1 SR is plotted (e.g from 1 subject)
  - plot_SR_std: 1 SR incl std is plotted (e.g. param ST from all hFB subjects during ST FB)
  - plot_2SR_std: 2 SR incl std are plotted (e.g. comparing ST from all vFB and ST from all hFB subjects during ST FB)
  - plot_3SR_std: 3 SR incl std are plotted (e.g. comparing ST from all hFB subjects during ST. POF and APF FB)
  - plot_correlation: during NW and during FB2 phase
for all plots, the labels, title, colors, savingname, etc can be adapted while calling the method. if no savingname is given, the plot will not be saved (the output path is fixed in the method). show = True shows the plot when running the code (default = False). yaxis = True (let yaxis adapt to data, othetwise yaxis fixed -> default = False).
for all plots the fontsizes are defined as class attributes and used in each method

GDI.py defines the GDI function (incl. plotting in datapath and printing values to excel -> Results_tables_all.xlsx) and the function to get data for GDI (GDI = Gait Deviation Index)
SUS_TLX.py defines the SUS function (incl. plotting in datapath and printing values to excel -> Results_tables_all.xlsx)(System Usability Scale) and the TLX_function (incl. plotting)(Task Load Index)
main_GDI_SUS_TLX.py gives an example how to use these functions to calculate hFB and vFB data and to compare them. 

The helperfunctions.py contains functions for simplifying the methods of the Subject class, the GDI.py and the Plotting class (e.g. open and read data files, calculate SR, etc)

The main_subj.py analyses all subjects from haptics and visual FB study. Plotting the mean of all subjects (of both haptics and visual) for each type of FB (targeting APF, ST, POF) and for each param. Correlation and statistical data are saved as well. Correlation plots are plotted.
The goal is to compare the effectiveness and intuitiveness of both FB modalities.

Statistical analysis/comparison has still to be done.
