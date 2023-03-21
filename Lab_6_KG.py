"""
Name:Kiefer Gallant
Lab#6
Description:This lab will create a single linked list class
and use it to create a deck of cards 

"""

from random import sample

class SingleLinkedList:
    """
    Description:This is a single linked list class
    that had nodes for each piece of data
    Parameters:
    Return: Single linked list
    
    """
    class Node:
        def __init__(self,data,nextNode):
            """
            Description:Contains the data and the reference
            to the next piece of data in the sll
            Parameters:data , next node
            Return:
    
            """
            self._data = data
            self._nextNode = nextNode

        def getData(self):
            """
            Description:Returns the data in the 
            node
            Parameters:self -instance of node class
            Return: the data in the node
    
            """
            return self._data

        def getNextNode(self):
            """
            Description:Returns the node adjacent to the 
            node referenced
            Parameters: self - reference to the next node
            Return: next node object
    
            """
            return self._nextNode

        def setNextNode(self,data):
            """
            Description: Changes the next node to 
            the new data 
            Parameters: self - instance of the node class
                        data - data inside the node
            Return:
    
            """
            self._nextNode = data
            

    def __init__(self):
        """
        Description: Initializes the sll class
        Parameters:size - length of slll
                   firstNode - first node in the
                   sll 
        Return:
    
        """
        self._size = 0
        self._firstNode = None

    def __len__(self):
        """
        Description: Returns the length of the sll as an int
        Parameters:self - instance of sll
        Return:size - int length of sll
    
        """
        return self._size

    def __str__(self):
        """
        Description:Returns string representation
        of the sll
        Parameters:self - instance of slll
        Return: string of sll
    
        """
        string = ""
        temp =self._firstNode 
        while (temp!=None):
            string+=temp._data + ", "
            temp=temp._nextNode
        return string

    def _is_empty(self):
        """
        Description:Checks to see if the sll is empty
        Parameters:self - instance of sll
        Return: integer of size
    
        """
        return self._size == 0

    def pushHead(self,data):
        """
        Description: Adds a node to the front of 
        the single linked list
        Parameters:data - data to be stored in 
                   node
        Return:
    
        """
        newNode=self.Node(data,self._firstNode)
        self._size+=1
        self._firstNode=newNode
        
    
    def popHead(self):
        """
        Description: Removes and returns the node at the 
        start of the sll
        Parameters:self - instance of sll
        Return:returnVal - Node that was removed
    
        """
        returnVal=self._firstNode._data
        self._firstNode = self._firstNode._nextNode
        self._size-=1
        return returnVal
        

    def __iadd__(self,sll2):
        """
        Description:
        Parameters:
        Return:
    
        """
        second_list = sll2._firstNode
        self.addNodesTail(second_list)
        

    def addNodesTail(self,node):
        """
        Description:Adds a node at the end of 
        the sll
        Parameters: node - node object to be added
        at the end of the sll
        Return:
    
        """
        tail = self._firstNode
        while(tail._nextNode != None):
            tail = tail._nextNode
        tail._nextNode = node
        

class Deck:
    """
    Description:Card deck that uses a single linked list
    Parameters:
    Return:
    
    """

    class Card:
        """
        Description:The deck class is made of cards that are 
        the node in the single linked list
        Parameters:
        Return:
    
        """
        def __init__(self,value:str,suit:str):
            """
            Description:Initializes the card class
            with the value of the card and the suit
            Parameters:value-value str of card
                       suit - suit of the card
            Return:
    
            """
            self._suit = suit
            self._value = value
        
        def getCard(self):
            """
            Description: Returns a list with the 
            value and suit of the of the card
            Parameters:self - instance of card
            Return: list with value and suit
    
            """
            return [self._value,self._suit]
           
        def __str__(self):
            """
            Description:String representation of 
            of the card
            Parameters:self - instance of card
            Return: string representation of card
    
            """
            return f"{self._suit} {self._value}"

    def __init__(self):
        """
        Description: Creates an instance of deck
        class using a single linked list
        Parameters: self - instance of deck class
        Return:
    
        """
        self._shuffledDeck = SingleLinkedList()

    def __len__(self):
        """
        Description:Returns the length of the deck
        Parameters:self - instance of the deck
        Return: Int of the length of deck 
    
        """
        return len(self._shuffledDeck)
    
    def initDeck(self):
        """
        Description:Loops through value and loops through
        suits and creates a list that will be added one by 
        one to the single linked list deck object
        Parameters:
        Return:list of random cards 
    
        """
        total_cards_list = []
        total_cards = [] #full of card objects
        for i in [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]:
            for j in ["♠","♥","♦","♣"]:
                total_cards_list.append([i,j])
                total_cards.append(self.Card(i,j))
        random_cards_list = sample(total_cards_list,52)
        random_cards_objects = sample(total_cards,52)

        for i in random_cards_objects:
            self._shuffledDeck.pushHead(i)
        return random_cards_objects

        


    def getCards(self,n:int):
        """
        Description: Removes cards from deck sll object 
        and retursn them as a list, if the user needs more 
        cards than are in the deck it adds a new deck
        Parameters:n - number of cards to return
        Return: list of the number of cards selected
    
        """
        card_list = []
        for i in range(n):
            if self._shuffledDeck._is_empty():
                self.addNewDeck()
            popped_card = self._shuffledDeck.popHead()
            card_list.append(popped_card.getCard())
        return card_list

    def addNewDeck(self):
        """
        Description:Creates a new deck and adds it 
        to the deck single linked list object
        Parameters:
        Return:
    
        """
        new_linked_list = SingleLinkedList()
        new_deck = self.initDeck()
        for i in new_deck:
            new_linked_list.pushHead(i)
        self._shuffledDeck.__iadd__(new_linked_list)

if __name__ == "__main__":
    s = SingleLinkedList()
    s.pushHead("Node 1")
    s.pushHead("Node 2")
    s.pushHead("Node 3")
    s.pushHead("Node 4")

    print(s)

    d = Deck()
    d.initDeck()
    c = d.getCards(4)
    print(c)
   
    