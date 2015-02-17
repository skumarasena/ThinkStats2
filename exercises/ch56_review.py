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

#############CHAPTER 6#############
#MOMENTS
#def RawMoment(xs, k):								#computes kth raw moment of xs
	#return sum(x**k for x in xs)/len(xs)			#1st moment is mean

#def CentralMoment(xs, k):							#computes kth central moment of xs
	#mean = RawMoment(xs, 1)						#2nd central moment is variance
	#return sum((x-mean)**k for x in xs)/len(xs)

#def StandardizedMoment(xs, k):						#computes kth standardized moment of xs
	#var = CentralMoment(xs, 2)
	#std = math.sqrt(var)
	#return CentralMoment(xs, k)/std**k


#SKEWNESS
#def skewness(xs):									#3rd standardized moment is skewness
	#return StandardizedMoment(xs, 3)

#def PearsonMedianSkewness(xs):						#computes Pearson's Median Skewness
	#median = xs.Median()		#or can use Allen's Median(xs)
	#mean = RawMoment(xs, 1)
	#var = CentralMoment(xs, 2)
	#std = math.sqrt(var)
	#gp = 3*(mean-median)/std
	#return gp
