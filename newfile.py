percentage = float(input("enter your percentage"))
match percentage:
  case percentage if 90<percentage<=100:
    print("outstanding")
  case s if 80<s<=90:
    print("grade A")
  case s if 70<s<=80:
    print("grade B")
  case s if 50<s<=70:
    print("grade C")
  case s if 0<s<=40:
    print("fail")
  case _ :
    print("invalid")