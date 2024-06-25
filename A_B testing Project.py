#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# In this Project I'll be working with sample data from a 
#farming simulation app. I'll utilize statistical testing 
#to articulate whether price packages of A/B/ or C are
#most responsive for users over the recorded span of a week


#Import libraries first
import pandas as pd
import numpy as np

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')

print(abdata.head())

num_visits = len(abdata)
print(num_visits)

#Let's say we determine that we need to generate a minimum of $1000
#in weekly revenue to justify adding an upgrade package 
#we need to discover what price points are most responsive to users.

#first lets explore how many sales we need to reach our price goal for each package 

num_sales_needed_099 = 1000 / .99
print(num_sales_needed_099)

#Now calculate the proportion of visitors needed, i'll do this for all the packages

p_sales_needed_099 = num_sales_needed_099 / num_visits
print(p_sales_needed_099)

num_sales_needed_199 = 1000 / 1.99
num_sales_needed_499 = 1000 / 4.99

p_sales_needed_199 = num_sales_needed_199 / num_visits
p_sales_needed_499 = num_sales_needed_499 / num_visits

print(p_sales_needed_199)
print(p_sales_needed_499)


#Since we have a single sample of categorical data and want to compare it to 
#a hypothetical population value, a binomial test is appropriate

#We need the number of visitors in the groups and
#the number of visitors who made a purchase for each group 

samp_size_099 = np.sum(abdata.group == 'A')
sales_099 = np.sum((abdata.group == 'A') & (abdata.is_purchase == 'Yes'))

samp_size_199 = np.sum(abdata.group == 'B')
sales_199 = np.sum((abdata.group == 'B') & (abdata.is_purchase == 'Yes'))

samp_size_499 = np.sum(abdata.group == 'C')
sales_499 = np.sum((abdata.group == 'C') & (abdata.is_purchase == 'Yes'))



from scipy.stats import binom_test

pvalueA = binom_test(sales_099,samp_size_099,p_sales_needed_099)
print(pvalueA)

pvalueB = binom_test(sales_199,samp_size_199,p_sales_needed_199)
print(pvalueB)

pvalueC = binom_test(sales_499,samp_size_499,p_sales_needed_499)
print(pvalueC)

#Group C is the only p-value below the threshold of 0.05. Therefore, the C group 
#is the only group where we would conclude that the purchase rate is significantly higher 
#than the target needed to reach $1000 revenue per week. Therefore, we should charge $4.99 for the upgrade!

