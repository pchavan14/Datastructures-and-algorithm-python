#Trie
#Trie is a tree - based data structure that organizes data in a heirarchy
#it is used to store and search strings in time efficient way , we even store end of strings propoerty
#It is used for auto completion and string searching
#we need trie for spelling checker and auto - completion

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_string = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    #insert string
    def insertString(self,word): #Time and space complexity is O(m)
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.end_of_string = True
        print("Successfully inserted")

    #search for a string in a trie
    def searchString(self,word): #Space complexity is O(1) , time complexity is O(m) (where m is the length of the string we are looking for)
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node == None:
                return False
            current = node
        
        #only is end of string is True , the complete string exists else it is just a prefix of any other string
        if current.end_of_string == True:
            return True
        else:
            return False
        
    def deleteString(self,word):
        pass 


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Api")
print(newTrie.searchString("Api"))

#Practical use of Trie
#Auto complextion feature
#Spell checker 
        





