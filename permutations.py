# Python program for the above approach
import math 
# Function to find the possible
# permutations
# H = até aonde vai calcular
# l = de onde começa a calcualr
def permutations(ressult, nums, l, h) :
     
    # Base case
    # Add the vector to result and return
    if (l == h) :
        ressult.append(nums);
        for i in range(len(nums)):
            print(nums[i], end=' ');
        print('')
        
        return;

    # Permutations made
    for i in range(l, h + 1):
         
        # Swapping
        temp = nums[l];
        nums[l] = nums[i];
        nums[i] = temp;
 
        # Calling permutations for
        # next greater value of l
        permutations(ressult, nums, l + 1, h);
        

        # Backtracking
        temp = nums[l];
        nums[l] = nums[i];
        nums[i] = temp;
 
# Function to get the permutations
def permute(nums):
    print("number of permutations; ", math.factorial(len(nums)))
    # Declaring result variable
    x = len(nums) - 1;
    result = [];
     
    # Calling permutations for the first
    # time by passing l
    # as 0 and h = nums.size()-1
    permutations(result, nums, 0, x);
    return result;
 
# Driver Code
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5];
    res = permute(nums);
