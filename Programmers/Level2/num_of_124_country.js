function solution(n) {
    var answer = '';
    while(n > 0){
        n -= 1
        var div = n%3
        if(div == 0){
            answer += '1'
        }
        else if(div == 1){
            answer += '2'
        }
        else if(div == 2){
            answer += '4'
        }
        n = parseInt(n/3)
    }
    answer = answer.split("").reverse().join("")
    return answer;
}