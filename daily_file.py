# !/bin/python3
"""
function now works to match any pattern that has an integrated datestamp.

main thing is the day_stamp_name - it is the generalized method to handle what we want.


Originally: Utility to capture the geics file - it might be easier to build a framework since we know
the origins of most of the files....

defines a "Type_Exception" here - I may make a new supplemental module specifically for type exceptions

.-- .... .- -
.- .-. .
-.-- --- ..-
.-.. --- --- -.- .. -. --.
.- -
... ..- -.- .- ..--..

Public version of the daily_file

"""

import time;
import datetime;
import ftplib; # might as well use the built in ftp library for this, better than using the external mechanism.
from shutil import copy as cp ; # I like the shorthand.


class TypeException(Exception):
    """
    Exception classification to be raised on the improper type of data being passed.
    """
    pass
    # loads the default __init__ method - I could attempt to initialize this one with
    # additional fields to be more descriptive...
    

    
def day_stamp_name(as_of_date = None, format_string = "", date_diff = 0):
    """
    generalized date stamp function - need to use a format string (see strftime()) 
    format string, and difference in date - should be a signed integer.
    
    This general form is much nicer than having an individual definition for each file.
    """
    # since this component is dynamic it must be handled here.
    as_of_date = as_of_date or datetime.datetime.now();
    if type(as_of_date) == tuple and as_of_date.len>0:
        s = as_of_date;
        as_of_date = s[0]
        if s.len>1: format_string = s[1]
        if s.len>2: date_diff = s[2]
        # might allow use in some more... creative ways.
    try:
        pass;
        if type(as_of_date)==datetime.datetime:
            as_of_date = as_of_date.toordinal();
        elif type(as_of_date) in (float,int):
            as_of_date = as_of_date; # leave it alone
        else: raise TypeException("as_of_date appears to be of an incompatible type. please use a datetime.datetime, int, or float.")
        as_of_date = as_of_date+date_diff
        as_of_date = datetime.datetime.fromordinal(as_of_date).strftime(format_string);
    except TypeException as excepttt:
        raise TypeException(excepttt); # that will be the type exception - break the process.
    except Exception as exceptt:
        pass;
        raise Exception(exceptt);
    return as_of_date;

def main( arg=None ):
    """
    """
    pass
        
if __name__!="__main__":
    print("imported daily_file.py")
