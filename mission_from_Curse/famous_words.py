import sys


try: 
    f = open(r"C:\8200\python_files\mission_from_Curse\file_words.txt", "r")
    words = f.read().split(" ")
    
    dict_words = {}
   
    n = int(sys.argv[1])


    for word in (words):
        if(word in dict_words):
            dict_words[word] += 1
        else:
            dict_words[word] = 1


    sorted_dict = sorted(dict_words.items(), key = lambda x: x[1], reverse = True)


    for i in range(n):
        print(sorted_dict[i][0])

    f.close()
except Exception as e:
    print("Error")