// Run by Node.js

/**
 * 5. 잘못된 등수
 * 시험을 치르는데 원래라면 몇 번의 시험을 치건 간에 등수가 같다.
 * 하지만 학생들이 부정행위를 해서 등수를 올렸다
 * 한 시험에서 반드시 한명의 학생만 부정행위를 한다.
 * 한 시험에서 부정행위를 한 학생은 다음 시험에서는 부정 행위를 하지 않는다.
 * 부정행위를 하면 반드시 등수가 오른다
 * 총 3개의 시험 등수가 주어지고
 * 원래의 시험 등수를 출력하는 문제
 */
const readline = require('readline');

(async () => {
    let rl = readline.createInterface({ input: process.stdin });

    let N = null
    let input = []
    let count = -1

    for await (const line of rl) {
        if(!N){
            N = +line
        } else{
            const sp = line.split(" ").map(el => parseInt(el))
            if(isNaN(sp[sp.length - 1])){
                sp.pop()
            }
            input.push(sp)
        }
        count += 1
        if(count === 3) rl.close()
    }

    const solution = (N, input) => {

        let cand1 = new Set()
        let cand2 = new Set()
        let cand3 = new Set()
        // 1st test
        for(let i = 0; i < N; i++){
            let test1 = input[0].slice(0)
            let test2 = input[1].slice(0)
            let test3 = input[2].slice(0)

            let temp1 = test1[i]
            let temp2 = test2[i]
            let temp3 = test3[i]

            test1.splice(i,1)
            test2.splice(i,1)
            test3.splice(i,1)

            for(let j = i; j < N; j++){

                let a1 = test1.slice(0, j)
                let b1 = test1.slice(j)

                let a2 = test2.slice(0, j)
                let b2 = test2.slice(j)

                let a3 = test3.slice(0, j)
                let b3 = test3.slice(j)

                let c1 = a1.concat(temp1).concat(b1)
                let c2 = a2.concat(temp2).concat(b2)
                let c3 = a3.concat(temp3).concat(b3)

                cand1.add(c1.toString())
                cand2.add(c2.toString())
                cand3.add(c3.toString())
            }
        }

        let _arr1 = [...cand1]
        let _arr2 = [...cand2]
        let _arr3 = [...cand3]

        let diff = _arr1.filter(x => _arr2.includes(x)).filter(x => _arr3.includes(x))

        let ans = diff[0]
        for(let i = 0; i < N-1; i++){
            ans = ans.replace(","," ")
        }
        console.log(ans)
    }

    solution(N, input)

    process.exit();
})();
