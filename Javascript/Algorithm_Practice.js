
//1
function printodd(){
    for (let index = 0; index < 20; index++) {
        if(index%2 !=0){
            console.log(index);
        }
    }
}


//2

function sumPrint(){
    var sum = 0;
    for (var x = 0 ; x<=5;x++) {
        sum= sum + x;
        console.log("Num :"+x+" sum :"+sum);
    }
}
sumPrint()