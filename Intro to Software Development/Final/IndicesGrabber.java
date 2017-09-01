// Steve Klein

public class IndicesGrabber {
	
	public static int[] getIndices(String columnString, String[] desired)
	{
		String[] columnNames = columnString.split(",");
		int[] output = new int[desired.length];
		int currentPosition = 0;
		for (String desiredName : desired)
		{
			for (int iterator = 0; iterator < columnNames.length; iterator++)
			{
				if (desiredName.equals(columnNames[iterator]))
				{
					output[currentPosition] = iterator;
					currentPosition++;
				}
			}
		}
		return output;
	}
}
