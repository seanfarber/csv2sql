#! /usr/bin/env python3

# author: Sean Farber Date: 2/7/2017

import csv
import os

file = open('category1.csv')
reader = csv.reader(file)
dataList = list(reader)

row = []
for i in range(len(dataList)):
	row.append(tuple(dataList[i]))

tableData = open('tableData.sql', 'w')
for i in range(1, len(dataList)):
	tableData.write('INSERT INTO Category VALUES' + str(row[i]) + ';\n')
tableData.close()
