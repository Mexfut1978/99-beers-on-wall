"""
# While Loop
# For in --key differences in 'for in' loop clearly defined start and finish to loop
# While--while loops don't stop on a list and has to be told to stop(sentinal value)

"""
# nums = list(range(1,100))
#   print(nums)

# ####for in loop


# for num in nums:  <--- to print out the list of numbers
#     print(num)


# # while len(nums) > 0:       <-- length of nums is great than 0
# #     print(nums.pop())      <--iterates over list and pops off the value--starts at 99 and goes to 1

(nums.pop())      <--iterates over list and pops off the value--starts at 99 and goes to 1

# This is an example

# nums = list(range(1, 100))

# while len(nums) > 0:
#   print(nums.pop())

# Guessing Game ------------------------------

# def guessing_game():
#   while True:
#     print('What is your guess?')
#     guess = input()

#     if guess == '42':
#       print('You correctly guessed it!')
#       return False
#     else:
#       print(f"No, {guess} isn't the answer, please try again\n")

# guessing_game()