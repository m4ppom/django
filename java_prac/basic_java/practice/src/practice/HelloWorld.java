package practice;

import java.util.Scanner;

public class HelloWorld {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Hello World");
		System.out.println("주석하는법?");
		int marsa;
		final int MARSA2 = 2;
		final double PI = 3.1415926535;
		
		double circleArea;
		circleArea = 3*3*PI;
		
		int i1 = 5;
		int i2 = 3;
		int i3 = 4;
		
		int i4 = ++i3;
		System.out.println(i4);
		
		int i5 = i3++;
		
		System.out.println(i5);
		System.out.println(i3);
		
		
		int ii = 10;
		int jj = 10;
		System.out.println(ii == jj);
		
		if (i1 > i2) {
			System.out.println("li is bigger than l2");
		}
		else {
			
		}
		int value = 1;
		
		switch(value) {
			case 1:
				System.out.println("1");
			case 3:
				System.out.println("3");
				break;
			default :
				System.out.println("다른숫자"); // 걸린거부터 나머지 다 출력해
		}
		// 멈추게하려면 break 써줘야함.
		int value2 = 0;
		Scanner scan = new Scanner(System.in);
		do {
			value = scan.nextInt();
			System.out.println("입력받은값:"+value);
		}
		while(value != 10);
		
		
		// for 문
		for (int i = 1; i<=100; i++) {
			System.out.println("값"+value);
		}
		
	}
	

}
