# Part 1
# Name: Yian Bian
# Student ID:260886212

import doctest
import random

def flatten_lists(nested):
    """
    (list) -> list
    Replaces any lists inside this list with their values.
    >>> flatten_lists([[0], [1, 2], 3])
    [0, 1, 2, 3]
    >>> flatten_lists([[1, 2],[3, 4]])
    [1, 2, 3, 4]
    >>> flatten_lists([2, [4, 6, 8], 9])
    [2, 4, 6, 8, 9]
    """
    # create an empty list
    new_list = []
    for i in nested:
        # to see if the element in the list is a list or string.
        if type(i) == list:
            # if it's a list replace it with its value
            for num in range(len(i)):
                 new_list += [i[num]]
        # if it's a string then just remain it.
        else:
            new_list += [i]
    return new_list


def flatten_dict(d):
    """
    (dict) -> list
    Return a list that contains the keys of the dictionary repeated v times
    where v is the value associated with the key in the dictionary
    >>> flatten_dict({'LIBERAL': 5,'NDP': 2})
    ['LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'NDP', 'NDP']
    >>> flatten_dict({'NDP': 1,'CPC': 2})
    ['NDP', 'CPC', 'CPC']
    >>> flatten_dict({'LIBERAL': 0,'NDP': 2})
    ['NDP', 'NDP']
    """
    # create a new list
    new_list = []
    for key in d:
        # use key to multiply by it's value to let it repeat.
        new_list += [key]*d[key]
    return new_list


def add_dicts(d1, d2):
    """
    (dict) -> dict
    Merge the two dictionaries. If a key is in both dictionares,
    add their values
    >>> add_dicts({'a':5, 'b':2, 'd':-1},{'a':7, 'b':1, 'c':5})
    {'a': 12, 'b': 3, 'd': -1, 'c': 5}
    >>> add_dicts({},{'a':7, 'b':1, 'c':5})
    {'a': 7, 'b': 1, 'c': 5}
    >>> add_dicts({'a':5, 'b':2, 'd':-1},{})
    {'a': 5, 'b': 2, 'd': -1}
    """
    # remain the first dictionary
    new_dict = d1
    for key in d2:
        # to see whether d2's keys is also in d1
        if key in new_dict:
            # if is in d1, then add d2's value to d1
            new_dict[key] += d2[key]
        else:
            # if not then create a new key
            new_dict[key] = d2[key]
    return new_dict


def get_all_candidates(ballots):
    """
    (list) -> list
    Return all the unique strings in the list and its nested contents.
    >>> get_all_candidates([{'GREEN':3, 'NDP':5},{'NDP':2,'LIBERAL':4},['CPC', 'NDP'],'BLOC'])
    ['GREEN', 'NDP', 'LIBERAL', 'CPC', 'BLOC']
    >>> get_all_candidates([{},{'NDP':2,'LIBERAL':4},['CPC', 'NDP'],'BLOC'])
    ['NDP', 'LIBERAL', 'CPC', 'BLOC']
    >>> get_all_candidates([[],{'NDP':2,'LIBERAL':4},['CPC', 'NDP'],'BLOC'])
    ['NDP', 'LIBERAL', 'CPC', 'BLOC']
    """
    # create a new list
    new_list = []
    for i in ballots:
    # first to see the type of i
        if type(i) == dict:
            # if it's a dictionary,just add the key to the created list
            for key in i:
                if new_list.count(key) == 0:
                    new_list += [key]
        elif type(i) == list:
            # if it's a list,
            # then see whether there is a same element in the created list
            # if there is, then we don't do anything to that element
            # if not, we add that element to the new created list
            for a in i:
                if new_list.count(a) == 0:
                    new_list += [a]
        else:
            # if is a string ,then just add it to the created list directly
            if new_list.count(i) == 0:
                    new_list += [i]
    return new_list       
    


###################################################### winner/loser

def get_candidate_by_place(result, func):
    """
    (dict,func) -> str
    Evaluate the function on the dictionary’s values.Return the key
    of the dictionary corresponding to that value. Break ties randomly
    >>> result = {'LIBERAL':4, 'NDP':6, 'CPC':6 ,'GREEN':4}
    >>> random.seed(0)
    >>> get_candidate_by_place(result, min)
    'GREEN'
    >>> random.seed(1)
    >>> get_candidate_by_place(result, min)
    'LIBERAL'
    >>> result = {'LIBERAL':4, 'NDP':7, 'CPC':6 ,'GREEN':4}
    >>> get_candidate_by_place(result, max)
    'NDP'
    """
    selection = []
    list_of_value = []
    # put all the values in the dictionary in a list
    for key in result:
        list_of_value.append(result[key])
    # if the values in the dictionary is empty, then just return empty
    if list_of_value == []:
        return []
    # a is the max/min value that the funcion asks for
    a = func(list_of_value)
    for key in result:
        # put the key that has the value a in a list
        if result[key] == a:
            selection.append(key)
    # there are more than one key having the value a
    # then just pick one among them randomly
    return selection[random.randint(0,len(selection)-1)]

     


def get_winner(result):
    """
    (dict) -> str
    Return the key with the greatest value.
    If there are ties, break them randomly.
    >>> get_winner({'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0})
    'NDP'
    >>> random.seed(1)
    >>> get_winner({'NDP': 2, 'GREEN': 2, 'LIBERAL': 1, 'BLOC': 0})
    'NDP'
    >>> random.seed(0)
    >>> get_winner({'NDP': 2, 'GREEN': 2, 'LIBERAL': 1, 'BLOC': 0})
    'GREEN'
    """
    # let the require function in get_candidate_by_place be max
    # then we can get the key with the maximum value
    return get_candidate_by_place(result, max) 
            
    


def last_place(result, seed = None):
    """
    (dict) -> str
    Return the key with the lowest value.
    If there are ties, break them randomly.
    >>> random.seed(1)
    >>> last_place({'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0})
    'LIBERAL'
    >>> last_place({'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 6})
    'LIBERAL'
    >>> last_place({'NDP': 2, 'GREEN': 1, 'LIBERAL': 1, 'BLOC': 0})
    'BLOC'
    """
    # let the require function in get_candidate_by_place be min
    # then we can get the key with the minimum value
    return get_candidate_by_place(result, min)


###################################################### testing help

def pr_dict(d):
    '''(dict) -> None
    Print d in a consistent fashion (sorted by key).
    Provided to students. Do not edit.
    >>> pr_dict({'a':1, 'b':2, 'c':3})
    {'a': 1, 'b': 2, 'c': 3}
    '''
    l = []
    for k in sorted(d):
        l.append( "'" + k + "'" + ": " + str(d[k]) )
    print('{' + ", ".join(l) + '}')


if __name__ == '__main__':
    doctest.testmod()
