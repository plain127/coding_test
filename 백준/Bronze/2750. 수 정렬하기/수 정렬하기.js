const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const N = Number(input[0]);
const arr = [];
for(let i=1; i<=N;i++){
    arr.push(Number(input[i]));
}

function selection_sort(A){
    const n = A.length;
    for(let i=0; i<n-1; i++){
        let least = i;
        for(let j = i+1; j<n; j++){
            if(A[j]<A[least]){
                least = j;
            }
        }
        let tmp = A[i];
        A[i] = A[least];
        A[least] = tmp;
    }
}


selection_sort(arr);

console.log(arr.join(""));
