ageGroup = []
price = []
dict_list = {}
itertime = int(input("How many Age Group you want to add: "))
count = 0
if itertime <= 4:
    while count < itertime:
        ageGroup.append(input(f"{count} AgeGroup: "))
        price.append(int(input(f"{count} Price: ")))
        dict_list.update({ageGroup[count]: price[count]})
        count = count + 1
else:
    print("We can only add upto 4.")
print(dict_list)