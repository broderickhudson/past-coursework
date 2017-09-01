// Broderick Hudson, IT214 Summer Session
// This file contains the Triangle type and all of its methods

// Package
package HB2Prog4;

public class Triangle
{
	// Private instance variables
	String name;
	Point vert1;
	Point vert2;
	Point vert3;
	double side1;
	double side2;
	double side3;
	
	// Constructor
	// Exceptions should probably be thrown for collinear and duplicate points in here
	public Triangle(String name, Point vert1, Point vert2, Point vert3)
	{
		this.name = name;
		this.vert1 = vert1;
		this.vert2 = vert2;
		this.vert3 = vert3;
		
		// Use sideLength to assign the side instance variables
		this.side1 = sideLength(vert1, vert2);
		this.side2 = sideLength(vert1, vert3);
		this.side3 = sideLength(vert2, vert3);
	}
	
	// Private Methods
	// This method calculates the side length when given two points
	private double sideLength(Point p1, Point p2)
	{
		// Initialize all x and y values
		double p1X = p1.getX();
		double p1Y = p1.getY();
		double p2X = p2.getX();
		double p2Y = p2.getY();
		
		// Distance = square root of change in x squared plus change in y squared
		// Calculate and return the side length using the above formula
		double sideLength = Math.sqrt((Math.pow((p2X - p1X), 2) + Math.pow((p2Y - p1Y), 2)));
		return sideLength;
	}
	
	// Public Methods
	// This method will return the name of the triangle as a string
	public String printName()
	{
		// Standardize the return structure by making the sentence part of the return value
		String name = "The name of the triangle is ";
		name += this.name;
		name += ".";
		
		// Return name, which contains the sentence, the name, and ends in a period
		return name;
	}
	
	// This method will return the triangle's vertices as a string
	public String listVertices()
	{
		// Standardize the return structure by including the word vertices
		String formattedVertices = "Vertices: ";
		
		// To make the code more readable, assemble the parenthesis and each point separately
		// Get the x and y values of vert1, and cast them as integers rounded to one decimal point
		double p1X = this.vert1.getX();
		double p1Y = this.vert1.getY();
		String p1xFormat = String.format("%.1f", p1X);
		String p1yFormat = String.format("%.1f", p1Y);
		String point1 = "(" + p1xFormat + "," + p1yFormat + ")";
		
		// Get the x and y values of vert2, and cast them as integers rounded to one decimal point
		double p2X = this.vert2.getX();
		double p2Y = this.vert2.getY();
		String p2xFormat = String.format("%.1f", p2X);
		String p2yFormat = String.format("%.1f", p2Y);
		String point2 = "(" + p2xFormat + "," + p2yFormat + ")";
		
		// Get the x and y values of vert3, and cast them as integers rounded to one decimal point
		double p3X = this.vert3.getX();
		double p3Y = this.vert3.getY();
		String p3xFormat = String.format("%.1f", p3X);
		String p3yFormat = String.format("%.1f", p3Y);
		String point3 = "(" + p3xFormat + "," + p3yFormat + ")";
		
		// With all the points constructed, assemble formattedVertices and return it
		formattedVertices += point1 + ", " + point2 + ", " + point3;
		return formattedVertices;
	}
	
	// This method will return the triangle's sides as a string
	public String[] listSides()
	{
		// Initialize the strings that will hold the values of each side
		String side1 = "Side 1 is ";
		String side2 = "Side 2 is ";
		String side3 = "Side 3 is ";
		
		// Get the side length of each side, and format them as strings with two decimals
		String side1Length = String.format("%.2f", this.side1);
		String side2Length = String.format("%.2f", this.side2);
		String side3Length = String.format("%.2f", this.side3);
		
		// Add the formatted number to each holding string
		side1 += side1Length;
		side2 += side2Length;
		side3 += side3Length;
		
		// Assemble an array of strings containing each of the sides
		String[] sides = {side1, side2, side3};
		
		// Construct sidesFormatted as all the sides together, separated by lines, and return it
		return sides;
	}
	
	// This method will see if any of the sides are collinear and return true if they are
	public boolean hasCollinearSides()
	{
		// Initialize epsilon and all of the variables
	    final double EPSILON = 0.00001;
	    double slope1;
	    double slope2;
	    
	    // Find the slope from the first point to the second
	    // If the denominator would end up as zero, set the slope to a sentinel value of 12345.66
	    if (this.vert1.getY() - this.vert2.getY() == 0)
	    	{
	    		slope1 = 12345.66;
	    	}
	    
		// If it wouldn't, just do math as expected
	    else
	    {
	    	slope1 = (this.vert1.getX() - this.vert2.getX())/(this.vert1.getY() - this.vert2.getY());
	    }
	    
	    // Find the slope from the first point to the third
	    // If the denominator would end up as zero, set the slope to a sentinel value of 12345.66
	    if (this.vert1.getY() - this.vert3.getY() == 0)
	    	{
	    		slope2 = 12345.66;
	    	}
	    
		// If it wouldn't, just do math as expected
	    else
	    {
	    	slope2 = (this.vert1.getX() - this.vert3.getX())/(this.vert1.getY() - this.vert3.getY());
	    }   
	    
	    // See if slope1 is the sentinel
	    if (slope1 == 12345.66)
	    {
	    	if (slope2 == 12345.66)
	    	{
	    		return true;
	    	}
	    }
	    
	    // Otherwise, if slope2 is the sentinel but slope1 isn't, they aren't collinear
	    else if (slope2 == 12345.66)
	    {
	    	return false;
	    }
	    
	    // If neither of them contained the sentinel value, we can check the difference as expected
	    // Use epsilon to determine if the two lines are collinear
	    if (Math.abs(slope1 - slope2) < EPSILON)
	    {
	    	return true;
	    }
	    
	    else
	    {
	    	return false;
	    }
	}
}