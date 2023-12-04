import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
# Zoom region inset axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Global
plt.rcParams['font.size'] = 8
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['figure.dpi'] = 300
#plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.constrained_layout.use'] = True

#
fig = plt.figure()

# figure size
fixed_width_mm = 80
fixed_height_mm = 54
fixed_width_inch = fixed_width_mm / 25.4
fixed_height_inch = fixed_height_mm / 25.4
fig.set_size_inches(fixed_width_inch, fixed_height_inch)
#fig.set_figwidth(fixed_width_inch)
#fig.set_figheight(fixed_height_inch)

# Import data
data = pd.read_csv('data.csv')
x = data['Time [ms]']
y1 = data['y1']
y2 = data['y2']

# Add subplot
ax = fig.add_subplot(111)
# curve
ax.plot(x, y1, color = 'r', label = 'yold', linewidth = 1)
ax.plot(x, y2, color = 'b', label = 'ynew', linewidth = 1)
# axis
ax.set_xlim(0, 5)
ax.set_ylim(0, 12)
ax.set_xticks(np.linspace(0, 5, 6),['0','1','2','3','4','5'])
ax.set_yticks(np.linspace(0, 12, 7),['0','2','4','6','8','10','12'])
ax.set_xlabel('Time (ms)')
ax.set_ylabel('ylabel')
# legend order
handles, labels = ax.get_legend_handles_labels()
order = [1, 0]   #(optional) order = [0, 1]
ax.legend([handles[idx] for idx in order], [labels[idx] for idx in order], 
					ncol = 1, loc = 'lower right', fontsize = 8) # ncol is the number of columns 
ax.grid(True, linestyle = '--', linewidth = 0.5, color = 'gray')
# annotate and text
ax.annotate('', xy=(1.5, 10), xytext=(1.5, 11.5), arrowprops=dict(arrowstyle='-|>',color='g'), color='g')
ax.text(1.6, 11, 'Text', fontsize = 8, color = 'g', ha = 'left', va = 'center')

# Zoom fig
x01, x02, y01, y02 = 1, 2, 9.6, 10.2
axins = ax.inset_axes([0.25, 0.25, 0.4, 0.4], xlim = (x01, x02), ylim = (y01, y02))
axins.plot(x, y1, color = 'b',linewidth = 0.8)
axins.plot(x, y2, color = 'r',linewidth = 0.8)
axins.set_xticks(np.linspace(1, 2, 3),['1','1.5','2'])
axins.set_yticks(np.linspace(9.6, 10.2, 3),['9.6', '9.9', '10.2'])
axins.patch.set_facecolor('#FFFEA4')
axins.grid(True,linestyle = '--', linewidth = 0.5, color = 'gray')
axins.annotate('', xy=(1.4, 9.72), xytext=(1.55, 10.1), arrowprops=dict(arrowstyle='-|>',color='g'), color='g')
axins.text(1.55, 10.1, 'Text', fontsize = 8, color = 'g', ha = 'left', va = 'center')
ax.indicate_inset_zoom(axins, alpha = 0.5, edgecolor = "m")
#(optional) mark_inset(ax, axins, loc1=3, loc2=1, fc="none", ec='gray', lw=1)

# (optional)
# fig.tight_layout()
# fig.subplots_adjust(top=0.97,bottom=0.18,right=0.97,hspace=0.2,wspace=0.2)

#
plt.show()