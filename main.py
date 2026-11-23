items = ['a','b','c','d']
initial_state = [2,1,1,1]
borrowing_state = [0,0,0,0]

def borrow_items():
    print(f"which item u want to borrow {items}")
    items_want_to_borrow = input("input items: ")
    

x = 1
while(x):
    x = int(input("Input options: "))
    if(x == 1):
        borrow_items()
        


