def item_in_common(arr1, arr2):
    dict = {};
    for item in arr1:
        dict[item] = True;

    for item in arr2:
        if item in dict:
            return True
    return False;

    
arr1 = list(map(int, input().strip().split(' ')));
arr2 = list(map(int, input().strip().split(' ')));

result = item_in_common(arr1, arr2);

print(result);