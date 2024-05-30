
import matplotlib.pyplot as plt

class Plotting:
    def __init__(self):
        self.xticks = 14 #fontsize xticks labels
        self.t = 18 #fontsize, title
        self.a = 0.8 #transparency of color = alpha
        self.f = 16 #fontsize, ticks and legend

    def plot_leftvsright(self, time, left, right, ylabel, title = [], save = False, show = False, savingname = []):
        plt.figure()
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
                    fontsize=self.xticks)
        # Adjust the plot to make sure labels fit well
        plt.subplots_adjust(bottom=0.2)
        plt.ylabel(ylabel, fontsize= self.f)
        plt.xticks(fontsize=self.f)
        plt.yticks(fontsize=self.f)
        plt.legend(loc='upper right', fontsize=self.f)
        if title:
            plt.title(title, fontsize = self.t)
        if save:
            plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Indiv\{savingname}')
        if show:
            plt.show()
    def plot_SR (self, x, y, label, save = False, show = False, title = [], color = 'm', baseline = True, savingname = []):
        plt.figure()
        plt.plot(x, y, marker='', markersize=4, linewidth=1, linestyle='-', color=color, label=label)
        plt.axhline(y=0.8, color='g', linestyle='--', linewidth=1, label='Target Value')
        plt.axhline(y=1, color='lightgrey', linestyle='-', linewidth=1)
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
            ax.text(pos, ax.get_ylim()[0] - 0.05 * (ax.get_ylim()[1] - ax.get_ylim()[0]), label, ha='center', va='top', fontsize=self.xticks)
        # Adjust the plot to make sure labels fit well
        plt.subplots_adjust(bottom=0.2)
        if baseline:
            plt.ylabel('Baseline SR [%]', fontsize = self.f)
        else:
            plt.ylabel('NW SR [%]', fontsize=self.f)
        plt.xticks(fontsize = self.f)
        plt.yticks(fontsize = self.f)
        plt.legend(loc='upper right', fontsize = self.f)
        if title:
            plt.title(title, fontsize = self.t)
        if save:
            plt.savefig(rf'C:\Users\User\Documents\CEFIR_LLUI\Plots\Indiv\{savingname}')
        if show:
            plt.show()