def check_positive(number):
  if number<=0:
    raise NegativeNumberError("Negative number entered.")

try:
  num=int(input("enter a positive number:"))
  check_positive(num)
  print("you entered a positive number")
except NegativeNumberError as e:
  print(e)
