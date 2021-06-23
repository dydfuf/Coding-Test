function solution(lottos, win_nums) {
    var answer = [];
    var count = 0
    var zero = 0
    lottos.map(lotto => {
        if(lotto === 0){
            zero++
        }
        win_nums.map(num => {
            if(lotto === num){
                count++
            }
        })
    })
    var max_count = count+zero
    
    // 최고순위
    if(7-max_count > 5){
        answer.push(6)
    }else{
        answer.push(7-max_count)
    }
    
    if(7-count > 5){
        answer.push(6)
    }else{
        answer.push(7-count)
    }

    return answer;
}