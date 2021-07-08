lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]     #the list we want to search
targetNum = 2   #the number we wanted to search for
start = lst[0]  #beginning of the list
end = lst[-1]   #end of the list
mid = int((start + end) //2)    #getting the middle of the list
steps = 0   #set steps to 0, going to record how many iterations to find what we want
lower = int(mid/2)  #lower quartile
upper = int(mid + lower)    #upper quartile
def binarySearch(mid, lower, upper, lst, start, end, steps):    #defining the function, variables passed as parameters 
    for i in range(len(lst)):   #runs for length of the list
        steps = steps + 1   #adds one to steps 
        if(targetNum > lst[mid]):   #if targetnum is greater than the median of the list
            start = mid     #this gets rid of anything less than the median 
            mid = int(upper)    #the upper quartile becomes the median
            lower = int((start + end -1)//2)    #the new lower quartile is calculated
            upper = ((mid + end)//2)    #new upper quartile calculates
        elif(targetNum < lst[mid]):     #if targetnum is less than the median of the list
            end = lst[mid]  #gets rid of anything more than the median
            mid = int(lower)    #the lower quartile becomes new median
            lower = int(mid//2) #new Lower quartile calculated
            upper = int(mid + lower) #new upper quartile calculated
        elif(targetNum == lst[mid]):    #if targetnumber is equal to the median 
            print(lst)
            print("Found in", steps, "Steps.", targetNum, "is at index:", lst.index(targetNum)) #output the number of steps and the index of the targetnum
            return True #returns true, the function is stopped
            break
    print(lst)
    print(targetNum, "is not in the list")
    return False #returns false, the function is stopped
          
 
    
print(binarySearch(mid, lower, upper, lst, start, end, steps)) #run and output the result of function (True or false)

