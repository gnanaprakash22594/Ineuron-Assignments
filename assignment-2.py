#1a

rows = 5 
for i in range(0, rows):  
    # This inner loop will print the stars  
    for j in range(0, i + 1):  
        print("*", end=' ')  
    # Change line after each iteration  
    print(" ")  
# For second pattern  
for i in range(rows, 0, -1):  
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ") 


#1b

word = input("Enter a word:")[::-1]
print(word)