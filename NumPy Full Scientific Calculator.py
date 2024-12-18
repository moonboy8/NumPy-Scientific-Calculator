import numpy as np
from scipy import stats

def menu():
    global choice
    global choice_1
    global choice_2
    global choice_3
    global choice_4
    global choice_5

    print("------------------------------------------------------------------------------------------------------------------")
    print("Hello, this is the NumPy Scientific Calculator made by Shrivardhan Boini. Choose what you want to do :)")
    print("1. Arithmetic Operations/Scalar Math")
    print("2. Trigonometry")
    print("3. Set Theory")
    print("4. Statistics")
    print("5. Matrices")
    print("6. Exit")
    
    while True:
        try:
            choice = int(input("What do you want to do (# value): "))
            if choice not in [1, 2, 3, 4, 5, 6]:
                print("Invalid input. Please enter a number between 1 and 6.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if choice == 1:
        print("-------------------------------------------------------------------------")
        print("This is the Arithmetic Operations/Scalar Math Menu")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Powers")
        print("6. Roots")
        print("7. Absolute Value")

        while True:
            try:
                choice_1 = int(input("What operation do you want to do (# value): "))
                if choice_1 not in [1, 2, 3, 4, 5, 6, 7]:
                    print("Invalid input. Please enter a number between 1 and 7.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    elif choice == 2:
        print("-------------------------------------------------------------------------")
        print("This is the Trigonometric Function Menu")
        print("1. Sin")
        print("2. Cosine")
        print("3. Tangent")
        print("4. Cosecant")
        print("5. Secant")
        print("6. Cotangent")
        print("7. Log")

        while True:
            try:
                choice_2 = int(input("What operation do you want to do (# value): "))
                if choice_2 not in [1, 2, 3, 4, 5, 6, 7]:
                    print("Invalid input. Please enter a number between 1 and 7.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    elif choice == 3:
        print("-------------------------------------------------------------------------")
        print("This is the Set Theory Menu")
        print("1. Union")
        print("2. Intersection")
        print("3. Difference")
        print("4. Symmetric Difference")
        print("5. Unique Values")

        while True:
            try:
                choice_3 = int(input("What operation do you want to do (# value): "))
                if choice_3 not in [1, 2, 3, 4, 5]:
                    print("Invalid input. Please enter a number between 1 and 5.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    elif choice == 4:
        print("-------------------------------------------------------------------------")
        print("This is the Statistics Menu")
        print("1. Median")
        print("2. Mean")
        print("3. Mode")
        print("4. Standard Deviation")
        print("5. Minimum")
        print("6. Maximum")
        print("7. Compute Percentile")

        while True:
            try:
                choice_4 = int(input("What operation do you want to do (# value): "))
                if choice_4 not in [1, 2, 3, 4, 5, 6, 7]:
                    print("Invalid input. Please enter a number between 1 and 7.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    elif choice == 5:
        print("-------------------------------------------------------------------------")
        print("This is the Matrices Menu")
        print("1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrices")
        print("4. Find Determinant")

        while True:
            try:
                choice_5 = int(input("What operation do you want to do (# value): "))
                if choice_5 not in [1, 2, 3, 4]:
                    print("Invalid input. Please enter a number between 1 and 4.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    elif choice == 6:
        print("Goodbye :)")
        exit()  

def operate():
    global choice, choice_1, choice_2, choice_3, choice_4, choice_5

    while True:
        menu()  # Show the menu

        # Arithmetic Operations
        if choice == 1:
            try:
                if choice_1 == 1:
                    a = float(input("What is the first number you wish to add: "))
                    b = float(input("What is the second number you wish to add: "))
                    answer = a + b
                    print(f"Your answer is: {answer}")
                elif choice_1 == 2:
                    a = float(input("What is the first number you wish to subtract: "))
                    b = float(input("What is the second number you wish to subtract: "))
                    answer = a - b
                    print(f"Your answer is: {answer}")
                elif choice_1 == 3:
                    a = float(input("What is the first number you wish to multiply: "))
                    b = float(input("What is the second number you wish to multiply: "))
                    answer = a * b
                    print(f"Your answer is: {answer}")
                elif choice_1 == 4:
                    a = float(input("What is the first number you wish to divide: "))
                    b = float(input("What is the second number you wish to divide: "))
                    if b != 0:
                        answer = a / b
                        print(f"Your answer is: {answer}")
                    else:
                        print("Error: Division by zero is not allowed.")
                elif choice_1 == 5:
                    base = float(input("What is the base: "))
                    power = float(input("What is the power: "))
                    answer = base ** power
                    print(f"Your answer is: {answer}")
                elif choice_1 == 6:
                    num = float(input("What is your desired number: "))
                    n = float(input("What is your desired root index: "))
                    answer = np.power(num, 1 / n)
                    print(f"Your answer is: {answer}")
                elif choice_1 == 7:
                    num = float(input("What is the number you want the absolute value of: "))
                    answer = abs(num)
                    print(f"Your answer is: {answer}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

        # Trigonometry Operations
        elif choice == 2:
            try:
                if choice_2 == 1:  # Sin
                    num = float(input("Enter angle in radians: "))
                    answer = np.sin(num)
                    print(f"Your answer is: {answer}")
                elif choice_2 == 2:  # Cos
                    num = float(input("Enter angle in radians: "))
                    answer = np.cos(num)
                    print(f"Your answer is: {answer}")
                elif choice_2 == 3:  # Tan
                    num = float(input("Enter angle in radians: "))
                    if np.isclose(np.cos(num), 0):
                        print("Error: Tan is undefined for this angle.")
                    else:
                        answer = np.tan(num)
                        print(f"Your answer is: {answer}")
                elif choice_2 == 7:  # Log
                    num = int(input("What number would you like to log: "))
                    base = int(input("Enter log base: "))
                    answer = np.log(num) / np.log(base)
                    print(f"Your answer is: {answer}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

        # Set Theory Operations
        elif choice == 3:
            try:
                if choice_3 == 1:  # Union
                    array1 = list(map(float, input("Enter first set (space-separated): ").split()))
                    array2 = list(map(float, input("Enter second set (space-separated): ").split()))
                    answer = np.union1d(array1, array2)
                    print(f"The union of the sets is: {answer}")
                elif choice_3 == 2:  # Intersection
                    array1 = list(map(float, input("Enter first set (space-separated): ").split()))
                    array2 = list(map(float, input("Enter second set (space-separated): ").split()))
                    answer = np.intersect1d(array1, array2)
                    print(f"The intersection of the sets is: {answer}")
                elif choice_3 == 3:  # Difference
                    array1 = list(map(float, input("Enter first set (space-separated): ").split()))
                    array2 = list(map(float, input("Enter second set (space-separated): ").split()))
                    answer = np.setdiff1d(array1, array2)
                    print(f"The difference of the sets is: {answer}")
                elif choice_3 == 5:  # Unique Values
                    array1 = list(map(float, input("Enter a set (space-separated): ").split()))
                    answer = np.unique(array1)
                    print(f"The unique values are: {answer}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

        # Statistics Operations
        elif choice == 4:
            try:
                if choice_4 == 1:  # Median
                    array1 = list(map(float, input("Enter an array (space-separated): ").split()))
                    answer = np.median(array1)
                    print(f"The median is: {answer}")
                elif choice_4 == 2:  # Mean
                    array1 = list(map(float, input("Enter an array (space-separated): ").split()))
                    answer = np.mean(array1)
                    print(f"The mean is: {answer}")
                elif choice_4 == 3:  # Mode
                    array1 = list(map(float, input("Enter an array (space-separated): ").split()))
                    answer = stats.mode(array1)
                    print(f"The mode is: {answer.mode[0]}")
                elif choice_4 == 4:  # Standard Deviation
                    array1 = list(map(float, input("Enter an array (space-separated): ").split()))
                    answer = np.std(array1)
                    print(f"The standard deviation is: {answer}")
                elif choice_4 == 5:  # Minimum
                    array1 = list(map(float, input("Enter an array (space-separated): ").split()))
                    answer = np.min(array1)
                    print(f"The minimum value is: {answer}")
                elif choice_4 == 6:  # Maximum
                    array1 = list(map(float, input("Enter an array (space-separated): ").split()))
                    answer = np.max(array1)
                    print(f"The maximum value is: {answer}")
                elif choice_4 == 7:  # Percentile
                    array1 = list(map(float, input("Enter an array (space-separated): ").split()))
                    percentile = float(input("Enter the desired percentile (0-100): "))
                    answer = np.percentile(array1, percentile)
                    print(f"The {percentile}-th percentile is: {answer}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

        # Matrices Operations
        elif choice == 5:
            try:
                if choice_5 == 1:  # Matrix Addition
                    row1 = int(input("Enter number of rows for first matrix: "))
                    col1 = int(input("Enter number of columns for first matrix: "))
                    matrix1 = []
                    print("Enter first matrix values row by row:")
                    for i in range(row1):
                        matrix1.append(list(map(float, input().split())))

                    row2 = int(input("Enter number of rows for second matrix: "))
                    col2 = int(input("Enter number of columns for second matrix: "))
                    matrix2 = []
                    print("Enter second matrix values row by row:")
                    for i in range(row2):
                        matrix2.append(list(map(float, input().split())))

                    if (row1 != row2) or (col1 != col2):
                        print("Error: Matrices must have the same dimensions for addition.")
                    else:
                        result = np.add(matrix1, matrix2)
                        print("The sum of the matrices is:")
                        print(result)
                elif choice_5 == 2:  # Matrix Subtraction
                    row1 = int(input("Enter number of rows for first matrix: "))
                    col1 = int(input("Enter number of columns for first matrix: "))
                    matrix1 = []
                    print("Enter first matrix values row by row:")
                    for i in range(row1):
                        matrix1.append(list(map(float, input().split())))

                    row2 = int(input("Enter number of rows for second matrix: "))
                    col2 = int(input("Enter number of columns for second matrix: "))
                    matrix2 = []
                    print("Enter second matrix values row by row:")
                    for i in range(row2):
                        matrix2.append(list(map(float, input().split())))

                    if (row1 != row2) or (col1 != col2):
                        print("Error: Matrices must have the same dimensions for subtraction.")
                    else:
                        result = np.subtract(matrix1, matrix2)
                        print("The difference of the matrices is:")
                        print(result)
                elif choice_5 == 3:  # Matrix Multiplication
                    row1 = int(input("Enter number of rows for first matrix: "))
                    col1 = int(input("Enter number of columns for first matrix: "))
                    matrix1 = []
                    print("Enter first matrix values row by row:")
                    for i in range(row1):
                        matrix1.append(list(map(float, input().split())))

                    row2 = int(input("Enter number of rows for second matrix: "))
                    col2 = int(input("Enter number of columns for second matrix: "))
                    matrix2 = []
                    print("Enter second matrix values row by row:")
                    for i in range(row2):
                        matrix2.append(list(map(float, input().split())))

                    if col1 != row2:
                        print("Error: Matrices must have compatible dimensions for multiplication.")
                    else:
                        result = np.matmul(matrix1, matrix2)
                        print("The product of the matrices is:")
                        print(result)
                elif choice_5 == 4:  # Determinant of Matrix
                    rows = int(input("Enter number of rows for the matrix: "))
                    cols = int(input("Enter number of columns for the matrix: "))
                    matrix = []
                    print("Enter matrix values row by row:")
                    for i in range(rows):
                        matrix.append(list(map(float, input().split())))

                    if rows != cols:
                        print("Error: Determinant is only defined for square matrices.")
                    else:
                        determinant = np.linalg.det(matrix)
                        print(f"The determinant of the matrix is: {determinant}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    operate()
