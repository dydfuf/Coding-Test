function solution(s) {
    var answer = [];
    let strlist = s.replace("{{","").replace("}}","").split("},{").map(el => el.split(","))
    let length = []
    strlist = strlist.sort((a,b) => {
        return a.length - b.length
    })
    answer.push(...strlist[0])
    
    for(let i = 1; i < strlist.length; i++){
        for(const r of answer){
            strlist[i] = strlist[i].filter(set => set !== r)
        }
        answer.push(...strlist[i])
    }

    return answer.map(el => parseInt(el));
}