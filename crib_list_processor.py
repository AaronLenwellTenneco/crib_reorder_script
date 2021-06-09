"""This script search crib list for items that are on an "always order" list and marks them accordingly. The file
must be saved at c:/users/public/documents as 'criblist.csv'. It is better to remove items not puchased in SAP first"""
import pandas as pd
from datetime import date

#crib_item_list is the proposed list of parts, scrubbed of NaN
criblist = "c:/users/public/documents/criblist.csv"
crib_item_list = pd.read_csv(criblist)
crib_item_list = crib_item_list[crib_item_list['Description'].notna()]

#always_order is the list of parts which are always needed
always_order = "c:/users/public/documents/search_terms.csv"
always_order_list = pd.read_csv(always_order)

#parts_to_order is a blank dataframe where the results will be stored
parts_to_order = pd.DataFrame()

#search for the term and save it to parts_to_order
for i in range(len(always_order_list.Description)):
    term = always_order_list.Description.iloc[i].upper()
    parts_to_order = parts_to_order.append(crib_item_list[crib_item_list['Description'].str.contains(term)])

#remove any duplicates
parts_to_order = parts_to_order.drop_duplicates()

#export final list to csv with today's date 
datestring = str(date.today())
parts_to_order.to_csv(f"c:/users/public/documents/Crib_AML_{datestring}.csv")
