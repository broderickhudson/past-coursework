// Broderick Hudson, IT214 Summer Session
// Assignment 3

// Import all important assets
import java.util.Scanner;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;
import java.util.Arrays;

class CourseDocuments
{
	// Set all important indexes here. Change them to match the text files
	// -----------------------------------
	// Courses.txt and all subsequent files
	final static int COURSE_ID = 0;
	final static int INSTRUCTOR_ID = 12;
	final static int DAY = 5;
	final static int TIME = 6;
	final static int OFFERING_PERIOD = 7;
	final static int ROOM_NUMBER = 8;
	final static int ENROLLMENT = 9;
	// -----------------------------------
	// InstructionType.txt
	final static int TYPE_COURSE_ID = 0;
	final static int TYPE_INSTRUCTION_TYPE = 1;
	// -----------------------------------
	
	// If the document has more than 10000 lines, change this variable
	final static int MAX_LINES = 10000;
	
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
	
	// This method will take two nested arrays, containing the contents of Courses.txt and InstructionType.txt
	// It will match the data together by CourseID, and set the final element to the other value in InstructionType.txt
	// NOTE: It works better if the arrays are sorted by CourseID
	public static void matchTypeToCourse(String[][] bigDocument, String[][] typeDocument)
	{
		for (String[] courseType : typeDocument)
		{
			for (String[] course : bigDocument)
			{
				if (courseType[TYPE_COURSE_ID].equals(course[COURSE_ID]))
				{
					course[(course.length - 1)] = courseType[TYPE_INSTRUCTION_TYPE];
				}
			}
		}
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
	public static String[][] condenseLines(String[][] array)
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
				if (array[index][DAY].equals(array[matchCheck][DAY]) &&
					array[index][TIME].equals(array[matchCheck][TIME]) &&
					array[index][OFFERING_PERIOD].equals(array[matchCheck][OFFERING_PERIOD]) &&
					array[index][ROOM_NUMBER].equals(array[matchCheck][ROOM_NUMBER]) &&
					array[index][INSTRUCTOR_ID].equals(array[matchCheck][INSTRUCTOR_ID]) &&
					!(array[matchCheck][COURSE_ID].equals("NO") || array[index][COURSE_ID].equals("NO")))
				{
					// If they match, combine every attribute that wasn't checked above
					for (int innerArrayIterator = 0; innerArrayIterator < array[index].length; innerArrayIterator++)
					{
						// If the current element is any of the ones that should remain the same, this will be false
						if (!(innerArrayIterator == DAY ||
							innerArrayIterator == TIME ||
							innerArrayIterator == OFFERING_PERIOD ||
							innerArrayIterator == ROOM_NUMBER ||
							innerArrayIterator == INSTRUCTOR_ID))
						{
							// If the two fields are already the same, it won't add them together
							if (!(array[index][innerArrayIterator].equals(array[matchCheck][innerArrayIterator])))
							{
								array[index][innerArrayIterator] += '/' + array[matchCheck][innerArrayIterator].trim();
							}
						}
					}
					
					// Combine the enrollment numbers specifically
					String enrollString1 = array[index][ENROLLMENT].trim();
					String enrollString2 = array[matchCheck][ENROLLMENT].trim();
					int enrollment1 = Integer.parseInt(enrollString1);
					int enrollment2 = Integer.parseInt(enrollString2);
					String newEnrollment = Integer.toString(enrollment1 + enrollment2);
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
				outputArray[currentLine] = array[currentLine];
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
			if (row[row.length - 1].contains("/"))
			{
				// If it does, split it into an array
				String[] allTypes = row[row.length - 1].split("/");
				
				// Begin another for loop that will append each element of allTypes to the course ID and add it to outputArray
				for (String type : allTypes)
				{
					String[] tempRow = Arrays.copyOf(row, row.length);
					tempRow[COURSE_ID] += type;
					tempRow[tempRow.length-1] = type;
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
		// Print some user information
		System.out.println("To prevent crashes, be sure to edit the indexes at which the program expects certain elements.");
		System.out.println("The program requires the following elements to be present and correctly labeled to function:");
		System.out.println("Course ID:        " + COURSE_ID);
		System.out.println("Instructor ID:    " + INSTRUCTOR_ID);
		System.out.println("Days:             " + DAY);
		System.out.println("Time:             " + TIME);
		System.out.println("Location:         " + ROOM_NUMBER);
		System.out.println("Enrollment:       " + ENROLLMENT);
		System.out.println();
		System.out.println("And in the Instruction Type file:");
		System.out.println("Course ID:        " + TYPE_COURSE_ID);
		System.out.println("Instruction Type: " + TYPE_INSTRUCTION_TYPE);
		
		// Use assembleCSVtoArray to create the arrays containing the contents of Courses.txt and InstructionType.txt
		String[][] coursesRaw = assembleCSVtoArray("Courses.txt");
		String[][] instructionType = assembleCSVtoArray("InstructionType.txt");
		
		// Use addColumn on the array containing the contents of Courses.txt
		// This will allow us to save the instruction type to it
		String[][] courses = addColumn(coursesRaw, instructionType[0][TYPE_INSTRUCTION_TYPE]);
		
		// Use matchTypeToCourse to combine courses and instructionType, resulting in an array that completes task 1
		matchTypeToCourse(courses, instructionType);

		// Use assembleArrayToCSV to output courses to a file called JoinCourse.txt
		assembleArraytoCSV(courses, "JoinCourse.txt");
		
		//
		// THIS COMPLETES TASK 1
		//
		
		// Use assembleCSVtoArray to create an array containing the contents of JoinCourse.txt
		String[][] joinCourse = assembleCSVtoArray("JoinCourse.txt");
		
		// Use condenseLines to get an array with all lines sharing 5 values condensed into 1
		String[][] finalJoinCourse = condenseLines(joinCourse);
		
		// Use assembleArraytoCSV to output joinCourse to a file called CombinCourses.txt
		assembleArraytoCSV(finalJoinCourse, "CombinCourses.txt");
		
		//
		// THIS COMPLETES TASK 2
		//
		
		// Use assembleCSVtoArray to create an array containing the contents of CombinCourses.txt
		String[][] combinCourses = assembleCSVtoArray("CombinCourses.txt");
		
		// Use expandLines to make any row with a slashed instruction type into two
		String[][] finalCombinCourses = expandLines(combinCourses);
		
		// Use assembleArraytoCSV to output combinCourses into a file called CourseFinal.txt
		assembleArraytoCSV(finalCombinCourses, "CourseFinal.txt");
		
		//
		// THIS COMPLETES TASK 3
		//
	}
}