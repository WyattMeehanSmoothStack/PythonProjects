"""
Created on Aug 13, 2021

@author: Wyatt Meehan
"""
import sys

import pandas as pd


def import_data():
    try:
        return pd.read_csv("C:\\Users\\meeha\\OneDrive\\Desktop\\SmoothStack\\PythonAssignments\\Salaries.csv")
    except FileNotFoundError:
        print("There was a problem with the file path, please check path is correct and file is present!")
        sys.exit("Program exiting")


if __name__ == '__main__':
    df = import_data()
    print(df.keys())

    # 1)
    print("1) ", df.head())

    # 2)
    print("\n2) ", df.info)

    # 3)
    print("\n3) Mean of first 10,000 base pay: ${:.2f}".format(df['BasePay'][0:10001].mean()))

    # 4)
    print("\n4) Max of TotalPayBenefits: ${}".format(df['TotalPayBenefits'].max()))

    # 5)
    jos_df = (df.loc[df['EmployeeName'] == 'JOSEPH DRISCOLL'])
    print("\n5) ", jos_df.iloc[0]["JobTitle"])

    # 6)
    print("6) $", jos_df.iloc[0]["TotalPayBenefits"])

    # 7)
    rich_df = (df.loc[df["TotalPayBenefits"] == df["TotalPayBenefits"].max()])
    print("7) ", rich_df.iloc[0]["EmployeeName"])

    # 8)
    poor_df = (df.loc[df["TotalPayBenefits"] == df["TotalPayBenefits"].min()])
    print("8) ", poor_df.iloc[0]["EmployeeName"])
    print("8) ", poor_df.iloc[0]["TotalPayBenefits"])

    # 9)
    avg_df = (df[(df["Year"] >= 2011) & (df["Year"] <= 2014)])

    # 10)
    print()
    print(len(pd.unique(df['JobTitle'])))

    # 11)
    print()
    print(df["JobTitle"].value_counts()[:7])

    # 12)
    print()
    print(len(pd.unique(df['JobTitle'])))

    # 13)

    # 14)
