// Broderick Hudson, IT214 Summer Session
// This file contains the Point class and all of its methods

// Package
package HB2Prog4;

public class Point
{
	// Private instance variables
	private double xVar;
	private double yVar;
	
	// Initialize EPSILON, to be used for judging equality
	// Adjust this if it needs to be more accurate
	final private double EPSILON = 0.0001;
	
	// Constructor
	public Point(double xVar, double yVar)
	{
		this.xVar = xVar;
		this.yVar = yVar;
	}
	
	// Private Methods
	// There are none
	
	// Public Methods
	// This method returns the x value as a double
	public double getX()
	{
		return this.xVar;
	}
	
	// This method returns the y value as a double
	public double getY()
	{
		return this.yVar;
	}
	
	// This method checks if two points are equal
	public boolean equals(Point p2)
	{
		// Get p2's x and y values
		double otherXVar = p2.getX();
		double otherYVar = p2.getY();
		
		// Get implied p1's x and y values
		double xVar = this.getX();
		double yVar = this.getY();
		
		// If p1 and p2's x values are the same, then check if their y values are
		if (Math.abs(xVar - otherXVar) <= EPSILON)
		{
			if (Math.abs(yVar - otherYVar) <= EPSILON)
			{
				return true;
			}
		}
		return false;
	}
}