//Wunderlin,Amanda
//The array will come from the 2d Array created from CSV File.
//The columnName will come from the parameters of the select Statment
//Will need to use this method on each column input
public class isColumn {
	
	// added static to method definition
	public static boolean isColumn(String [][]Array,String columnName)throws Exception
	{																			
		// changed the middle parameter to exclude the [i] index since this calclates the length
		// of the first element of the first array. instead of the length of the first array.
		// also changed it to length. Since that calculates the length of an array instead of 
		// the length() of a string
		for(int i = 0;i<Array[0].length;i++)
		{
			
			if(Array[0][i].equals(columnName))
			{
				return true;
			}
		}
		throw new Exception("Invalid column name.");
	
	}
}