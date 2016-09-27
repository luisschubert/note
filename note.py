import os, datetime, time

def showNotes():
    f = open("/Users/luisschubert/Documents/note/log.txt", "r")
#    i = 0
    for line in f.readlines():
        content = line.split('\t')
        datetimeString = content[1]
        datetimeString = datetimeString.replace("\n","")
        if dateMatches(datetimeString):
            print content[0]
 #           i += 1



def dateMatches(datetimeString):
    datetimeObject = datetime.datetime.strptime(datetimeString, '%Y-%m-%d %H:%M:%S')
    if datetimeObject.date() == datetime.datetime.today().date():
        return True
    else:
        return False

def saveNote(content):
    f = open("/Users/luisschubert/Documents/note/log.txt", "a")
    saveTime = datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S')
    logLine = content + "\t" + saveTime + '\n'
    f.write(logLine)

running = True

while running:
    os.system("clear")
    print ' - notes - '
    showNotes()
    command = raw_input("...")
    if command == "quit":
        running = False
    elif command != "":
	    saveNote(command)
