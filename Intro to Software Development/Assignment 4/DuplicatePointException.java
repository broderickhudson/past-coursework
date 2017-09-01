// Broderick Hudson, IT214 Summer Session
// This file contains the DuplicatePointException

// Package
package HB2Prog4;

public class DuplicatePointException extends Exception
{
	private static final long serialVersionUID = -8551785601838332626L;

	DuplicatePointException(String errorMessage)
	{
		super(errorMessage);
	}
}
