// Broderick Hudson, IT214 Summer Session
// Assignment 3
// This version is the in class one that sorts every data point that contains a slash

// Import all important assets
import java.util.Scanner;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;
import java.util.Arrays;

class CourseDocumentsClassFinal
{
	// Set all important indexes here. Change them to match the text files
	// -----------------------------------
	// Courses.txt and all subsequent files
	final static int COURSE_ID = 0;
	final static int COURSE_DETAILS = 1;
	final static int COURSE_NAME = 2;
	final static int ENROLLMENT = 3;
	final static int INSTRUCTION_TYPE = 4;
	final static int LAST_NAME = 5;
	final static int FIRST_NAME = 6;
	final static int INSTRUCTOR_ID = 7;
	final static int DAY_TIME = 8;
	// -----------------------------------
	// If the document has more than 10000 lines, change this variable
	final static int MAX_LINES = 10000;
	
	// This method sorts every column field with a slash in it
	public static void splitSort(String[][] array)
	{
		// Initialize a for loop to look at every field in every row in the array
		for (String[] row : array)
		{
			for (String data : row)
			{
				if (data.contains("/"))
				{
					String finalData = "";
					String[] tempData = data.split("/");
					Arrays.sort(tempData);
					for (String sorted : tempData)
					{
						finalData += sorted + "/";
					}
					String trueData = finalData.substring(0, (finalData.length()-2));
					data = trueData;
				}
			}
		}
	}
	
	// This method breaks up enrollment numbers separated with a / and returns the sum of them
	public static int splitSum(String numberString)
	{
		String[] numberArray = numberString.split("/");
		int total = 0;
		for (String number : numberArray)
		{
			int newNumber = Integer.parseInt(number);
			total += newNumber;
		}
		return total;
	}
	
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
		String[][] outputArray = new String[MAX_LINES][rowSize];
		
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
	
	// This method will add a blank element to the end of every array in a 2D array
	// This will be useful for giving us an extra blank element to set the type to
	public static String[][] addColumn(String[][] inputArray, String columnName)
	{
		// Initialize the final array
		String[][] outputArray = new String[(inputArray.length)][];
		
		// Use a for loop to add the old data to the new table, and set the last element of each row to "NA"
		for (int rowIterator = 0; rowIterator < inputArray.length; rowIterator++)
		{
			outputArray[rowIterator] = Arrays.copyOf(inputArray[rowIterator], (inputArray[0].length + 1));
			outputArray[rowIterator][(outputArray[0].length-1)] = "NA";
		}
		// Set the last element in the first row to columnName
		outputArray[0][(outputArray[0].length-1)] = columnName;
		
		// Return outputArray
		return outputArray;
	}
	
	// This method will take a 2D array, and write it to CSV in a file named after the argument fileName
	public static void assembleArraytoCSV(String[][] array, String fileName) throws FileNotFoundException
	{
		// Initialize the PrintWriter that will create the output file
		PrintWriter output = new PrintWriter(fileName);
		
		// Start nested for loops that print every data point to the output file
		for (String[] row : array)
		{
			// Use a counter to keep track of how many commas each line gets to ensure that the line does not end in a comma
			int commaCount = 0;
			int neededCommas = row.length - 1;
			for (String data : row)
			{
				// Prints each element of the row, and if the needed comma quantity hasn't been passed, a comma
				output.print(data);
				if (commaCount < neededCommas)
				{
					output.print(", ");
					commaCount++;
				}
			}
			// Print a blank new line, and the row is done!
			output.println();
		}
		// Close the PrintWriter
		output.close();
	}
	
	// This method takes an array and condenses lines using the criteria from Task 2
	public static String[][] condenseLinesTime(String[][] array)
	{
		// Initialize the final array
		String[][] outputArray = new String[array.length][array[0].length];
		
		// Use nested for loops to walk through the array and compare each line to every other line
		// Use indexes to prevent redundant comparisons
		for (int index = 1; index < array.length; index++)
		{
			for (int matchCheck = index+1; matchCheck < array.length; matchCheck++)
			{
				// Day, time, offering period, room, and instructor ID all need to match for them to be combined
				// Also be sure that neither course ID has been modified, which indicates that it's already been added
				if (array[index][DAY_TIME].equals(array[matchCheck][DAY_TIME])  &&
					array[index][INSTRUCTOR_ID].equals(array[matchCheck][INSTRUCTOR_ID]) &&
					!(array[matchCheck][COURSE_ID].equals("NO") || array[index][COURSE_ID].equals("NO")))
				{
					// If they match, combine every attribute that wasn't checked above
					for (int innerArrayIterator = 0; innerArrayIterator < array[index].length; innerArrayIterator++)
					{
						// If the current element is any of the ones that should remain the same, this will be false
						if (!(innerArrayIterator == DAY_TIME ||
							innerArrayIterator == INSTRUCTOR_ID ||
							innerArrayIterator == ENROLLMENT))
						{
							// If the two fields are already the same, it won't add them together
							if (!(array[index][innerArrayIterator].equals(array[matchCheck][innerArrayIterator])))
							{
								array[index][innerArrayIterator] += '/' + array[matchCheck][innerArrayIterator].trim();
							}
						}
					}
					
					// Combine the enrollment numbers specifically
					String enrollString = array[index][ENROLLMENT].trim();
					String otherEnrollString = array[matchCheck][ENROLLMENT].trim();
					int enroll1 = Integer.parseInt(enrollString);
					int enroll2 = Integer.parseInt(otherEnrollString);
					int enrollment = enroll1 + enroll2;
					
					// Cast the sum of the enrollments back to a string, and set the enrollment to that number
					String newEnrollment = Integer.toString(enrollment);
					array[index][ENROLLMENT] = newEnrollment;
					
					// To prevent matching courses from being added to each other ad infinitum, modify the extra's course ID
					array[matchCheck][COURSE_ID] = "NO";
				}
			}
		}
		// Now we have an array with elements combined, and some of them have "NO" for a course ID
		// Write every element that doesn't have that course ID to a new array
		// Use an iterator to do so
		int currentLine = 0;
		for (String[] line : array)
		{
			if (!(line[COURSE_ID].equals("NO")))
			{
				outputArray[currentLine] = line;
				currentLine++;
			}
		}
		// Make and return a copy of outputArray containing only the filled lines
		String[][] finalArray = new String[currentLine][outputArray[0].length];
		System.arraycopy(outputArray, 0, finalArray, 0, currentLine);
		return finalArray;
	}
	
	// This method takes an array and condenses lines using the criteria from Task 2
	public static String[][] condenseLinesID(String[][] array)
	{
		// Initialize the final array
		String[][] outputArray = new String[array.length][array[0].length];
		
		// Use nested for loops to walk through the array and compare each line to every other line
		// Use indexes to prevent redundant comparisons
		for (int index = 1; index < array.length; index++)
		{
			for (int matchCheck = index+1; matchCheck < array.length; matchCheck++)
			{
				// Day, time, offering period, room, and instructor ID all need to match for them to be combined
				// Also be sure that neither course ID has been modified, which indicates that it's already been added
				if (array[index][COURSE_ID].equals(array[matchCheck][COURSE_ID])  &&
					array[index][INSTRUCTOR_ID].equals(array[matchCheck][INSTRUCTOR_ID]) &&
					!(array[matchCheck][COURSE_ID].equals("NO") || array[index][COURSE_ID].equals("NO")))
				{
					// If they match, combine every attribute that wasn't checked above
					for (int innerArrayIterator = 0; innerArrayIterator < array[index].length; innerArrayIterator++)
					{
						// If the current element is any of the ones that should remain the same, this will be false
						if (!(innerArrayIterator == COURSE_ID ||
							innerArrayIterator == INSTRUCTOR_ID))
						{
							// If the two fields are already the same, it won't add them together
							if (!(array[index][innerArrayIterator].equals(array[matchCheck][innerArrayIterator])))
							{
								array[index][innerArrayIterator] += '/' + array[matchCheck][innerArrayIterator].trim();
							}
						}
					}
					// To prevent matching courses from being added to each other ad infinitum, modify the extra's course ID
					array[matchCheck][COURSE_ID] = "NO";
				}
			}
		}
		// Now we have an array with elements combined, and some of them have "NO" for a course ID
		// Write every element that doesn't have that course ID to a new array
		// Use an iterator to do so
		int currentLine = 0;
		for (String[] line : array)
		{
			if (!(line[COURSE_ID].equals("NO")))
			{
				outputArray[currentLine] = line;
				currentLine++;
			}
		}
		// Make and return a copy of outputArray containing only the filled lines
		String[][] finalArray = new String[currentLine][outputArray[0].length];
		System.arraycopy(outputArray, 0, finalArray, 0, currentLine);
		return finalArray;
	}	
	
	// This method takes an array and expands any line with a slashed instruction type into two for Task 3
	public static String[][] expandLines(String[][] array)
	{
		// Initialize the array that will hold all of the lines, and an iterator to keep track of the current line
		String[][] outputArray = new String[MAX_LINES][array[0].length];
		int currentLine = 0;
		
		// Use an enhanced for loop to iterate through each row and see if the instruction type contains a /
		for (String[] row : array)
		{
			// Remember that instruction type is always the last element of the row
			if (row[INSTRUCTION_TYPE].contains("/"))
			{
				// If it does, split it into an array
				String[] allTypes = row[INSTRUCTION_TYPE].split("/");
				
				// Begin another for loop that will append each element of allTypes to the course ID and add it to outputArray
				for (String type : allTypes)
				{
					String[] tempRow = Arrays.copyOf(row, row.length);
					tempRow[COURSE_ID] += type;
					tempRow[INSTRUCTION_TYPE] = type;
					outputArray[currentLine] = tempRow;
					currentLine++;
				}
			}
			// If it got here, we just add the line as it is and increment currentLine
			else
			{
				outputArray[currentLine] = row;
				currentLine++;
			}
		}
		// Make and return another array containing only the filled lines of the array
		String[][] finalArray = new String[currentLine][outputArray[0].length];
		System.arraycopy(outputArray, 0, finalArray, 0, currentLine);
		return finalArray;
	}
	
	// This is the main method
	public static void main(String args[]) throws FileNotFoundException
	{	
		//
		// THERE IS NO LONGER A TASK 1
		//
		
		// Use assembleCSVtoArray to create an array containing the contents of JoinCourse.txt
		String[][] coursesDocument = assembleCSVtoArray("JoinCourse.txt");
		
		// Use condenseLinesTime to get an array with all rows sharing a time and instructor condensed into 1
		// This method also combines enrollment values
		coursesDocument = condenseLinesTime(coursesDocument);
		splitSort(coursesDocument);
		
		//
		// THIS COMPLETES TASK 2
		//
		
		// Use expandLinesTime to make any row with a slashed instruction type into two
		coursesDocument = expandLines(coursesDocument);
		splitSort(coursesDocument);
		
		//
		// THIS COMPLETES TASK 3
		//
		
		// Use condenseLinesID to get an array with all lines sharing class ID and instructor condensed into 1
		coursesDocument = condenseLinesID(coursesDocument);
		splitSort(coursesDocument);
		
		// Use assembleArraytoCSV to output coursesDocument into a file called CourseFinal4.txt
		assembleArraytoCSV(coursesDocument, "CourseFinal4.txt");
		
		//
		// THIS COMPLETES TASK 4
		//
	}
}