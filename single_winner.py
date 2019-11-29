# Part 2
# Name: Yian Bian
# Student ID:260886212

from a3_helpers import *


def count_plurality(ballots):
    """
    (list) -> dict
    Count how many votes each candidate got.
    >>> pr_dict(count_plurality(['LIBERAL', 'LIBERAL', 'NDP', 'LIBERAL']))
    {'LIBERAL': 3, 'NDP': 1}
    >>> pr_dict(count_plurality(['CPC', 'LIBERAL', 'NDP', 'LIBERAL']))
    {'CPC': 1, 'LIBERAL': 2, 'NDP': 1}
    >>> pr_dict(count_plurality(['NDP', 'LIBERAL']))
    {'LIBERAL': 1, 'NDP': 1}
    """
    # create a new dictionary
    count_dict = {}
    for i in ballots:
        # see whether i is already a key in the new dictionary
        # if it is, then just add 1 to the value of the key
        if i in count_dict:
            count_dict[i] = (count_dict[i]+1)
        # if it isn't, then add a new key with the value 1
        else:
            count_dict[i] = 1
    return count_dict
    

def count_approval(ballots):
    """
    (list) -> dict
    Count how many votes each candidate got.
    >>> count_approval([['LIBERAL', 'NDP'], ['NDP'], ['NDP', 'GREEN', 'BLOC']])
    {'LIBERAL': 1, 'NDP': 3, 'GREEN': 1, 'BLOC': 1}
    >>> count_approval(['LIBERAL', 'NDP', 'NDP', 'NDP', 'GREEN', 'BLOC'])
    {'LIBERAL': 1, 'NDP': 3, 'GREEN': 1, 'BLOC': 1}
    >>> count_approval([['LIBERAL', 'NDP'], [], 'NDP', ['NDP', 'GREEN', 'BLOC']])
    {'LIBERAL': 1, 'NDP': 3, 'GREEN': 1, 'BLOC': 1}
    >>> count_approval(['LIBERAL', 'LIBERAL', 'NDP', 'LIBERAL'])
    {'LIBERAL': 3, 'NDP': 1}
    """
    # create a new dictionary
    count_dict = {}
    for i in ballots:
    # to see if i is a list or string
        if type(i) == list:
        # if i is a list
            if i != []:
                # and if the list isn't empty
                # then we go on to see if the element in the key
                # is already a key in the new dictionary
                for element in i:
                    # if the element is already a key in the dictionary
                    # then we add 1 to the value associated to the key
                    if element in count_dict:
                        count_dict[element] = (count_dict[element]+1)
                    # if it's not a key
                    # then we create a new key with the value 1
                    else:
                        count_dict[element] = 1
        else:
        # if it's not a list, then we use the string directly
        # just repeat the process with the element in the list again 
            if i in count_dict:
                count_dict[i] = (count_dict[i]+1)
            else:
                count_dict[i] = 1
    return count_dict

def count_rated(ballots):
    """
    (list) -> dict
    Sum up the scores for each candicate.
    >>> count_rated([{'LIBERAL':5, 'NDP':2}, {'NDP':4, 'GREEN':5}])
    {'LIBERAL': 5, 'NDP': 6, 'GREEN': 5}
    >>> count_rated([{'LIBERAL':5}, {'NDP':4, 'GREEN':5}])
    {'LIBERAL': 5, 'NDP': 4, 'GREEN': 5}
    >>> count_rated([{'LIBERAL':5}, {'NDP':4, 'GREEN':5}, {'LIBERAL':5}])
    {'LIBERAL': 10, 'NDP': 4, 'GREEN': 5}
    >>> count_rated([{}, {'NDP':4, 'GREEN':5}])
    {'NDP': 4, 'GREEN': 5}
    """
    # create a new dictionary
    score_dict = {}
    for i in ballots:
        for item in i:
        # see whether the key in i is already a key in the new dictionary
            if item in score_dict:
            # if the key is already in
            # then we just add the value 
                score_dict[item] = (score_dict[item]+i[item])
            else:
            # if it's not in
            # then we create a new key the value
                score_dict[item] = i[item]
    return score_dict
            

def count_first_choices(ballots):
    """
    (list) -> dict
    Count how many ballots for which that party was the first choice.
    >>> pr_dict(count_first_choices([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], \
    ['NDP', 'BLOC']]))
    {'BLOC': 0, 'GREEN': 1, 'LIBERAL': 0, 'NDP': 2}
    >>> pr_dict(count_first_choices([[], ['GREEN', 'NDP'], \
    ['NDP', 'BLOC']]))
    {'BLOC': 0, 'GREEN': 1, 'NDP': 1}
    >>> pr_dict(count_first_choices([[], ['GREEN', 'NDP'], [], \
    ['NDP', 'BLOC'], []]))
    {'BLOC': 0, 'GREEN': 1, 'NDP': 1}
    """
    # create a new dictionary
    count_dict = {}
    # create a list with the elements that appears in ballots
    choice_list = flatten_lists(ballots)
    # let all the element in the list be a key in the dictionary
    # and make all the value 0
    for i in choice_list:
        count_dict[i] = 0
    for element in ballots:
        # first test if the element is empty
        # because empty list won't have first choice
        if element != []:
            # if the list is not empty
            # then add 1 to the value of the key that is the first one in the list
            count_dict[element[0]] = count_dict[element[0]]+1
    return count_dict
            
    


if __name__ == '__main__':
    doctest.testmod()
    
