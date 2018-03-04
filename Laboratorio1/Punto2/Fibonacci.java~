import java.util.Scanner;

public class Fibonacci {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		System.out.print("Introduzca el n-esimo numero de la serie de Fibonnaci que desea calcular: ");
		double n = sc.nextInt();
		double n1 = 0;
		double n2 = 1;

		if (n > 1) {
			for (double i = 0; i < n - 1; i++) {
				n2 = n1 + n2;
				n1 = n2 - n1;
			}
		} else if (n == 0) {
			n2 = 0;
		} else if (n == 1) {
			n2 = 1;
		} else {
			System.out.println("Error, ingrese un valor mayor o igual a 0");
		}

		byte b = (byte) n2;
		System.out.println("byte: " + b);
		short s = (short) n2;
		System.out.println("short: " + s);
		int i = (int) n2;
		System.out.println("int: " + i);
		long l = (long) n2;
		System.out.println("long: " + l);
		float f = (float) n2;
		System.out.println("float: " + f);
		System.out.println("double: " + n2);
	}
}

/*
 * Se calculo el n-esimo termino de la serie de Fibonacci con diferentes tipos de variables, con el fin de hallar el overflow para cada caso.
 * A continuación se presenta el tipo de variable junto al valor n que provoco overflow.
 * 
 * byte 	n=16, 	resultado = -37 
 * short 	n=26, 	resultado = -9679 
 * int 		n=47, 	resultado = -1323752223 
 * long 	n=93, 	resultado = -6246583658587674878 
 * float 	n=187,	resultado = Infinity 
 * double 	n=1477, resultado = Infinity
 * 
 */