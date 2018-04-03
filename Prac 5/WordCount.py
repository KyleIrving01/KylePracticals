
words = input("Enter a sentence")
my_string = words.lower().split()
my_dict = {}
for item in my_string:
    if item in sorted(my_dict):
        my_dict[item] += 1
    else:
        my_dict[item] = 1
#print (my_dict)

print("\n".join("{}:\t{}".format(k, v)
                for k, v in sorted(my_dict.items())))

