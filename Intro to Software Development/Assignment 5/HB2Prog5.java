// Broderick Hudson, IT214 Summer Session
// This file contains all of the classes, as well as the test driver for program 5.

// This is the abstract class Shape
abstract class Shape
{
	// Member Variables
	protected String color;
	protected boolean filled;
	
	// Constructors
	public Shape()
	{
		this.color = "Unfilled";
		this.filled = false;
	}
	
	public Shape(String color, boolean filled)
	{
		this.color = color;
		this.filled = false;
	}
	
	// Accessor Methods
	public String getColor()
	{
		return this.color;
	}
	
	public boolean isFilled()
	{
		return this.filled;
	}
	
	public abstract double getArea();
	public abstract double getPerimeter();
	
	public String toString()
	{
		String string = "";
		boolean filled = this.isFilled();
		if (filled)
		{
			string += this.color;
		}
		else
		{
			string += "Unfilled";
		}
		string += " Shape";
		return string;
	}
	
	// Mutator Methods
	public void setColor(String color)
	{
		this.color = color;
	}
	
	public void setFilled(boolean filled)
	{
		this.filled = filled;
	}
}

// This is the class Circle
class Circle extends Shape
{
	// Member Variables
	protected double radius;
	
	// Constructors
	public Circle()
	{
		super();
		this.radius = 0;
	}
	
	public Circle(double radius)
	{
		super();
		this.radius = radius;
	}
	
	public Circle(double radius, String color, boolean filled)
	{
		super(color, filled);
		this.radius = radius;
	}
	
	// Accessor Methods
	public double getRadius()
	{
		return this.radius;
	}
	
	@Override
	public double getArea()
	{
		return Math.PI * Math.pow(this.radius, 2);
	}
	
	@Override
	public double getPerimeter()
	{
		return 2 * Math.PI * this.radius;
	}
	
	@Override
	public String toString()
	{
		String string = "";
		boolean filled = this.isFilled();
		if (filled)
		{
			string += this.color;
		}
		else
		{
			string += "Unfilled";
		}
		string += " Circle";
		return string;
	}
}

// This is the rectangle class
class Rectangle extends Shape
{
	// Member Variables
	protected double width;
	protected double length;
	
	// Constructors
	public Rectangle()
	{
		super();
		this.width = 0;
		this.length = 0;
	}
	
	public Rectangle(double width, double length)
	{
		super();
		this.width = width;
		this.length = length;
	}
	
	public Rectangle(double width, double length, String color, boolean filled)
	{
		super(color, filled);
		this.width = width;
		this.length = length;
	}
	
	// Accessor Methods
	public double getWidth()
	{
		return this.width;
	}
	
	public double getLength()
	{
		return this.length;
	}
	
	@Override
	public double getArea()
	{
		return this.width * this.length;
	}
	
	@Override
	public double getPerimeter()
	{
		return 2 * (this.width + this.length);
	}
	
	@Override
	public String toString()
	{
		String string = "";
		boolean filled = this.isFilled();
		if (filled)
		{
			string += this.color;
		}
		else
		{
			string += "Unfilled";
		}
		string += " Rectangle";
		return string;
	}
	
	// Mutator Methods
	public void setWidth(double width)
	{
		this.width = width;
	}
	
	public void setLength(double length)
	{
		this.length = length;
	}
}

class Square extends Rectangle
{
	// Member Variables
	// None
	
	// Constructors
	public Square()
	{
		super();
	}
	
	public Square(double side)
	{
		super(side, side);
	}
	
	public Square(double side, String color, boolean filled)
	{
		super(side, side, color, filled);
	}
	
	// Accessor Methods
	public double getSide()
	{
		return this.width;
	}
	
	@Override
	public String toString()
	{
		String string = "";
		boolean filled = this.isFilled();
		if (filled)
		{
			string += this.color;
		}
		else
		{
			string += "Unfilled";
		}
		string += " Square";
		return string;
	}
	
	// Mutator Methods
	public void setSide(double side)
	{
		this.width = side;
		this.length = side;
	}
	
	@Override
	public void setWidth(double side)
	{
		this.width = side;
		this.length = side;
	}
	
	@Override
	public void setLength(double side)
	{
		this.width = side;
		this.length = side;
	}
}

public class HB2Prog5
{
	public static void main(String[] args)
	{
		Shape s1 = new Circle(5.5, "RED", false);
		System.out.println(s1);
		System.out.println(s1.getArea());
		System.out.println(s1.getPerimeter());
		System.out.println(s1.getColor());
		System.out.println(s1.isFilled());
		// System.out.println(s1.getRadius()); // ERROR HERE
		
		Circle c1 = (Circle)s1;
		System.out.println(c1);
		System.out.println(c1.getArea());
		System.out.println(c1.getPerimeter());
		System.out.println(c1.getColor());
		System.out.println(c1.isFilled());
		System.out.println(c1.getRadius());
		
		// Shape s2 = new Shape(); // ERROR HERE
		
		Shape s3 = new Rectangle(1.0, 2.0, "RED", false);
		System.out.println(s3);
		System.out.println(s3.getArea());
		System.out.println(s3.getPerimeter());
		System.out.println(s3.getColor());
		// System.out.println(s3.getLength()); // ERROR HERE
		
		Rectangle r1 = (Rectangle)s3;
		System.out.println(r1);
		System.out.println(r1.getArea());
		System.out.println(r1.getPerimeter());
		System.out.println(r1.getColor());
		System.out.println(r1.getLength());
		
		Shape s4 = new Square(6.6);
		System.out.println(s4);
		System.out.println(s4.getArea());
		System.out.println(s4.getColor());
		// System.out.println(s4.getSide); // ERROR
		
		Rectangle r2 = (Rectangle)s4;
		System.out.println(r2);
		System.out.println(r2.getArea());
		System.out.println(r2.getColor());
		// System.out.println(r2.getSide); // ERROR
		System.out.println(r2.getLength());
	}
}
