// Broderick Hudson, IT214 Summer Session
// This is my second attempt at making the condition work

// I suspect that all of the compilation errors will go away once the placeholders for other people's methods go away

/* How to implement
 * 1. Use NewCondition's only method, createCondition, to create the condition statement
 * 2. Then initialize a for loop, iterating through every row of the 2D array
 * 3. Use the ConditionStatement method, checkCondition, on every row.
 *    If it returns true, it fulfills the condition, and should be passed along to the method that adds it to a new array.
 */

class ConditionFormatError extends Exception
{
	private static final long serialVersionUID = -3433413433571657666L;
	public ConditionFormatError(String message)
	{
		super(message);
	}
}



public class Condition
{
	//
	// Use this method before the for loop to create the condition to check every row against
	//
	public static ConditionStatement createConditions(String condition, String[] columnNames) throws Exception
	{
		// Split the condition into an array
		String[] conditionArray = condition.split(" ");
		
		// Eliminate all parenthesis from every element of the string, and if it's numeric, cast it to an integer
		for (String piece : conditionArray)
		{
			if (piece.contains("("))
			{
				String newString = piece.replace("(", "");
				piece = newString;
			}
			if (piece.contains(")"))
			{
				String newString = piece.replace("(", "");
				piece = newString;
			}
		}
		if (conditionArray.length == 3)
		{
			// There's only one condition, so just pass it to the constructor and return it
			ConditionStatement finalCondition = new ConditionStatement(conditionArray[0], conditionArray[1], conditionArray[2], columnNames);
			return finalCondition;
		}
		else if (conditionArray.length == 7)
		{
			// There are two conditions separated by a logic operator
			ConditionStatement finalCondition = new ConditionStatement(conditionArray[0], conditionArray[1], conditionArray[2], conditionArray[3], conditionArray[4], conditionArray[5], conditionArray[6], columnNames);
			return finalCondition;
		}
		// If it isn't 3 or 7 long, the condition is bogus
		else
		{
			throw new ConditionFormatError("Ensure that all elements of the condition are one word and seperated by spaces, then try again.");
		}
	}
}
