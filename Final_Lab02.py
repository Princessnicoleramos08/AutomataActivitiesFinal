moore_machine = {
    'A_A': {'0': 'A_A', '1': 'B_B'},
    'B_B': {'0': 'C_A', '1': 'B_B'},
    'C_A': {'0': 'D_B', '1': 'E_C'},
    'D_B': {'0': 'D_C', '1': 'C_C'},
    'E_C': {'0': 'B_C', '1': 'C_C'},
    'D_C': {'0': 'D_C', '1': 'C_C'},
    'C_C': {'0': 'D_B', '1': 'E_C'},
    'B_C': {'0': 'C_A', '1': 'B_B'},
}

state_output = {
    'A_A': 'A',
    'B_B': 'B',
    'C_A': 'A',
    'D_B': 'B',
    'E_C': 'C',
    'D_C': 'C',
    'C_C': 'C',
    'B_C': 'C',
}

def process_input(input_string):
    current_state = 'A_A'
    output_sequence = [state_output[current_state]]
    for symbol in input_string:
        current_state = moore_machine[current_state][symbol]
        output_sequence.append(state_output[current_state])
    return ''.join(output_sequence)

inputs = ["00110", "11001", "10110", "101111"]
for inp in inputs:
    print(f"Input: {inp} → Output: {process_input(inp)}")
