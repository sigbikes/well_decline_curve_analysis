#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 18:09:56 2018

@author: Sig
"""
import os
import pandas as pd

########################### Data Directories################
demo_dir = '/Users/Sig/Python/Git/well_decline_curve_analysis/data/'
data_dir = '/Users/Sig/Documents/WHR_PC/Gen3/'
prog_dir = '/Users/Sig/Python/Git/well_decline_curve_analysis/'

########################### Data Files######################
demo_heads = 'Well_header_data.csv'
demo_prod = 'Production_Time_Series.CSV'
data = '20180605_Gen3_Prod.csv'


os.chdir(demo_dir)

demo_head_df = pd.read_csv(demo_dir+demo_heads)
head_cols = demo_head_df.columns()

df = pd.read_csv(data_dir)
