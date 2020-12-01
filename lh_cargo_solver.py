import pandas as pd
import itertools

def lh_cargo_solver(numbers_on_left_side, number_on_right_side): 
    output_equation = '?'
    equations = pd.DataFrame()
    operators = ['+','-','*','/']

    for i in range(len(numbers_on_left_side)):
        old_list = []
        
        try:
            if isinstance(numbers_on_left_side[i+1], int): # operator will be appended only if there is one more value on left side
                for o in range(len(operators)):
                    old_list.append(str(numbers_on_left_side[i])) #+ str(operators[o]))

        except IndexError:
            for o in range(len(operators)):
                old_list.append(str(numbers_on_left_side[i]))

        equations[str(i)] = old_list

        if output_equation == number_on_right_side:
            print('yes')
    
    no_of_iterations = 4 ** (len(numbers_on_left_side)-1)
    print(no_of_iterations)

    equations_new = pd.DataFrame()
    for i in range(no_of_iterations):
        equations_new = equations_new.append(equations.head(1))
        
    #print(equations_new)

    # insert the operators  
    operator_list = create_operators(len(numbers_on_left_side)-1)
    #print(my_set)

    """
    a = equations_new.head(1)['0'] + operator_list[5][0] #6+
    b = equations_new.head(1)['1'] + operator_list[5][1] #6-
    c = equations_new.head(1)['2'] + operator_list[5][2] #4-
    d = equations_new.head(1)['3'] #2
    tbe = a[0] + b[0] + c[0] + d[0]
    """    

    for item in range(len(operator_list)):
        test_equation = ""
        for col in range(len(equations_new.columns)):
            if col < len(operator_list[1]):
                # all rows are equal.... so 
                test_equation += equations_new.head(1)[str(col)] + operator_list[item][col]
            else:
                test_equation += equations_new.head(1)[str(col)]
        
        # conversion from pandas Series to string includes index and blanks
        if eval(test_equation.to_string()[5:]) == number_on_right_side:
            print('evaluation result: ', test_equation)            
        #    return test_equation
            
    return operator_list, equations_new

def create_operators(required_no):
    i=0
    somelist=[]
    l = ['+', '-', '*', '/'] 
    operator_set = []
    for j in range(required_no): # * 2 = 16; * 3 = #64; *4 = 256, ...
        somelist.append(l)
    
    # cartesian product
    for element in itertools.product(*somelist):
        i+=1
        operator_set.append(element)
    print(i)
    return operator_set

left_side = [6,6,4]
res = lh_cargo_solver(left_side, 4)
