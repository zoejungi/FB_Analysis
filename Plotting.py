import numpy as np
import matplotlib.pyplot as plt

class Plotting:

    #to have all plots with the same fontsizes

    xticks = 14 #fontsize xticks labels
    t = 18 #fontsize, title
    a = 0.8 #transparency of color = alpha
    f = 16 #fontsize, ticks and legend

    @classmethod
    def plot_leftvsright(csl, time, left, right, ylabel, title = [], show = False, savingname = []):
        plt.figure(figsize = (10, 8))
        plt.plot(time, left, label='Left', linewidth=1, linestyle='-', color='red')
        plt.plot(time, right, label='Right', linewidth=1, linestyle='-', color='royalblue')
        ax = plt.subplot()
        ax.set_xlim(time.iloc[1], time.iloc[-1])
        xticks = [time.iloc[1], 60, 240, 300, 480]
        ax.set_xticks(xticks)  # only set ticks every second location, starting with first location
        ax.set_xticklabels([''] * len(xticks))  # Set empty labels
        for tick in xticks[:]:
            ax.axvline(x=tick, color='lightgray', linestyle='dotted', alpha=0.7)
        # Define the labels
        labels = ['NW', 'FB1', 'No FB1', 'FB2', 'No FB2']
        # Define positions for the labels
        label_positions = [(time.iloc[1] + 60) / 2, (60 + 240) / 2, (240 + 300) / 2, (300 + 480) / 2, (480 + 640) / 2]
        # Add labels at the specified positions
        for pos, label in zip(label_positions, labels):
            ax.text(pos, ax.get_ylim()[0] - 0.05 * (ax.get_ylim()[1] - ax.get_ylim()[0]), label, ha='center', va='top',
                    fontsize=csl.xticks)
        # Adjust the plot to make sure labels fit well
        plt.subplots_adjust(bottom=0.2)
        plt.ylabel(ylabel, fontsize= csl.f)
        plt.xticks(fontsize=csl.f)
        plt.yticks(fontsize=csl.f)
        plt.legend(loc='upper right', fontsize=csl.f)
        if title:
            plt.title(title, fontsize = csl.t)
        if savingname:
            plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Indiv\{savingname}')
        if show:
            plt.show()
        plt.close()
    @classmethod
    def plot_SR (cls, x, y, label, show = False, title = [], color = 'm', yaxis = False, baseline = True, savingname = [], target = True):
        plt.figure(figsize = (10, 8))
        plt.plot(x, y, marker='', markersize=4, linewidth=1, linestyle='-', color=color, label=f'{label}')
        plt.axhline(y=1, color='lightgrey', linestyle='-', linewidth=1)

        if target:
            plt.axhline(y=0.8, color='g', linestyle='--', linewidth=1, label='Target SR')
            plt.axhspan(0.75, 0.85, facecolor='palegreen', alpha=0.2)
        ax = plt.subplot()
        if yaxis:
            # Autoscale the y-axis
            plt.autoscale(enable=True, axis='y', tight=False)
        else:
            ax.set_yticks([0.7, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00, 1.05, 1.1])
            ax.set_yticklabels(('70', '75', '80', '85', '90', '95', '100', '105', '110'))
            ax.set_ylim(0.7,1.1)

        ax.set_xlim(x.iloc[1], x.iloc[-1])
        xticks = [x.iloc[1], 60, 240, 300,480]
        ax.set_xticks(xticks)  # only set ticks every second location, starting with first location
        ax.set_xticklabels([''] * len(xticks))  # Set empty labels
        for tick in xticks[:]:
            ax.axvline(x=tick, color='lightgray', linestyle='dotted', alpha=0.7)
        # Define the labels
        labels = ['NW', 'FB1', 'No FB1', 'FB2', 'No FB2']
        # Define positions for the labels
        label_positions = [(x.iloc[1] + 60) / 2, (60 + 240) / 2, (240 + 300) / 2, (300 + 480) / 2, (480 + 640) / 2]
        # Add labels at the specified positions
        for pos, label in zip(label_positions, labels):
            ax.text(pos, ax.get_ylim()[0] - 0.05 * (ax.get_ylim()[1] - ax.get_ylim()[0]), label, ha='center', va='top', fontsize=cls.xticks)
        # Adjust the plot to make sure labels fit well
        plt.subplots_adjust(bottom=0.2)
        if baseline:
            plt.ylabel('Baseline SR [%]', fontsize = cls.f)
        else:
            plt.ylabel('NW SR [%]', fontsize=cls.f)
        plt.xticks(fontsize = cls.f)
        plt.yticks(fontsize = cls.f)
        plt.legend(fontsize = cls.f, bbox_to_anchor=(0.65, 1.1), loc='upper left', borderaxespad=0.)
        if title:
            plt.title(title, fontsize = cls.t)
        if savingname:
            plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Indiv\{savingname}')
        if show:
            plt.show()
        plt.close()
    @classmethod
    def plot_SR_std (cls, x, y, y_std, label = None, show = False, yaxis = False, title = [], color = 'c', baseline = True, savingname = [], target = True):
        plt.figure(figsize = (10, 8))
        plt.fill_between(x, np.array(y) - np.array(y_std), np.array(y) + np.array(y_std), color=color, alpha=0.1)
        plt.plot(x, y, marker='o', markersize=4, linewidth=1, linestyle='-', color=color, label=f'Mean SR$_{{{label}}}$')
        plt.axhline(y=1, color='lightgrey', linestyle='-', linewidth=1)

        if target:
            plt.axhline(y=0.8, color='g', linestyle='--', linewidth=1, label='Target SR')
            plt.axhspan(0.75, 0.85, facecolor='palegreen', alpha=0.2)
        ax = plt.subplot()
        if yaxis:
            # Autoscale the y-axis
            plt.autoscale(enable=True, axis='y', tight=False)
        else:
            ax.set_yticks([0.7, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00, 1.05, 1.1])
            ax.set_yticklabels(('70', '75', '80', '85', '90', '95', '100', '105', '110'))
            ax.set_ylim(0.7,1.1)

        ax.set_xlim(x.iloc[1], x.iloc[-1])
        xticks = [x.iloc[1], 60, 240, 300,480]
        ax.set_xticks(xticks)  # only set ticks every second location, starting with first location
        ax.set_xticklabels([''] * len(xticks))  # Set empty labels
        for tick in xticks[:]:
            ax.axvline(x=tick, color='lightgray', linestyle='dotted', alpha=0.7)
        # Define the labels
        labels = ['NW', 'FB1', 'No FB1', 'FB2', 'No FB2']
        # Define positions for the labels
        label_positions = [(x.iloc[1] + 60) / 2, (60 + 240) / 2, (240 + 300) / 2, (300 + 480) / 2, (480 + 640) / 2]
        # Add labels at the specified positions
        for pos, label in zip(label_positions, labels):
            ax.text(pos, ax.get_ylim()[0] - 0.05 * (ax.get_ylim()[1] - ax.get_ylim()[0]), label, ha='center', va='top', fontsize=cls.xticks)
        # Adjust the plot to make sure labels fit well
        plt.subplots_adjust(bottom=0.2)
        if baseline:
            plt.ylabel('Baseline SR [%]', fontsize = cls.f)
        else:
            plt.ylabel('NW SR [%]', fontsize=cls.f)
        plt.xticks(fontsize = cls.f)
        plt.yticks(fontsize = cls.f)
        plt.legend(fontsize = cls.f, bbox_to_anchor=(0.65, 1.1), loc='upper left', borderaxespad=0.)
        if title:
            plt.title(title, fontsize = cls.t)
        if savingname:
            plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Summary\{savingname}')
        if show:
            plt.show()
        plt.close()
    @classmethod
    def plot_2SR_std (cls, x1, y1, y1_std, x2, y2, y2_std, label1, label2, show = False, title = [], yaxis = False, color = ['purple', 'darkgreen'], baseline = True, savingname = [], target = True):
        plt.figure(figsize = (10, 8))

        plt.fill_between(x1, np.array(y1) - np.array(y1_std), np.array(y1) + np.array(y1_std), color=color[0], alpha=0.1)
        plt.plot(x1, y1, marker='o', markersize=4, linewidth=1, linestyle='-', color=color[0],
         label=f'Mean SR$_{{{label1}}}$')
        plt.fill_between(x2, np.array(y2) - np.array(y2_std), np.array(y2) + np.array(y2_std), color=color[1], alpha=0.1)
        plt.plot(x2, y2, marker='o', markersize=4, linewidth=1, linestyle='-', color=color[1],
                 label=f'Mean SR$_{{{label2}}}$')
        plt.axhline(y=1, color='lightgrey', linestyle='-', linewidth=1)

        if target:
            plt.axhline(y=0.8, color='g', linestyle='--', linewidth=1, label = 'Target SR')
            plt.axhspan(0.75, 0.85, facecolor='palegreen', alpha=0.2)
        ax = plt.subplot()
        if yaxis:
            # Autoscale the y-axis
            plt.autoscale(enable=True, axis='y', tight=False)
        else:
            ax.set_yticks([0.7, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00, 1.05, 1.1])
            ax.set_yticklabels(('70', '75', '80', '85', '90', '95', '100', '105', '110'))
            ax.set_ylim(0.7,1.1)

        ax.set_xlim(x1.iloc[1], x1.iloc[-1])
        xticks = [x1.iloc[1], 60, 240, 300,480]
        ax.set_xticks(xticks)  # only set ticks every second location, starting with first location
        ax.set_xticklabels([''] * len(xticks))  # Set empty labels
        for tick in xticks[:]:
            ax.axvline(x=tick, color='lightgray', linestyle='dotted', alpha=0.7)
        # Define the labels
        labels = ['NW', 'FB1', 'No FB1', 'FB2', 'No FB2']
        # Define positions for the labels
        label_positions = [(x1.iloc[1] + 60) / 2, (60 + 240) / 2, (240 + 300) / 2, (300 + 480) / 2, (480 + 640) / 2]
        # Add labels at the specified positions
        for pos, label in zip(label_positions, labels):
            ax.text(pos, ax.get_ylim()[0] - 0.05 * (ax.get_ylim()[1] - ax.get_ylim()[0]), label, ha='center', va='top', fontsize=cls.xticks)
        # Adjust the plot to make sure labels fit well
        plt.subplots_adjust(bottom=0.2)
        if baseline:
            plt.ylabel('Baseline SR [%]', fontsize = cls.f)
        else:
            plt.ylabel('NW SR [%]', fontsize=cls.f)
        plt.xticks(fontsize = cls.f)
        plt.yticks(fontsize = cls.f)
        plt.legend(fontsize = cls.f, bbox_to_anchor=(0.65, 1.1), loc='upper left', borderaxespad=0.)
        if title:
            plt.title(title, fontsize = cls.t)
        if savingname:
            plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Summary\{savingname}')
        if show:
            plt.show()
        plt.close()
    @classmethod
    def plot_3SR_std (cls, x1, y1, y1_std, x2, y2, y2_std, x3, y3, y3_std, label1, label2, label3, show = False, yaxis = False, title = [], color = ['c', 'm', 'burlywood'], baseline = True, savingname = [], target = True):
        plt.figure(figsize = (10, 8))

        plt.fill_between(x1, np.array(y1) - np.array(y1_std), np.array(y1) + np.array(y1_std), color=color[0], alpha=0.1)
        plt.plot(x1, y1, marker='o', markersize=4, linewidth=1, linestyle='-', color=color[0],
         label=f'Mean SR$_{{{label1}}}$')
        plt.fill_between(x2, np.array(y2) - np.array(y2_std), np.array(y2) + np.array(y2_std), color=color[1], alpha=0.1)
        plt.plot(x2, y2, marker='o', markersize=4, linewidth=1, linestyle='-', color=color[1],
                 label=f'Mean SR$_{{{label2}}}$')
        plt.fill_between(x3, np.array(y3) - np.array(y3_std), np.array(y3) + np.array(y3_std), color=color[2], alpha=0.1)
        plt.plot(x3, y3, marker='o', markersize=4, linewidth=1, linestyle='-', color=color[2],
                 label=f'Mean SR$_{{{label3}}}$')
        plt.axhline(y=1, color='lightgrey', linestyle='-', linewidth=1)

        if target:
            plt.axhline(y=0.8, color='g', linestyle='--', linewidth=1, label = 'Target SR')
            plt.axhspan(0.75, 0.85, facecolor='palegreen', alpha=0.2)
        ax = plt.subplot()
        if yaxis:
            # Autoscale the y-axis
            plt.autoscale(enable=True, axis='y', tight=False)
        else:
            ax.set_yticks([0.7, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00, 1.05, 1.1])
            ax.set_yticklabels(('70', '75', '80', '85', '90', '95', '100', '105', '110'))
            ax.set_ylim(0.7,1.1)

        ax.set_xlim(x1.iloc[1], x1.iloc[-1])
        xticks = [x1.iloc[1], 60, 240, 300,480]
        ax.set_xticks(xticks)  # only set ticks every second location, starting with first location
        ax.set_xticklabels([''] * len(xticks))  # Set empty labels
        for tick in xticks[:]:
            ax.axvline(x=tick, color='lightgray', linestyle='dotted', alpha=0.7)
        # Define the labels
        labels = ['NW', 'FB1', 'No FB1', 'FB2', 'No FB2']
        # Define positions for the labels
        label_positions = [(x1.iloc[1] + 60) / 2, (60 + 240) / 2, (240 + 300) / 2, (300 + 480) / 2, (480 + 640) / 2]
        # Add labels at the specified positions
        for pos, label in zip(label_positions, labels):
            ax.text(pos, ax.get_ylim()[0] - 0.05 * (ax.get_ylim()[1] - ax.get_ylim()[0]), label, ha='center', va='top', fontsize=cls.xticks)
        # Adjust the plot to make sure labels fit well
        plt.subplots_adjust(bottom=0.2)
        if baseline:
            plt.ylabel('Baseline SR [%]', fontsize = cls.f)
        else:
            plt.ylabel('NW SR [%]', fontsize=cls.f)
        plt.xticks(fontsize = cls.f)
        plt.yticks(fontsize = cls.f)
        plt.legend(fontsize = cls.f, bbox_to_anchor=(0.65, 1.1), loc='upper left', borderaxespad=0.)
        if title:
            plt.title(title, fontsize = cls.t)
        if savingname:
            plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Summary\{savingname}')
        if show:
            plt.show()
        plt.close()
    @classmethod
    def plot_correlation(cls, df, FB, show = False, save = False):
        #plot correlation graphs during ST, APF and POF using df_correlation file having data from all subjects in all conditions and for all SR_params

        df_ST = df[(df['condition'] == 'NWduringST') | (df['condition'] == 'duringST')]
        df_POF = df[(df['condition'] == 'NWduringPOF') | (df['condition'] == 'duringPOF')]
        df_APF = df[(df['condition'] == 'NWduringAPF') | (df['condition'] == 'duringAPF')]

        columns_ST = df_ST.columns.drop(['condition', 'subject_ID', 'cycle_number', 'SR_ST'])
        columns_POF = df_POF.columns.drop(['condition', 'subject_ID', 'cycle_number', 'SR_POF'])
        columns_APF = df_APF.columns.drop(['condition', 'subject_ID', 'cycle_number', 'SR_APF'])

        for i in range(len(columns_ST)):
            plt.figure(figsize = (8,8))
            plt.scatter(df_ST[df_ST["condition"] == "duringST"]["SR_ST"],df_ST[df_ST["condition"] == "duringST"][columns_ST[i]], marker="o", facecolors='none', edgecolors='r', s=1, label="FB2")
            plt.scatter(df_ST[df_ST["condition"] == "NWduringST"]["SR_ST"],df_ST[df_ST["condition"] == "NWduringST"][columns_ST[i]], marker="o", facecolors='none', edgecolors='b', s=1, label="NW")

            plt.xlabel("ST SR", fontsize=cls.f)
            plt.ylabel(columns_ST[i], fontsize=cls.f)
            plt.legend(fontsize=cls.f, bbox_to_anchor=(0.65, 1.1), loc='upper left', borderaxespad=0.)
            plt.ylim(0.5, 2.3)
            plt.xlim(0, 3)
            plt.xticks(fontsize=cls.f)
            plt.yticks(fontsize=cls.f)

            # Linear regression
            coeffs = np.polyfit(df_ST["SR_ST"], df_ST[columns_ST[i]], 1)
            poly = np.poly1d(coeffs)
            plt.plot(df_ST["SR_ST"], poly(df_ST["SR_ST"]), color='black', label=f'Linear regression: y={coeffs[0]:.2f}x + {coeffs[1]:.2f}', linewidth=1)
            if save:
                plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Correlation\{FB}_CorrST_{columns_ST[i]}.png')
            if show:
                plt.show()
            plt.close()

        for i in range(len(columns_POF)):
            plt.figure(figsize=(8, 8))
            plt.scatter(df_POF[df_POF["condition"] == "duringPOF"]["SR_POF"],
                        df_POF[df_POF["condition"] == "duringPOF"][columns_POF[i]], marker="o", facecolors='none',
                        edgecolors='r', s=1, label="FB2")
            plt.scatter(df_POF[df_POF["condition"] == "NWduringPOF"]["SR_POF"],
                        df_POF[df_POF["condition"] == "NWduringPOF"][columns_POF[i]], marker="o", facecolors='none',
                        edgecolors='b', s=1, label="NW")

            plt.xlabel("POF SR", fontsize=cls.f)
            plt.ylabel(columns_POF[i], fontsize=cls.f)
            plt.legend(fontsize=cls.f, bbox_to_anchor=(0.65, 1.1), loc='upper left', borderaxespad=0.)
            plt.ylim(0.5, 2.3)
            plt.xlim(0, 3)
            plt.xticks(fontsize=cls.f)
            plt.yticks(fontsize=cls.f)

            # Linear regression
            coeffs = np.polyfit(df_POF["SR_POF"], df_POF[columns_POF[i]], 1)
            poly = np.poly1d(coeffs)
            plt.plot(df_POF["SR_POF"], poly(df_POF["SR_POF"]), color='black',
                     label=f'Linear regression: y={coeffs[0]:.2f}x + {coeffs[1]:.2f}', linewidth=1)
            if save:
                plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Correlation\{FB}_CorrPOF_{columns_POF[i]}.png')
            if show:
                plt.show()
            plt.close()

        for i in range(len(columns_APF)):
            plt.figure(figsize=(8, 8))
            plt.scatter(df_APF[df_APF["condition"] == "duringAPF"]["SR_APF"],
                        df_APF[df_APF["condition"] == "duringAPF"][columns_APF[i]], marker="o", facecolors='none',
                        edgecolors='r', s=1, label="FB2")
            plt.scatter(df_APF[df_APF["condition"] == "NWduringAPF"]["SR_APF"],
                        df_APF[df_APF["condition"] == "NWduringAPF"][columns_APF[i]], marker="o", facecolors='none',
                        edgecolors='b', s=1, label="NW")

            plt.xlabel("APF SR", fontsize=cls.f)
            plt.ylabel(columns_APF[i], fontsize=cls.f)
            plt.legend(fontsize=cls.f, bbox_to_anchor=(0.65, 1.1), loc='upper left', borderaxespad=0.)
            plt.ylim(0.5, 2.3)
            plt.xlim(0, 3)
            plt.xticks(fontsize=cls.f)
            plt.yticks(fontsize=cls.f)

            # Linear regression
            coeffs = np.polyfit(df_APF["SR_APF"], df_APF[columns_APF[i]], 1)
            poly = np.poly1d(coeffs)
            plt.plot(df_APF["SR_APF"], poly(df_APF["SR_APF"]), color='black',
                     label=f'Linear regression: y={coeffs[0]:.2f}x + {coeffs[1]:.2f}', linewidth=1)
            if save:
                plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Correlation\{FB}_CorrAPF_{columns_APF[i]}.png')
            if show:
                plt.show()
            plt.close()