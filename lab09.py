# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    #  Ill first try a nested for loop, the outerloop  will pick an indice then add it with the others until it checks out and moves to the next 
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer. [3,2,4], 6 [1, 2]
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums), 1):
            if (nums[i] + nums[j] == target):
                return [i, j]
            
    return print("No matches found")
    


def max_profit(prices):
    # Outline:
    #   So my goal for this onne is to loop over each day and get the biggest price as i go and then calculate the profit between the biggest
    #  and the first day. then day it for the second day and all its possible biggest until i reach the last day and i can just return the updated profit
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    profit = 0
    
    for i in range(len(prices)):
        biggest = prices[i]
        for j in range(i+1, len(prices)):
            if prices[j] > biggest:
                biggest = prices[j]
        if (biggest -prices[i] > profit):
            profit = biggest - prices[i]
    return profit

def max_subarray(nums):
    # Outline:
    #   Ill first make a largest variable and leave it, then ill try to loop thorugh the list to and get a start indexes the subarray
    # and for every start index ill use a for loop to get all the possible end indexs. then ill make the sub array and compare its sum to largest
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    largest = nums[0]
    for i in range(len(nums)):
        for j in range(i, len(nums), 1):
            sumSubarray = sum(nums[i:j+1])
            if largest < sumSubarray:
                largest = sumSubarray

    return largest



def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    # This is a problem ive done before so ill use a list as a stack and for every bracket if its an opening one then i add its closing version to the stack. that way 
    # that way at the end i can just check if the it starts with a closing bracket then its empty and returns false or if its a closing one it should be the same as the last closing one added to the stack
    # TODO: return True if every bracket in `s` is closed correctly and in the right and at the end because the pop they should all be zero
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    stack = []

    for bracket in s:
        if bracket == '(':
            stack.append(')')

        elif bracket == '[':
            stack.append(']')

        elif bracket == '{':
            stack.append('}')
            
        else:
            if len(stack) == 0 or bracket != stack.pop():
                return False

    return len(stack) == 0


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    print(two_sum([3, 2, 4], 6))   # [0, 1]
    print(max_profit([]))
    print(max_subarray([-1, -2, -3]))
    print(is_balanced("([)]"))


if __name__ == "__main__":
    main()
