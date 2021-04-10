 Change Item Value 
 *****************

 thislist = ["apple", "banana", "cherry"]
 thislist[1] = "blackcurrant"

 print(thislist)

 Output : ['apple', 'blackcurrant', 'cherry']

 Change a Range of Item Values :
 *****************************

 -> To change the value of items within a specific range, define a list with the    new values, and refer to the range of index numbers where you want to insert    the new values:

   thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
   thislist[1:3] = ["blackcurrant", "watermelon"]
   print(thislist)

   Output : ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']



  thislist = ["apple", "banana", "cherry"]

  thislist[1:2] = ["blackcurrant", "watermelon"]

  print(thislist)

  output : ['apple', 'blackcurrant', 'watermelon', 'cherry']

 Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

  thislist = ["apple", "banana", "cherry"]

  thislist[1:3] = ["watermelon"]

  print(thislist)
  
 OUtput : ['apple', 'watermelon']

 Insert Items :
 ************

 -> To insert a new list item, without replacing any of the existing values, we can use the insert() method.

 -> The insert() method inserts an item at the specified index:

    thislist = ["apple", "banana", "cherry"]
    thislist.insert(2, "watermelon")
    print(thislist)

  Output : ['apple', 'banana', 'watermelon', 'cherry']






