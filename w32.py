def validate():
    divcount = 0;
    notDivcount =0;
    for x in range(1500,2500):
        if (x%5==0) and (x%7==0):
            divcount = divcount + 1
            print(x) 
        else:
          notDivcount = notDivcount + 1
    print("divcount,", divcount );
    print("notDivcount,", notDivcount );                   

validate()                    