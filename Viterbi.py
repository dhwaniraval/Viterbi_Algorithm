import sys

# Total states
total_states = 3
state = ['S', 'C', 'H']

# 2-D array state transition values
transition_matrix = [[0, 0.2, 0.8], [0, 0.6, 0.4], [0, 0.3, 0.7]]

# 2-D array observation likelihood values
observation_likelihood = [[0, 0, 0, 0], [0, 0.5, 0.4, 0.1], [0, 0.2, 0.4, 0.4]]

if len(sys.argv) > 1:

    # Input string as observation sequence
    observation_sequence = sys.argv[1]

    # Break the sequence in observation O
    O = ['']
    for i in range(0, len(observation_sequence)):
        O.append(int(observation_sequence[i]))

    # n = 3
    time = len(observation_sequence) + 1

    viterbi = [[0] * time for i in range(total_states)]
    backTrack = [[0] * time for i in range(total_states)]

    # Initialization, fill the values for observation 1 from start state s to total_states
    for s in range(1, total_states):
        viterbi[s][1] = transition_matrix[0][s] * observation_likelihood[s][O[1]]
        backTrack[s][1] = 0  # or should it be 0 or s?

    # s is state, t is observation time, i iterates through all states from 1 to total_states
    for t in range(2, len(O)):
        for s in range(1, total_states):
            max = 0
            argmax = 0

            for i in range(1, total_states):
                if max < viterbi[i][t - 1] * transition_matrix[i][s] * observation_likelihood[s][O[t]]:
                    max = viterbi[i][t - 1] * transition_matrix[i][s] * observation_likelihood[s][O[t]]
                    argmax = i

            viterbi[s][t] = max
            backTrack[s][t] = argmax

    best_path_pointer = []
    for i in range(0, len(O)):
        best_path_pointer.append(0)

    max = 0
    agrmax = 0
    for i in range(1, total_states):
        if max < viterbi[i][len(O) - 1]:
            max = viterbi[i][len(O) - 1]
            argmax = i

    best_path_probability = max;
    best_path_pointer[len(O) - 1] = argmax

    for i in range(len(O) - 1, 1, -1):
        best_path_pointer[i - 1] = backTrack[best_path_pointer[i]][i]

    most_likely_sequence = ""
    for i in range(1, len(best_path_pointer)):
        most_likely_sequence = most_likely_sequence + " " + state[best_path_pointer[i]]

    print("\nGiven Observation Sequence = " + observation_sequence)
    print("Most Likely Weather Sequence = " + most_likely_sequence)
    print("Most Likely Probability : " + str(best_path_probability))
