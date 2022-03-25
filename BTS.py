def BTS(suduko,constraints,domain,assigned_var,fixed_cells):
    alphabet = ['A','B','C','D','E','F','G','H','I']
    number = ['1','2','3','4','5','6','7','8','9']
    # Check if assignment is complete & correct
    output = True
    for i in suduko:
        if suduko[i] == 0:
            output = False
            break

    if output == True:
        final_array = ''
        for i in suduko:
            val = suduko[i]
            final_array = final_array + str(val)
        return(final_array)
    
    # Check if assignment is complete & incorrect
    output = True
    for i in domain:
        if len(domain[i]) == 0:
            output = False
            break

    if output == False:
        return('Failure')

    # Assignment is incomplete.
        
    # Iterate over all domain values of the cell with smallest domain
    cell = None
    length = math.inf
    for i in domain:
        if len(domain[i]) < length:
            if (i not in assigned_var) and (i not in fixed_cells):
                cell = i
                length = len(domain[i])
                
    Domain_cell = domain[cell]
        
    for i in Domain_cell:
        constraints_i = constraints[cell]
        output = True
            
        for j in constraints_i:
            if suduko[j] == i:
                output = False
                break
            
        # if value consistent with assignment
        if output == True:
            suduko[cell] = i
            assigned_var.append(cell)
            neighbor_removed = list() # List of neighbors from which value was removed
            
            # Forward checking (Remove the added value from domain of neighbours)
            for j in constraints_i:
                domain_neighbor = domain[j]
                if i in domain_neighbor:
                    index = domain_neighbor.index(i)
                    domain_neighbor.pop(index)
                    domain[j] = domain_neighbor
                    neighbor_removed.append(j)
    
            # Recursively add values to suduko
            result = BTS(suduko,constraints,domain,assigned_var)
                
            if result != 'Failure':
                return(result)
                
            # Re-add old values to domain of neighbours
            suduko[cell] = 0
            index = assigned_var.index(cell)
            assigned_var.pop(index)
            for j in neighbor_removed:
                domain_neighbor = domain[j]
                domain_neighbor.append(i)
                domain[j] = domain_neighbor
                              
    return('Failure')