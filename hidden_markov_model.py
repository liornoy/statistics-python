import random

START = 1
TOSS_FAKE = 2
TOSS_FAIR = 3
NEXT_FAKE = 4
NEXT_FAIR = 5
FAKE = 6
FAIR = 7
CUBES_OUTPUT_FILE_NAME="CUBES_OUT"
TOSS_OUTPUT_FILE_NAME = "TOSS_OUT"
ERR = -1
SEED = 10
DEFAULT_CHAR = "X"
CUBES_MAP = dict([(6,"U"),(7,"F")])

random.seed(SEED)


def state(s):
    return {
        START: [(FAKE, 0.5), (FAIR, 0.5)],
        TOSS_FAKE: [
            ("1", 0.1),
            ("2", 0.1),
            ("3", 0.1),
            ("4", 0.1),
            ("5", 0.1),
            ("6", 0.5),
        ],
        TOSS_FAIR: [
            ("1", 0.1666),
            ("2", 0.1666),
            ("3", 0.1666),
            ("4", 0.1666),
            ("5", 0.1666),
            ("6", 0.1666),
        ],
        NEXT_FAKE: [(FAKE, 0.9), (FAIR, 0.1)],
        NEXT_FAIR: [(FAKE, 0.95), (FAIR, 0.05)],
    }[s]


def simulate_prob(probs):
    if is_sum_one(probs) == False:
        return ERR
    prob_prefix_sum = prefix_sum_arr(probs)
    rnd = random.uniform(0, 1)
    return get_chosen(prob_prefix_sum, rnd)


def is_sum_one(probs):
    return sum(probs) == 1


def prefix_sum_arr(probs):
    if len(probs) <= 1:
        return probs

    prob_p = [probs[0]]
    for p in probs[1:]:
        prob_p.append(prob_p[-1] + p)
    return prob_p


def get_chosen(prob_p, rnd):
    if len(prob_p) <= 1:
        return 0
    for i, p in enumerate(prob_p):
        if rnd <= p:
            return i
    return ERR


def get_probs(q):
    probs = []
    for desc, prob in q:
        probs += [prob]
    return probs


def draw_state(s):
    states = state(s)
    i = simulate_prob(get_probs(states))
    return states[i][0]


def run_turn(cube):
    toss_type = TOSS_FAIR if cube == FAIR else TOSS_FAKE
    next_type = NEXT_FAIR if cube == FAIR else NEXT_FAKE
    toss = draw_state(toss_type)
    next_cube = draw_state(next_type)
    return toss, next_cube


def write_list(item_list, f_name):
    f = open(f_name, "w")
    f.write("\n".join(str(item) for item in item_list))
    f.close()

def translate_symbol(item_list,mapping,default_val):
    t = []
    for item in item_list:
        t += [mapping.get(item,default_val)]
    return t
    
def run_simulation(N):
    cubes = []
    tosses = []

    # Drawing the first cube
    cube = draw_state(START)

    # Simulate N games
    for _ in range(N):
        toss, next_cube = run_turn(cube)
        cubes += [cube]
        tosses += [toss]
        cube = next_cube

    write_list(translate_symbol(cubes,CUBES_MAP,DEFAULT_CHAR), CUBES_OUTPUT_FILE_NAME)
    write_list(tosses, TOSS_OUTPUT_FILE_NAME)
   
run_simulation(10)