let operation = prompt("select an operation to perform: ")

let num1 = parseInt(prompt("First Number: "))
let num2 = parseInt(prompt("Second Number: "))

if (operation == "+") {
    console.log(num1 + num2) 
    //return num1 + num2
} else if (operation == "-") {
    console.log(num1 - num2) 
    //return num1 - num2
} else if (operation == "*") {
    console.log(num1 * num2)
    //return num1 * num2
} else if (operation == "/") {
    console.log(num1 / num2)
    //return num1 / num2 
}