### Data Science Review ###
###   Chapters 1,2,3    ###

## Modules ##
import pandas as pds
import thinkstats2 as ts2
import thinkplot as tplt

## Data ##
import nsfg

## Histograms ##

# Given a list of things, things...
things = ['cheese', 'chocolate', 'kale', 'chocolate', 'pepper flakes', 'cheese']

# Using a dictionary:

dict_hist = {}
for thing in things:
	dict_hist[thing] = dict_hist.get(thing, 0) + 1	# dictionary.get(key, default value) --> dictionary['key'] unless dictionary['key'] does not exist--then 0.
print 'Dictionary histogram:', dict_hist

# Using a counter
from collections import Counter 	# Requires this module
counter_hist = Counter() # Creates a counter object
for thing in things:
	counter_hist[thing] += 1	# Increment. It counts. Surprise! 
print 'Counter histogram:', counter_hist

# Using thinkstats module
ts2_hist = ts2.Hist(things)	# Note capital letter in class name.
print 'thinkstats2 histogram:', ts2_hist	# That's all. Thanks Allen!

# The thinkstats2 Hist object has a variety of other helpful methods
# These include 'Copy', 'Exp', 'Freq', 'Freqs', 'GetDict', 'Incr', 'IsSubset',  
#  'Items', 'Largest', 'Log', 'MakeCdf', 'MaxLike', 'Mult', 'Print', 'Remove', 
#  'Render', 'Scale', 'Set', 'SetDict', 'Smallest', 'Subtract', 'Total', 'Values', ...] 
# See dir(ts2_hist) for complete methods/attr.

# Frequency:
# There are multiple ways to access the number of times a particular 'thing' has occurred
ts2_hist['cheese']
ts2_hist.Freq('cheese')

# The frequency of an unknown item is 0
ts2_hist['cheefse']			# = 0
ts2_hist.Freq('cheefse')	# = 0

# You can get multiple frequencies at a time
ts2_hist.Freqs(['cheese', 'kale'])

# What are all of the values our histogram is counting?
print ts2_hist.Values() 	# Note capital letter
print sorted(ts2_hist.Values()) 	# You can sort them too!

# How about everything?
for h_value, h_freq in ts2_hist.Items():
	print h_value, h_freq	# You can even iterate through them

## Plotting ##
print '\nMapping string categories for numerical values for plotting histogram...\nLegend below.'
newhist = {}
for i, (value, freq) in enumerate(sorted(ts2_hist.Items())):
	newhist[i] = freq
	print value, '-->', i
print '.'*60

newts2hist = ts2.Hist(newhist)
tplt.PrePlot(1, cols=3)	# Sets stage for plotting multiple graphs in same figure. Can take no. of rows & cols.
						# First param notes how many 'lines' or data sets graphed per figure.
tplt.Hist(newts2hist)
tplt.Show(title = 'Histogram', xlabel = 'item', ylabel = 'no. of occurences') # Show figure. Optionally add labels, etc.
# Other options include title, xlabel, ylabel, xscale, yscale, xticks, yticks, axis, legend, and loc.


