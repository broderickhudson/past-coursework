/* Broderick Hudson, IT214 Summer Session
This program will take an input of under 15 characters and output it as large letters */

// Import Scanner so that the user can input a string
import java.util.Scanner;

class BigLetters
{
	// This method takes two arrays, the final output and a 5x7 letter, and appends each line of the letter to the correct line of the final output
	public static void fiveBySevenAppend(String[] character, String[] output)
	{
		output[0] = output[0] + character[0];
		output[1] = output[1] + character[1];
		output[2] = output[2] + character[2];
		output[3] = output[3] + character[3];
		output[4] = output[4] + character[4];
		output[5] = output[5] + character[5];
		output[6] = output[6] + character[6];
	}
	
	// This is the main method
	public static void main(String[] args)
	{		
		// Declare the array of lists that will contain the contents of each of the seven lines
		String[] outputLines = {"", "", "", "", "", "", ""};
		
		// Declare every character as an array of 7 strings, which will be used to create the 5x7 letters
		String[] charA = {"     ", "     ", " *** ", "    *", " ****", "*   *", " ****"};
		String[] charB = {"*    ", "*    ", "*    ", "* ** ", "**  *", "*   *", "**** "};
		String[] charC = {"     ", "     ", " *** ", "*    ", "*    ", "*   *", " *** "};
		String[] charD = {"    *", "    *", "    *", " ** *", "*  **", "*   *", " ****"};
		String[] charE = {"     ", "     ", " *** ", "*   *", "*****", "*    ", " *** "};
		String[] charF = {"  ** ", " *   ", " *   ", "***  ", " *   ", " *   ", " *   "};
		String[] charG = {"     ", " ****", "*   *", "*   *", " ****", "    *", " *** "};
		String[] charH = {"*    ", "*    ", "* ** ", "**  *", "*   *", "*   *", "*   *"};
		String[] charI = {"     ", "     ", "  *  ", "     ", "  *  ", "  *  ", "  *  "};
		String[] charJ = {"   * ", "     ", "  ** ", "   * ", "   * ", "*  * ", " **  "};
		String[] charK = {"*    ", "*    ", "*  * ", "* *  ", "**   ", "* *  ", "*  * "};
		String[] charL = {" **  ", "  *  ", "  *  ", "  *  ", "  *  ", "  *  ", " *** "};
		String[] charM = {"     ", "     ", "** * ", "* * *", "* * *", "*   *", "*   *"};
		String[] charN = {"     ", "     ", "* ** ", "** * ", "*   *", "*   *", "*   *"};
		String[] charO = {"     ", "     ", " *** ", "*   *", "*   *", "*   *", " *** "};
		String[] charP = {"     ", "     ", "**** ", "*   *", "**** ", "*    ", "*    "};
		String[] charQ = {"     ", "     ", " ** *", "*  **", " ****", "    *", "    *"};
		String[] charR = {"     ", "     ", "* ** ", "**  *", "*    ", "*    ", "*    "};
		String[] charS = {"     ", "     ", " *** ", "*   *", " *** ", "    *", "**** "};
		String[] charT = {" *   ", " *   ", "***  ", " *   ", " *   ", " *  *", "  ** "};
		String[] charU = {"     ", "     ", "*   *", "*   *", "*   *", "*  **", " ** *"};
		String[] charV = {"     ", "     ", "*   *", "*   *", "*   *", " * * ", "  *  "};
		String[] charW = {"     ", "     ", "*   *", "*   *", "* * *", "* * *", " * * "};
		String[] charX = {"     ", "     ", "*   *", " * * ", "  *  ", " * * ", "*   *"};
		String[] charY = {"     ", "     ", "*   *", "*   *", " ****", "    *", " *** "};
		String[] charZ = {"     ", "     ", "*****", "   * ", "  *  ", " *   ", "*****"};
		String[] char0 = {" *** ", "*   *", "*  **", "* * *", "**  *", "*   *", " *** "};
		String[] char1 = {"  *  ", " **  ", "  *  ", "  *  ", "  *  ", "  *  ", " *** "};
		String[] char2 = {" *** ", "*   *", "    *", "   * ", "  *  ", " *   ", "*****"};
		String[] char3 = {"*****", "   * ", "  *  ", "   * ", "    *", "*   *", " *** "};
		String[] char4 = {"   * ", "  ** ", " * * ", "*  * ", "*****", "   * ", "   * "};
		String[] char5 = {"*****", "*    ", "**** ", "    *", "    *", "*   *", " *** "};
		String[] char6 = {"  ** ", " *   ", "*    ", "**** ", "*   *", "*   *", " *** "};
		String[] char7 = {"*****", "    *", "   * ", "  *  ", " *   ", " *   ", " *   "};
		String[] char8 = {" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "};
		String[] char9 = {" *** ", "*   *", "*   *", " ****", "    *", "   * ", " **  "};
		String[] charSpace = {"     ", "     ", "     ", "     ", "     ", "     ", "     "};
		
		// Print some use information for the user
		System.out.println("This program only accepts lowercase letters and numbers.");
		System.out.println("All input must also contain 15 characters or less.");
		System.out.println();
		
		// Initialize a loop to ensure that the input is valid, and have the user input a string
		boolean invalidInput = true;
		Scanner input = new Scanner(System.in);
		String bigLetters = "blank";
		while (invalidInput == true)
		{
			System.out.print("Enter a string: ");
			bigLetters = input.nextLine();
			
			// Check that the string is 15 characters or less
			if (bigLetters.length() > 15)
			{
				System.out.println("The input string must contain fewer than 15 characters.");
			}
			else
			{
				// Check that the string only contains a-z, 0-9, and spaces by using a Java Regular Expression
				String desired = "^[a-z0-9 ]+$";  
				if (!(bigLetters.matches(desired)))
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
		
		// The input is now valid, so we can begin assembling the big letters
		int bigLength = bigLetters.length();
		for (int iterator = 0; iterator < bigLength; iterator++)
		{
			char letter = bigLetters.charAt(iterator);
			
			// Use switch to match each character to a function call that appends the correct letter to the output array
			switch (letter)
			{
				case 'a':
					fiveBySevenAppend(charA, outputLines);
					break;
				case 'b':
					fiveBySevenAppend(charB, outputLines);
					break;
				case 'c':
					fiveBySevenAppend(charC, outputLines);
					break;
				case 'd':
					fiveBySevenAppend(charD, outputLines);
					break;
				case 'e':
					fiveBySevenAppend(charE, outputLines);
					break;
				case 'f':
					fiveBySevenAppend(charF, outputLines);
					break;
				case 'g':
					fiveBySevenAppend(charG, outputLines);
					break;
				case 'h':
					fiveBySevenAppend(charH, outputLines);
					break;
				case 'i':
					fiveBySevenAppend(charI, outputLines);
					break;
				case 'j':
					fiveBySevenAppend(charJ, outputLines);
					break;
				case 'k':
					fiveBySevenAppend(charK, outputLines);
					break;
				case 'l':
					fiveBySevenAppend(charL, outputLines);
					break;
				case 'm':
					fiveBySevenAppend(charM, outputLines);
					break;
				case 'n':
					fiveBySevenAppend(charN, outputLines);
					break;
				case 'o':
					fiveBySevenAppend(charO, outputLines);
					break;
				case 'p':
					fiveBySevenAppend(charP, outputLines);
					break;
				case 'q':
					fiveBySevenAppend(charQ, outputLines);
					break;
				case 'r':
					fiveBySevenAppend(charR, outputLines);
					break;
				case 's':
					fiveBySevenAppend(charS, outputLines);
					break;
				case 't':
					fiveBySevenAppend(charT, outputLines);
					break;
				case 'u':
					fiveBySevenAppend(charU, outputLines);
					break;
				case 'v':
					fiveBySevenAppend(charV, outputLines);
					break;
				case 'w':
					fiveBySevenAppend(charW, outputLines);
					break;
				case 'x':
					fiveBySevenAppend(charX, outputLines);
					break;
				case 'y':
					fiveBySevenAppend(charY, outputLines);
					break;
				case 'z':
					fiveBySevenAppend(charZ, outputLines);
					break;
				case '0':
					fiveBySevenAppend(char0, outputLines);
					break;
				case '1':
					fiveBySevenAppend(char1, outputLines);
					break;
				case '2':
					fiveBySevenAppend(char2, outputLines);
					break;
				case '3':
					fiveBySevenAppend(char3, outputLines);
					break;
				case '4':
					fiveBySevenAppend(char4, outputLines);
					break;
				case '5':
					fiveBySevenAppend(char5, outputLines);
					break;
				case '6':
					fiveBySevenAppend(char6, outputLines);
					break;
				case '7':
					fiveBySevenAppend(char7, outputLines);
					break;
				case '8':
					fiveBySevenAppend(char8, outputLines);
					break;
				case '9':
					fiveBySevenAppend(char9, outputLines);
					break;
				case ' ':
					fiveBySevenAppend(charSpace, outputLines);
					break;

			}
		}
				
		// Print each element of the outputLines array
		System.out.println();
		System.out.println(outputLines[0]);
		System.out.println(outputLines[1]);
		System.out.println(outputLines[2]);
		System.out.println(outputLines[3]);
		System.out.println(outputLines[4]);
		System.out.println(outputLines[5]);
		System.out.println(outputLines[6]);
		
		// Close the scanner
		input.close();
	}
}