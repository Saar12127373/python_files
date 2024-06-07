# turn from decimal to binary:

def decimalToBinary(number, n):
    arr = []
    for i in range(1, n+1):

        if(number - (2 ** (n-i)) >= 0):
            number -= 2**(n-i)
            arr.append(1) 
            # print(1, end ="")

        else:
            # print(0, end="")
            arr.append(0)
    return arr

# turn from 0 to 1 and the oppiset:

def oppiste(number, n):
    binary_list = decimalToBinary(number, n)
    for i in range(n):
        if(binary_list[i] == 0):
            binary_list[i] = 1
        else:
            binary_list[i] = 0

    return binary_list

# add one to the oppiste binary:
def add_one(number, n):
    oppiste_binary = oppiste(number, n)
    for i in range(n-1 ,-1, -1):
        if(oppiste_binary[i] == 1):
            oppiste_binary[i] = 0
        else:
            # found a 0 replace to 1 and break:
            oppiste_binary[i] = 1
            return oppiste_binary
        # couldnt find a 0 just retrun zeros:
    return oppiste_binary      


def main():

    number = int(input("enter the number you want to turn into bits: "))
    n = int(input("enter how many bits you would like to use: "))
   
    print(number)

    print("number in binary: ")

    print(decimalToBinary(number, n))

    print("the minus binary: ")

    print(add_one(number, n))
    print("i love adididwadwadawdaw")
main()