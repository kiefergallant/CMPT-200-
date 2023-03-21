"""

Name: Kiefer Gallant 

Lab 7

Description:This lab will create a program that will search a list 
of words to check if there are any other words that are anagrams
of the original word

"""

import random


class DailyAnagram:

    def __init__(self,nletters:int,nanagrams:int):
        """
        Description:This initializes the class 
        Params:nletters - number of letters the anagram should contain
               Nanagrams - number of anagrams that should be displayed
        Return:
        """
        self._nletters = nletters
        self._nanagrams = nanagrams
        self._dictionary = []

    def loadDictionary(self,filename:str):
        """
        Description:This function will load the word list 
        file and return a list where every word is an item
        in the list or a blank list if file cannot be found
        Params:filename - name of file to load
        Return:
        """
        try:
            with open(filename,"r") as dictionary_file:
                for line in dictionary_file:
                    self._dictionary.append(line.strip("\n"))
        except:
            return []
        
    def __randomWordFromDictionary(self):

        """
        Description:This function will return a random word 
        from the dictionary
        Parameters:self - instance of anagram
        Return:random word
        """
        nletters_list = []
        for word in self._dictionary:
            if len(word) == self._nletters:
                nletters_list.append(word)
        random_word = random.choice(nletters_list)
        return random_word

    def __permutation(self,word:str):

        """
        Description:Uses recursion to create permutations of word
        Parameters:word - string 
        Return:list of permutations 
        """
  
        #Base case
        if len(word) == 1:
            return [word]
        else:
            permutations_list = []
            for i in range(len(word)):
                letter = word[i]
                remainder_of_word = word[:i] + word[i+1:]
                remainder_permutations = self.__permutation(remainder_of_word)
                for permutation in remainder_permutations:
                    permutations_list.append(letter + permutation)
            return permutations_list
        
    def __isWord(self,word): 
        """
        Description:Checks the dictionary to see
        if the word is actually a word in the dictionary
        Parameters:word - string of letters
        Return:True if word is in dict or False if not

        """
        if word in self._dictionary:return True
        else:return False

    def __removeNonWords(self,list_of_words):
        """
        Description:Removes non words from the list of words
        Parameters:list of words - list of strings
        Return:list of words that are actually words in dictionary
        """
        valid_dictionary_words_list = []
        for word in list_of_words:
            if self.__isWord(word):
                valid_dictionary_words_list.append(word)
        return valid_dictionary_words_list

    def __findAnagrams(self,word): 
        """
        Description:Creates permutations of the word and 
        removes strings that are not real words
        Parameters:word - string
        Return:permuations of word that are valid dictionary
        words
        """
        permutations = self.__permutation(word)
        valid_dictionary_words = self.__removeNonWords(permutations)
        return valid_dictionary_words
    
    def __removeDuplicates(self,list_of_words):
        """
        Description:Removes duplicates recursively from list of words
        Parameters:list_of_words - list of words containing duplicates
        Return:List of words with duplicates removed
        """
        if len(list_of_words) == 0:
            return []
        else:
            first = list_of_words[0]
            remainder = list_of_words[1:]
            unique_words_list = self.__removeDuplicates(remainder)
            if first in unique_words_list:
                return unique_words_list
            else:
                return [first] + unique_words_list
        
    def getDailyAnagram(self):
        """
        Description:Main function that gets words with anagrams
        removes the duplicates and then prints the anagrams
        Parameters:self - instance of DailyAnagram
        Return:
        """
        random_word , anagrams = self.__getWordWithAnagrams()
        unique_anagrams = self.__removeDuplicates(anagrams)
        self.__printAnagram(unique_anagrams,random_word)
    
    def __printAnagram(self,anagrams_list,word):
        
        """ 
        Description:Prints the anagrams and the original word
        Parameters:anagrams_list - list of anagrams
                   word - original word
        Return:
        """
        print(f"Find the Anagrams for the word:{word}")
        print(f"Solutions {anagrams_list}")

    def __getWordWithAnagrams(self):
        """
        Description:This function will generate a random word and then it will 
        find anagrams of the random word, count the number of anagrams and keep
        generating random words and their anagrams untill the number of anagrams
        is greater than Nanagrams and then it will return the anagrams and random
        word
        Parameters:self
        Return:random_word - original word 
               anagrams - list of anagrams of original word
        """
        random_word = self.__randomWordFromDictionary()
        anagrams = self.__findAnagrams(random_word)
        number_of_anagrams = self.__countAnagrams(anagrams)
        while number_of_anagrams <= self._nanagrams:
            random_word = self.__randomWordFromDictionary()
            anagrams = self.__findAnagrams(random_word)
            number_of_anagrams = self.__countAnagrams(anagrams)
        return (random_word,anagrams)


    def __countAnagrams(self,anagrams_list):
        """
        Description:Counts the number of anagrams in the list
        Parameters:anagrams list - list of anagrams
        Return:int of length of list
        """
        return len(anagrams_list)


letters_in_word = 5
min_anagrams = 2
da = DailyAnagram(letters_in_word,min_anagrams)
da.loadDictionary("wordlist.txt")
da.getDailyAnagram()