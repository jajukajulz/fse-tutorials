
a = 5
b = 0
print(a/b)

# anatomy of try/catch
try:
    # code for which an error might occur
    pass
except:
       # optional block
       # Handling of exception (if required)
       pass
else:
       # execute if no exception
       pass
finally:
      # code in a finally block is always executed
      pass

# Example of an IO error
try:
    file = open('filename.txt')
    file.write('Hello World')
    
except Exception as e:
    print('Cannot open the file :', e)
    
finally:
    # Make sure to close the file after
    file.close()

# Example of an UnboundLocalError
def display_student_number():
    print(student_number)
    student_number = "ABC12345"

display_student_number()

# Create a memory error using an infinite loop
def create_large_list_infinite_loop():
    data = large_list = [0] * (10**9)  # Attempting to create a list with more than a billion elements
    large_list = []
    while True:
        large_list.append(data)

create_large_list_infinite_loop()