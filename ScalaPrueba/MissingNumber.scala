// Clase que representa el conjunto de los primeros 100 números
class NumberSet(start: Int, end: Int) {
  private var numbers = (start to end).toSet // Se establece el conjunto de los primeros 100 números naturales
  // Método para extraer un número del conjunto
  def extract(num: Int): Unit = {
    if (numbers.contains(num)) {
      numbers = numbers - num 
    } else {
      println(s"El número $num no existe en el conjunto.") // Si x>100 o x<1, por lo tanto, no existe
    }
  }
  // Método para calcular el número que falta en el conjunto de los primeros 100 números. 
  def findMissingNumber(): Int = {
    val totalSum = (start to end).sum // Suma de todos los numeros del conjunto = 5050
    val currentSum = numbers.sum //  numbers = numbers - num 
    totalSum - currentSum // Operación para lograr encontrar el número faltante. 
  }
}

// Objeto principal con el método main tradicional
object MissingNumber {
  def main(args: Array[String]): Unit = {
    
    if (args.length != 1) { // Validamos que se pase exactamente un argumento
      println("Uso: MissingNumber <numero_a_extraer>")
      sys.exit(1)
    }

    val userInput = try { // Intentamos convertir el argumento a un número entero
      args(0).toInt
    } catch {
      case _: NumberFormatException =>
        println("Error: el argumento debe ser un número entero.")
        sys.exit(1)
    }

    if (userInput < 1 || userInput > 100) { // Verifica que el número esté entre 1 y 100
      println("El número debe estar entre 1 y 100.")
      sys.exit(1)
    }

    val numberSet = new NumberSet(1, 100) // Conjunto de los primeros 100 numeros naturales
    numberSet.extract(userInput) // Uso del Método extract

    val missingNumber = numberSet.findMissingNumber() // Calculamos el número faltante

    // Mostramos el resultado
    println(s"Se extrajo el número: $userInput")
    println(s"El número faltante es: $missingNumber")
  }
}

