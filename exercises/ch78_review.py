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


#############CHAPTER 7#############
#SCATTER PLOTS
#def SampleRows(df, nrows, replace=False):							#random sample of rows from dataframe
	#indices = np.random.choice(df.index, nrows, replace=replace)
	#sample = df.loc[indices]
	#return sample

#thinkplot.Scatter(x, y)											#makes scatterplot of x and y
	#thinkplot.Show()
#thinkstats2.Jitter(x, amt)											#jitters dataset x by amt
#thinkplot.HexBin(x, y)												#makes hexbin scatterplot of x and y

#MEASURES OF RELATIONSHIP
#thinkstats2.Cov(xs, ys)											#computes covariance of two datasets
#thinkstats2.Corr(xs, ys)											#computes Pearson's correlation (linear)
#thinkstats2.SpearmanCorr(xs, ys)									#computes Spearman's rank correlation (nonlinear)



#############CHAPTER 8#############
