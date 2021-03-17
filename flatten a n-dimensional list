flatten_list=[]
def flatten(initial_list):
    for i in initial_list:
        try:
            flatten(i)
        except TypeError:
            flatten_list.append(i)


flatten(list)
print(final_list)
