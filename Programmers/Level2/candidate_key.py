from itertools import combinations

def solution(relation):

    rows = list(zip(*relation))

    L = len(relation[0])
    keys = list(range(L))

    candidate_keys = []

    for i in range(1, L+1):
        for comb in combinations(keys, i):

            history = list()
            for aRelation in relation:
                temp = [aRelation[a] for a in comb]

                if temp in history:
                    break
                else:
                    history.append(temp)
            else:
                for aCkey in candidate_keys:
                    if set(aCkey).issubset(set(comb)):
                        break
                else:
                    candidate_keys.append(comb)

    return len(candidate_keys)

if __name__ == "__main__":
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

    print(solution(relation))