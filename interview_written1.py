# 1: print the list of anagrams in the given list of words
n = int(input("No of Iteration: "))
list = []
ana = {}
for i in range(n):
    word = input("enter a word: ")
    list.append(word)
    sorted_word = "".join(sorted(word))
    if sorted_word in ana:
        ana[sorted_word].append(word)
    else:
        ana[sorted_word] = [word]
for sorted_word , words in ana.items():
    if len(words) > 1:
        print(words)


#  2: print all the pairs of numbers in the given list which make sum N

list_numbers = []
num = 10
for i in range(7):
    num = int(input("enter a num: "))
    list_numbers.append(num)
print(list_numbers)
for i in range(len(list_numbers)):
     for j in range(i+1,len(list_numbers)):
            if list_numbers[i] + list_numbers[j] == num:
                print("Sum of  two numbers is ",list_numbers[i],list_numbers[j], "=", num)

l = [4,3,6,8,7,11,2]
n = 10
for i in range(len(l)):
     for j in range(i+1,len(l)):
          if l[i] + l[j] == n:
               print(l[i],l[j])



# 3 : print which 3 consecutive numbers make the highest sum

numbers = [1, -2, 3, 4, -5, 8, -3, 2, 1]
max_sum = float('-inf')
max_sum_indices = []

for i in range(len(numbers)-2):
    current_sum = numbers[i] + numbers[i+1] + numbers[i+2]
    if current_sum > max_sum:
        max_sum = current_sum
        max_sum_indices = [i, i+1, i+2]

print(numbers[max_sum_indices[0]], numbers[max_sum_indices[1]], numbers[max_sum_indices[2]])