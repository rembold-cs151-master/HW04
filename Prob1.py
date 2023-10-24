##################################################
# Name:
# Collaborators:
# Estimate of time spent (hr):
##################################################

def create_histogram_array(imax, data):
    """ Computes a histogram of the entries of data given imax different bins (starting
    from index 0 and going up to imax - 1).

    Inputs:
        imax (integer): number of possible different elements to count
        data (list of integers): the list of data to compute a histogram for
    Outputs:
        (list of integers): the histogram array
    """
    pass # Add your code below and remove this pass!



def print_histogram(array):
    """ Prints the counts of a histogram given by array to the screen. 

    Inputs:
        array (list of integers): a histogram array
    Outputs:
        None
    """
    pass # Add your code below and remove this pass!



def create_histogram_graph(array, width, height):
    """ Creates and returns a GCompound wherein GRects have been used to represent
    the amount in each histogram index.

    Inputs:
        array (list of integers): a histogram array
        width (integer): the desired width of the GCompound
        height (integer): the desired height of the GCompound
    Outputs:
        (GCompound): a single GCompound with the necessary rectangles added
    """
    from pgl import GCompound, GRect
    # Add your code below




def test_create_histogram_graph():
    """ Tests the create_histogram_graph function """
    from pgl import GWindow
    WIDTH, HEIGHT = 800, 600
    gw = GWindow(WIDTH, HEIGHT)
    PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
    array = create_histogram_array(10, PI_DIGITS)
    graph = create_histogram_graph(array, WIDTH, HEIGHT)
    gw.add(graph)






if __name__ == '__main__':
    # Some testing printouts for your use!
    PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
    array = create_histogram_array(10, PI_DIGITS)
    print(array)
    # print_histogram(array) # uncomment once you have defined print_histogram
    # test_create_histogram_graph() # uncomment once you have defined create_histogram_graph

