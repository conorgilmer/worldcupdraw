#!/bin/awk
# Usage : awk -f groups.awk seedings.csv
# or   cat seedings.csv | awk -f groups.awk
# calculate the toughness of the group?
#
# EuroSeed, WorldSeeding, Name, Points, Pot, Group,
#
BEGIN { FS = ","
        grp = "A";
	sum = 0;
	n=0;
	potnum = 0;
	potsum = 0;
        print "\nWorld Cup Draw Group Strength"
        print "\nNo.\tEuro\tWorld\tCountry Assoc.\tPoints\tPot\tGroup\tPot Pos\n";
}
{

	if ($6 == grp) {
		sum = sum + $4;
		potpos = $1 - (9 * n);
        	printf "%s\t%s\t%s\t %s\t%s\t%s\t%s\t%d\n" , NR, $1, $2, $3, $4, $5, $6, potpos;
		++n;
		potsum = potsum + potpos;
};
}
END {
        printf "\nTotal Group Score  %d\n\n", sum;
        printf "\nTotal Group Pot Score  %d\n\n", potsum;
}

