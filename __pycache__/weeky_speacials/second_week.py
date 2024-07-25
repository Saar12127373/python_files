# def how_many_cases(amount_stairs):
#     count = 1
#     jump = 2
#     while(jump <= amount_stairs):
#         count += 1
#         jump += 2
#     return count

# def again():
#     while True:
#         amount = input("Enter amount of stairs or enter stop to quit: ")
#         if amount.lower() == "stop":
#             return 0
#         else:
#             print(how_many_cases(int(amount)))

# def main():
#     again()


# main()

def mystery(n):
    if n < 2:
        return 1
    else:
        return mystery(n -1) + mystery(n -2) + mystery(n -3)
    
result = mystery(5)
print(result)