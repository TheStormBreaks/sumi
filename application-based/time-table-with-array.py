timeTable = {"mon":[],"tue":[],"wed":[],"th":[],"fri":[]}

def initTimeTable():
    
    for t in [9,10,11,12,13,14,15,16]:
        for d in timeTable.keys():
            timeTable[d].append(None)
            
def insertIntoTimeTable(day,time,course):
    if timeTable[day][time-9] == None:
        timeTable[day][time-9]=course
        return course
    else:
        return None
    
def insert(days,timeSlots,course):
    for i in range(0, 3, 1):
        if timeTable[days[i *3: (i*3) +3]][timeSlots[0]-9]==None:
            timeTable[days[i *3: (i*3) +3]][timeSlots[0]-9] = course
    else:
        return None

def delete(day, time):
    timeTable[day][time-9] = None
   
 
def replace(day, time, course):
    timeTable[day][time-9] = course

initTimeTable()
print(timeTable)

insertIntoTimeTable("mon",13,("CSC203A","DSA"))
print(timeTable)

insert("montuewed",[9,9,9],("CSC203A","DSA"))
print(timeTable)

delete("mon", 9)
print(timeTable)

replace("mon", 13, ("CSC204","LD"))
print(timeTable)
