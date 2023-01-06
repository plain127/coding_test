const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const N = Number(input[0]);
const maxNum = 2000000;
class Queue{
    constructor(size){
        this.data =[];
        this.size = size;
        this.length = 0;
        this.front = 0;
        this.rear = -1;
    }
    isEmpty(){
       return (this.length == 0);
    }
    enqueue(item){
        if (this.length<this.size){
            this.rear++;
            this.data[this.rear%this.size] = item;
            this.length++;
        }
    }
    addFront(item){
        if(this.length<this.size){
            this.front--;
            this.data[this.front%this.size] = item;
            this.length++;
        }
    }
    dequeue(){
        if(!this.isEmpty()){
            const value = this.peek();
            this.data[this.front%this.size] = null;
            this.front++;
            this.length--;
            return value;
        }
    }
    deleteRear(){
        if(!this.isEmpty()){
            const value = this.back();
            this.data[this.rear%this.size] = null;
            this.rear--;
            this.length--;
            return value;
        }
    }
    peek(){
        if(!this.isEmpty()){
            return this.data[this.front%this.size];
        }
    }
    back(){
        return this.data[this.rear%this.size];
    }
}

const q = new Queue(maxNum);
const result = [];

for(let i=1;i<=N;i++){
    let cmd = input[i].split(' ');
    if (cmd[0]==='push_back'){
        q.enqueue(cmd[1]);
    }
    else if(cmd[0] === 'push_front'){
        q.addFront(cmd[1]);
    }
    else if(cmd[0] === 'pop_front'){
        if(q.length == 0){
            result.push(-1);
        }
        else{
        result.push(q.dequeue());
        }
    }
    else if(cmd[0] === 'pop_back'){
        if(q.length == 0){
            result.push(-1);
        }
        else{
        result.push(q.deleteRear());
        }
    }
    else if(cmd[0] === 'size'){
        result.push(q.length);
    }
    else if(cmd[0] === 'empty'){
        if(!q.isEmpty()){
            result.push(0);
        }
        else{
            result.push(1);
        }
    }
    else if(cmd[0] ==='front'){
        if(!q.isEmpty()){
            result.push(q.peek());
        }
        else{
            result.push(-1);
        }
    }
    else if(cmd[0] === 'back'){
        if(!q.isEmpty()){
            result.push(q.back());
        }
        else{
            result.push(-1)
        }
    }
}   

console.log(result.join('\n'));
