number=int(input('enter a number:'))
reverse_number=0
temp=number
while temp>0:
  digit=temp%10
  reverse_number=reverse_number*10+digit
  temp=temp//10
if number==reverse_number:
  print(f"{number} is a palindrome number")
else:
  print(f"{number} is not a palindrome number")

number=input('enter a number:')
if number==number[::-1]:
  print("palindrome number")
else:
  print("not a palindrome number")

def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
