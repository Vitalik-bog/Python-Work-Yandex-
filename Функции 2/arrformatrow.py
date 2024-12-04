def printArrayFormatted(arr, numCols):
   while len(arr) % numCols != 0:
      arr.append('-')
   for i in range(len(arr)):
      if i % numCols == 0 and i !=0:
         print()
      print(arr[i], end='\t')
   if len(arr) > 0:
      print()
#printArrayFormatted([], 1)

