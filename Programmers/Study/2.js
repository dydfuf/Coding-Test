// Run by Node.js턴
/**
 * 2. 반 별로 줄서기
 * 문자열이 들어오고 인접한 것 끼리 없에기
 * ex) aaabbbcda => abcda
 * 이때 a는 한곳에 모여있지 않으므로 탈락
 * 각 알파벳을 순서대로 짝수팀 홀수팀 나눔
 * 따라서 잘 인접한 bcd중에서 짝수팀 홀수팀 개수 세서 이긴팀 출력
 * 단 무승부 없다
 * 반은 반드시 짝수개
 * */

const readline = require('readline');

(async () => {
    let rl = readline.createInterface({ input: process.stdin });

    let input = null

    for await (const line of rl) {
        input = line
        rl.close();
    }

    const solution = (str) => {
        const _arr = str.split("")

        const odd = ["a","c","e","g","i","k","m","o","q","s","u","w","y"]
        const even = ["b","d","f","h","j","l","n","p","r","t","v","x","z"]
        const validAlpha = []

        for(let i = 0; i < _arr.length; i++){
            let now = [_arr[i], 0]
            for(let j = i; j < _arr.length; j++){
                if(now[0] === _arr[j]) now[1]+=1
                else break
            }
            if(validAlpha.includes(now[0])){
                validAlpha.splice(validAlpha.indexOf(now[0]), 1)
            } else validAlpha.push(now[0])
            i += now[1]-1
        }

        let oddCnt = 0
        let evenCnt = 0


        validAlpha.forEach(item => {
            if(odd.includes(item)) oddCnt+=1
            if(even.includes(item)) evenCnt+=1
        })

        if(oddCnt > evenCnt) console.log("W")
        else console.log("B")
    }

    solution(input)

    process.exit();
})();
