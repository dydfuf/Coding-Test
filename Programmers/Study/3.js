// Run by Node.js개
/**
 * 3. 도미노를 세우자
 * 작은숫자 순서대로 정렬되어 있던 도미노를 누군가 임의로 순서를 바꾸어 놓았다.
 * 예를들어
 * 1 2 3 4 5
 * 를
 * 1 3 2 4 5 로 바꾸었다면
 * 도미노를 2개 바꾼것
 *
 * 입력이 주어졌을때 몇개의 도미노가 바뀐것일까
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
        // 현재 조각이 다음 조각보다 크기가 큰 경우 => 해당하는 조각을 한칸 앞으로 전진
        // 순서와 크기가 맞지 않는 조각을 빼서? 해당 조각보다 한 칸 앞에 둔다?


        let oriArr = data.map(el => +el)
        oriArr.sort((a,b) =>{
            return a - b
        })
        data = data.map(el => +el)

        let cnt = 0

        for(let i = 0; i < N; i++){
            if(oriArr[i] !== data[i]){
                cnt += 1
            }
        }

        return cnt
    }

    console.log(solution(N, data))

    process.exit();
})();

