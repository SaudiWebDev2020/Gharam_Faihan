//1
function makeItBig(arr) {
    for (let index = 0; index < arr.length; index++) {
        if (arr[index] > 0) {
            arr[index] = "big";
        }

    }
    console.log(arr);
}
// 2
function printLowReturnHigh(arr) {
    var low = arr[0];
    var high = 0;

    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < low) {
            low = arr[i];
        } else if (arr[i] > high) {
            high = arr[i];
        }
    }
    console.log("Lowest value is " + low);
    return high;
}
// 3
function printOneReturnOthers(arr) {
    for (var i = 1; i < arr.length; i++) {
        console.log("Element number " + (i + 1) + " is " + arr[i]);
    }
    return arr[0];
}


// 4
function DoubleVision(arr) {
    var newArr = [];
    for (let index = 0; index < arr.length; index++) {
        newArr.push(arr[index] + arr[index]);
    }
    return newArr;
}
//5
function CountPositives(arr) {
    var count = 0;
    for (let index = 0; index < arr.length; index++) {
        if (arr[index] > 0) {
            count++;
        }
    }
    arr.pop();
    arr.push(count);
    return arr;
}
//6
function EvensandOdds(array) {
    for (let index = 0; index < array.length; index++) {
        if (array[index] % 2 != 0 && array[index - 1] % 2 != 0 && array[index - 2] % 2 != 0) {
            console.log("That Odd !")
        }
        else if (array[index] % 2 == 0 && array[index - 1] % 2 == 0 && array[index - 2] % 2 == 0) {
            console.log("Even more so!");
        }

    }
}
//7



function incrementSeconds(arr){
    for (var i=0;i<arr.length;i++){
      if(i % 2 !==0){
        arr[i] = arr[i] + 1; 
      }
      console.log(arr[i]);
    }
    return arr;
  }
  
//8
function previousLengths(arr){
    for (var i=arr.length-1;i>0;i--){
        arr[i] = arr[i-1].length;
    }
    return arr;
  }


//9

function AddSeven(array) {
    var newArr = [];
    for (let index = 0; index < array.length; index++) {
        newArr.push(array[index] + 7);
    }
    return newArr;
}

//10 

function ReverseArray(arr) {

        for (var i = 0; i <= Math.floor((arr.length - 1) / 2); i++) {
            let x = arr[i];
            arr[i] = arr[arr.length - 1 - i];
            arr[arr.length - 1 - i] = x;
        }
        console.log("This is the array "+arr)
 }

//11

function OutlookNegative(arr) {
    var newArr= [] 
    for (let index = 0; index < arr.length; index++) {
        if (arr[index]>0 ){
            newArr.push(-Math.abs(arr[index]))
        } else 
        newArr.push(arr[index])
    }
    console.log("This is the array "+arr)
    console.log("This is the  new array "+newArr)
 }


//12

function AlwaysHungry(array) {
    var count = 0;
    for (let index = 0; index < array.length; index++) {
        if (array[index] == "food") {
            console.log("yummy!")
            count++;
        }
    }
    if (count == 0) {
        console.log("im hungry");
    }
}


//13
function swapTowardCenter(arr){
    var temp = arr[0]; 
    arr[0] = arr[arr.length-1];
    arr[arr.length-1] = temp;
    var temp2 = arr[2];
    arr[2] = arr[arr.length-3];
    arr[arr.length-3] = temp2;
    console.log(arr);
  }

//14

function scaleArray(arr, num) {
    for (let index = 0; index < arr.length; index++) {
        arr[index] = arr[index] * num;
    }
    console.log(arr);
}