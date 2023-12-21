import os
from collections import deque
from copy import deepcopy

from day20.modules import FlipFlop, Conjunction, Broadcast, Button


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    inputs = read_input(file_name)
    networks = {}
    for line in inputs:
        left, right = line.split(" -> ")

        name = left
        if left == "broadcaster":
            networks[left] = Broadcast(left)

        elif left.startswith("%"):
            name = name[1:]
            networks[name] = FlipFlop(name)
        elif left.startswith("&"):
            name = name[1:]
            networks[name] = Conjunction(name)

        connected_modules = right.split(", ")
        for module in connected_modules:
            networks[name].next_modules.append(module)

    for k, v in networks.items():
        for module in v.next_modules:
            if networks.get(module) and isinstance(networks[module], Conjunction):
                networks[module].previous_modules[k] = "low"

    return networks


def is_equal_to_original(networks, original_networks):
    for k, v in networks.items():
        if isinstance(v, FlipFlop):
            if v.state != original_networks[k].state:
                return False

        if isinstance(v, Conjunction):
            if v.previous_modules != original_networks[k].previous_modules:
                return False

    return True


def push_button(networks):
    button = Button(name="button", next_modules=["broadcaster"])
    results = button.propagate()
    pulse_queue = deque([results])
    high_pulses, low_pulses = 0, 0

    while pulse_queue:
        pulse = pulse_queue.popleft()
        # print(pulse)

        from_module = pulse["from"]
        to_module = pulse["to"]
        pulse_type = pulse["pulse_type"]
        # print(f"{from_module} -{pulse_type}->  {to_module}")
        if pulse_type == "high":
            high_pulses += 1
        else:
            low_pulses += 1

        if to_module == "rx":
            if pulse_type == "low":
                raise Exception("low pulse received")
        if not networks.get(to_module):
            # print(f"sending to test module {to_module}")
            continue

        pulses = networks[to_module].propagate(pulse_type=pulse_type, received_from=from_module)
        for pulse in pulses:
            pulse_queue.append(pulse)

    return {"high_pulses": high_pulses, "low_pulses": low_pulses, "networks": networks}


def simulate(networks, total_button_pressed=1000):
    original_inputs = deepcopy(networks)
    button_pressed = 0
    high_pulses, low_pulses = 0, 0

    while button_pressed < total_button_pressed:
        # print(f"<<<<<<<<<   Button pressed: {button_pressed} >>>>>>>>>>>")
        result = push_button(networks=networks)
        button_pressed += 1

        high_pulses += result["high_pulses"]
        low_pulses += result["low_pulses"]
        networks = result["networks"]

        flip_flops = [network for network in networks.values() if isinstance(network, FlipFlop)]
        off_flip_flops = [flip_flop for flip_flop in flip_flops if flip_flop.state == "off"]

        is_all_off = len(off_flip_flops) == len(flip_flops)
        if is_all_off:
            # print("All lights are off")
            total_high_pulses = (high_pulses * total_button_pressed) / button_pressed
            total_low_pulses = (low_pulses * total_button_pressed) / button_pressed
            return {
                "button_pressed": button_pressed,
                "high_pulses": int(total_high_pulses),
                "low_pulses": int(total_low_pulses),
            }

        is_equal = is_equal_to_original(networks, original_inputs)
        if is_equal:
            # print("Networks are equal to original")
            total_high_pulses = (high_pulses * total_button_pressed) / button_pressed
            total_low_pulses = (low_pulses * total_button_pressed) / button_pressed
            return {
                "button_pressed": button_pressed,
                "high_pulses": int(total_high_pulses),
                "low_pulses": int(total_low_pulses),
            }

    return {"button_pressed": button_pressed, "high_pulses": high_pulses, "low_pulses": low_pulses}


def solve_part1(inputs):
    result = simulate(inputs)
    return result["high_pulses"] * result["low_pulses"]


def solve_part2(inputs):
    pass


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("input.txt", part=1)
    # assert solve(".txt", part=1) == 1020211150
    # solve("demo_input.txt", part=1)
