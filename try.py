# Example of an IO error
try:
    file = open('filename.txt')
    file.write('Hello World')
except Exception as e:
    print('Cannot open the file :', e)
finally:
    # this block is always executed regardless of exception generation.  
    print('This is always executed')  