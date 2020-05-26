from cs103 import *
from typing import NamedTuple, List, Optional
import csv
import numpy as np
from scipy.stats import linregress
from scipy import stats

LinregressResult = NamedTuple('LinregressResult', [('slope',float),
                                                   ('intercept',float),
                                                   ('rvalue',float),
                                                   ('pvalue',float),
                                                   ('stderr',float)])
#interp. The output values from the regression analysis done on the graph 
#includes slope(the slope of the line of best fit), intercept(mean y value at x=0), r-value(Coefficient of Correlation),
# p-value(relates to null hypothesis and stderr( the standard error)

L1=LinregressResult(slope=0.009229976186394427, intercept=8.189871851812939,
rvalue=0.5289714375338503, pvalue=0.00011096338597135931, stderr=0.0021832966579997553)

L2= LinregressResult(slope=0.7252747252747253, intercept=3.27992888127114,
rvalue=0.34979523, pvalue=0.022610223, stderr=1.52186398636788)

@typecheck
def fn_for_LinregressResult(lin: LinregressResult)->...:
    #template based on compound(5 fields)
    return...(lin.slope,
             lin.intercept,
             lin.rvalue,
             lin.pvalue,
             lin.stderr)

# optional[int]
#interp. for dealing with revenue cells that lack data. Either an integer or a None value

OP1 = None
OP2 = 32000

# template based off of Optional
@typecheck
def fn_for_oi(oi:Optional[int])->...:
    
    if oi is None:
        return ...
    else:
        return ...(oi)
             






Campus = Optional[str]
# interp. The campus of the specific University
# if campus field is blank it means the university doesnt have multiple campuses, None will be displayed
# if there is a string present then it will be the output

A1 = None
A2 = "Stanislaus"
A3 = "San Jose"

@typecheck
def fn_for_campus(p:str) -> ...:
    # template based on Optional and reference rule
    if a is None:
        return ...
    else:
        return ...(p)
    
CrimeStatistics = NamedTuple("CrimeStatistics",[("university",str),
                                                ("campus",Campus),
                                                ("enrollment",int), # in range [0,...]
                                                ("violent_crimes",int),# in range [0,...]
                                                ("property_crimes",int), # in range [0,...]
                                                ("arson",int)]) # in range [0,...]
#interp, an individual university's enrollment and campus crime statistics
#    university is the main name of the institution
#    campus is the specific branch of the university and an optional[str]
#    enrollment is the total number of students attending
#    violent crimes comprises total number of: Murder and nonnegligent manslaughter, Rape, Robbery, Aggravated assault
#    property crimes comprises total number of: Burglary, Larceny-theft, Motor vehicle theft 
#    arson represents all arson crimes commited


U1 = CrimeStatistics("California State University","Fresno",23179,13,267,1)
U38 = CrimeStatistics("University of California", "Hastings College of law",1003,19,40,0)

@typecheck
def fn_for_crime(cs:CrimeStatistics)->...:
    #template based on compound(6 fields)
    return ...(cs.university, #str
              cs.campus,      #optional[str]
              cs.enrollment, #int in range [0,...]
              cs.violent_crimes, #int in range [0,...]
              cs.property_crimes, #int in range [0,...]
              cs.arson) #int in range [0,...]

# List[CrimeStatistics]
# interp. a list of universities coupled with their crime numbers
# items on the list each contain all 6 fields from CrimeStatistics compound data

LOC0 = []
LOC1 = [U1,U38]

# template based on arbitrary-sized and the reference rule
@typecheck
def fn_for_cr(loc: List[CrimeStatistics]) -> ...:
    # description of accumulator
    acc = ... # type:...
    for cs in loc:
        ...(acc, fn_for_crime(cs))
    return ...(acc)

import matplotlib.pyplot as plt
from matplotlib import pyplot

@typecheck
def main(filename: str) -> None:
    """
    Reads the Crime statistics from given filename, analyzes the data, 
    and returns a scatterplot of student enrollment and overall crime numbers
    """
    # Template from HtDAP, based on composition 
    return scatterplot(read(filename)) 


@typecheck
def read(filename: str)-> List [CrimeStatistics]:
    """
    Reads information from provided file and returns
    a list of Universities with their name,campus((None) if no string in this field)
    and crime statistics(3 categories).
    """
    #return [] #stub
    # Template from htDAP
    
    #loc contains all results read so far
    loc = [] #type List[CrimeStatistics]
    
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        
        
        for row in reader:
            university = row[0].replace("4", "")
            campus = parse_campus(row[1])
            enrollment = parse_int(row[2].replace(",", ""))
            violent_crimes = parse_int(row[3])
            property_crimes = parse_int(row[8])
            arson = parse_int(row[12])
            
            if valid(enrollment):
                cs = CrimeStatistics(university,
                                    campus,
                                    enrollment,
                                    violent_crimes,
                                    property_crimes,
                                    arson)
                
                loc.append(cs)
    return loc
    

@typecheck
def scatterplot(loc: List[CrimeStatistics]) -> None: 
    """ 
    Creates a scatterplot of student enrollment(x) and total
    crimes commited(y),returns None
    """ 
    # return None #stub
    #template based on visualization
    
    x = enrollment_list(loc)
    y = crime_list(loc)
    
    
    pyplot.scatter(x,y)
    pyplot.xlabel("Enrollment")
    pyplot.ylabel("Total crime per campus")
    pyplot.title("correlation between enrollment and crimes committed")
    
        
    
    pyplot.show()
    print(linregress(x,y))
    
    
    return None



#campus data helper
@typecheck
def parse_campus(p: str) -> Campus:
    """
    If campus field is empty, returns None else returns the present string
    """
    # return '' #stub
    #template from optional
    if p is '':
        return None
    else:
        return p

    
@typecheck
def enrollment_list(loc:List[CrimeStatistics])->List[int]:
    """
    From a given file returns a list of enrollment numbers per university
    """
    # return [] #stub
    # template from List[CrimeStatistics]
    # enrollments is all enrollment values seen so far
    enrollments = [] # type: List[int]
    
    for cs in loc:
        enrollments.append(cs.enrollment)
    return enrollments

@typecheck
def crime_list(loc:List[CrimeStatistics])->List[int]:
    """
    from a given file returns a list of the sum of the three crime categories for each university
    """
    # return [] #stub
    #template from List[CrimeStatistics]
    # crime_count is all the seperate university total crimes seen so far
    crime_count = [] #type: List[int]
    for cs in loc:
        crime_count.append(sum_crimes(cs))
    return crime_count

@typecheck
def sum_crimes(cs:CrimeStatistics)-> int:
    """
    returns the sum of all three crime categories for each university
    """
    # return 0 # stub
    #template from atomic
    crimes_total = (cs.violent_crimes+cs.property_crimes+cs.arson)
    return crimes_total


@typecheck
def valid(rv:Optional[int])->bool:
    """
    Identifies if a revenue row is empty or has an integer present.
    If None returns false if int returns true
    """
    # return False # stub
    # template from optional
    if rv is None:
        return False
    else:
        return True
    
   


    start_testing()
expect(main("california_crime_by_campus.csv"),None)
#should produce a graph of all data with printed regression analysis
expect(main("multiple schools.csv"),None)
#should produce 3 data points and print the regression analysis for them

#test for read
expect(read("csu san jose.csv"),[CrimeStatistics(university='California State University', campus='San Jose', 
enrollment=32713, violent_crimes=29, property_crimes=442, arson=1)])

expect(read("multiple schools.csv"),
[CrimeStatistics(university='California State University', campus='Stanislaus', enrollment=9045, violent_crimes=2, property_crimes=72, arson=0), 
CrimeStatistics(university='College of the Sequoias', campus=None, enrollment=10647,violent_crimes=4, property_crimes=70, arson=0), 
CrimeStatistics(university='Contra Costa Community College',campus=None, enrollment=35481, violent_crimes=3, property_crimes=194, arson=1)
])

#tests for parse_campus
expect(parse_campus(''),None)
expect(parse_campus("San Bernardino"),"San Bernardino")
expect(parse_campus("Sacramento"),"Sacramento")
#tests for enrollment
expect(enrollment_list(LOC0),[])
expect(enrollment_list(LOC1),[23179,1003])
#tests for total_crimes
expect(crime_list(LOC0),[])
expect(crime_list(LOC1),[281,59])
#tests for sum_crimes
expect(sum_crimes(U1),281)
expect(sum_crimes(U38),59)



summary()
