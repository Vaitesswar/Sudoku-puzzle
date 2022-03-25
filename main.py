import numpy as np
import pandas as pd
import math
from AC3 import AC3
from BTS import BTS

def main(input_string):
    # Prepare the dictionary representing position of values in sudoku
    alphabet = ['A','B','C','D','E','F','G','H','I']
    number = ['1','2','3','4','5','6','7','8','9']
    cell_values = [int(d) for d in input_string]
    suduko = {}
    fixed_cells = list() # Fixed cells should not have constraints
    all_cells = list()

    i = 0

    for j in alphabet:
        for k in number:
            key = j + k
            val = int(cell_values[i])
            suduko[key] = val
            if val != 0:
                fixed_cells.append(key)
            all_cells.append(key)
            i += 1

    # Finding all possible constaints
    constraints = list()

    for i in all_cells:
        if i not in fixed_cells: # A fixed cell only has 1 constraint which is itself.
            letter, num = list(i)

            # Same row constraint
            for j in number:
                if j != num:
                    pair = (i,letter + j)
                    constraints.append(pair)

            # Same column constraint
            for j in alphabet:
                if j != letter:
                    pair = (i, j + num)
                    constraints.append(pair)

            # Same box constraint
            start_letter = math.floor(alphabet.index(letter)/3)*3
            start_number = math.floor(number.index(num)/3)*3

            # Within the range of the box
            for j in range(start_letter,start_letter + 3):
                for k in range(start_number,start_number + 3):
                    new_val = alphabet[j] + number[k]
                    if new_val != i:
                        pair = (i, alphabet[j] + number[k])
                        if pair not in constraints:
                            constraints.append(pair)

    # Finding the domains for each variable (allowable values)
    domain = {}

    for i in all_cells:
        if i not in fixed_cells:
            domain[i] = [1,2,3,4,5,6,7,8,9]
        else:
            domain[i] = [suduko[i]]

    output = AC3(suduko,constraints,domain,fixed_cells)
    if output != False:
        file = open("output.txt","w") 
        file.write(output + " " + "AC3")
        file.close()  
    else:
        # Prepare the dictionary representing position of values in sudoku
        alphabet = ['A','B','C','D','E','F','G','H','I']
        number = ['1','2','3','4','5','6','7','8','9']
        cell_values = [int(d) for d in input_string]
        suduko = {}
        constraints = {}
        fixed_cells = list() # Fixed cells should not have constraints
        all_cells = list()

        i = 0

        for j in alphabet:
            for k in number:
                key = j + k
                val = int(cell_values[i])
                suduko[key] = val
                if val != 0:
                    fixed_cells.append(key)
                all_cells.append(key)
                constraints[key] = [] # Different from AC3
                i += 1

        # Finding all possible constaints

        for i in all_cells:
            if i not in fixed_cells: # A fixed cell only has 1 constraint which is itself.
                letter, num = list(i)
                constraints_i = constraints[i]

                # Same row constraint
                for j in number:
                    if j != num:
                        neighbor = letter + j
                        constraints_i.append(neighbor)

                # Same column constraint
                for j in alphabet:
                    if j != letter:
                        neighbor = j + num
                        constraints_i.append(neighbor)

                # Same box constraint
                start_letter = math.floor(alphabet.index(letter)/3)*3
                start_number = math.floor(number.index(num)/3)*3

                # Within the range of the box
                for j in range(start_letter,start_letter + 3):
                    for k in range(start_number,start_number + 3):
                        neighbor = alphabet[j] + number[k]
                        if neighbor != i:
                            if neighbor not in constraints_i:
                                constraints_i.append(neighbor)

                constraints[i] = constraints_i

        # Use domain from AC3

        assigned_var = []
        output = BTS(suduko,constraints,domain,assigned_var,fixed_cells)

        file = open("output.txt","w") 
        file.write(output + " " + "BTS")
        file.close()  
        
if __name__ == "__main__":
    input_string = sys.argv[1]
    main(input_string)