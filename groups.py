
###############################################################################
# groups.py
# 
# by Conor Gilmer
# 
# Calcualte the "toughness" of the groups based on seedings and points  
# 
# Tasks
# 1 - Create a seedings set from seedings csv file
# 2 - Anlayse Data
# 3 - Create Report/Write to file
###############################################################################

###############################################################################
# IMPORTS
###############################################################################
import decimal

###############################################################################
# CONSTANTS
# - these are the fields in the data file
###############################################################################

# Input File Headings 
EURORANK  = "European Ranking"
FIFARANK  = "World Ranking"
COUNTRY   = "Country"
POINTS    = "Points"
POT       = "Pot"
GROUP     = "Group"

# Report Headings
TEAMS      = "Teams"
TPOINTS    = "Total Points"
AVGEU      = "Avg Euro Rank"
AVGWC      = "Avg World Rank"
AVGPP      = "Avg Pot Position"

###############################################################################
# round a float to 2 decmials and return it as a String
###############################################################################
def roundToTwo(num):
    number = 0.0
    number = round(num,2)
    return str(number)

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
# - calculate points sum, avg rankings
# - save stats to set and return
###############################################################################
def analyseGroups(dataSet, grp):
    print "\nAnalyse Group " + grp 
    points      = 0
    euroavg     = 0.0
    fifaavg     = 0.0
    teams       = 0
    potposavg   = 0.0
    # print dataSet
    for line in dataSet:
        record = {}
	record = line
	if record[GROUP] == grp:
	    potpos = int(record[EURORANK]) - (9 * teams)
	    print "%s %d" % (record[COUNTRY],  potpos)
	    teams   = teams + 1
	    points  = points + int(record[POINTS])
	    euroavg = euroavg + int(record[EURORANK])
	    fifaavg = fifaavg + int(record[FIFARANK])
	    potposavg = potposavg + potpos
    print "Teams \t \t\t%d" % teams
    print "FIFA Points\t\t%d" % points
    euroavg = euroavg/teams
    fifaavg = fifaavg/teams
    potposavg = potposavg/teams
    print "Avg. Euro Ranking  \t %.2f" % euroavg 
    print "Avg. World Ranking \t %.2f" % fifaavg
    print "Avg. Pot Position  \t %.2f" % potposavg
    # save group stats record
    outputRecord          = {}
    outputRecord[GROUP]   = grp
    outputRecord[TEAMS]   = teams
    outputRecord[TPOINTS] = points
    outputRecord[AVGEU]   = euroavg
    outputRecord[AVGWC]   = fifaavg
    outputRecord[AVGPP]   = potposavg
    return outputRecord


###############################################################################
# 3. Generate Report
# - print report
# - write report to file 
###############################################################################
def generateReport(filename, dataSet):

    print "Generating Report" 

    fout = open(filename,'w')
    title = "World Cup Qualifying Draw";
    fout.write(title + "\n");
    headings = GROUP + "\t" + TEAMS + "\t"+ TPOINTS+"\t"+AVGEU+ "\t"+ AVGWC + "\t" + AVGPP
    fout.write(headings + "\n")
    print title
    print headings
    for line in dataSet:
        record = {}
	record = line
	#print record
	strg = str(record[GROUP]) + "\t" + str(record[TEAMS]) +"\t"+ str(record[TPOINTS])+ "\t\t"+roundToTwo(record[AVGEU])+ "\t\t" + roundToTwo(record[AVGWC]) + "\t" + roundToTwo(record[AVGPP])
        fout.write(strg + "\n")
	print strg
    fout.close()

    print "End of Report Generator"

###############################################################################
# main - starts the program
###############################################################################
def main():

    # Read in Data
    print "Read in seedings."
    seedingsSet  = []
    reportSet    = []
    groups       = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    seedingsFile = "seedings.csv"
    reportFile   = "output.rep"
    seedingsSet  = createSeedingsSet(seedingsFile)
    print "Seedings read in.\n"

    # Analyse Data 
    print "Calculate Group Toughness"    
    # call analyseGroups(seedingsSet);
    # for each group and append to set
    for gp in groups:
        reportSet.append(analyseGroups(seedingsSet, gp))
    print "Done Analysing Group.\n"

    # Write Report
    print "Write Report"
    generateReport(reportFile, reportSet);
    print "Done Writing Report.\n"

    # add call to appropriate function

    print "Program finished."
    
    

# call main function
main()
