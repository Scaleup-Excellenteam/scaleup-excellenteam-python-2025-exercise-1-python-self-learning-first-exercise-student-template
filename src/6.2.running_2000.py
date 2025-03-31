import time
def running_2000(func,*parameters,**kwargs):
    """
        Measures the time taken to execute a given function with the specified parameters and keyword arguments.

        Parameters:
        func (function): The function to execute.
        *parameters: The positional arguments to pass to the function.
        **kwargs: The keyword arguments to pass to the function.

        Returns:
        float: The time taken to execute the function in seconds.
        """
    # Record the start time of the function execution
    start_time=time.time()
    # Call the function with the passed parameters and keyword arguments
    func(*parameters,**kwargs)
    end_time=time.time()
    # Calculate the time taken to execute the function
    the_time=end_time-start_time
    return the_time



def main():
   print(running_2000(print, "Hello"))
   print(running_2000(zip, [1, 2, 3], [4, 5, 6]))
   print(running_2000("Hi {name}".format, name="Bug"))



if __name__ == "__main__":
    main()