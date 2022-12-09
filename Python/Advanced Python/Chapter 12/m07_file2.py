# In this file __name__ will have value "m06_file1" 
#### OR ####
# If the module is being run directly from the command line, the __name__ is set to string “__main__”
import m06_file1   # import statement takes and executes the entire program of that module, so if we want to import only functions then in that module's code we give this condition as an entry point "if __name__ == '__main__':"
m06_file1.greet("Harry")   