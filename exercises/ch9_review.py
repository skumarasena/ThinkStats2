#Codebook available at: www.cdc.gov/nchs/nsfg/nsfg_cycle6.htm
#More codebook info: http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=pregResp&fileCode=PREG

#To run notebooks: cd to "ThinkStats2/code" ==> ipython notebook --matplotlib inline

#ThinkStats2 documentation: http://greenteapress.com/thinkstats2/thinkstats2.html
#ThinkStats2 Github: https://github.com/AllenDowney/DataScience/blob/master/thinkstats2.py

#Pandas DataFrame documentation: http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.html
#Pandas Series documentation: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html



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


#############CHAPTER 9#############
#test = TestClassName(data)                 #given data from an experiment, computes pvalue
    #pvalue = test.PValue()

