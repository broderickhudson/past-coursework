// Broderick Hudson, IT214 Summer Session
// This program asks if Red, Green, and Blue are present, and outputs the color that they form

// Import scanner, so that the user can input the presence of RGB
import java.util.Scanner;

class ColorOutput
{
	// This method takes in two lists (first is indexes and second is strings) and removes the elements of the first from the second
	public static void removeListFromList(int[] remove, String[] trueList)
	{
		for (int deleteColor : remove)
		{
			trueList[deleteColor] = "no";
		}
	}
	
	// This is the main function
	public static void main(String[] args)
	{
		// Initialize an array containing all possible output colors
		// Black at [0] is the one that takes them all, [1] takes none of them, and [2] takes only red
		String[] allColors = {"Black", "Black", "Black", "Blue", "Green", "White", "Purple", "Yellow"};
		
		// Initialize arrays for Red, Blue, and Green, containing the indexes of the colors that they contribute to
		int[] redColors = {0, 6, 7, 2};
		int[] greenColors = {4, 5, 7, 0};
		int[] blueColors = {3, 5, 6, 0};
		
		// Initialize arrays for Red, Blue, and Green, containing the indexes of the colors that they don't contribute to
		int[] redNotColors = {3, 4, 5, 1};
		int[] greenNotColors = {2, 3, 6, 1};
		int[] blueNotColors = {2, 4, 7, 1};
		
		// Initialize values that will contain the user's input for the presence of each color
		// I used strings instead of chars because it prevents the user from breaking the program
		String isRed = "U";
		String isGreen = "U";
		String isBlue = "U";
		
		// Create a scanner, and start a loop to ensure that the input is good for red	
		Scanner inputRed = new Scanner(System.in);
		boolean invalidInput = true;
		while (invalidInput == true)
		{
			System.out.print("Is Red present?     Y/N: ");
			isRed = inputRed.next();
			
			// If red is present, the color can't be any of the ones that red doesn't contribute to
			if (isRed.equals("Y"))
			{
				removeListFromList(redNotColors, allColors);
				invalidInput = false;
			}
			
			// If red is not present, the color can't be any of the ones that red contributes to
			else if (isRed.equals("N"))
			{
				removeListFromList(redColors, allColors);
				invalidInput = false;
			}
			else
			{
				System.out.println("Invalid input. Enter 'Y' for Yes or 'N' for No.");
			}				
		}

		// Start a loop to ensure that the input is good for green
		Scanner inputGreen = new Scanner(System.in);
		invalidInput = true;
		while (invalidInput == true)
		{
			System.out.print("Is Green present?   Y/N: ");
			isGreen = inputGreen.next();
			
			// If green is present, the color can't be any of the ones that green doesn't contribute to
			if (isGreen.equals("Y"))
			{
				removeListFromList(greenNotColors, allColors);
				invalidInput = false;
			}
			
			// If green is not present, the color can't be any of the ones that green contributes to
			else if (isGreen.equals("N"))
			{
				removeListFromList(greenColors, allColors);
				invalidInput = false;
			}
			else
			{
				System.out.println("Invalid input. Enter 'Y' for Yes or 'N' for No.");
			}
		}
		
		// Start a loop to ensure that the input is good for blue
		Scanner inputBlue = new Scanner(System.in);
		invalidInput = true;
		while (invalidInput == true)
		{
			System.out.print("Is Blue present?    Y/N: ");
			isBlue = inputBlue.next();
					
			// If blue is present, the color can't be any of the ones that blue doesn't contribute to
			if (isBlue.equals("Y"))
			{
				removeListFromList(blueNotColors, allColors);
				invalidInput = false;
			}
					
			// If blue is not present, the color can't be any of the ones that blue contributes to
			else if (isBlue.equals("N"))
			{
				removeListFromList(blueColors, allColors);
				invalidInput = false;
			}
			else
			{
				System.out.println("Invalid input. Enter 'Y' for Yes or 'N' for No.");
			}
		}
		
		// Only one element in allColors doesn't equal 'no', which means that it's the answer
		// Print that element
		System.out.println();
		System.out.print("The resulting color is: ");
		for (String color : allColors)
		{
			if (!(color.equals("no")))
			{
				System.out.print(color);
			}
		}
		
		// Close all of the scanners
		inputRed.close();
		inputGreen.close();
		inputBlue.close();
	}
}