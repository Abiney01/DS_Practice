def isPossible(arr):
    n = len(arr)
    count = 0  # Count of modifications
    
    for i in range(n - 1):
        print(i,"index value")
        
        if arr[i] > arr[i + 1]:  # Found a violation
            count += 1
            if count > 1:
                return False  # More than one modification needed
            
            # Check if we can modify arr[i] or arr[i+1]
            if i == 0 or arr[i - 1] <= arr[i + 1]:
                arr[i] = arr[i + 1]
                print(arr[i])  # Modify arr[i] to match arr[i+1]
            else:
                arr[i + 1] = arr[i] 
                print(arr[i]) # Modify arr[i+1] to match arr[i]
    
    return True
print(isPossible([-2,7,-1,0,1,2]))