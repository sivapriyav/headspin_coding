def insertElement(index,element):
    print(my_list[:insert_index-1]+[insert_element]+my_list[insert_index-1:])

    
my_list=['n','i','k','j','t','h','a']
insert_index=int(input("Enter index to which element to be inserted: "))
insert_element=input("Enter element to be inserted: ")
insertElement(insert_index,insert_element)