
/**

	This will be the driver for the program, it takes an input file name, then calls 
	the method with multiple string and string array arguments to run the program.

*/ 


// import scanner for input, and io for files
import java.util.*;
import java.io.*;

public class newDriver {

	// main method
	public static void main(String[] args) {
		
		// define the input stream
		Scanner input = new Scanner(System.in);
		
		// set a boolean to check for valid input file
		boolean checking = true;

		// define the input file name String
		String inputFileName = "";

		// while checking for a valid input file
		while (checking) {

			// try 
			try {

				// output a prompt
				System.out.print("Please enter an input file name: ");
				
				// set the inputfile to the input
				inputFileName = input.next();

				// try to open the file with the filename
				File testOpen = new File(inputFileName);
				if (!(testOpen.exists())) { throw new FileNotFoundException(); }

				// set the boolean checking to false to break the while loop
				checking = false;

			// catch the exception if the input file is not found
			} catch (FileNotFoundException e) {

				// print out a message to the user
				System.out.println("That file was not found.");
			}
		}
		input.close();

		/* parameters for the select method */
		// condition for the boolean
		String conditionString = "city <= Austin OR state = IN";
		
		// condition for asc/dec sorting order
		String ascDec = "ASC";

		// array list of fields for sorting the data
		String[] fieldSorts = {"city", "first_name"};

		// array list for output fields
		String[] outputFields = {"first_name", "city", "state"};

		// call the select method
		try {
			select(inputFileName, conditionString, ascDec, fieldSorts, outputFields);
		} catch (Exception e) {	return; }

	}

	// define the select method
	public static void select(String file, String conditionString, String sortOrder, String[] sortBy, String[] outputFieldList) throws FileNotFoundException {
	
		// declare a string array to hold all of the field names necessary to the program
		String[] allFields = new String[sortBy.length + outputFieldList.length];

		// add the two field arrays to the array defined above for checking if the fields are valid
		System.arraycopy(sortBy, 0, allFields, 0, sortBy.length);
		System.arraycopy(outputFieldList, 0, allFields, sortBy.length, outputFieldList.length);
		
		// set a 2D array equal to the ArrayReader method that takes in a file name, and returns the file as a 2D array
		String[][] inputData = ArrayReader.assembleCSVtoArray(file);

		// for all fields to be used
		for (String element : allFields) {
			
			// try statement to see if it is a valid column name
			try {
				isColumn.isColumn(inputData, element);
			}
			// catch the exception thrown if the column name is not found
			catch (Exception e) {

				// output the exception message and exit the program
				System.out.println(e);
				System.exit(0);
			}
		}

		// once all of the field names to be used have been validated, we find their indices in the file
		int[] sortingIndices = IndicesGrabber.getIndices(new Scanner(new File(file)).nextLine(), sortBy);
		int[] outputIndices = IndicesGrabber.getIndices(new Scanner(new File(file)).nextLine(), outputFieldList);

		// we define a new condition to be declare in the try statement below
		ConditionStatement condition = new ConditionStatement();

		// try to define a new condition object for checking if rows satisfy the string condition
		try {
			condition = Condition.createConditions(conditionString, inputData[0]);

		// catch an exception if something is not valid, print the exception to the screen and exit the program
		} catch (Exception e) {
			System.out.println(e);
			System.exit(0);
		}

		// declare a new 2d string array to hold all of the rows that satisfy the condition
		String[][] selectedData = new String[10000][outputIndices.length];

		// set an integer count to keep the current row in the selectedData
		int currentRow = 0;
		String[][] sortedArray = new String[10000][inputData[0].length];
		// try statement to try to sort and output the selected data
		try {
			// calls the sorting method
			sortedArray = Arraysort.sort2d(inputData, sortingIndices, sortOrder);

		// if an exception is thrown, print the exception message to the user and exit the program
		} catch (Exception e) {
			System.out.println(e);
			System.exit(0);
		}
		// for each string array in the input data
		for (String[] row : sortedArray)
		{if (row[0] == null) { break; }
			// if the row satisfies the condition
			if (condition.checkCondition(row))
			{
				// add the new array to selected data with only the output indices
				addNewArrayTweaked.addToArray(row, currentRow, selectedData, outputIndices);
				currentRow++;
			}
		}
		
		// try to write the output
		try {
			output.writeOutput(selectedData);

		// catch any exceptions and return them to the user		
		} catch (Exception e) { 
			System.out.println(e);
		}
	}
}