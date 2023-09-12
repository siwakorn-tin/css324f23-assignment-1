def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s
    
    def pour(source, target, max_amount):
        if source > 0:
            amount_to_pour = min(source, max_amount - target)
            if amount_to_pour > 0:
                new_source = source - amount_to_pour
                new_target = target + amount_to_pour
                yield ((new_source, new_target, z), amount_to_pour)

    max_x, max_y, max_z = 8, 5, 3

    yield from pour(x, y, max_y)
    yield from pour(x, z, max_z)
    yield from pour(y, x, max_x)
    yield from pour(y, z, max_z)
    yield from pour(z, x, max_x)
    yield from pour(z, y, max_y)

# Example usage:
# for state, amount_poured in successors((8, 0, 0)):
#     print(f"Pour {amount_poured} units: {state}")
