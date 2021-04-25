function solution2(answers) {
    var answer = [];
    let one = [];
    let two = [];
    let three = [];

    for(let i = 0; i < 2000; i++){
        one.push(1,2,3,4,5);
    }

    for(let i = 0; i < 1250; i++){
        two.push(2,1,2,3,2,4,2,5);
    }

    for(let i = 0; i < 1000; i++){
        three.push(3,3,1,1,2,2,4,4,5,5)
    }

    let one_correct = 0;
    let two_correct = 0;
    let three_correct = 0;

    for(let i = 0; i < answers.length; i++){
        if(one[i] === answers[i]){
            one_correct += 1;
        }
        if(two[i] === answers[i]){
            two_correct += 1;
        }
        if(three[i] === answers[i]){
            three_correct += 1;
        }
    }
    let max = Math.max(one_correct, two_correct, three_correct)
    if(one_correct === max){
        answer.push(1)
    }
    if(two_correct === max){
        answer.push(2)
    }
    if(three_correct === max){
        answer.push(3)
    }

    return answer;
}

function solution(answers){
    let answer = [];
    let a1 = [1,2,3,4,5];
    let a2 = [2,1,2,3,2,4,2,5];
    let a3 = [3,3,1,1,2,2,3,3,5,5];

    let a1c = answers.filter((a,i) => a === a1[i % a1.length]).length;
    let a2c = answers.filter((a,i) => a === a2[i % a2.length]).length;
    let a3c = answers.filter((a,i) => a === a2[i % a3.length]).length;
    let max = Math.max(a1c, a2c, a3c);

    if (a1c === max ) {answer.push(1)}
    if (a2c === max ) {answer.push(2)}
    if (a3c === max ) {answer.push(3)}

    return answer
}

let answer_arr = [[1,2,3,4,5], [1,3,2,4,2]]
answer_arr.map(answer => {
    console.log(solution(answer))
})