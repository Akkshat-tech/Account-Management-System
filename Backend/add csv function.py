def add_csv():
    global cb
    wb=openpyxl.load_workbook('database_project.xlsx')
    ws1=wb["purchase invoice"]                                          
    maxi=ws1.max_column
    col=[]
    for j in range(1,maxi+1):
        cell=ws1.cell(row=1,column=j)
        col.append(cell.value)
#print(col)
    print()
    ws2=wb["sales invoice"]
    max_col=ws1.max_column
    cols=[]
    for i in range(1, max_col + 1):
        cell_obj = ws2.cell(row = 1, column = i)
        cols.append(cell_obj.value)
#print(cols)
    from pandas import DataFrame
    csvfile=input("enter path for csv file here: ")
    df=pd.read_csv(csvfile)
#print(df)
    l_val = df.columns.tolist()
    print()
#print(l_val)
    newdf=df.loc[:,col]
    c=newdf.columns.tolist()
#print(c)
    print()
    lis=newdf.values.tolist()
    print("kindly confirm the entries of the file")
    print()
    for i in range(1,1+len(lis)):
        print(i,") ",lis[i-1])
            
        print()
    print("press 1 to enter \n2 to drop any faulty entry")
#print(l)
    csf=input("enter 1 or 2 here: ")
    if (csf=='1'):
        while True:
            print('press 1 to add to sales invoice\npress 2 to add to purchase invoice')
            i=(input('enter 1 or 2 here:'))
            if i=='1':
                for list_of_values in lis:
                    ws2.append(list_of_values)
                    cb["A1"]=cb["A1"].value+list_of_values[-1]
                    wbcb.save("current_balance.xlsx")
                break
                 
            elif i=='2':
                for list_of_values in lis:
                    ws1.append(list_of_values)
                    cb["A1"]=cb["A1"].value-list_of_values[-1]
                    wbcb.save("current_balance.xlsx")
                break
                
            else:
                print('kindly enter 1 or 2 only')
                
    elif csf=='2':
        while True:
                totalnumber=int(input("enter the total number of entries that are faulty or press 0 to exit feature: "))
                if totalnumber==0:
                    break
                if (totalnumber<=len(lis)and totalnumber>0):
                    ael=[]
                    for h in range (totalnumber):
                        k=int(input("enter the sr. number of the entry that contains fault"))
                        ael.append(lis[k-1])
                    for eles in lis:
                        if eles in ael:
                            lis.remove(eles)
                    print("kindly confirm the entries of the file")
                    for i in range(1,1+len(lis)):
                        print(i,") ",lis[i-1])
                        print()
                    print('press 1 to add to sales invoice\npress 2 to add to purchase invoice\nto exit function press 3')
                    i=(input('enter 1 or 2 here:'))
                    if i=='1':
                        for list_of_values in lis:
                            ws2.append[list_of_values]
                            cb["A1"]=cb["A1"].value+list_of_values[-1]
                            wbcb.save("current_balance.xlsx")
                        break
                    elif i=='2':
                        for list_of_values in lis:
                            ws1.append[list_of_values]
                            cb["A1"]=cb["A1"].value-list_of_values[-1]
                            wbcb.save("current_balance.xlsx")
                        break
                    elif i=='3':
                        print("function exited")
                        break
                    else:
                        print('kindly enter 1 or 2 only')
                        
                else:
                    print("the number you entered exceeds the total number of entries in the file you uploaded")
    
    else:
        print("enter 1 or 2 only")
            
    wb.save('database_project.xlsx')
    wbcb.save("current_balance.xlsx")

add_csv()
