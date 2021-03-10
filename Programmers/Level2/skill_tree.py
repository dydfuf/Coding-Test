def solution(skill, skill_trees):
    answer = 0
    skill_list = []
    for aSkill in skill:
        skill_list.append(aSkill)
    skill_list.reverse()

    for aSkillTree in skill_trees:
        temp_skill_list = skill_list[:]
        valid = True
        for aSkill in aSkillTree:
            if aSkill in temp_skill_list:
                if aSkill == temp_skill_list[-1]:
                    temp_skill_list.pop()
                else:
                    valid = False
                    break

        if valid:
            answer += 1

    return answer


if __name__ == "__main__":
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    print(solution(skill, skill_trees))
