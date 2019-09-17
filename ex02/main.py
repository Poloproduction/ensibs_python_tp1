import sys
import re
from math import sqrt

def main(line):
    """
    Compute square root of a number.

    @param line: line readed from file containing a float
    @type line: string
    @raise Exception: if BAD INPUT
    @return value
    @rtype float
    """
    if(re.match(r'^[0-9]*\.[0-9]*$', line) and (line != '.')):
        #TODO: Should we block int ? (we did here)
        try:
            value = float(line)
            return sqrt(value)
        except:
            raise Exception(200, "BAD INPUT: Failed casting to float")
    else:
        raise Exception(100, "BAD INPUT: Not a float")


if __name__ == "__main__":
    if(len(sys.argv) > 1):
        try:
            f = open(sys.argv[1], "r")
        except:
            print("Error while opening file")
        for line in f.readlines():
            try:
                result = main(line.strip())
            except Exception as exception :
                error_code = exception.args[0]
                error_msg = exception.args[1]
                print(error_msg + ', error code : ' + str(error_code))
            else :
                print("Square root = " + str(result))
    else:
        print("Error: you must enter file name")