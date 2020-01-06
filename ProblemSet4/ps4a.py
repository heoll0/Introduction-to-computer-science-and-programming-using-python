# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    all_list=[]
    if len(sequence)==1:
        all_list.append(sequence)
    else:
        first_letter=sequence[0]
        list2=get_permutations(sequence[1:])
        for i in range(len(list2)):
            str1=list2[i]
            for i in range(len(str1)+1):
                str2=str1[:i]+first_letter+str1[i:]
                all_list.append(str2)
    return all_list

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))

#    example_input = 'avd'
#    print('Input:', example_input)
#    print('Expected Output:', ['avd', 'adv', 'dva', 'dav', 'vad', 'vda'])
#    print('Actual Output:', get_permutations(example_input))
#    example_input = 'egd'
#    print('Input:', example_input)
#    print('Expected Output:', ['egd', 'edg', 'deg', 'dge', 'gde', 'ged'])
#    print('Actual Output:', get_permutations(example_input))
#    example_input = 'rng'
#    print('Input:', example_input)
#    print('Expected Output:', ['rng', 'rgn', 'grn', 'gnr', 'nrg', 'ngr'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
     pass