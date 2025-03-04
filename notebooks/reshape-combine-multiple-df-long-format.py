# Alexey Gilman's Python Solution

import pandas as pd
df = pd.read_csv("data/combine-df-diff-categoricals.csv")

"""
index based categories. data format must be consistent with respect to index:
i.e., rows 0-5 must be category "age", rows 6-7 must be category "sex"
"""

#define categories and their positions and add as column
ctgr = {0:"age",
        1:"age",
        2:"age",
        3:"age",
        4:"age",
        5:"age",
        6:"sex",
        7:"sex",
        8:"adhd",
        9:"adhd",
        10:"adhd",
        11:"anxiety",
        12:"anxiety",
        13:"anxiety",
        14:"OCD",
        15:"OCD",
        16:"OCD"
       }

df["category"] = pd.Series(ctgr)

#rename redundant category fields
df = df.rename(columns = {"age_cat":"subcategory",
                          "Sex":"subcategory",
                          "CME_MentalHealthDiagnosis_adhd":"subcategory",
                          "CME_MentalHealthDiagnosis_anxiety":"subcategory",
                          "CME_MentalHealthDiagnosis_ocd":"subcategory"})

#regex rename percent and count columns
df.columns = (df.columns
              .str.replace(r'(?i).*count.*', 'count', regex=True)
              .str.replace(r'(?i).*percent.*', 'percent', regex=True))

#merge columns by name 
df = df.T.groupby(df.columns).first().T

#reorder columns 
df = df[["category", "subcategory", "count", "percent"]]
