average = 0
with open("log.txt") as log:
    logText = log.readlines()
    for i in logText:
        x=i.strip("seconds\n")
        i=float(x)
        average+=i
average/=(len(logText))
print(average)