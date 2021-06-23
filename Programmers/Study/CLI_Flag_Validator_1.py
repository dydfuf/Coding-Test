def check_string(param):
    if param.isalpha():
        return True
    else:
        return False


def check_number(param):
    if param.isnumeric():
        return True
    else:
        return False


def solution(program, flag_rules, commands):
    answer = True

    rules_dash = []
    rules_req = []

    for rules in flag_rules:
        spt_rule = rules.split(" ")
        rules_dash.append(spt_rule[0])
        rules_req.append(spt_rule[1])

    for command in commands:
        print("command  : ",command)
        split_cmd = command.split(" ")

        if split_cmd[0] != program:
            # 올바르지 않은 프로그램 이름
            return False
        else:
            split_cmd.pop(0)
            print(split_cmd)
            while len(split_cmd) > 2:
                if split_cmd[0] in rules_dash:
                    if rules_req[rules_dash.index(split_cmd[0])] == "STRING":
                        # split_cmd[1] 이 String 인지 check
                        if check_string(split_cmd[1]):
                            split_cmd.pop(0)
                            split_cmd.pop(0)
                        else:
                            return False

                    elif rules_req[rules_dash.index(split_cmd[0])] == "NUMBER":
                        # split_cmd[1] 이 Number 인지 check
                        if check_number(split_cmd[1]):
                            split_cmd.pop(0)
                            split_cmd.pop(0)
                        else:
                            return False

                    elif rules_req[rules_dash.index(split_cmd[0])] == "NULL":
                        # split_cmd[1] 이 NULL 인지 check
                        if split_cmd[1][0] == "-":
                            split_cmd.pop(0)
                        else:
                            return False

                else:
                    return False

            print(split_cmd)

    return answer


if __name__ == "__main__":
    arr_program = ["line", "line"]
    arr_flag_rules = [["-s STRING", "-n NUMBER", "-e NULL"], ["-s STRING", "-n NUMBER", "-e NULL"]]
    arr_commands = [["line -n 100 -s hi -e", "lien -s Bye"], ["line -s 123 -n HI", "line fun"]]
    for program, flag_rules, commands in zip(arr_program, arr_flag_rules, arr_commands):
        print(solution(program, flag_rules, commands))
