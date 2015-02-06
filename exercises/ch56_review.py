#Codebook available at: www.cdc.gov/nchs/nsfg/nsfg_cycle6.htm
#More codebook info: http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=pregResp&fileCode=PREG

#To run notebooks: cd to "ThinkStats2/code" ==> ipython notebook --matplotlib inline


#imports all data and functions in nsfg
import nsfg 

#imports all histogram, pdf, and cdf-generating functions
import thinkstats2

#imports all histogram, pdf, and cdf-plotting functions
import thinkplot

#imports math stuff
import numpy



#Creates a DataFrame of pregnancy data
df = nsfg.ReadFemPreg()


#############CHAPTER 5#############
#CDFs: DISTRIBUTIONS
#cdf = thinkstats2.Cdf()															#Lognormal CDF plotted as normal
	#thinkplot.Cdf(cdf, label='label')
	#thinkplot.Show(xlabel='xaxis', ylabel='yaxis', xscale='log')

#cdf = thinkstats2.Cdf()															#Pareto CDF plotted as line
	#thinkplot.Cdf(cdf, label='label')
	#thinkplot.Show(xlabel='xaxis', ylabel='yaxis', xscale='log', yscale='log')		#slope -a, intercept a*log(xm)

#PLOTTING CCDF
#thinkplot.Cdf(cdf, label='label', complement='True')						#plots CCDF as line
	#thinkplot.Show(xlabel='xaxis', ylabel='yaxis', yscale='log')			#plots CCDF on log scale
																			#if exponential distribution, line of slope -lambda

#NORMAL PROBABILITY PLOT
#xs, ys = thinkstats2.NormalProbability(sample)				#generates vectors for normal probability plot
															#xs: sorted values from sample. ys: normal distribution sample
#thinkplot.Plot(xs, ys, label='label')						#generates normal probability plot

#def MakeNormalPlot(sample)									#creates normal probability plot and compares to model
	#mean = sample.mean()
	#std = sample.std()

	#xs = [-xbound, xbound]		#choose appropriate bounds here!
	#fxs, fys = thinkstats2.FitLine(xs, inter=mean, slope=std)
	#thinkplot.Plot(fxs, fys)

	#xs, ys = thinkstats2.NormalProbability(sample)	
	#thinkplot.Plot(xs, ys, label='label')
