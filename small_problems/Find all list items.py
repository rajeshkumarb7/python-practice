def index_all(search_list,item):
    index_list=[]
    for index,value in enumerate(search_list):
        if value==item:
            index_list.append([index])
        elif isinstance(search_list[index],list): #isinstance(x, list) → returns True if x is a list, used to check before going inside nested lists.
            for i in index_all(search_list=search_list[index],item=item):
                index_list.append([index]+i)
    return index_list

"""
Find all positions (indexes) of an item (like 2) in a nested list, at any depth.

🔍 Step-by-step working

Loop through each element with enumerate()
→ gives both index and value

If value matches item (2) →
add [index] to result list.

If value is a list →
call index_all() recursively to check inside that sublist.

Combine outer index with inner indexes ([index] + i)
→ forms full path to each match.
"""
l=[[1,5,2],4,[5,87,2,3],[[1,2,4],[5,2,3]]]
print(index_all(l,2))

