package groups;
import java.util.*;
import java.text.DecimalFormat;

public class Teams
{
	Teams(	int	euroRank,
			int	worldRank, 
			String	country, 
			int	points,
			int	pot,
			char	group) 
	{
		this.euroRank      = euroRank; 
		this.worldRank     = worldRank; 
		this.country       = country; 
		this.points        = points; 
		this.pot    	   = pot; 
		this.group         = group; 
	}

	int    euroRank; 
	int    worldRank; 
	String country; 
	int    points; 
	int    pot; 
	char   group; 

	public int    getEuroRank()  { return euroRank;}
	public int    getWorldRank() { return worldRank;}
	public String getCountry()   { return country;}
	public int    getPoints()    { return points;}
	public int    getPot()       { return pot;}
	public char   getGroup()     { return group;}

	public String toLine()
	{
		return "" + country + "\t" + euroRank + "\t" + worldRank + "\t" + points + "\t" + pot + "\t" + group;
	}

	public String formatDouble(Double d){
		DecimalFormat df = new DecimalFormat("####0.00");
		return df.format(d);
	}

	public String toString()
	{
		return "Team Info " + "\n" +
		"Country          = " + country + "\n" +
		"Euro Rank        = " + euroRank + "\n" +
		"World Rank       = " + worldRank + "\n" +
		"Points           = " + points + "\n" +
		"Pot              = " + pot + "\n" +
		"Group            = " + group + "\n" ;
	}
}

