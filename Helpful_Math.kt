fun main() {
    val s = readLine() ?: ""
 
    val numbers = mutableListOf<Int>()
 
    for (char in s) {
        if (char != '+') {
            numbers.add(char.digitToInt())
        }
    }
    numbers.sort()
    val result = numbers.joinToString("+")
    println(result)
}