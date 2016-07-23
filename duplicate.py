__author__ = 'Rick'
# removes duplicate items from a list
def remove_duplicate(user_list):
    clean = []
    for i in user_list:
        if i not in clean:
            clean.append(i)
    print(clean)
    return clean