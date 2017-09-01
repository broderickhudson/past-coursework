// Broderick Hudson, IT214 Summer Session
// This file contains the main method, which will run the program using Point and Triangle objects

// Package
package HB2Prog4;

// Import all needed assets
import java.util.Scanner;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;
import java.util.ArrayList;

// Open the file to be read in
class HB2Prog4
{
	// This is the main method
	public static void main(String[] args) throws FileNotFoundException, DuplicatePointException, CollinearException
	{
		// Initialize the arraylist that will contain all of the triangle objects
		ArrayList<Triangle> myTri = new ArrayList<Triangle>();
		
		// Open the file to be read
		File inputFile = new File("triInput.txt");
		Scanner input = new Scanner(inputFile);
		
		// Open the output file
		PrintWriter output = new PrintWriter("HB2myTri.txt");
		
		// Start the loop that will iterate through the file
		while (input.hasNextLine())
		{
			// Get the next line, and split it one spaces
			String line = input.nextLine();
			String[] lineArray = line.split(" ");
			
			// [0] is the name, [1][2] are p1, [3][4] are p2, and [5][6] are p3
			// Create point objects
			double p1x = Double.parseDouble(lineArray[1]);
			double p1y = Double.parseDouble(lineArray[2]);
			double p2x = Double.parseDouble(lineArray[3]);
			double p2y = Double.parseDouble(lineArray[4]);
			double p3x = Double.parseDouble(lineArray[5]);
			double p3y = Double.parseDouble(lineArray[6]);
			Point p1 = new Point(p1x, p1y);
			Point p2 = new Point(p2x, p2y);
			Point p3 = new Point(p3x, p3y);
			
			// Now check if the triangle has duplicate points
			// Do the entire thing in try/catch, so that if an exception is thrown, the loop can continue
			try
			{
				if (p1.equals(p2))
				{
					throw new DuplicatePointException(lineArray[0] + ": p1 and p2 are equal.");
				}
				
				else if (p1.equals(p3))
				{
					throw new DuplicatePointException(lineArray[0] + "p1 and p3 are equal.");
				}
				
				else if (p2.equals(p3))
				{
					throw new DuplicatePointException(lineArray[0] + "p2 and p3 are equal.");
				}
				
				else
				{
					// Now create the triangle, and check if it has collinear points
					Triangle triangle = new Triangle(lineArray[0], p1, p2, p3);

					if (triangle.hasCollinearSides())
					{
						throw new CollinearException(triangle.name + " has collinear sides.");
					}
					
					else
					{
						// If it didn't have collinear sides, add it to the array
						myTri.add(triangle);
					}
				}
			}
			
			// Handle duplicate points
			catch (DuplicatePointException e)
			{
				System.out.println(lineArray[0] + " has duplicate points.");
				output.println(lineArray[0] + " has duplicate points.");
			}
			
			// Handle collinear lines
			catch (CollinearException e)
			{
				System.out.println(lineArray[0] + " has collinear lines.");
				output.println(lineArray[0] + " has collinear lines.");
			}
		}
		
		// Print a blank line to separate any error messages
		System.out.println();
		output.println();
		
		// Now, output the name, vertices, and sides of every triangle in the array
		for (Triangle triangle : myTri)
		{
			// Initialize the sides
			String[] sides = triangle.listSides();
			
			// Print the name
			System.out.println(triangle.printName());
			output.println(triangle.printName());
			
			// Print the vertices
			System.out.println(triangle.listVertices());
			output.println(triangle.listVertices());
			
			// Print the sides
			System.out.println(sides[0]);
			System.out.println(sides[1]);
			System.out.println(sides[2]);
			output.println(sides[0]);
			output.println(sides[1]);
			output.println(sides[2]);
			
			// Print a blank line for space
			System.out.println();
			output.println();
		}
		
		// Close the input and output
		input.close();
		output.close();
	}
}
