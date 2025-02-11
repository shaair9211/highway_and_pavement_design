import openpyxl
import os
import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()



excel_file_path = r'C:\Users\shaai\PycharmProjects\pythonProject\Highway and Pavement\data_sheet for ESAL.xlsx'
workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook['Sheet1']

def ESAL(AADT, Tf, Gr, D, L):
    ESAL = (AADT) * (Tf) * (Gr) * (D) *(L) * (365)
    return ESAL

def EALF(load, a, b, k):
    LEF = (load / (18*a)) ** k #a=1.00,1.83,2.66 for single tandem and tridem
    EALF = LEF * b # b=1.0, 0.857, 1.033 for single axle to single, tandem to single & tridem to single
    return EALF

def Gr(r, Y):
    r = r/100
    if r>0:
        Gr = (((1+r)**Y)-1)/r
    elif r == 0:
        Gr = 20
    return Gr

def AADT(vol, hr_counted, WF, MF):
    HF = 1+(0.02*(24 - hr_counted))
    AADT = vol * HF * WF * MF
    return(AADT)


C3 = float(sheet['C3'].value)
C4 = float(sheet['C4'].value)
C5 = float(sheet['C5'].value)
C6 = float(sheet['C6'].value)
C7 = float(sheet['C7'].value)
C8 = float(sheet['C8'].value)

D3 = float(sheet['D3'].value)
D4 = float(sheet['D4'].value)
D5 = float(sheet['D5'].value)
D6 = float(sheet['D6'].value)
D7 = float(sheet['D7'].value)
D8 = float(sheet['D8'].value)

E3 = float(sheet['E3'].value)
E4 = float(sheet['E4'].value)
E5 = float(sheet['E5'].value)
E6 = float(sheet['E6'].value)
E7 = float(sheet['E7'].value)
E8 = float(sheet['E8'].value)

F3 = float(sheet['F3'].value)
F4 = float(sheet['F4'].value)
F5 = float(sheet['F5'].value)
F6 = float(sheet['F6'].value)
F7 = float(sheet['F7'].value)
F8 = float(sheet['F8'].value)

G7 = float(sheet['G7'].value)
G8 = float(sheet['G8'].value)

D10 = float(sheet['D10'].value) #no of hours counted
D11 = float(sheet['D11'].value) #Weekly factor
D12 = float(sheet['D12'].value) #Monthly Factor
D13 = float(sheet['D13'].value) #Years

D15 = float(sheet['D15'].value) #Directional Distribution
D16 = float(sheet['D16'].value) #Lane Distribution
D17 = float(sheet['D17'].value) #k value


AADT_1 =  121   # AADT(C3, D10, D11, D12)
AADT_2 =  35   # AADT(C4, D10, D11, D12)
AADT_3 =  121   # AADT(C5, D10, D11, D12)
AADT_4 =  423   # AADT(C6, D10, D11, D12)
AADT_5 =  302   # AADT(C7, D10, D11, D12)
AADT_6 =  36   # AADT(C6, D10, D11, D12)


AADT = AADT_1 + AADT_2 + AADT_3 + AADT_4 + AADT_5 + AADT_6
print('AADT is coming out to be:', AADT)

Gr_1 = Gr(D3, D13)
Gr_2 = Gr(D4, D13)
Gr_3 = Gr(D5, D13)
Gr_4 = Gr(D6, D13)
Gr_5 = Gr(D7, D13)
Gr_6 = Gr(D8, D13)


EALF_front1 = EALF(E3, 1.0, 1.0, D17)
EALF_front2 = EALF(E4, 1.0, 1.0, D17)
EALF_front3 = EALF(E5, 1.0, 1.0, D17)
EALF_front4 = EALF(E6, 1.0, 1.0, D17)
EALF_front5 = EALF(E7, 1.0, 1.0, D17)
EALF_front6 = EALF(E8, 1.0, 1.0, D17)

EALF_rear_11 = EALF(F3, 1.0, 1.0, D17)
EALF_rear_12 = EALF(F4, 1.0, 1.0, D17)
EALF_rear_13 = EALF(F5, 1.0, 1.0, D17)
EALF_rear_14 = EALF(F6, 1.83, 0.857, D17)
EALF_rear_15 = EALF(F7, 1.0, 1.0, D17)
EALF_rear_16 = EALF(F8, 1.83, 0.857, D17)

EALF_rear_21 = EALF(G7, 1.83, 0.857, D17)
EALF_rear_22 = EALF(G8, 2.66, 1.033, D17)

Tf_1 =  EALF_front1 + EALF_rear_11
Tf_2 =  EALF_front2 + EALF_rear_12
Tf_3 =  EALF_front3 + EALF_rear_13
Tf_4 =  EALF_front4 + EALF_rear_14
Tf_5 =  EALF_front5 + EALF_rear_15 + EALF_rear_21
Tf_6 =  EALF_front6 + EALF_rear_15 + EALF_rear_22


ESAL_1 = ESAL(AADT_1, Tf_1, Gr_1, D15, D16)
ESAL_2 = ESAL(AADT_2, Tf_2, Gr_2, D15, D16)
ESAL_3 = ESAL(AADT_3, Tf_3, Gr_3, D15, D16)
ESAL_4 = ESAL(AADT_4, Tf_4, Gr_4, D15, D16)
ESAL_5 = ESAL(AADT_5, Tf_5, Gr_5, D15, D16)
ESAL_6 = ESAL(AADT_6, Tf_6, Gr_6, D15, D16)

ESAL = ESAL_1 + ESAL_2 + ESAL_3 + ESAL_4 + ESAL_5 + ESAL_6

print('The value of ESAL is coming out to be:', ESAL)


    

result = messagebox.showinfo("Result", f"The value of ESAL is coming out to be: {ESAL} ")


workbook.close()
