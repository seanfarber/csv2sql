#! /usr/bin/env python3

# author: Sean Farber Date: 2/7/2017

import csv
import os
import sys

file = open(sys.argv[1])
reader = csv.reader(file)
dataList = list(reader)

row = []
for i in range(len(dataList)):
	row.append(tuple(dataList[i]))

print('Enter the name of the table you want to input into')
tableName = input()

print('Enter the name of the output file ex. file.sql')
outPutFile = input()

tableData = open(outPutFile, 'w')
for i in range(1, len(dataList)):
	tableData.write('INSERT INTO ' + tableName + ' VALUES' + str(row[i]) + ';\n')
tableData.close()
