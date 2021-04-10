 Remove Specified Item :
 *********************

 -> The remove() method removes the specified item.

 thislist = ["apple", "banana", "cherry"]
 thislist.remove("banana")
 print(thislist)

 Output : ['apple', 'cherry']

 Remove Specified Index :
 **********************    
 -> The pop() method removes the specified index.
 
 thislist = ["apple", "banana", "cherry"]
 thislist.pop(1)
 print(thislist)

Output : ['apple', 'cherry']

 -> If you do not specify the index, the pop() method removes the last item.

 thislist = ["apple", "banana", "cherry"]
 thislist.pop()
 print(thislist)

 Output : ['apple', 'banana']

 -> The del keyword also removes the specified index:
   
  thislist = ["apple", "banana", "cherry"]
  del thislist[0]
  print(thislist)

  Output : ['banana', 'cherry']

 -> The del keyword can also delete the list completely.

  thislist = ["apple", "banana", "cherry"]
  del thislist

  Output : 

      Clear the List :
      **************    
 
    -> The clear() method empties the list.

    -> The list still remains, but it has no content.

    thislist = ["apple", "banana", "cherry"]
    thislist.clear()
    print(thislist)
   
    Output : []


