def AC3(suduko,constraints,domain,fixed_cells):
    alphabet = ['A','B','C','D','E','F','G','H','I']
    number = ['1','2','3','4','5','6','7','8','9']
    while len(constraints) != 0:
        (X,Y) = constraints.pop(0)
        truth,domain = Revise(suduko,constraints,domain,X,Y)
        if truth == True:
            Domain_X = domain[X]
            if len(Domain_X) == 0:
                return(False)
            
            # Since domain of X changed, need to check (neighbors(X) except Y, X) pairs again.
            letter, num = list(X)
            letter_1, num_1 = list(Y)
        
            # Same row constraint
            for j in number:
                if j != num and j != num_1:
                    pair = (letter + j, X)
                    if pair not in constraints:
                        constraints.append(pair)

            # Same column constraint
            for j in alphabet:
                if j != letter and j != letter_1:
                    pair = (j + num, X)
                    if pair not in constraints:
                        constraints.append(pair)

            # Same box constraint
            start_letter = math.floor(alphabet.index(letter)/3)*3
            start_number = math.floor(number.index(num)/3)*3

            # Within the range of the box
            for j in range(start_letter,start_letter + 3):
                for k in range(start_number,start_number + 3):
                    new_val = alphabet[j] + number[k]
                    if new_val != X and new_val != Y:
                        pair = (alphabet[j] + number[k], X)
                        if pair not in constraints:
                            constraints.append(pair)
    
    output = True
    # Check whether there is only 1 domain value for each variable
    for j in domain:
        Domain_arr = domain[j]
        if len(Domain_arr) != 1:
            output = False
            break
            
    if output == True:
        output = ''
        for j in domain:
            val = domain[j][0]
            output = output + str(val)

    return(output)        