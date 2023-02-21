import numpy as np
from pandas import read_csv
import datetime as dt
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from matplotlib.widgets import SpanSelector


# load a single file as a numpy array
def load_file(filepath):
	dataframe = read_csv(filepath, header=None, delimiter=';')
	return dataframe.values

result = load_file('second_day_no_sleep.csv')

EEG_AF3:    list[float] = []
EEG_F7:     list[float] = []
EEG_F3:     list[float] = []
EEG_FC5:    list[float] = []
EEG_T7:     list[float] = []
EEG_P7:     list[float] = []
EEG_O1:     list[float] = []
EEG_O2:     list[float] = []
EEG_P8:     list[float] = []

for i in range(2, len(result)):
	
	EEG_AF3.append(result[i][4])
	EEG_F7.append(result[i][5])
	EEG_F3.append(result[i][6])
	EEG_FC5.append(result[i][7])
	EEG_T7.append(result[i][8])
	EEG_P7.append(result[i][9])
	EEG_O1.append(result[i][10])
	EEG_O2.append(result[i][11])
	EEG_P8.append(result[i][12])


x: list[float] = []
start = 0
size = len(EEG_F7)


for i in range(0, size):
	x.append(i)

# Setting Plot and Axis variables as subplots()
# function returns tuple(fig, ax)
Plot, Axis = plt.subplots(9)
 
# Adjust the bottom size according to the
# requirement of the user
plt.subplots_adjust(bottom=0.2)
 
# Set the x and y axis to some dummy data

 
# plot the x and y using plot function
EEG_AF3_C   = Axis[0]
EEG_F7_C    = Axis[1]
EEG_F3_C    = Axis[2]
EEG_FC5_C   = Axis[3]
EEG_T7_C    = Axis[4]
EEG_P7_C    = Axis[5]
EEG_O1_C    = Axis[6]
EEG_O2_C    = Axis[7]
EEG_P8_C    = Axis[8]



EEG_AF3_C.plot(range(start, size), EEG_AF3[start:size])
EEG_F7_C.plot(x[start:size], EEG_F7[start:size])
EEG_F3_C.plot(x[start:size], EEG_F3[start:size])
EEG_FC5_C.plot(x[start:size], EEG_FC5[start:size])
EEG_T7_C.plot(x[start:size], EEG_T7[start:size])
EEG_P7_C.plot(x[start:size], EEG_P7[start:size])
EEG_O1_C.plot(x[start:size], EEG_O1[start:size])
EEG_O2_C.plot(x[start:size], EEG_O2[start:size])
EEG_P8_C.plot(x[start:size], EEG_P8[start:size])


# Choose the Slider color
slider_color = 'White'
 
# Set the axis and slider position in the plot
axis_position = plt.axes([0.2, 0.1, 0.65, 0.03],
                         facecolor = slider_color)

freq = Slider(ax=axis_position,
                        label='Pos',
			            valmin=start,
			            valmax=size)
 
# update() function to change the graph when the
# slider is in use
def update(val):
    pos = freq.val
    
    EEG_AF3_C.axis([pos, pos+600.0, 0, 6000])
    EEG_F7_C.axis([pos, pos+600.0, 0, 6000])
    EEG_F3_C.axis([pos, pos+600.0, 0, 8000])
    EEG_FC5_C.axis([pos, pos+600.0, 0, 8000])
    EEG_T7_C.axis([pos, pos+600.0, 0, 4500])
    EEG_P7_C.axis([pos, pos+600.0, 0, 4500])
    EEG_O1_C.axis([pos, pos+600.0, 0, 4500])
    EEG_O2_C.axis([pos, pos+600.0, 0, 4500])
    EEG_P8_C.axis([pos, pos+600.0, 0, 4500])


    Plot.canvas.draw_idle()
 
# update function called using on_changed() function
freq.on_changed(update)
 
# Display the p
EEG_F7_C.yaxis.set_ticks(np.arange(0.0, 5000.0, 1000.0))
EEG_AF3_C.yaxis.set_ticks(np.arange(0.0, 5000.0, 1000.0))
EEG_F3_C.yaxis.set_ticks(np.arange(0.0, 10000.0, 2000.0))
EEG_FC5_C.yaxis.set_ticks(np.arange(0.0, 10000.0, 2000.0))
EEG_T7_C.yaxis.set_ticks(np.arange(0.0, 10000.0, 2000.0))
EEG_P7_C.yaxis.set_ticks(np.arange(0.0, 5000.0, 2000.0))
EEG_O1_C.yaxis.set_ticks(np.arange(0.0, 5000.0, 2000.0))
EEG_O2_C.yaxis.set_ticks(np.arange(0.0, 5000.0, 2000.0))
EEG_P8_C.yaxis.set_ticks(np.arange(0.0, 5000.0, 2000.0))


def onselect(vmin, vmax):
	return 0

EEG_F7_SPAN = SpanSelector(
	ax=EEG_F7_C,
	onselect=onselect,
	direction='horizontal',
    useblit=True,
    drag_from_anywhere=True,
    interactive=True,
)

EEG_AF3_SPAN = SpanSelector(
	ax=EEG_AF3_C,
	onselect=onselect,
	direction='horizontal',
    useblit=True,
    drag_from_anywhere=True,
    interactive=True,
)

EEG_F3_SPAN = SpanSelector(
	ax=EEG_F3_C,
	onselect=onselect,
	direction='horizontal',
    useblit=True,
    drag_from_anywhere=True,
    interactive=True,
)

EEG_FC5_SPAN = SpanSelector(
	ax=EEG_FC5_C,
	onselect=onselect,
	direction='horizontal',
    useblit=True,
    drag_from_anywhere=True,
    interactive=True,
)
#5
EEG_T7_SPAN = SpanSelector(
	ax=EEG_T7_C,
	onselect=onselect,
	direction='horizontal',
    useblit=True,
    drag_from_anywhere=True,
    interactive=True,
)
#6
EEG_P7_SPAN = SpanSelector(
	ax=EEG_P7_C,
	onselect=onselect,
	direction='horizontal',
    useblit=True,
    drag_from_anywhere=True,
    interactive=True,
)
#7
EEG_O1_SPAN = SpanSelector(
	ax=EEG_O1_C,
	onselect=onselect,
	direction='horizontal',
    useblit=True,
    drag_from_anywhere=True,
    interactive=True,
)
#8
EEG_O2_SPAN = SpanSelector(
	ax=EEG_O2_C,
	onselect=onselect,
	direction='horizontal',
    useblit=True,
    drag_from_anywhere=True,
    interactive=True,
)
#9
EEG_P8_SPAN = SpanSelector(
	ax=EEG_P8_C,
	onselect=onselect,
	direction='horizontal',
    useblit=True,
    drag_from_anywhere=True,
    interactive=True,
)
plt.show()
