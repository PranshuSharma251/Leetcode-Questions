digits = [4,3,2,1]
digits.reverse()
print(digits)
def add_one(digits):
    if digits[i] <9:
        digits[i] += 1
        return(digits)
    elif digits[i] == 9 and i!=len(digits):
        digits[i] = 0
    

class Solution:
  def plusOne(self, digits: list[int]) -> list[int]:
    for i, d in reversed(list(enumerate(digits))):
      if d < 9:
        digits[i] += 1
        return digits
      digits[i] = 0

    return [1] + digits