Subject class, where kinematic, kinetic and spatiotemporal gait parameters are calculated per gait cycle for left and right for 1 subject during 1 testing. 
The gait parameters include:
  - maximal ankle plantarflexion at push off, maximal kneeflexion during swing phase
  - push off force, mean vertical GRF (ground reaction force)
  - stance time, swing time, step width, step height, step length
The SR (symmetry ratio) is calculated as well (raw and normalized by the SR during NW - Natural Walking):
  - SR = leftParamValue/rightParamValue
  - SR_NW = SR/(SR during NW)

The functions to calculate these parameters and the respective time during the measurement are in the functions.py.
The helperfunctions.py contains functions for simplifying the functions in functions.py (e.g. open and read data files, calculate SR, etc)

The main.py analyses all subjects from haptics and visual FB study (LLUI). Plotting the mean of all subjects (of both haptics and visual) for each type of FB (targeting APF, ST, POF) and for each param.
The goal is to compare the effectiveness and intuitiveness of both FB modalities.
