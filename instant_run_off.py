# Part 3
# Name Yian Bian
# ID: 260886212

from single_winner import *

################################################################################

def votes_needed_to_win(ballots, num_winners):
    '''
    (list) -> int
    Return an integer of votes a candiate would need to win
    >>> votes_needed_to_win([{'CPC':3, 'NDP':5}, {'NDP':2, 'CPC':4}, \
    {'CPC':3, 'NDP':5}], 1)
    2
    >>> votes_needed_to_win(['g']*20, 2)
    7
    >>> votes_needed_to_win([{'CPC':3}, ['CPC', 'NDP'], [], 'NDP'], 3)
    2
    '''
    # calculate the needed votes using the formula
    # for we need to rounddown the number so I use "//"
    vote_needed = len(ballots)//(num_winners+1)+1
    return vote_needed

def has_votes_needed(result, votes_needed):
    """
    (dict) -> bool
    a boolean representing whether the candidate with the most votes
    in this election has at least votes needed votes.
    >>> has_votes_needed({'BDP': 4, 'LIBERAL': 3},4)
    True
    >>> has_votes_needed({'LIBERAL':4, 'NDP':6, 'CPC':6 ,'GREEN':4},5)
    True
    >>> has_votes_needed({'LIBERAL':4, 'NDP':6, 'CPC':6 ,'GREEN':4},7)
    False
    >>> has_votes_needed({},9)
    False
    """
    # first check if it's an empty dictionary
    # if it is, then return False
    if result == {}:
        return False
    # if is not, then get the highest vote 
    highest_vote = result[get_winner(result)]
    # return whether the highest vote is greater than or equal
    # to the needed votes
    return highest_vote >= votes_needed
################################################################################


def eliminate_candidate(ballots, to_eliminate):
    '''
    (list) -> list
    Return: a new list of ranked ballots where all the candidates in to
    eliminate have been removed.
    If all candidates on a ballot have been eliminated,
    it should become an empty list.
    >>> eliminate_candidate([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], \
    ['NDP', 'BLOC']], ['NDP', 'LIBERAL'])
    [[], ['GREEN'], ['BLOC']]
    >>> eliminate_candidate([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], \
    ['NDP', 'BLOC'], []], ['NDP', 'LIBERAL'])
    [[], ['GREEN'], ['BLOC'], []]
    >>> eliminate_candidate([['GREEN', 'NDP'], ['NDP', 'BLOC']], \
    ['NDP', 'LIBERAL'])
    [['GREEN'], ['BLOC']]
    '''
    # create a new list
    new_list = []
    # and make a copy of the ballots with the new list
    for i in ballots:
        new_list.append(i[:])
    for item in new_list:
        for element in item[:]:
         # if the element of to_eliminate is in the new list
         # then remove the element from the list
            if element in to_eliminate:
                item.remove(element)

    return new_list
    


################################################################################


def count_irv(ballots):
    """
    (list) -> dict
    Return how many votes each candidate ends with after counting with IRV
    >>> pr_dict(count_irv([['NDP'], ['GREEN', 'NDP', 'BLOC'], ['LIBERAL', 'NDP'],\
    ['LIBERAL'], ['NDP', 'GREEN'], ['BLOC', 'GREEN', 'NDP'], ['BLOC',\
    'CPC'], ['LIBERAL', 'GREEN'], ['NDP']]))
    {'BLOC': 0, 'CPC': 0, 'GREEN': 0, 'LIBERAL': 3, 'NDP': 5}
    >>> pr_dict(count_irv([[], ['GREEN', 'NDP', 'BLOC'], ['LIBERAL', 'NDP'],\
    ['LIBERAL'], ['NDP', 'GREEN'], ['BLOC', 'GREEN', 'NDP'], ['BLOC',\
    'CPC'], ['LIBERAL', 'GREEN'], ['NDP']]))
    {'BLOC': 0, 'CPC': 0, 'GREEN': 0, 'LIBERAL': 0, 'NDP': 5}
    >>> pr_dict(count_irv([['NDP','LIBERAL'], ['LIBERAL'], ['NDP', 'GREEN'], ['BLOC', 'GREEN', 'NDP'], ['LIBERAL', 'GREEN'], ['NDP']]))
    {'BLOC': 0, 'GREEN': 0, 'LIBERAL': 2, 'NDP': 4}
    """
    # copy ballots with a new list but without empty list
    new_list = []
    for i in ballots:
        if i != []:
            new_list.append(i[:])
    # get all the candidates and count first choices
    all_candidate = get_all_candidates(new_list)
    first_choice = count_first_choices(new_list)
    total_votes = len(ballots)
    # get the candidate with the most choices at the first time
    winner = get_winner(first_choice)




    # if the candidate doesn't have a majority
    # then just repeat the process again till one has a majority
    while (first_choice[winner]/total_votes <= 1/2):
        # find the candidate that has the least votes
        last_one = last_place(first_choice)
        for element in new_list:
            # first if there's an empty, remove it
            if element == []:
                new_list.remove(element)
            # if there's no empty list
            # remove the candidate that has the least votes from the list
            elif last_one in element:
                new_list = eliminate_candidate(new_list,[last_one])
        # the count the first_choice again
        first_choice = count_first_choices(new_list)
        # if there's candidate with no vote
        # delete the candidate from the first_choice
        for candidate in all_candidate:
            if candidate in first_choice and first_choice[candidate] == 0: 
                del first_choice[candidate]
        # get the winner with the most choices
        winner = get_winner(first_choice)



    # we have already had a candidate that has a majority
    # then we add other candidates that have been removed from
    # the dictionary during the process with the value 0
    for item in all_candidate:
        if not item in first_choice:
            first_choice[item] = 0
    return first_choice
    
                            
    
    
    

################################################################################

if __name__ == '__main__':
    doctest.testmod()
