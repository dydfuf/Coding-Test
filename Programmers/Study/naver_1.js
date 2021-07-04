function solution(k, rates) {
    var answer = k;

    let arr = []

    //* reates앞에서 부터 순회해서 k보다 큰 것 지우기
    let i_temp = -1
    for(let i = 0; i < rates.length; i += 1){
        if(rates[i] <= k){
            i_temp = i
            break
        }
    }

    //* 모든 rates가 k보다 커서 어떤 것도 살 수 없을 때
    if(i_temp === -1) return k
    //* reates앞에서 살 수 없는것 지우기
    else{
        rates = rates.slice(i_temp, rates.length)
    }
    console.log(rates)

    for(let i = 0; i < rates.length; i += 1){
        for(let j = i+1; j < rates.length; j += 1){
            if(rates[j] - rates[i] <= 0){
                i = j-1
                break
            }
            if(arr.length === 0){
                arr.push([i,j,rates[j] - rates[i]])
            }else{
                let temp = arr[arr.length -1]
                if(i === temp[0] && j > temp[1]){
                    arr.pop()
                    arr.push([i,j,rates[j] - rates[i]])
                }else{
                    arr.push([i,j,rates[j] - rates[i]])
                }
            }
            if(j === rates.length - 1){
                i = j
            }
        }
    }
    if(arr.length === 0) return k
    for(let i = 0; i < arr.length; i += 1){
        answer += arr[i][2]
    }
    return answer;
}