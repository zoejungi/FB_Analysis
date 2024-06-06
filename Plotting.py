import numpy as np
import matplotlib.pyplot as plt

class Plotting:

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
    def plot_SR (cls, x, y, label, show = False, title = [], color = 'm', baseline = True, savingname = [], target = True):
        plt.figure(figsize = (10, 8))
        plt.plot(x, y, marker='', markersize=4, linewidth=1, linestyle='-', color=color, label=f'{label}')
        plt.axhline(y=1, color='lightgrey', linestyle='-', linewidth=1)

        if target:
            plt.axhline(y=0.8, color='g', linestyle='--', linewidth=1, label='Target Value')
            plt.axhspan(0.75, 0.85, facecolor='palegreen', alpha=0.2, label='Margin zone')
        ax = plt.subplot()
        ax.set_yticks([0.7, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00, 1.05, 1.1])
        ax.set_yticklabels(('70', '75', '80', '85', '90', '95', '100', '105', '110'))
        ax.set_xlim(x.iloc[1], x.iloc[-1])
        ax.set_ylim(0.7,1.1)

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
    def plot_SR_std (cls, x, y, y_std, label = None, show = False, title = [], color = 'c', baseline = True, savingname = [], target = True):
        plt.figure(figsize = (10, 8))
        plt.fill_between(x, np.array(y) - np.array(y_std), np.array(y) + np.array(y_std), color=color, alpha=0.1)
        plt.plot(x, y, marker='o', markersize=4, linewidth=1, linestyle='-', color=color, label=f'Mean SR$_{{{label}}}$')
        plt.axhline(y=1, color='lightgrey', linestyle='-', linewidth=1)

        if target:
            plt.axhline(y=0.8, color='g', linestyle='--', linewidth=1, label='Target Value')
            plt.axhspan(0.75, 0.85, facecolor='palegreen', alpha=0.2, label='Margin zone')
        ax = plt.subplot()
        ax.set_yticks([0.7, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00, 1.05, 1.1])
        ax.set_yticklabels(('70', '75', '80', '85', '90', '95', '100', '105', '110'))
        ax.set_xlim(x.iloc[1], x.iloc[-1])
        ax.set_ylim(0.7,1.1)

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
    def plot_2SR_std (cls, x1, y1, y1_std, x2, y2, y2_std, label1, label2, show = False, title = [], color = ['purple', 'darkgreen'], baseline = True, savingname = [], target = True):
        plt.figure(figsize = (10, 8))

        plt.fill_between(x1, np.array(y1) - np.array(y1_std), np.array(y1) + np.array(y1_std), color=color[0], alpha=0.1)
        plt.plot(x1, y1, marker='o', markersize=4, linewidth=1, linestyle='-', color=color[0],
         label=f'Mean SR$_{{{label1}}}$')
        plt.fill_between(x2, np.array(y2) - np.array(y2_std), np.array(y2) + np.array(y2_std), color=color[1], alpha=0.1)
        plt.plot(x2, y2, marker='o', markersize=4, linewidth=1, linestyle='-', color=color[1],
                 label=f'Mean SR$_{{{label2}}}$')
        plt.axhline(y=1, color='lightgrey', linestyle='-', linewidth=1)

        if target:
            plt.axhline(y=0.8, color='g', linestyle='--', linewidth=1)
            plt.axhspan(0.75, 0.85, facecolor='palegreen', alpha=0.2)
        ax = plt.subplot()
        ax.set_yticks([0.7, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00, 1.05, 1.1])
        ax.set_yticklabels(('70', '75', '80', '85', '90', '95', '100', '105', '110'))
        ax.set_xlim(x1.iloc[1], x1.iloc[-1])
        ax.set_ylim(0.7,1.1)

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
    def plot_3SR_std (cls, x1, y1, y1_std, x2, y2, y2_std, x3, y3, y3_std, label1, label2, label3, show = False, title = [], color = ['c', 'm', 'burlywood'], baseline = True, savingname = [], target = True):
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
            plt.axhline(y=0.8, color='g', linestyle='--', linewidth=1)
            plt.axhspan(0.75, 0.85, facecolor='palegreen', alpha=0.2)
        ax = plt.subplot()
        ax.set_yticks([0.7, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00, 1.05, 1.1])
        ax.set_yticklabels(('70', '75', '80', '85', '90', '95', '100', '105', '110'))
        ax.set_xlim(x1.iloc[1], x1.iloc[-1])
        ax.set_ylim(0.7,1.1)

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