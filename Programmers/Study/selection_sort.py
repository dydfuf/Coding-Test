def solution(sorting_list):

    for i in range(len(sorting_list)):

        
        for j in range(i+1, len(sorting_list)):
            if sorting_list[j] > sorting_list[j+1]:


    return sorting_list

if __name__ == "__main__":
    sorting_list = [5, 4, 3, 2, 1, 8, 7, 9, 6,1]
    print(solution(sorting_list))