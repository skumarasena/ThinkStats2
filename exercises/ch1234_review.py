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



#############CHAPTER 1#############

#GENERAL
#type(var)																	#gives you type of variable
#len(var)																	#gives you length of array/series/dataframe
#sample = numpy.random.choice(series_name, sample_size, replace=True)		#random sample from Series series_name of sample_size, replacing

#CREATING DATAFRAMES
#df = pandas.DataFrame(array)		#creates new DataFrame from 2D array
#df = nsfg.DataSetName()			#creates new DataFrame containing dataset "DataSetName"
#df2 = df[df.col_name == ...]		#creates new DataFrame containing elements satisfying condition
#df2 = df.loc['row1', 'row2', ...]	#creates new DataFrame from rows with labels "row1", "row2", ...
#df2 = df.loc['row1':'row2']		#creates new DataFrame from rows with labels "row1" through "row2" (inclusive)
#df2 = df.iloc[row1, row2, ...]		#creates new DataFrame from rows with numeric indices "row1", "row2", ... (zero-indexed)
#df2 = df.iloc[row1:row2]			#creates new DataFrame from rows with numeric indices "row1" through "row2" (not including row2)

#READING FROM DATAFRAME
#df.columns 													#returns an "Index" of column names
#df.columns[i] 													#returns the name of the ith column
#df = pandas.DataFrame(array, columns=['col1', 'col2', ...])	#renames columns to "col1", "col2", ...
#df = pandas.DataFrame(array, index=['index1', 'index2', ...])	#renames rows to "index1", "index2", ...

#WRITING TO DATAFRAME
#df['new_col'] = ...		#creates new column in DataFrame. Note: DO NOT df.new_col!!!	

#CREATING SERIES
#series = df['col_name'] 		#sets x to be the Series representing the column "col_name"
#series = df.col_name			#does the same. AVOID
#series = df.col_name == ...	#creates boolean Series with a condition
#series = df.loc['row_name']	#creates Series from row with label "row_name"
#series = df.iloc[row_num]		#creates Series from row with index "row_num" (zero-indexed)

#REFERENCING ELEMENTS IN SERIES
#series[i]					#returns ith element of Series (and just the element)
#series[i:j]				#returns ith to jth (not including j) elements, of Series including indices

#ANALYSIS
#df.col_name.value_counts().sort_index()		#prints sorted value counts
#df.col_name.mean()								#calculates average of data
#df.col_name.var()								#computes variance
#df.col_name.std()								#computes standard deviation

#def CohenEffectSize(group1, group2):			#computes Cohen's d (effect size) for two Series
	#diff = group1.mean() - group2.mean()

	#var1 = group1.var()
	#var2 = group2.var()
	#n1, n2 = len(group1), len(group2)

	#pooled_var = (n1*var1 + n2*var2)/(n1+n2)
	#d = diff/math.sqrt(pooled_var)
	#return d



#############CHAPTER 2#############

#CREATING HISTOGRAMS
#hist = thinkstats2.Hist([3, 4, 5, 6])		#creates Hist from list
#hist = thinkstats2.Hist(df.col_name)		#creates Hist from pandas Series
#d2 = d[d.col_name == ...]					#creates Hist from DataFrame condition
	#hist = thinkstats2.Hist(d2.col_name)

#ACCESSING FREQUENCIES
#hist.Freq(elem)						#finds frequency of element "elem"
#hist[elem]								#finds frequency of element "elem"

#ACCESSING VALUES
#hist.Values()							#returns unsorted list of elements
#for val in sorted(hist.Values()): 		#sorted list of val/freq tuples (include list = [])
	#list.append((val, hist.Freq(val)))
#for val, freq in hist.Items():			#sorted list of val/freq tuples (initialize list)
#hist.Smallest(n)						#list of lowest n values in Hist (val/freq tuples)
#hist.Largest(n)						#list of highest n values in Hist (val/freq tuples)


#MAKING HISTOGRAM PLOTS
#thinkplot.Hist(hist, label='label')	#creates and shows histogram plot
	#thinkplot.Show(xlabel='value', ylabel='frequency')



#############CHAPTER 3#############

#CREATING PMFs
#pmf = thinkstats2.Pmf([2,3,4,5])		#creates Pmf from list
#pmf = thinkstats2.Pmf(df.col_name)		#creates Pmf from pandas Series

#ACCESSING PROBABILITIES
#pmf.Prob(elem)							#finds probability of element "elem"
#pmf[elem]								#finds probability of element "elem"	
#pmf.Mult(elem, factor)					#multiplies probability of element "elem" by "factor" 
											#(non-normalized result)
#pmf.Normalize()						#normalizes Pmf so probabilities add to 1
#pmf.Total()							#sums probabilities of Pmf (if normalized, should be 1)
#pmf2 = pmf.Copy()						#copies Pmf "pmf" to "pmf2"
#pmf.Mean()								#computes average value of Pmf

#MAKING PMF PLOTS
#thinkplot.Hist(pmf, label='label')		#plots Pmf as a histogram (bar graph)
	#thinkplot.Show()

#BIASING PMF
#def BiasPmf(pmf, label):				#biases PMF as in "classroom size" example
	#new_pmf = pmf.Copy(label = label)	#multiplies each probability by how many people observe it

	#for x, p in pmf.Items():
		#new_pmf.Mult(x, x)		

	#new_pmf.Normalize()
	#return new_pmf

#UNBIASING PMF
#def UnbiasPmf(pmf, label):				#unbiases PMF as in "classroom size" example
	#new_pmf = pmf.Copy(label = label)	#divides each probability by how many people observe it

	#for x, p in pmf.Items():
		#new_pmf.Mult(x, 1.0/x)

	#new_pmf.Normalize()
	#return new_pmf



#############CHAPTER 4#############

#CREATING CDFs
#cdf = thinkstats2.Cdf([3, 4, 5, 6])		#creates Cdf from list
#cdf = thinkstats2.Cdf(df.col_name)			#creates Cdf from pandas Series

#ACCESSING VALUES/PROBABILITIES
#cdf.Prob(elem)								#computes probability p = Cdf(elem)
#cdf.Value(prob)							#computes elem such that prob = Cdf(elem)
#cdf.PercentileRank(elem)					#computes percentile rank of elem, equivalent to 100*Cdf(elem)
#cdf.Percentile(prob)						#computes elem, equivalent to Value(prob/100)
#cdf.Random()								#selects random element from CDF
#cdf.Sample(sample_size)					#selects random sample of size "sample_size" from CDF

#MAKING CDF PLOTS
#thinkplot.Cdf(cdf, label='label')									#plots CDF as line
	#thinkplot.Show(xlabel = 'xaxis', ylabel='yaxis')