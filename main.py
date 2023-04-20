
list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def brute_force_merge_lists(list_1, list_2) -> list:
    """
    Complete this function, by merging the information from list_1 and list_2
    to create a new list, which has all the information about each student from
    both lists in one single dict.
    - Both lists are unsorted
    - Both lists can have missing values (for ex list_2 has missing id=2)
    """

    list_3 = []
    for i in list_1:
        for j in list_2:
            if i["id"] == j["id"]:
                i.update(j)
                list_3.append(i)
                break
        else:
            list_3.append(i)

    for i in list_2:
        for j in list_3:
            if i["id"] == j["id"]:
                break
        else:
            list_3.append(i)

    return list_3

def merge_lists(list_1, list_2) -> list:
    """
    Complete this function, by merging the information from list_1 and list_2
    to create a new list, which has all the information about each student from
    both lists in one single dict.
    - Both lists are unsorted
    - Both lists can have missing values (for ex list_2 has missing id=2)
    """

    # IDEA: sort the lists by id
    # IDEA: use a while loop to iterate through both lists
    # IDEA: if the id's match, merge the dicts
    # IDEA: if the id's don't match, add the smaller id to the list
    # IDEA: if one list is empty, add the other list to the end of the new list
    # IDEA: return the new list
    list_3 = []
    list_1.sort(key=lambda x: x["id"])
    list_2.sort(key=lambda x: x["id"])
    while list_1 and list_2:
        if list_1[0]["id"] == list_2[0]["id"]:
            list_1[0].update(list_2[0])
            list_3.append(list_1.pop(0))
            list_2.pop(0)
        elif list_1[0]["id"] < list_2[0]["id"]:
            list_3.append(list_1.pop(0))
        else:
            list_3.append(list_2.pop(0))
    list_3.extend(list_1)
    list_3.extend(list_2)
    return list_3


list_3 = brute_force_merge_lists(list_1, list_2)
print(list_3)
list_3 = merge_lists(list_1, list_2)
print(list_3)
