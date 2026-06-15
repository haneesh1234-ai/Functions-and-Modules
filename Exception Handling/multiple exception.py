try:
    num1 = int(input("enter the numerator"))
    num2 = int(input("enter the denominator"))

    result = num1 / num2
    print("result is : ", result)

except ZeroDivisionError as zde:
    print(zde)
except ValueError as ve:
    print(ve)

finally:
    print("code endds succefully")