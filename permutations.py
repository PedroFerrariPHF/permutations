# Python program for the above approach
import math

counter = 0
# Function to find the possible
# permutations
# H = até aonde vai calcular
# l = de onde começa a calcualr
def permutations(ressult, nums, l, h, counter) :
     
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
        permutations(ressult, nums, l + 1, h, counter);
        

        # Backtracking
        temp = nums[l];
        nums[l] = nums[i];
        nums[i] = temp;
 
# Function to get the permutations
def permute(nums, nums2):
    print(math.factorial(len(nums)))
    # Declaring result variable
    x = len(nums) - 1;
    x2 = len(nums2) -1;
    result = [];
     
    # Calling permutations for the first
    # time by passing l
    # as 0 and h = nums.size()-1
    permutations(result, nums, 0, x, counter);
    return result;
 
# Driver Code
if __name__ == '__main__':
    nums = [4, 6, 5,];
    nums2 = [8, 3, 9];
    res = permute(nums, nums2);
