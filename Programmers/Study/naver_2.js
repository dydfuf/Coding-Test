function solution(money, cost) {
    var answer = -1;
    let arr = []
    //* 모든 cost가 money보다 큰 경우
    let max_cost = Math.min(...cost)
    if(max_cost > money){
        return 0
    }
    for(let i = 0; i < cost.length; i += 1){
        let temp = 0
        for(let j = i; j < cost.length; j+= 1){
            temp += cost[j]
            if(temp < money){
                arr.push(j-i)
            }
        }
    }
    answer = Math.max(...arr) + 1
    return answer;
}