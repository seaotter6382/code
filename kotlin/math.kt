fun main() {
	println(plus(number1 = 3, number2 = 8))
	println(minus(number1 = 10, number2 = 2))
	println(divide(number1 = 10, number2 = 5))
	println(multi(number1 = 4, number2 = 5))
}

fun plus(number1: Int, number2: Int): String {
    var num3 = number1 + number2
    return ("the sum of $number1 and $number2 is $num3")
}

fun minus(number1: Int, number2: Int): String {
    var num3 = number1 - number2
    return ("the diffrence of $number1 and $number2 is $num3")
} 

fun divide(number1: Int, number2: Int): String {
    var num3 = number1 / number2
    return ("the quotient of $number1 and $number2 is $num3")
}

fun multi(number1: Int, number2: Int): String {
    var num3 = number1 * number2
    return ("the product of $number1 and $number2 is $num3")
}
