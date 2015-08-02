package groups;
import java.util.*;
import java.text.DecimalFormat;

/* class for the seasons results and for writing report */
public class Groups
{
	Groups(		char	group,
			int	teams,
			double	points, 
			double	avgEuro, 
			double	avgWorld, 
			double  avgPot) 
	{
		this.group      = group;
		this.teams      = teams;
		this.points     = points;
		this.avgEuro    = avgEuro;
		this.avgWorld   = avgWorld;
		this.avgPot     = avgPot;
	}

	char   group; 
	int    teams; 
	double points; 
	double avgEuro; 
	double avgWorld; 
	double avgPot; 

	public char   getGroup()     { return group;} 
	public int    getTeams()     { return teams;} 
	public double getPoints()    { return points;} 
	public double getAvgEuro()   { return avgEuro;} 
	public double getAvgWorld()  { return avgWorld;} 
	public double getAvgPot()    { return avgPot;} 

        public String formatDouble(Double d){
                DecimalFormat df = new DecimalFormat("####0.00");
                return df.format(d);
        }


	public String toString()
	{
		return "Group Info Summary" + "\n" +
		"Group            = " + group + "\n" +
		"Teams            = " + teams + "\n" +
		"Total Points     = " + points + "\n" +
		"Avg Euro Rank    = " + avgEuro + "\n" +
		"Avg World Rank   = " + avgWorld + "\n" +
		"Avg Pot Position = " + avgPot;
	}
}

