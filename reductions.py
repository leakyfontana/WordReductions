# -*- coding: utf-8 -*-
"""
Functions about word reductions

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Xander Dyer (xdyer )
"""
__version__ = 1

def loadWords():
    '''
    This function opens the words_alpha.txt file, reads it
    line-by-line, and adds each word into a list.  It returns
    the list containing all words in the file.
    '''
    with open('words_alpha.txt') as wordFile:
        wordList = []
        
        for line in wordFile:
            wordList.append(line.rstrip('\n'))

    return wordList

def reduceOne(firstString, secondString, wordList):
    # This function checks if a given string is a valid reduction of another
    # string if one char is removed and both words are in the wordList
    # Input: two strings and a wordList
    # Returns: Whether secondString is a valid reduction of firstString


    if firstString not in wordList:
        #print("First word is not in the wordList")
        return False
    
    if secondString not in wordList:
        #print("Second word is not in the wordList")
        return False
      
    i = 0
    while i < len(firstString):
        if secondString == (firstString[:i] + firstString[i+1:]):
            return True
        i += 1
        
    return False
                
def reduceAll(word, wordList):
    # This function finds all valid reductions when removing one char from a
    # given string
    # Input: a word and a wordList
    # Returns: a list of valid one char reductions
    count = 0
    reduced = []
    
    while count < len(word):
        reduced.append(word[:count] + word[count+1:])
        count = count + 1
        
    return [word for word in reduced if word in wordList] 
        
def reduceTwoAll(word, wordList):
    # This function finds all valid reductions when removing two chars from a
    # given string
    # Input: a word and a wordList
    # Returns: a list of valid two char reductions
    reduced = []
    reduced2 = []
    cleaned = []
    
    i = 0
    while i < len(word):
        reduced.append(word[:i] + word[i+1:])
        reduced2.append(reduceAll(reduced[i], wordList))
        i += 1
    
    cleaned = [item for item2 in reduced2 for item in item2]
    reduced.clear()
    [reduced.append(item) for item in cleaned if item not in reduced]
    #print(reduced)
    return reduced
    
    

def validateReduction(reduction, wordList):
    # This function checks if all reductions that occur sequentially in a
    # given list of strings are valid
    # Input: a list of word reductions and a wordList
    # Returns: whether or not the reductions within the list are valid
    
    if len(reduction) < 1:
        #print("Invalid input list of reductions, Please input a list of at" +
              #"least one word")
        return False
    
    
    while len(reduction) != 1:
        if reduceOne(reduction[-2], reduction[-1], wordList):
            reduction.remove(reduction[-1])
        else:
            return False
        
    if len(reduction) == 1:
        if reduction[0] in wordList:
            return True
        else: 
            #print("Word not in wordList")
            return False
        
    return True
               
            

def main():
    # Here is where you will call your test cases
    wordList = loadWords()
    test1(wordList)
    test2(wordList)
    test3(wordList)
    test4(wordList)

    

###############################################################

# Here is where you will write your test case functions
    
# Below are the tests for reduceOne()
def test1(wordList):
    #Tests all branches of the function: if the words are in wordList, if 
    #there is a valid reduction between the words provided
    assert reduceOne("leave", "eave", wordList) == True, ("The function does" +
    " not provide proper feedback for a valid reduction")
    assert reduceOne("leaves", "eave", wordList) == False, ("The function does" 
    + " not provide proper feedback for a valid reduction")
    assert reduceOne("cat", "bat", wordList) == False, ("The function does" + 
    " not provide proper feedback for an invalid reduction")
    assert reduceOne("gggggg", "ggg", wordList) == False, ("The function does" 
    + " not provide proper feedback for a word not in wordList")
    assert reduceOne("eave", "leave", wordList) == False, ("The function does" 
    + " not provide proper feedback for an invalid reduction")
    assert reduceOne("artt", "art", wordList) == False, ("The function does" 
    + " not provide proper feedback for an invalid reduction")
    

# Tests the reduceAll() function
def test2(wordList):
    # Tests the functionality of the function by providing words that have valid
    # reductions that appear on the wordList and those that do not as well as 
    # testing an empty word
    assert reduceAll("boats", wordList) == ["oats", "bats", "bots", "boas", 
                                            "boat"], ("The function does not" +
    "return the proper list of reductions for the given word")
    assert reduceAll("ggg", wordList) == [], ("The function does not return" +
    "the proper list of reductions for the given word")
    assert reduceAll("t", wordList) == [], ("The function does not return " + 
    "the proper list of reductions for the given word")
    assert reduceAll("ct", wordList) == ["t", "c"], ("The function does not" +
    "return the proper list of reductions for the given word")
    assert reduceAll("", wordList) == [], ("The function does not" +
    "return the proper list of reductions for the given word")
    assert reduceAll("eerie", wordList) != ["rie", "ere", "eer"], ("The func" +
    "tion does not return the proper list of reductions for the given word")

# Tests the reduceTwoAll() function
def test3(wordList):
    # Tests the functionality of the function by providing words that have valid
    # "double" and "single" reductions that appear on the wordList and those 
    # that do not as well as testing an empty word
    assert reduceTwoAll("eerie", wordList) == ["rie", "ere", "eer"], (""
    + "The function does not return the proper list of reductions for the"
    + "given word")
    assert reduceTwoAll("", wordList) == [], ("The function does not" +
    "return the proper list of reductions for the given word")
    assert reduceTwoAll("ct", wordList) == [], ("The function does not" +
    "return the proper list of reductions for the given word")
    assert reduceTwoAll("ggg", wordList) == ["g"], ("The function does not" 
    + "return the proper list of reductions for the given word")
    assert reduceTwoAll("length", wordList) == ["lgth", "lent", "leng"], ("The" 
    + "function does not return the proper list of reductions for the given" 
    + "word")
    
# Tests the validateReduction() function
def test4(wordList):
    # Tests the functionality of the function by providing lists of words
    # that reduce correctly, incorrectly, are by themselves and appear/ do not
    # appear on the wordList
    assert validateReduction(["turntables", "turntable", "turnable", "tunable",
                              "unable"], wordList) == True, ("The function" + 
    "does not provide proper feedback for a valid reduction")
    assert validateReduction(["affidavit"], wordList) == True, ("The function"  
    + "does not provide proper feedback for a valid reduction")
    assert validateReduction([""], wordList) == False, ("The function"  
    + "does not provide proper feedback for a invalid reduction")
    assert validateReduction(["ggg"], wordList) == False, ("The function"  
    + "does not provide proper feedback for a invalid reduction")
    assert validateReduction(["cat", "bat"], wordList) == False, ("The function"  
    + "does not provide proper feedback for a invalid reduction")
    
    
    


    
###############################################################    
    
if __name__ == "__main__":
    main()    