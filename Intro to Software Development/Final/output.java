

import java.io.*;

public class output {

	public static void writeOutput(String[][] data) throws FileNotFoundException  {

		PrintWriter output = new PrintWriter("Output.txt");
		for (String[] line : data) {
			for (int i = 0; i < line.length - 1; i++) {
				if (line[i] == null)
				{
					output.close();
					System.exit(0);
				}
				output.print(line[i] + ",");
				System.out.print(line[i] + ",");
			} output.println(line[line.length - 1]);
			System.out.println(line[line.length - 1]);
		}
		output.close();
	}
}