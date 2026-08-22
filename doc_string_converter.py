import inspect
import Luis_ProgrammingExercise_1  # replace with your assignment name (without .py)

#replace docstring_example with your assignment name in the next 2 lines of code
with open("Luis_ProgrammingExercise_1_design_doc.txt", "w") as doc:
    doc.write(f"# Technical Design Document: {Luis_ProgrammingExercise_1.__name__}\n\n")
    #replace with your name, the date, and the description of the program
    doc.write(f"# Name: Luis Calel De Leon\n")
    doc.write(f"# Date: August 22, 2026\n")
    doc.write(f"# Program Description: This program will ask user how many tickets they want, check if"
              f"its within limit and valid, and run until all tickets are sold out.\n\n")

    #replace docstring_example with your assignment name 
    for name, func in inspect.getmembers(Luis_ProgrammingExercise_1, inspect.isfunction):
        doc.write(f"## Function: {name}\n")
        doc.write(f"{inspect.getdoc(func)}\n\n")
    
    #replace with link to your repository
    doc.write(f"#Link to your repository: https://github.com/alex23442/COP2373.git")
print('Complete')