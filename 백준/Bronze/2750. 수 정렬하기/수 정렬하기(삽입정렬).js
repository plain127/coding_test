const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = Number(input[0]);
const arr = [];
for(let i=1; i<=N;i++){
    arr.push(Number(input[i]));
}

function insertion_sort(A){
    const n = A.length;
    for(let i=1; i<n; i++){
       let key = A[i];
       j = i-1;
       while(j>=0 && A[j]>key){
        A[j+1]=A[j];
        j--;
       }
       A[j+1] = key;
    }
}


insertion_sort(arr);

console.log(arr.join(""));
