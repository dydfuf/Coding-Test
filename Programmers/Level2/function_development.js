function solution(progresses, speeds) {
    var answer = [];
    var div = []
    progresses.map((p,idx) => {
        if((100-p)%speeds[idx] === 0){
            div.push((100-p)/speeds[idx])
        }
        else{
            div.push(parseInt((100-p)/speeds[idx]) + 1)
        }
    })
    var temp = parseInt(div[0])
    var count = 0
    div.map((aDiv,idx) => {
        if(parseInt(aDiv) <= temp){
            count++
        }
        else{
            answer.push(count)
            count = 1
            temp = aDiv
        }
    })
    answer.push(count)
    return answer;
}