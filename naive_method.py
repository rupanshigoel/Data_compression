#  start 
import basic
import string


def frequency_words(s):
    """This function finds out frequency of words from a string and returns a dictionary."""

    #created a dictionary d that stores the frequency as the values to the keys(words)
    d={}

    #using split function seperated the words from the string s 
    s=s.split()

    #traversing through the string 
    for i in s:

        # if i is in d then increase the frequency of the word by one 
        if i in d:
            d[i]+=1
        #else put its frequency as one 
        else:
            d[i]=1
        
    return d


def substitute_make(d):
    """This function takes a dictionary with frequency of words and returns the substitution dictionary which has substitutions
    with the capital letter doublets of the English alphabet"""

    # l=[i for i in range(100)]
    #created a string x that contains 10 upper case letter doublets of the alphabet
    x=['AA','BB','CC','DD','EE','FF','GG','HH','II','JJ']
    # s=''
    # for i in l:
        # s+=str(i)
    
    a=0 # pointer to x
    d_ans={} # the substitute dict

    #converted dicionary to value key pair nested list using key_value_list function
    d=basic.key_value_list(d)

    #using quick_sort sorted the list 
    d=basic.quick_sort(d)

    #reversed the list so that the maximum occuring words come first 
    d=d[::-1]
    
    #traversing through the list d
    for i in d:
        #if the pointer a has reached length of x then the substitution with capital letters stops
        if a==len(x):
            break
        
        #the words are replaced one by one til 10th word with the capital letter of the alphabet from string x
        else:
            d_ans[i[1]]=x[a]
            a=a+1
    return d_ans

def naive_approach(s):
    """This function replaces the most frequently occuring words with symbols to reduce size."""
    
    #dictionary is made containing the frequency of the words using decrypt_words function
    d=frequency_words(s)

    #created the dictionary which contains the substitutions for the string s
    d=substitute_make(d)
    
    #created a list key containing the keys of the dictionary d 
    key=list(d.keys())

    ans="" # the final string with changed words

    #traversing through the list containing the words of the string s
    for i in s.split():
        if i in key:  #if the word is in key list
            ans+=d[i]+' '  # then substiution is made and added to the string ans
        else:  #otherwise
            ans+=i+ ' '  # the word is added as it is to the string ans
    return ans
