import random 
import time 
import matplotlib.pyplot as plt 
import sys

"""
Name:Kiefer Gallant

Lab #2

Description: This program consists of a timer class that 
will be used in the benchmark class that times functions, 
it will also create a dotproduct function. It also creates 
two trace functions that are benchmarked and plotted
on a graph using matplotlib

**** The graphing takes 2-3 minutes to complete ****

"""

#-------------------------------------------------------------------------#
# This progress bar is adpated from the following post and 
# tracks the progress of the benchmarking of the data
#https://stackoverflow.com/questions/3160699/python-progress-bar

def progressbar(it, prefix="", size=60, out=sys.stdout): # Python3.3+
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}/{}".format(prefix, "#"*x, "."*(size-x), j, count), 
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)

#-------------------------------------------------------------------------#



# Question 1 

class Timer:
    
    def __init__(self):
        """
        Description: This initalizes a timer object
        Parameters: 
        Return: timer object
        """
        self._startTime = time.time()
        self._endTime = None

    def reset(self):
        """
        Description: This fuction restarts the timer 
        Parameters: 
        Return: 
        """
        self._startTime = time.time()
        self._endTime = None

    def elapsed(self):
        """
        Description: This calculates the time elapsed since the
        timer was started or reset
        Parameters: 
        Return: float - elapsed time
        """
        self._endTime = time.time()
        return  self._endTime - self._startTime 

def dotProduct(A,B):
    """
    Description: This calculates the dot product of two lists
    of floats
    Parameters: A,B - lists of floats
    Return: Dot product of the two lists
    """
    dot_product_total_sum = 0
    for i in range(len(A)):
        a_list_value = A[i]
        b_list_value = B[i]
        total = a_list_value * b_list_value
        dot_product_total_sum += total            
    return dot_product_total_sum

def create_random_lists(n):
    """
    Description: Creates lists of size n and fills it with 
    random floats from -100 to 100
    Parameters: n - integer , lengths of lists 
    Return: A,B - two lists full of random floats
    from -100 to 100
    """
    A = []
    B = []
    for num in range(n+1):
        A.append(random.uniform(-100,100))
        B.append(random.uniform(-100,100))
    return (A,B)

A,B = create_random_lists(10**4)
C,D = create_random_lists(10**5)
E,F = create_random_lists(10**6)

t = Timer()
dotProduct(A,B)
print(t.elapsed())
t.reset()


t = Timer()
dotProduct(C,D)
print(t.elapsed())
t.reset()


t = Timer()
dotProduct(E,F)
print(t.elapsed())
t.reset()

#Question 2

class Benchmark:
    """
    Description: This class will create a framework to benchmark 
    the times for various functions 
    """
    def __init__(self,_fName:str=None,_nLow:int = 1,_nHigh:int = 4):
        """
        Description: Initializes the benchmark object
        Parameters: fName - function name to benchmark
                    _nLow - lower boundry exponent power
                    _nHigh - upper boundry exponent power   
        Return: Benchmark object 
        """
        self._fName = _fName
        self._nLow = _nLow
        self._nHigh = _nHigh
        self._nSize = []
        self._time = []

    def determineSizeData(self):
        """
        Description: Creates a list with the different sizes of 
        data
        Parameters:    
        Return: _nSize - a list full of integers of the different
        sizes of data
        """
        self._nSize = [10**num for num in range((self._nLow),(self._nHigh+1))]    
        return self._nSize

    def createMatrixVariable(self,n:int,vlow:float,vhigh:float):
        """
        Description: Creates multi dimensional list of floats (nxn)
        with elements randomly genereated in the vlow to vhigh
        Parameters: n - size of matrix
                    vlow - lower boundary for the random float
                    vhigh - upper boundary for the random float 
        Return: returns a nxn matrix full of random floats 
                ranging from vlow to vhigh 
        """
        matrix = []
        # Part of the loading bar in terminal 
        for i in progressbar(range(n), "Computing: ", 40):
            matrix.append([random.uniform(vlow,vhigh) for j in range(n)])
        return matrix

    def runBenchMarkData(self,vlow:float,vhigh:float):
        """
        Description: Runs the function with the random matrix data
        and times how long it will take with each data set
        Parameters: vlow - lower boundary for the random floats inside 
                    the matrix
                    vhigh - upper boundary for the random floats inside 
                    the matrix 
        Return: 
        """
        t = Timer()
        for dataSize in self._nSize:
            matrix = self.createMatrixVariable(dataSize,vlow,vhigh)
            t.reset()
            self._fName(matrix)
            time_elapsed = t.elapsed()
            self._time.append(time_elapsed)
            
    def getBenchMarkData(self):
        """
        Description: returns the benchmarking data in a tuple 
        Parameters:
        Return: _nsize - various sizes of data to test
                _time - time benchmarking data for various sizes
        """
        return (self._nSize,self._time)

    def plotGraph(self):
        """
        Description: Plots the graphs and creates the axis's labels
        titles and legend  
        Parameters: 
        Return: 
        """
        plt.plot(self._nSize,self._time,marker="X")
        plt.yscale('log')
        plt.xscale('log')
        plt.xlabel("Data Size (n)")
        plt.ylabel("Time (s)")
        plt.title("Lab# 2 Question 3 \n Log-Log Plot of Data Size vs. Time")
        plt.legend(["Trace Method 1","Trace Method 2"])
        
#Question 3

def trace_method_one(matrix):
    """
    Description: Calculates the trace of a matrix and returns it 
    Parameters: matrix - nxn matrix
    Return: Sum of the trace of a matrix
    """
    trace_sum = 0
    for row_number in range(len(matrix)):
        for column_number in range(len(matrix)):
            if row_number == column_number:
                trace_sum+= matrix[row_number][column_number]
    return trace_sum

def trace_method_two(matrix):
    """
    Description: Calculates the trace of a matrix and returns it 
    Parameters: matrix - nxn matrix
    Return: Sum of the trace of a matrix
    """
    trace_sum = 0
    for i in range(len(matrix)):
        trace_sum+= matrix[i][i]
    return trace_sum



def main():
    a = Benchmark(trace_method_one)
    b = Benchmark(trace_method_two)

    a.determineSizeData()
    b.determineSizeData()

    a.runBenchMarkData(1,5)
    b.runBenchMarkData(1,5)

    a.plotGraph()
    b.plotGraph()

    plt.show()


main()







