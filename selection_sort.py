arr = [8,6,7,5,3,0,9,666,13]

def selection_sort(arr):
    #so lets get the length first
    len_arr = len(arr)
    #let's start the roller coaster loops!
    for i in range(len_arr):
        #need to set what min is for each pass we are gonna do
        min_index = i
        #compare it with what's left
        for j in range(i+1, len_arr):
            #if we find sometihng smaller, we gotta update
            if arr[j] < arr[min_index]:
                min_index = j
        #if it changed, we gotta do a swappy swap
        if min_index != i:
            #we gonna do this:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp
            #now lets return and print

    return(arr)

print (selection_sort(arr)) 

#now ask me to do that without looking LOL