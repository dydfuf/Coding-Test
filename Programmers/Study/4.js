// Run by Node.js
/**
 * 4. 뒤통수가 따가워
 * N명의 사람이 각자 의 자리에서 일정한 높이에 올라있다
 * 반드시 모든 사람은 왼쪽에서 오른쪽을 보고
 * 자신보다 높은 사람이 앞에 있다면 그 다음 사람을 볼 수 없다.
 * 즉, a가 b를 보려면 a와 b사이에 있는 모든 사람의 높이는 a,b보다 작아야 한다.
 */
const readline = require('readline');

(async () => {
    let rl = readline.createInterface({ input: process.stdin });

    let N = null
    let data = null
    let count = 0

    for await (const line of rl) {
        if(!N){
            N = +line
        } else{
            const sp = line.split(" ").map(el => parseInt(el))
            if(isNaN(sp[sp.length - 1])){
                sp.pop()
            }
            data = sp
        }
        count += 1
        if(count === 2){
            rl.close()
        }
    }

    const solution = (N, data) => {

        let _arr = new Array(N).fill(0)

        for(let i = 0; i < N; i++){
            let now = data[i]
            for(let j = i+1; j < N; j++){
                _arr[j] += 1
                if(data[j] >= now) break
            }
        }

        let str = _arr.toString()
        for(let i = 0; i < N-1; i++){
            str = str.replace(","," ")
        }
        console.log(str)
    }

    solution(N, data)

    process.exit();
})();
