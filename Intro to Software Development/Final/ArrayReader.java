// Broderick Hudson, IT214 Summer Session
// This is a backup function for reading in CSV to an array

// added
import java.io.*;
import java.util.*;


public class ArrayReader
{
	// This method will open a document, and turn every line into an array (with the elements split by commas)
	// It will then return a nested array containing the data from each line as an element
	public static String[][] assembleCSVtoArray(String docName) throws FileNotFoundException
	{
		// Begin reading the file using the supplied argument document name
		File inputFile = new File(docName);
		Scanner inputReader = new Scanner(inputFile);
			
		// Read in the first line (header), split it, and use the length of the line to help create the array
		String header = inputReader.nextLine();
		String[] headerArray = header.split(",");
		int rowSize = headerArray.length;
			
		// Initialize the array that will contain all of the data from the file
		String[][] outputArray = new String[10000][rowSize]; //MAX_LINES changed to 10000
		
		// Trim the elements of headerArray
		for (int iterator = 0; iterator < headerArray.length; iterator++)
		{
			String newHeader = headerArray[iterator].trim();
			headerArray[iterator] = newHeader;
		}
			
		// Use an iterator to keep track of the length of the array, and make the header the first element of the array
		int currentLine = 0;
		outputArray[currentLine] = headerArray;
		currentLine++;
		
		// Use a while loop to take the next line of the document, split it by commas, and append it to outputArray[currentLine]
		while (inputReader.hasNextLine())
		{
			String line = inputReader.nextLine();
			String[] lineArray = line.split(",");
			
			// Trim each element in the line
			for (int iterator = 0; iterator < lineArray.length; iterator++)
			{
				String newElement = lineArray[iterator].trim();
				lineArray[iterator] = newElement;
			}
			outputArray[currentLine] = lineArray;
			currentLine++;
		}
		
		// Create a copy of the output array, which contains only the elements that hold a line of the file
		String[][] finalArray = new String[currentLine][rowSize];
		System.arraycopy(outputArray, 0, finalArray, 0, currentLine);
		
		// Close the scanner (no real reason, just good practice) and return the final array
		inputReader.close();
		return finalArray;
	}
}