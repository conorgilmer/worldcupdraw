
###############################################################################
# Tasks
# 1 - Create a seedings set
# 2 - Anlayse Data
# 3 - Create Report
###############################################################################

###############################################################################
# CONSTANTS
# - these are the fields in the data file
###############################################################################

EURORANK  = "European Ranking"
FIFARANK  = "World Ranking"
COUNTRY   = "Country"
POINTS    = "Points"
POT       = "Pot"
GROUP     = "Group"

###############################################################################
# 1. Create a seedings set
# - Read in file
# - Create a dictionary for each line
# - Add this dictionary to a list
#
###############################################################################
def createSeedingsSet(filename):
    # read in Data to a Set 
    dataSet = []

    fin = open(filename,'r')

    # Read in file
    for line in fin:
        line = line.strip()
        line_list = line.split(',')
        # Create a dictionary for the line
        record = {}
	record[EURORANK]    = line_list[0]
	record[FIFARANK]    = line_list[1]
	record[COUNTRY]     = line_list[2]
	record[POINTS]      = line_list[3]
	record[POT]         = line_list[4]
	record[GROUP]       = line_list[5]

        # Add the dictionary to a list
        dataSet.append(record)        

    fin.close()
    print "Seedings Set Populated"
    # return the Set 
    return dataSet


###############################################################################
# 2. analyseGroups
###############################################################################
def analyseGroups(dataSet, grp):
    print "\nAnalyse Group " + grp 
    anSet   = []
    points  = 0
    euroavg = 0
    fifaavg = 0
    teams   = 0
#    print dataSet
    for line in dataSet:
        record = {}
	record = line
	if record[GROUP] == grp:
	    print record[COUNTRY]
	    teams   = teams + 1
	    points  = points + int(record[POINTS])
	    euroavg = euroavg + int(record[EURORANK])
	    fifaavg = fifaavg + int(record[FIFARANK])
    print "There are %d teams in the group" % teams
    print "There total %d points of the group" % points
    euroavg = euroavg/teams
    fifaavg = fifaavg/teams
    print "There avg European Ranking of the group is %d" % euroavg 
    print "There avg World Ranking of the group is %d" % fifaavg

    anSet = dataSet
    return anSet


###############################################################################
# 3. Generate Report
# 
###############################################################################
def generateReport(filename, dataSet):

    print "Generating Report" 


###############################################################################
# main - starts the program
###############################################################################
def main():

    # Read in Data
    print "Read in seedings."
    seedingsSet = []
    reportSet = []
    groups = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    seedingsFile = "seedings.csv"
    reportFile = "output.rep"
    seedingsSet = createSeedingsSet(seedingsFile)
    print "Seedings read in.\n"

    # Analyse Data 
    print "Calculate Group Toughness"    
    # call analyseGroups(seedingsSet);
    for gp in groups:
        reportSet = analyseGroups(seedingsSet, gp);
    print "Done Analysing Group.\n"

    # Write Report
    print "Write Report"
    generateReport(reportFile, reportSet);
    print "Done Writing Report.\n"

    # add call to appropriate function

    print "Program finished."
    
main()
