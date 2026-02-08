import 'dart:io';
import 'dart:math';
void main(List<String> arguments) {
  print("Введите число");
  double num1 = double.parse(stdin.readLineSync()!);
  print("Введите еще число");
  double num2 = double.parse(stdin.readLineSync()!);
  print("Введи операцию");
  String op = stdin.readLineSync()!;
  

  switch (op){
  case "+": 
  print({num1+num2});
  break;
   case "-": 
  print({num1-num2});
  break;
   case "*": 
  print({num1*num2});
  break;
  case "!=": 
  print({num1!=num2});
  break;
  case "=": 
  print({num1=num2});
  break;
  case ">": 
  print({num1>num2});
  break;
  case "<": 
  print({num1<num2});
  break;
  case ">=": 
  print({num1>=num2});
  break;
  case "<=": 
  print({num1<=num2});
  break;
  case "==":
  print("Равно: ${num1==num2}");
  break;
      
  case "/":
  if (num1==0  num2==0){
    print("нельзя делить на ноль");
  }else {print({num1/num2}); break;}
  break;

  case "~/":
  if (num1==0  num2==0){
    print("нельзя делить на ноль");
  }else {print({num1/num2}); break;}
  break;

  case "%":
  if (num1==0  num2==0){
    print("нельзя делить на ноль");
  }else {print({num1/num2}); break;}
  break;
      
  case "pow": 
      print(pow(num1,num2));
  break;
      
  case "&&":
    print("Введи True|False");
  bool num1 = bool.parse(stdin.readLineSync()!);
  print("Введи True|False");
  bool num2 = bool.parse(stdin.readLineSync()!);
  print("Выводится: ${num1&&num2}"); 
  break;
  
  case "":
    print("Введи True|False");
  bool num1 = bool.parse(stdin.readLineSync()!);
  print("Введи True|False");
  bool num2 = bool.parse(stdin.readLineSync()!);
  print("Выводится: ${num1||num2}"); 
  break;
      
  case "!":
    print("Введи True|False");
  bool num1 = bool.parse(stdin.readLineSync()!);
  print("Введи True|False ");
  bool num2 = bool.parse(stdin.readLineSync()!);
  print("Выводится: ${!num1}"); 
  break;
  default: print("Неверный выбор");
  }
}
