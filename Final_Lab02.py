moore_machine = {
    'A_A': {'output':'A', '0':'A_A', '1':'B_B'},
    'B_A': {'output':'A', '0':'C_C', '1':'D_B'},
    'C_C': {'output':'C', '0':'D_B', '1':'B_B'},
    'D_B': {'output':'B', '0':'B_B', '1':'C_C'},
    'B_B': {'output':'B', '0':'C_C', '1':'D_B'},
    'C_B': {'output':'B', '0':'D_B', '1':'B_B'},
    'D_C': {'output':'C', '0':'B_B', '1':'C_C'},
}

def run_moore(input_string):
    state = 'A_A'  

    output = moore_machine[state]['output']

    for bit in input_string:
        state = moore_machine[state][bit]
        output += moore_machine[state]['output']

    return output

inputs = ["00110", "11001", "1010110", "1011111"]
for s in inputs:
    print(s, "→", run_moore(s))
