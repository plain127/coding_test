const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = Number(input[0]);
const arr = [];
for(let i=1; i<=N;i++){
    arr.push(Number(input[i]));
}

function bubble_sort(A){
    const n = A.length;
    for(let i = n-1; i>0; i--){
        let bChanged = false;
        for(let j = 0; j<i; j++){
            if(A[j]>A[j+1]){
                let tmp = A[j];
                A[j] = A[j+1];
                A[j+1] = tmp;
                bChanged = true;
            }
        }
        if(!bChanged){
            break;
        }
    }
}


bubble_sort(arr);

console.log(arr.join(""));
