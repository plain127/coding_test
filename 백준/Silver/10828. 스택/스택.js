const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const N = Number(input[0]);
const stack = [];
const result = [];
for(let i =1; i<=N; i++){
    let cmd = input[i].split(' ');
    if(cmd[0] === 'push'){
        stack.push(cmd[1]);
    }
    else if(cmd[0] === 'pop'){
        if(stack.length == 0){
            result.push(-1);
        }
        else{
            result.push(stack.pop());
        }
    }
    else if (cmd[0] === 'size'){
        result.push(stack.length);
    }
    else if (cmd[0] === 'empty'){
        if(stack.length == 0){
            result.push(1);
        }
        else{
            result.push(0);
        }
    }
    else if(cmd[0] ==='top'){
        if(stack.length == 0){
            result.push(-1);
        }
        else{
            result.push(stack[stack.length-1]);
        }
    }
}

console.log(result.join('\n'));
