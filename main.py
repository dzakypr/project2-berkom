items = ['a','b','c','d']
initial_state = [2,1,1,1]
borrowing_state = [0,0,0,0]

def search_item_index(item):
    x = 0
    for i in items:
        if i == item:
            return x
        x += 1
    return -1

def borrow_items():
    index = -1
    while(index < 0):
        print(f"which item u want to borrow {items}")
        items_want_to_borrow = input("input items: ")
        index = search_item_index(items_want_to_borrow)
        if(index < 0):
            print("Item is not found or already borrowed")
        if(initial_state[index] - borrowing_state[index] == 0):
            index = -1
            print("Item is already borrowed")
        else:
            borrowing_state[index]+=1




x = 1
while(x):
    x = int(input("Input options: "))
    if(x == 1):
        borrow_items()
        


