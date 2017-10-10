# @package examples 
# @author Christopher Gallo
# This is the base for all examples. Put what your example does here.
#pprint allows us to deal with complex data structures
# from pprint import pprint as pp

# class example():
#     def __init__(self):
#         """Setup
#         """
#         pass
#     def main(self):
#         """Says Hello World 
#         """
#         print("Hello World")

        
# if __name__ == "__main__":
#     main = example()
#     main.main()


#create an array of unsorted integers and arrage them in ascending order
# try and think about it before coding
# if array[0] > array[1] change the order for these two and so on and so forth.
# This approach only compares items next to each other so you might/would have to perform this multiple times.
class bubble_sort():
    def main(self, my_array):
        is_sorted = False;
        while not is_sorted:
            is_sorted = True
            for i in range(0, len(my_array)):
                if i + 1 == len(my_array):
                    continue #this basically allows for the while loop to continue
                if my_array[i] > my_array[i+1]:
                    temp = my_array[i]
                    my_array[i] = my_array[i+1]
                    my_array[i+1] = temp
                    is_sorted = False
        return my_array


if __name__ == "__main__":
    my_array = [3,1,8,9,7,5]
    main = bubble_sort()
    result = main.main(my_array)
    print(result)


#dir() <--everything that python can do with whatever you input by spitting all of it out


#Interview Question:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 50,000,000

#brute force way
class sum_finder():
    def main(self, max):
        count = 0
        for i in range(1,max):
            if i % 3 == 0 or i % 5 == 0:
                count+=i
        return count
if __name__ == "__main__":
    main=sum_finder()
    result=main.main(50000000)
    print(result)



#more efficient way
class sigma_finder():
    def sum_divisible_by(self, number, max):
        p = int(max / number) #<-- ensures no floating numbers are used
        sum = number * (p * (p + 1)) / 2
        return int(sum)
    def main(self, limit):
        limit = limit - 1 
        result = self.sum_divisible_by(3, limit) + self.sum_divisible_by(5, limit) - self.sum_divisible_by(15, limit)
        return result
if __name__ == "__main__":
    limit = 50000000
    main = sigma_finder()
    result = main.main(limit)
    print("The sum of all the multiples of 3 or 5 below %s is %s" % (limit,result))