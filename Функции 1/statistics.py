def getmedian(data):
    data.sort()
    if len(data) > 1:
        if len(data) % 2 != 0:
            median = float(data[len(data) // 2])
        else:
            median = float((data[len(data) // 2 -1] + data[len(data) // 2])/2)
        return median
    elif len(data) == 1:
        return data[0]
    else:
        return 0
def getaverage(data):
    if len(data) > 1:
        return sum(data)/len(data)
    elif bool(data):
        return data[0]
def printStatistics(arr):
    if not bool(arr):
        print('count: '+str(len(arr)), 'average: '+str(0), 'min: '+str(0), 'max: '+str(0), 'median: '+str(0), sep='\n')
    else:
        arr = [float(i) for i in arr]
        print('count: '+str(len(arr)), 'average: '+str(getaverage(arr)), 'min: '+str(min(arr)), 'max: '+str(max(arr)), 'median: '+str(getmedian(arr)), sep='\n')
