//Sorting and Displaying data
//Arun Babu


import java.io.*;
import java.util.StringTokenizer; 
import java.lang.*;

public class Arraysort
{
	public static String[][] sort2d(String strarray2[][],int sortarrayin[],String sortOrderin) throws 
IOException
	{

		
		String[][] strarray1=new String[strarray2.length][strarray2[0].length];		//array to store sorted elements
		//String[][] strarray2=new String[1000][1000];
		int i=0;
		int j=0;
		int k=0;
		int l=0;
		String sortOrder=sortOrderin;
		/*while ((line1 = 	br1.readLine()) != null) 
		{
			StringTokenizer st1 = new StringTokenizer(line1,",");
			while (st1.hasMoreTokens())
			{
				strarray2[i][j]	= st1.nextToken();
				j++;
			}
			k=j;
			j=0;
			i++;
			l=i;
		}*/
	 l = strarray2.length - 1;
		

		
		k = strarray2[0].length;
		


		for(i=0;i<strarray2.length;i++)			//copying the input 2d array to a new array
		{
			for(j=0;j<strarray2[i].length;j++)
			{
				strarray1[i][j]=strarray2[i][j];
			}
		}
		Integer[] sortarray=new Integer[sortarrayin.length];
				i=0;
		for(int value:sortarrayin)
		{
			sortarray[i++]=Integer.valueOf(value);
		}
		Integer counter = 0;
		for ( i = 0; i < sortarray.length; i ++)  //count number of elements
		{
			if (sortarray[i] != null)
			{
				counter ++;
			}
		}
		l = strarray1.length - 1;
		k = strarray1[0].length;
		//sortarray[]={0,1};
		int x=sortarray[0];		//taking 1st element to sort
		int y=0;
		if(counter>1)		//if there are 2 elements to sort, taking the 2nd one
		{
		 y=sortarray[1];
		}
		for(i=1;i<l;i++)		//comparing and swapping loop
		{
			for(j=i+1;j<l;j++)
			{
				if((strarray1[i][x].compareTo(strarray1[j][x]))>0)
				{
					for (int a=0;a<k;a++)
					{
					String temp=strarray1[i][a];
					strarray1[i][a]=strarray1[j][a];
					strarray1[j][a]=temp;
					}
				}					
			}
		}
		if(counter>1)		//check and compare 2nd element
		{
			for(i=1;i<l;i++)
			{
				for(j=i+1;j<l;j++)
				{
					if(((strarray1[i][x].compareTo(strarray1[j][x]))==0)&&((strarray1[i][y].compareTo(strarray1[j][y]))>0))	//will compare only if 1st comparing columns are same.
					{
						for (int a=0;a<k;a++)
						{
						String temp=strarray1[i][a];
						strarray1[i][a]=strarray1[j][a];
						strarray1[j][a]=temp;
						}
					}					
				}
			}
		}

		
		PrintWriter pw=new PrintWriter(new File("Final.txt"));
		StringBuilder sb = new StringBuilder();
		for(j=0;j<k;j++)		//1st row is the column names, it will be written irrespective of the order
		{
			sb.append(strarray1[0][j]);
			if(j!=k-1)
			sb.append(",");
		}



		if(sortOrder.equals("DESC"))		//checking the sortorder
		{
			sb.append(System.getProperty("line.separator"));
			for(i=l-1;i>0;i--)
			{
				for(j=0;j<k;j++)
				{
					sb.append(strarray1[i][j]);
					if(j!=k-1)
					sb.append(",");
				}
				sb.append(System.getProperty("line.separator"));
			}
		}	
		else if(sortOrder.equals("ASC"))
		{
			sb.append(System.getProperty("line.separator"));
			for(i=1;i<l;i++)
			{
				for(j=0;j<k;j++)
				{
					sb.append(strarray1[i][j]);
					if(j!=k-1)
					sb.append(",");
				}
				sb.append(System.getProperty("line.separator"));
			}
		}

		pw.write(sb.toString());
		pw.close();
		

        	String[][] strarray3 = new String[10000][strarray2[0].length];
		BufferedReader br1 = new BufferedReader(new FileReader("Final.txt"));
		String line1 = null;
		j = 0;
		i = 0;
		k = 0; 
		l =0;
		while ((line1 = 	br1.readLine()) != null) 
		{
			StringTokenizer st1 = new StringTokenizer(line1,",");
			while (st1.hasMoreTokens())
			{
				strarray3[i][j]	= st1.nextToken();
				j++;
			}
			k=j;
			j=0;
			i++;
			l=i;
		} return strarray3;
	}
}	