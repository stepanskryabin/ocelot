import os

from openpyxl import load_workbook


PATH = os.path.abspath(os.getcwd())
FILE = "\\test.xlsx"

xfile = load_workbook(filename=PATH+FILE)

sheet = xfile[xfile.sheetnames[0]]

val = sheet.iter_cols(min_col=1, min_row=1, values_only=True)
