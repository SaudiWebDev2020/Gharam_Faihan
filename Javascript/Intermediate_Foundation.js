//1
function sigma(a) {
    var sum = 0;
    for (let index = 0; index <= a; index++) {
        sum = sum + index;
    }
    return sum;
}

//2
function Factorial(a) {
    var sum = 1;
    for (let index = 1; index <= a; index++) {
        sum = sum * index;
    }
    return sum;
}
//4
function SecondtoLast(array) {
    if (array.length <= 1) {
        console.log("Null")
    } else
        console.log(array[array.length - 2])
}

//5 
function NthtoLast(array, num) {
    if (array.length <= num) {
        console.log("Null")
    } else console.log(array[num])
}


//6
function SecondLargest(array) {
    array.sort();
    if (array.length <= 1) {
        console.log("Null")
    } else
            console.log(array[array.length - 1])
}

