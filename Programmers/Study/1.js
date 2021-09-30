// Run by Node.js
/**
 * 1. 사장님 도박은 재미로 하셔야 합니다.
 * 1줄씩 입력 되고 입력된 모든 값을 더해서 리턴
 * */

const readline = require('readline');

(async () => {
    let rl = readline.createInterface({ input: process.stdin });

    let answer = 0

    for await (const line of rl) {
        let input = +line


        if(input === -1){
            rl.close()
        } else{
            answer += input
        }
    }

    console.log(answer)

    process.exit();
})();
