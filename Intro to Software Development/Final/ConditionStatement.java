



// added class into new file and declared it public
public class ConditionStatement
{
	// Member Variables
	private String column1;
	private String criteria1;
	private String operator1;
	private int columnIndex1;
	private boolean isLong;
	private String logicCondition;
	private String column2;
	private String criteria2;
	private String operator2;
	private int columnIndex2;
	
	// added blank constructor to initialize condition before actually creating it in a try statement
	public ConditionStatement() {}

	// Constructors
	// This is for short ones with no logic condition
	public ConditionStatement(String column, String operator, String criteria, String[] columnNames) throws Exception
	{
		if (operator.equals("=") || operator.equals("!=") || operator.equals(">") || operator.equals(">=" ) || operator.equals("<") || operator.equals("<="))
		{
			this.operator1 = operator;
		}
		else
		{
			throw new ConditionFormatError("The operator " + operator + " is invalid");
		}
		
		//if (ColumnCheck.isColumn(columnNames, column))
		//{
			this.column1 = column;
		//}
		//else
		//{
		//	throw new ConditionFormatError(column + " is not a column in the given document.");
		//}
		
		this.criteria1 = criteria;
		
		// Use the column header to find the index of the appropriate column
		for (int iterator = 0; iterator < columnNames.length; iterator++)
		{
			if (this.column1.equals(columnNames[iterator]))
			{
				this.columnIndex1 = iterator;
			}
		}
		
		// Set the boolean to indicate that the condition is one piece
		this.isLong = false;
	}
	
	// This is for longer ones with a logic condition
	public ConditionStatement(String column1, String operator1, String criteria1, String logicOperator, String column2, String operator2, String criteria2, String[] columnNames) throws Exception
	{
		if (operator1.equals("=") || operator1.equals("!=") || operator1.equals(">") || operator1.equals(">=" ) || operator1.equals("<") || operator1.equals("<="))
		{
			this.operator1 = operator1;
		}
		else
		{
			throw new ConditionFormatError("The operator " + operator1 + " is invalid");
		}
		
		//if (ColumnCheck.isColumn(columnNames, column1))
		//{
			this.column1 = column1;
		//}
		//else
		//{
		//	throw new ConditionFormatError(column1 + " is not a column in the given document.");
		//}
		
		this.criteria1 = criteria1;
		
		// Use the column header to find the index of the appropriate column
		for (int iterator = 0; iterator < columnNames.length; iterator++)
		{
			if (this.column1.equals(columnNames[iterator]))
			{
				this.columnIndex1 = iterator;
			}
		}
		
		// Set the boolean to indicate that the condition is two pieces
		this.isLong = true;
		
		// Make sure the logic condition is valid
		if (logicOperator.equals("AND"))
		{
			this.logicCondition = "AND";
		}
		else if (logicOperator.equals("OR"))
		{
			this.logicCondition = "OR";
		}
		// If it isn't AND or OR, throw an error
		else
		{
			throw new ConditionFormatError(logicOperator + " is not a valid operator. Use AND or OR.");
		}
		
		// Assign the second set of variables
		if (operator2.equals("=") || operator2.equals("!=") || operator2.equals(">") || operator2.equals(">=" ) || operator2.equals("<") || operator2.equals("<="))
		{
			this.operator2 = operator2;
		}
		else
		{
			throw new ConditionFormatError("The operator " + operator2 + " is invalid");
		}
		
		//if (ColumnCheck.isColumn(columnNames, column2))
		//{
			this.column2 = column2;
		//}
		//else
		//{
		//	throw new ConditionFormatError(column2 + " is not a column in the given document.");
		//}
		
		this.criteria2 = criteria2;
		
		// Use the column header to find the index of the appropriate column
		for (int iterator = 0; iterator < columnNames.length; iterator++)
		{
			if (this.column2.equals(columnNames[iterator]))
			{
				this.columnIndex2 = iterator;
			}
		}		
	}	
	
	// Accessor Method
	public boolean checkCondition(String[] row)
	{
		if (this.isLong)
		{
			// Use two boolean values to keep track of each half of the condition
			boolean cond1;
			boolean cond2;
			if (this.operator1.equals("="))
			{
				if (row[this.columnIndex1].equals(this.criteria1))
				{
					cond1 = true;
				}
				else
				{
					cond1 = false;
				}
			}
			else if (this.operator1.equals("!="))
			{
				if (row[this.columnIndex1].equals(this.criteria1))
				{
					cond1 = false;
				}
				else
				{
					cond1 = true;
				}
			}
			else if (this.operator1.equals("<="))
			{
				int result = row[this.columnIndex1].compareTo(this.criteria1);
				if (result <= 0)
				{
					cond1 = true;
				}
				else
				{
					cond1 = false;
				}
			}
			else if (operator1.equals("<"))
			{
				int result = row[this.columnIndex1].compareTo(this.criteria1);
				if (result < 0)
				{
					cond1 = true;
				}
				else
				{
					cond1 = false;
				}
			}
			else if (operator1.equals(">="))
			{
				int result = row[this.columnIndex1].compareTo(this.criteria1);
				if (result <= 0)
				{
					cond1 = false;
				}
				else
				{
					cond1 = true;
				}
			}
			else // (operator1.equals(">"))
			{
				int result = row[this.columnIndex1].compareTo(this.criteria1);
				if (result < 0)
				{
					cond1 = false;
				}
				else
				{
					cond1 = true;
				}
			}
			
			// Now repeat all that, but for cond2 with the second set of info
			if (this.operator2.equals("="))
			{
				if (row[this.columnIndex2].equals(this.criteria2))
				{
					cond2 = true;
				}
				else
				{
					cond2 = false;
				}
			}
			else if (this.operator2.equals("!="))
			{
				if (row[this.columnIndex2].equals(this.criteria2))
				{
					cond2 = false;
				}
				else
				{
					cond2 = true;
				}
			}
			else if (this.operator2.equals("<="))
			{
				int result = row[this.columnIndex2].compareTo(this.criteria2);
				if (result <= 0)
				{
					cond2 = true;
				}
				else
				{
					cond2 = false;
				}
			}
			else if (operator2.equals("<"))
			{
				int result = row[this.columnIndex2].compareTo(this.criteria2);
				if (result < 0)
				{
					cond2 = true;
				}
				else
				{
					cond2 = false;
				}
			}
			else if (operator2.equals(">="))
			{
				int result = row[this.columnIndex2].compareTo(this.criteria2);
				if (result <= 0)
				{
					cond2 = false;
				}
				else
				{
					cond2 = true;
				}
			}
			else // (operator2.equals(">"))
			{
				int result = row[this.columnIndex2].compareTo(this.criteria2);
				if (result < 0)
				{
					cond2 = false;
				}
				else
				{
					cond2 = true;
				}
			}
			// Now, with two booleans assigned, return them in whatever relationship the condition wants
			if (this.logicCondition.equals("AND"))
			{
				return (cond1 && cond2);
			}
			else // "OR"
			{
				return (cond1 || cond2);
			}
		}
		
		// If it isn't a long one, just return from the initial assessment
		else
		{
			if (this.operator1.equals("="))
			{
				if (row[this.columnIndex1].equals(this.criteria1))
				{
					return true;
				}
				else
				{
					return false;
				}
			}
			else if (this.operator1.equals("!="))
			{
				if (row[this.columnIndex1].equals(this.criteria1))
				{
					return false;
				}
				else
				{
					return true;
				}
			}
			else if (this.operator1.equals("<="))
			{
				int result = row[this.columnIndex1].compareTo(this.criteria1);
				if (result <= 0)
				{
					return true;
				}
				else
				{
					return false;
				}
			}
			else if (operator1.equals("<"))
			{
				int result = row[this.columnIndex1].compareTo(this.criteria1);
				if (result < 0)
				{
					return true;
				}
				else
				{
					return false;
				}
			}
			else if (operator1.equals(">="))
			{
				int result = row[this.columnIndex1].compareTo(this.criteria1);
				if (result <= 0)
				{
					return false;
				}
				else
				{
					return true;
				}
			}
			else // (operator.equals(">"))
			{
				int result = row[this.columnIndex1].compareTo(this.criteria1);
				if (result < 0)
				{
					return false;
				}
				else
				{
					return true;
				}
			}
		}
	}
}