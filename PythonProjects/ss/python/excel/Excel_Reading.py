'''
Created on Aug 11, 2021

@author: Wyatt Meehan
'''
import datetime
import re

import openpyxl


def read_month(path):
    pattern = "expedia_report_monthly_(.*?).xlsx"
    month_year = re.search(pattern, path).group(1)
    print(month_year)

    workbook = openpyxl.load_workbook(path, data_only=True)
    worksheet1 = workbook['Summary Rolling MoM']
    for row in worksheet1.iter_rows(worksheet1.min_row, worksheet1.max_row):
        for cell in row:
            if cell.value is not None:
                print(type(cell.value), end=" || ")
        print(" \n")

if __name__ == '__main__':
    read_month(
        "C:\\Users\\meeha\\git\\PythonProjects\\PythonProjects\\.pydevproject"
        "\\PythonProjects\\ss\\python\\excel\\expedia_report_monthly_january_2018.xlsx")
