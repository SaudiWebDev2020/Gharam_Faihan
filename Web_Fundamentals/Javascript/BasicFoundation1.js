//Print Statment
console.log(swapValues([1,2,3,4]));

// 1

function getTo255() {
    for (var i = 1 ; i <= 255 ; i++){ 
        console.log(i);
    }
}



// 2

function getEven1000() {
    for (var i = 1 ; i <= 1000 ; i++){ 
        if ( i % 2 == 0){
        console.log(i);
        }
    }
}

// 3

function sumOdd5000() {
    var sum = 0;
    for (var i = 1 ; i <= 5000 ; i++){ 
        if ( i % 2 != 0){
            sum+= i;
        }
    }
    console.log(sum);
}

// 4

function iterateAnArray(arr) {
    var sum =0;
    for (var i = 0 ; i < arr.length ; i++){ 
        sum+= arr[i];
    }
    console.log(arr);
    console.log(sum);
}

// 5

function findMax(arr) {
    var max =0;
    for (var i = 0 ; i < arr.length ; i++){ 
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    console.log(arr);
    console.log(max);
}

// 6 

function findAvg(arr) {
    var sum =0;
    for (var i = 0 ; i < arr.length ; i++){ 
        sum+=arr[i];
    }
    console.log(arr);
    console.log(sum/arr.length);
}

// 7 

function arrayOdd() {
    for (var i = 1 ; i <= 50 ; i++){ 
        if (i % 2 != 0) {
            console.log(i);
        }
    }
}

// 8 

function returnArrayCountGreaterThanY(arr, Y){ 
    arrGreaterThanY = [];
    for (var i = 0 ; i <= arr.length-1  ; i++){ 
        if ( arr[i] > Y){ 
            arrGreaterThanY.push(arr[i]);
        }
    }
}

// 9 

function squareArrayVals(arr){ 
    for (var i = 0 ; i <= arr.length-1  ; i++){ 
        squar = Math.sqrt(arr[i]);
        arr[i] = squar;
    }
}

// 10

function zeroOutArrayNegativeVals(arr){
    for (var i = 0 ; i <= arr.length-1  ; i++){ 
        if ( i < 0 ) {
            arr[i] = 0; 
        }
    }
}

// 11 

function printMaxMinAverageArrayVals(arr) { 
    max = Math.max(arr);
    console.log(max);

    min = Math.min(arr);
    console.log(min);

    avg = Math.avg(arr);
    console.log(avg);
}

// 12 

function swapValues(arr) {
    var temp = arr[0];
    arr[0] = arr[arr.length-1];
    arr[arr.length-1] = temp;
    console.log(arr);
}

// 13 

function swapStringForArrayNegativeVals(arr) { 
    for (var i = 0 ; i <= arr.length-1  ; i++){ 
        if ( arr[i] < 0 ){ 
            arr[i] = 'Dojo';
        }
    }
}

