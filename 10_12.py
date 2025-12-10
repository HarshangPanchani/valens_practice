try:
    print(2)
except IndexError as e:
    print(" except that An error occurred:", e)
# except ZeroDivisionError as e:
#     print(" except that A division by zero occurred:", e)
finally:
    print("finally.")
print("This line runs after the try-except-finally block.")

print("finally executes whether an exception occurs or not. but above line skips the execution if the error was not handled ")