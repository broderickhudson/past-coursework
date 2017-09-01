// Broderick Hudson, IT214 Summer Session
// Assignment 1 Quiz

// Make all important imports
import java.util.Scanner;
import java.util.Arrays;

class BigLetterPrinter
{
	// This method effectively adds an element to an array
	static int[] addElement(int[] array, int added)
	{
	    array  = Arrays.copyOf(array, array.length + 1);
	    array[array.length - 1] = added;
	    return array;
	}
	public static void main(String[] args)
	{
		// Declare all of the letters as an array of arrays, each one representing a character 0-9, a-z
		// The character's numeric value is equal to its index in this list
		String[][] bigLetters = {
		{" *** ", "*   *", "*  **", "* * *", "**  *", "*   *", " *** "}, // 0
		{"  *  ", " **  ", "  *  ", "  *  ", "  *  ", "  *  ", " *** "}, // 1
		{" *** ", "*   *", "    *", "   * ", "  *  ", " *   ", "*****"}, // 2
		{"*****", "   * ", "  *  ", "   * ", "    *", "*   *", " *** "}, // 3
		{"   * ", "  ** ", " * * ", "*  * ", "*****", "   * ", "   * "}, // 4
		{"*****", "*    ", "**** ", "    *", "    *", "*   *", " *** "}, // 5
		{"  ** ", " *   ", "*    ", "**** ", "*   *", "*   *", " *** "}, // 6
		{"*****", "    *", "   * ", "  *  ", " *   ", " *   ", " *   "}, // 7
		{" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "}, // 8
		{" *** ", "*   *", "*   *", " ****", "    *", "   * ", " **  "}, // 9
		{"     ", "     ", " *** ", "    *", " ****", "*   *", " ****"}, // a
		{"*    ", "*    ", "*    ", "* ** ", "**  *", "*   *", "**** "}, // b
		{"     ", "     ", " *** ", "*    ", "*    ", "*   *", " *** "}, // c
		{"    *", "    *", "    *", " ** *", "*  **", "*   *", " ****"}, // d
		{"     ", "     ", " *** ", "*   *", "*****", "*    ", " *** "}, // e
		{"  ** ", " *   ", " *   ", "***  ", " *   ", " *   ", " *   "}, // f
		{"     ", " ****", "*   *", "*   *", " ****", "    *", " *** "}, // g
		{"*    ", "*    ", "* ** ", "**  *", "*   *", "*   *", "*   *"}, // h
		{"     ", "     ", "  *  ", "     ", "  *  ", "  *  ", "  *  "}, // i
		{"   * ", "     ", "  ** ", "   * ", "   * ", "*  * ", " **  "}, // j
		{"*    ", "*    ", "*  * ", "* *  ", "**   ", "* *  ", "*  * "}, // k
		{" **  ", "  *  ", "  *  ", "  *  ", "  *  ", "  *  ", " *** "}, // l
		{"     ", "     ", "** * ", "* * *", "* * *", "*   *", "*   *"}, // m
		{"     ", "     ", "* ** ", "** * ", "*   *", "*   *", "*   *"}, // n
		{"     ", "     ", " *** ", "*   *", "*   *", "*   *", " *** "}, // o
		{"     ", "     ", "**** ", "*   *", "**** ", "*    ", "*    "}, // p
		{"     ", "     ", " ** *", "*  **", " ****", "    *", "    *"}, // q
		{"     ", "     ", "* ** ", "**  *", "*    ", "*    ", "*    "}, // r
		{"     ", "     ", " *** ", "*   *", " *** ", "    *", "**** "}, // s
		{" *   ", " *   ", "***  ", " *   ", " *   ", " *  *", "  ** "}, // t
		{"     ", "     ", "*   *", "*   *", "*   *", "*  **", " ** *"}, // u
		{"     ", "     ", "*   *", "*   *", "*   *", " * * ", "  *  "}, // v
		{"     ", "     ", "*   *", "*   *", "* * *", "* * *", " * * "}, // w
		{"     ", "     ", "*   *", " * * ", "  *  ", " * * ", "*   *"}, // x
		{"     ", "     ", "*   *", "*   *", " ****", "    *", " *** "}, // y
		{"     ", "     ", "*****", "   * ", "  *  ", " *   ", "*****"}, // z
		{"     ", "     ", "     ", "     ", "     ", "     ", "     "}}; // space
		
		// Initialize a loop to ensure that the input is valid, and have the user input a string
		boolean invalidInput = true;
		Scanner input = new Scanner(System.in);
		String inputString = "!!!";
		while (invalidInput == true)
		{
			System.out.print("Enter a string: ");
			inputString = input.nextLine();
			
			// Check that the string is 15 characters or less
			if (inputString.length() > 15)
			{
				System.out.println("The input string must contain fewer than 15 characters.");
			}
			else
			{
				// Check that the string only contains a-z, 0-9, and spaces by using a Java Regular Expression
				String desired = "^[a-z0-9 ]+$";  
				if (!(inputString.matches(desired)))
				{
					System.out.println("The input string must only contain lowercase letters and numbers");
				}
				else
				{
					// If it made it this far, the string is valid, so we can set invalidInput to false
					invalidInput = false;
				}
			}
		}
		// Now that we know the input is valid, we can convert our input into an array of numbers values
		int[] bigLettersOutput = {};
		int asciiChar;
		for (int iterator = 0; iterator < inputString.length(); iterator++)
		{
			char character = inputString.charAt(iterator);
			if (character == ' ')
			{
				asciiChar = 36;
			}
			else
			{
				asciiChar = Character.getNumericValue(character);
			}
			bigLettersOutput = addElement(bigLettersOutput, asciiChar);
		}
		
		// Now that the input is converted to numeric values, each value lines up with the index, and printing is easy
		System.out.println();
		for (int line = 0; line < 7; line++)
		{
			for (int character : bigLettersOutput)
			{
				System.out.print(bigLetters[character][line]);
			}
			System.out.println();
		}
		
		// Close the scanner
		input.close();
	}
}