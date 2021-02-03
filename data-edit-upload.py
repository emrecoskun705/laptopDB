import mysql.connector

mydb = mysql.connector.connect(
    user='root',
    password='password',#enter password
    host='127.0.0.1',
    database='laptop'
)

mycursor = mydb.cursor()
def laptop_table():
    filename = "laptop3.csv"
    laptopDict = {}
    with open(filename,encoding="UTF-8") as file:
        lines = file.readlines()
        i = 0
        for line in lines:
            line = line.split(";")
            if i == 0:
                laptopDict[int(line[0][-1:])] = line[1:]
            else:
                laptopDict[int(line[0])] = line[1:]
            i+=1

    appereanceDict = {}
    with open("appereance3.txt",encoding="UTF-8") as file:
        lines = file.readlines()
        i = 0
        for line in lines:
            line = line.split(";")
            #print(line)
            if i == 0:
                
                appereanceDict[int(line[0][-1:])] = line[1:]
            else:
                appereanceDict[int(line[0])] = line[1:]            
            i+=1

    with open("new.txt", "w", encoding="UTF-8") as file:
        for i in range(1,326):
            laptopInfo = laptopDict[i]
            #print(int(laptopInfo[12]))
            #print(laptopInfo)
            appereance = appereanceDict[int(laptopInfo[11])]
            file.write(str(i)+";")
            file.write(";".join(laptopInfo[:-1]))
            file.write(";")
            file.write(";".join(appereance))

def convertDouble():
    with open("laptop4.csv",encoding="UTF-8") as file:
        lines = file.readlines()
        i = 0
        for line in lines:
            line = line.split(";")
            ls = [5 ,12, 13, 14 ,15, 17]
            for j in ls:
                doubleValue = line[j]
                if "," in doubleValue:
                    doubleValue = doubleValue.replace(",",".")
                    print(doubleValue)
                    line[j] = doubleValue
            lines[i] = ";".join(line)
            i += 1

        with open("laptop4_1.txt","w" ,encoding="UTF-8") as file2:
            for i in lines:
                
                file2.write(i)

#convertDouble()
#convertDouble()

def deleteHardwareIDColumn():
    with open("laptop4_1forHardware.txt",encoding="UTF-8") as file:
        lines = file.readlines()
        i = 0
        for line in lines:
            line = line.split(";")
            
            line = line[:11] + line[12:]
            lines[i] = ";".join(line)
            i+=1
        with open("laptop4_withoutHardwareID.txt", "w", encoding="UTF-8") as file2:
            for line in lines:
                file2.write(line)

#deleteHardwareIDColumn()

def nullChange():
    with open("laptop4_1forHardware.txt",encoding="UTF-8") as file:
        lines = file.readlines()
        i = 0
        for line in lines:
            line = line.split(";")
            
            

            i+=1



def showWirelessTypes():
     with open("hardware3.csv",encoding="UTF-8") as file:
        lines = file.readlines()

        a = []
        for line in lines:
            line = line.split(";")
           
            if line[6] not in a:
                a.append(line[6])

        print(a)



#showWirelessTypes()


def laptopID():
    
    with open("laptops_general_data.txt",encoding="UTF-8") as file:
        lines = file.readlines()
            
        with open("laptop_laptopID.txt","w",encoding="UTF-8") as file2:
            a = []
            for line in lines:
                line = line.split(";")
                b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 36, 37, 38, 39, 40]
                c = []
                #print(line)
                for k in b:
                    c.append(line[k])
                if c not in a:
                    a.append(c)
                id = a.index(c) + 1
                file2.write(str(id))
                file2.write(";")
                file2.write(";".join(line))
#laptopID()

def hardwareID():
    with open("laptop_laptopID.txt",encoding="UTF-8") as file:
        lines = file.readlines()
            
        with open("laptop_laptopID_hardwareID.txt","w",encoding="UTF-8") as file2:
            a = []
            for line in lines:
                line = line.split(";")
                b = [11, 23, 34, 35]
                c = []
                #print(line)
                for k in b:
                    c.append(line[k])
                if c not in a:
                    a.append(c)
                id = a.index(c) + 1
                file2.write(str(id))
                file2.write(";")
                file2.write(";".join(line))

#hardwareID()

def processorID():
    with open("laptop_laptopID_hardwareID.txt",encoding="UTF-8") as file:
        lines = file.readlines()
            
        with open("laptop_laptopID_hardwareID_processorID.txt","w",encoding="UTF-8") as file2:
            a = []
            for line in lines:
                line = line.split(";")
                b = [14, 15, 16, 17]
                c = []
                #print(line)
                for k in b:
                    c.append(line[k])
                if c not in a:
                    a.append(c)
                id = a.index(c) + 1
                file2.write(str(id))
                file2.write(";")
                file2.write(";".join(line))

#processorID()

def graphicsID():
    with open("laptop_laptopID_hardwareID_processorID.txt",encoding="UTF-8") as file:
        lines = file.readlines()
            
        with open("laptop_laptopID_hardwareID_processorID_graphicsID.txt","w",encoding="UTF-8") as file2:
            a = []
            for line in lines:
                line = line.split(";")
                b = [26, 27, 28]
                c = []
                #print(line)
                for k in b:
                    c.append(line[k])
                if c not in a:
                    a.append(c)
                id = a.index(c) + 1
                file2.write(str(id))
                file2.write(";")
                file2.write(";".join(line))

#graphicsID()

def storageID():
    with open("laptop_laptopID_hardwareID_processorID_graphicsID.txt",encoding="UTF-8") as file:
        lines = file.readlines()
            
        with open("laptop_laptopID_hardwareID_processorID_graphicsID_storageID.txt","w",encoding="UTF-8") as file2:
            a = []
            for line in lines:
                line = line.split(";")
                b = [20, 21, 22,23,24,25]
                c = []
                #print(line)
                for k in b:
                    c.append(line[k])
                if c not in a:
                    a.append(c)
                id = a.index(c) + 1
                file2.write(str(id))
                file2.write(";")
                file2.write(";".join(line))

#storageID()

###### LOAD TO THE DATABASE ######
ALL_ID_FILENAME = "laptop_laptopID_hardwareID_processorID_graphicsID_storageID.txt"
def loadLaptop():
    with open(ALL_ID_FILENAME,encoding="UTF-8") as file:
        lines = file.readlines()
        
        checkID = []
        for line in lines:
            line = line.split(";")
            print(line)
            if line[4] == "":
                one = None
            else:
                one = int(line[4])
                if one not in checkID:
                    checkID.append(one)
                else:
                    continue

            if line[5] == "":
                two = None
            else:
                two = line[5]

            if line[16] == "":
                three = None
            else:
                three = line[16]

            if line[8] == "":
                four = None
            else:
                #print(line[8].replace(",", ""))
                four = float(line[8].replace(",", ""))

            if line[9] == "":
                five = None
            else:
                five = float(line[9].replace(",", ""))

            if line[6] == "":
                six = None
            else:
                six = float(line[6].replace(",", "."))

            if line[7] == "":
                seven = None
            else:
                seven = int(line[7])

            if line[10] == "":
                eight = None
            else:
                eight = line[10]

            if line[11] == "":
                nine = None
            else:
                nine = line[11]

            if line[41] == "":
                ten = None
            else:
                ten = int(line[41])

            if line[42] == "":
                eleven = None
            else:
                eleven = int(line[42])

            if line[43] == "":
                tweleve = None
            else:
                tweleve = float(line[43].replace(",", "."))

            if line[44] == "":
                thirteen = None
            else:
                thirteen = float(line[44].replace(",", "."))

            if line[45] == "" or line[45] == "\n":
                fourteen = None
            else:
                print(line[45].replace(",", "."))
                fourteen = float(line[45].replace(",", "."))

            if line[14] == "":
                fifteen = None
            else:
                fifteen = float(line[14].replace(",", "."))

            if line[12] == "":
                sixteen = None
            else:
                sixteen = line[12]

            if line[13] == "" or line[13] == "\n":
                seventeen = None
            else:
                seventeen = float(line[13].replace(",", "."))


            
            sql = """INSERT INTO laptop VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            val = [one, two, three, four, five,six ,seven ,eight ,nine ,ten , eleven,tweleve ,thirteen ,fourteen , fifteen,sixteen ,seventeen]
            
            mycursor.execute(sql, val)
        mydb.commit()
#loadLaptop()
def loadHardware():
    with open(ALL_ID_FILENAME,encoding="UTF-8") as file:
        lines = file.readlines()
        
        checkID = []
        for line in lines:
            line = line.split(";")
            
            if int(line[3]) not in checkID:
                one = (int(line[3]))
                checkID.append(int(line[3]))
            else:
                continue
            two = (line[15])
            three = (line[39])
            if line[38] == "":
                four = None
            else:
                four = int(line[38])
            five = (line[27])
            
            sql = """INSERT INTO Hardware VALUES(%s, %s, %s, %s, %s)"""
            val = [one, two, three, four, five]
            mycursor.execute(sql, val)
        mydb.commit()
#loadHardware()
def laptopHasHardware():
    with open(ALL_ID_FILENAME,encoding="UTF-8") as file:
        lines = file.readlines()
        
        checkID = []
        for line in lines:
            line = line.split(";")
            values = (line[4], line[3])
            if values not in checkID:
                checkID.append(values)
            else: 
                continue

            sql = """INSERT INTO Laptop_has_Hardware VALUES(%s, %s)"""
            val = values
            mycursor.execute(sql, val)
        mydb.commit()
#laptopHasHardware()

def loadGraphics():
    with open(ALL_ID_FILENAME,encoding="UTF-8") as file:
        lines = file.readlines()
        
        checkID = []
        for line in lines:
            line = line.split(";")
            
            if int(line[1]) not in checkID:
                one = (int(line[1]))
                checkID.append(int(line[1]))
            else:
                continue
            two = (line[28])
            three = (line[39])
            if line[38] == "":
                four = None
            else:
                four = int(line[38])
            
            
            sql = """INSERT INTO Graphics VALUES(%s, %s, %s, %s)"""
            val = [one, two, three, four]
            mycursor.execute(sql, val)
        mydb.commit()
#loadGraphics()
def hardwareHasGraphics():
    with open(ALL_ID_FILENAME,encoding="UTF-8") as file:
        lines = file.readlines()
        
        checkID = []
        for line in lines:
            line = line.split(";")
            values = (line[3], line[1])
            if values not in checkID:
                checkID.append(values)
            else: 
                continue

            sql = """INSERT INTO Hardware_has_Graphics VALUES(%s, %s)"""
            val = values
            mycursor.execute(sql, val)
        mydb.commit()
#hardwareHasGraphics()

def loadStorage():
    with open(ALL_ID_FILENAME,encoding="UTF-8") as file:
        lines = file.readlines()
        
        checkID = []
        for line in lines:
            line = line.split(";")
            
            if int(line[0]) not in checkID:
                one = (int(line[0]))
                checkID.append(int(line[0]))
            else:
                continue
            two = (line[23])
            if line[21] == "":
                three = None
            else:
                three = int(line[21])
            four = line[22]
            if line[24] == "":
                five = None
            else:
                five = int(line[24])
            six = line[25]
            seven = line[26]
            
            sql = """INSERT INTO Storage VALUES(%s, %s, %s, %s, %s, %s, %s)"""
            val = [one, two, three, four, five, six, seven]
            mycursor.execute(sql, val)
        mydb.commit()
#loadStorage()
def hardwareHasStorage():
    with open(ALL_ID_FILENAME,encoding="UTF-8") as file:
        lines = file.readlines()
        
        checkID = []
        for line in lines:
            line = line.split(";")
            values = (line[3], line[0])
            if values not in checkID:
                checkID.append(values)
            else: 
                continue

            sql = """INSERT INTO Hardware_has_Storage VALUES(%s, %s)"""
            val = values
            mycursor.execute(sql, val)
        mydb.commit()
#hardwareHasStorage()
def loadProcessor():
    with open(ALL_ID_FILENAME,encoding="UTF-8") as file:
        lines = file.readlines()
        
        checkID = []
        for line in lines:
            line = line.split(";")
            
            if int(line[2]) not in checkID:
                one = (int(line[2]))
                checkID.append(int(line[2]))
            else:
                continue
            two = (line[17])
            three = line[18]
            if line[19] == "":
                four = None
            else:
                
                four = float(line[19].replace(",", "."))  
            
            if line[20] == "":
                five = None
            else:
                five = int(line[20])
            
            
            sql = """INSERT INTO Processor VALUES(%s, %s, %s, %s, %s)"""
            val = [one, two, three, four, five]
            mycursor.execute(sql, val)
        mydb.commit()
#loadProcessor()

def hardwareHasProcessor():
    with open(ALL_ID_FILENAME,encoding="UTF-8") as file:
        lines = file.readlines()
        
        checkID = []
        for line in lines:
            line = line.split(";")
            values = (line[3], line[2])
            if values not in checkID:
                checkID.append(values)
            else: 
                continue

            sql = """INSERT INTO Hardware_has_Processor VALUES(%s, %s)"""
            val = values
            mycursor.execute(sql, val)
        mydb.commit()
#hardwareHasProcessor()

def hardwareHasPortType():
    with open(ALL_ID_FILENAME,encoding="UTF-8") as file:
        lines = file.readlines()
        
        checkID = []
        for line in lines:
            line = line.split(";")
            control = [33, 34,35, 36, 37]
            i = 1
            for j in control:
                port = line[j]
                if port == "":
                    port = 0
                            
                values = (i, int(line[3]), port)
                if values not in checkID:
                    checkID.append(values) 
                    sql = """INSERT INTO Hardware_has_PortType VALUES(%s, %s, %s)"""
                    val = values
                    mycursor.execute(sql, val)
                i += 1
        mydb.commit()
#hardwareHasPortType()
def hardwareHasConnectivityType():
    with open(ALL_ID_FILENAME,encoding="UTF-8") as file:
        lines = file.readlines()
        sql = """INSERT INTO Hardware_has_connectivityType VALUES(%s, %s)"""
        checkID = {}
        for line in lines:
            line = line.split(";")
            typeCon = line[31]
            if typeCon == "":
                continue
            hID = line[3]
            checkID.setdefault(hID, [])
                  
            if "Wi-Fi" in typeCon and "Wi-Fi" not in checkID[hID]:
                val = (hID, 1)
                mycursor.execute(sql, val)
                checkID[hID].append("Wi-Fi") 
            
            if "Bluetooth" in typeCon and "Bluetooth" not in checkID[hID]:
                val = (hID, 2)
                mycursor.execute(sql, val)
                checkID[hID].append("Bluetooth") 
        mydb.commit()
#hardwareHasConnectivityType()

def hardwareHasWirelessType():
    with open(ALL_ID_FILENAME,encoding="UTF-8") as file:
        lines = file.readlines()
        sql = """INSERT INTO Hardware_has_wirelessType VALUES(%s, %s)"""
        checkID = {}
        for line in lines:
            line = line.split(";")
            typeCon = line[32]
            if typeCon == "":
                continue
            hID = line[3]
            checkID.setdefault(hID, [])

            wifiID = ["a","b","g","n","ac","ax"]
            string = line[32][6:]
            stringLs = string.split("/")
           # print(stringLs)
            for i in stringLs:
                if i not in checkID[hID]:
                    checkID[hID].append(i)
                    wID = wifiID.index(i)
                    val = (hID, wID+1)
                    mycursor.execute(sql, val)

        mydb.commit()
hardwareHasWirelessType()
mycursor.close()
        
    
        
