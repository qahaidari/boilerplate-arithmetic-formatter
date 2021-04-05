def arithmetic_arranger(problems, solution):
  
  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""
  if len(problems) > 5:
    print("Error: Too many problems.")
    exit()

  for problem in problems:
    items = problem.split()
    
    operand1_str = items[0]
    operator = items[1]
    operand2_str = items[2]

    if not (operator == "+" or operator == "-"):
      print("Error: Operator must be '+' or '-'.")
      exit()
  
    try:
      operand1 = int(operand1_str)
      operand2 = int(operand2_str)
    except:
      print("Error: Numbers must only contain digits.")
      exit()

    width1 = len(operand1_str)
    width2 = len(operand2_str)
    
    if (width1 > 4) or (width2 > 4):
      print("Error: Numbers cannot be more than four digits.")
      exit()

    ralign = max(width1, width2) + 2
   
    line1 += operand1_str.rjust(ralign) + "    " 

    if operator == "+":
      result = operand1 + operand2
      line2 += operator + operand2_str.rjust(ralign - 1) + "    "
    elif operator == "-":
      result = operand1 - operand2
      line2 += operator + operand2_str.rjust(ralign - 1) + "    "
    
    # dashes
    dashes = ""
    for i in range(ralign):
      dashes += "-" 
   
    line3 += dashes.rjust(ralign) + "    "
    if solution == True:
      line4 += str(result).rjust(ralign) + "    "
  
  if solution == True:
    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()
    line4 = line4.rstrip()
    arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
  else:
    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()
    arranged_problems = line1 + '\n' + line2 + '\n' + line3

  return arranged_problems
