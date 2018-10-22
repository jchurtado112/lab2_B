# Jesus Hurtado, CS 2302 - Data Structures, Fall 2018, TR: 10:30am-11:50am
# Create a linkedlist of passwords by reading off a file with their number of times 
# found in the file. Then perform bubble sort and merge sort on it, and finally,
# for each sort method print the 20 most used passwords in the file.
 
class Node: #Node class
    
    def __init__(self, password="", count=0):
        self.password = password
        self.count = count
        self.next=None

class Linkedlist:   #Linkedlist class to perform operations
    
    #Initialize the head node used to point to first element in list
    def __init__(self): 
        self.head = Node()
        
    def add(self, password):    # Method to add a node
        new_node = Node(password,1)
        temp = self.head
        isinLL=0
        
        #If node (password) has already been added to linked list, its count will add +1
        while temp.next != None and isinLL == 0: 
            temp=temp.next
            if temp.password == new_node.password:
                temp.count+=1
                isinLL+=1
                return
        #If node is not in the linkedlist yet, it will be added at the end of linkedlist    
        if isinLL == 0:
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=new_node
            return
    
        
    def create_dictionary(self):  #Create a dictionary from the content of file
        j=0
        dictionary={}
        with open("my_file.txt") as file:  #Opening a file to retrieve content
            for line in file:
                j+=1
                
        #Each of the passwords found in each line will be stored in a list
                passwords_in_line=[]
                passwords_in_line=[word for word in line.split()]
        #Then each of the passwords will be stored in the dictionary and its count
                for password in passwords_in_line:
                    if password in dictionary:
                        dictionary[password]+=1
                    else:
                        dictionary[password]=1
                if j >= 100:
                    return dictionary
    
    #Now from the contents of the dictionary create a linkedlist            
    def create_ll_from_dictionary(self, dictionary_1): 
        new_list = Linkedlist()
        for element in dictionary_1:
            for k in range(dictionary_1[element]):
                new_list.add(element)
                #print("So far the linkedlist is saving these: ")
                #new_list.display()
                
        return new_list    # returns the new list created
        
        
    def bubble_sort(self): #Bubble sort the linkedlist created from dictionary
        limit=20    #Maximum numer of most used passwords to be printed
        items=[]    #Will store the count of each of the passwords found
        most_used_pass=[]   #Will help to determine if a password has already been entered
        temp=self.head
        
         #Iterate through the linkedlist to append each of the nodes' count
        while temp.next!=None:  
            temp=temp.next
            items.append(temp.count)
        
        #Bubble sort the count of the nodes in descending order
        for i in range(len(items)-1, 0, -1):
            for j in range(i):
                if items[j] < items[j+1]:
                    t=items[j]
                    items[j]=items[j+1]
                    items[j+1]=t
        
        #Print only the nodes's info if it is one of the 20 with the highest count
        #temp=self.head
        i=0
        while i < limit:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
                if temp.count == items[i] and temp.password not in most_used_pass:
                    most_used_pass.append(temp.password)
                    print("Password #{} = {}, # of times found: {}".format(i+1, temp.password,temp.count))
                    i+=1
                    break
            
    #This will sort the linkedlist for solution A        
    def get_most_used(self):
        most_used=[]
        limit=20
        temp=None
        
        #Will iterate 20 times through the linkedlist to find password with 
        #highest count in each iteration
        for i in range(limit):   
            temp = self.head
            control=0
            maximum=0
            #Will iterate through each of the nodes to get max count and will
            # check if that password has already been added to the 20 most used passwords
            while temp != None:
                if control == 0:
                    temp=temp.next
                    control+=1
                if temp.password in most_used:
                    temp=temp.next
                elif temp.password not in most_used and maximum < temp.count :
                        maximum = temp.count
                        temp=temp.next
                else:
                    temp=temp.next
        
            #Will look for password that has a count equal to the maximum count 
            #found in this iteration        
            temp = self.head
            get_out = 0
            while temp.next != None:
                temp=temp.next
                if temp.count == maximum and get_out == 0 and temp.password not in most_used:
                    most_used.append(temp.password)
                    print("Most used password: {}, times found: {}".format(temp.password,temp.count))
                    get_out+=1
    
    def length(self):   #Will return the length of the linkedlist
        total_nodes = 0
        temp = self.head
        while temp.next != None:
            total_nodes+=1
            temp=temp.next
        return total_nodes
    
    def display(self): #Will display current modifications to the linkedlist
        elements=[]
        temp = self.head
        while temp!=None:
            #print("Password: {}, count: {}".format(temp.password,temp.count))
            elements.append(temp.password)
            temp=temp.next
        print(elements)
    
    def display_20_sorted(self): #Will display the 20 most used passwords
        temp=self.head
        i=0
        while temp != None and i <20:
            #temp=temp.next
            print("Most used password #{} = {}, count: {}".format(i+1,temp.password,temp.count))
            i+=1
            temp=temp.next
            
   
                
def read_file(list_1):  #Will read off the file and retrieve content and create linkedlist
    i=0
    with open("my_file.txt") as file:
        for line in file:
            i+=1
            passwords_in_line=[]
            passwords_in_line=[word for word in line.split()]
            for password in passwords_in_line:
                list_1.add(password)
            if i >= 100:
                return
                

# function will merge two linked lists
def mergeLists(l1, l2):
    temp = None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if  l1.count > l2.count:
        temp = l1
        temp.next = mergeLists(l1.next, l2)
    else:
        temp = l2
        temp.next = mergeLists(l1, l2.next)
    return temp

# function will sort the linked list using mergeSort
def mergeSort(head):
    if head is None or head.next is None:
        return head 
    l1, l2 = divideLists(head)
    l1 = mergeSort(l1)
    l2 = mergeSort(l2)
    return mergeLists(l1, l2)

# function will divide a linked list into two equal linked lists
def divideLists(head):
    slow = head                     # slow is a pointer to reach the mid of linked list
    fast = head                     # fast is a pointer to reach the end of the linked list
    if fast:
        fast = fast.next            
    while fast:
        fast = fast.next            # fast is incremented twice while slow is incremented once per loop
        if fast:
            fast = fast.next
            slow = slow.next
    mid = slow.next
    slow.next = None
    return head, mid

          
def main(): #Main method
    option = input("Enter what option (either A or B) you want to choose to get the twenty most used passwords: ")
    if option == 'A':    #If option A creates and stores into linkedlist all content from the file
        mylist_1 = Linkedlist()
        read_file(mylist_1)
        print("--------------------------------------------------------------------------------------")
        print()
        print("Displaying linkedlist created from the content in the file")
        print()
        print("--------------------------------------------------------------------------------------")
        mylist_1.display()
        print()
        print()
        print("The top 20 most used passwords:")   #Displays the 20 most used passwords
        print("--------------------------------------------------------------")
        mylist_1.get_most_used()
    else:    # If option B creates dictionary and then bubble sort and merge sort is applied to linkedlist
        if option == 'B':
            my_list2 = Linkedlist()
            my_list3 = Linkedlist()
            
            dictionary_2 = my_list2.create_dictionary()
            print("----------------------------------------------------------")
            print()
            print("Displaying the dictionary created")
            print()
            print("----------------------------------------------------------")
            print(dictionary_2)   #Prints out dictionary
            print()
            print()
            linked_2 = my_list2.create_ll_from_dictionary(dictionary_2)
            print("----------------------------------------------------------")
            print()
            print("Displaying the linkedlist created from dictionary")
            print()
            print("----------------------------------------------------------")
            linked_2.display() #Prints out linkedlist created from dictionary
            print()
            print()
            length_linked_2 = linked_2.length()   #Displays the length of linkedlist
            print("This is the length of list created from dictionary: {}".format(length_linked_2))
            print()
            print()
            print("----------------------------------------------------------")
            print()
            print("Displaying the bubble sorted linkedlist")
            print()
            print("----------------------------------------------------------")
            linked_2.bubble_sort()   #Displays bubble sorted linkedlist
            print()
            print()
            print("-----------------------------------------------------------")
            print()
            print("Now linkedlist will be sorted using merge sort")
            print()
            print("----------------------------------------------------------")
            print()   #Creates dictionary for merge sorting algorithm
            dictionary_3 = my_list3.create_dictionary()
            print("Dictionary created for merge sorted linkedlist")
            print()
            print(dictionary_3)
            print()
            print()    #Creates a linkedlist out of the content of the dictionary
            linked_3 = my_list3.create_ll_from_dictionary(dictionary_3)
            print("----------------------------------------------------------")
            print()
            print("Linkedlist created from dictionary to be merge sorted")
            print()
            print("----------------------------------------------------------")
            linked_3.display()    #This linkedlist will be merge sorted
            print()
            print()
            print("----------------------------------------------------------")
            print()    #Displays a merge sorted linkedlist
            print(" * Displaying the MERGE SORTED linkedlist *")
            print()
            print("----------------------------------------------------------")
            my_list_m=Linkedlist()
            read_file(my_list_m)
            my_list_m.head = mergeSort(my_list_m.head)
            my_list_m.display()
            print()
            print()
            my_list_m.display_20_sorted()
    

main()    #Program starts