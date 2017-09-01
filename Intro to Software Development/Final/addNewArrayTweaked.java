//is one of these what we were looking for the first one takes in an array at a time assuming that only the ones already passed the
//condition are being put through.
//the second one has a 2D array as an input to the method and i put in an ifcondition that could be used to see if they passed the
//conditions or not.


public class addNewArrayTweaked
{
	//method if row is an array
	public static void addToArray(String[] row, int currentRow, String[][] array, int[] outputIndices)
	{
		
		for (int i = 0; i < outputIndices.length; i++) {
			array[currentRow][i] = row[outputIndices[i]];
		}
	}
}

