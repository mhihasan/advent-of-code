class Module:
    def __init__(self, name, next_modules=None):
        self.name = name
        self.next_modules = next_modules or []

    def propagate(self, **kwargs):
        raise NotImplementedError


class FlipFlop(Module):
    def __init__(self, name, next_modules=None):
        super().__init__(name, next_modules)
        self.state = "off"

    def propagate(self, *, pulse_type=None, **kwargs):
        if pulse_type == "high":
            return []

        assert pulse_type == "low"

        if self.state == "off":
            self.state = "on"
            return [
                {
                    "from": self.name,
                    "pulse_type": "high",
                    "to": module,
                }
                for module in self.next_modules
            ]
        elif self.state == "on":
            self.state = "off"
            return [
                {
                    "from": self.name,
                    "pulse_type": "low",
                    "to": module,
                }
                for module in self.next_modules
            ]


class Conjunction(Module):
    def __init__(self, name, next_modules=None):
        super().__init__(name, next_modules)
        self.previous_modules = {}

    def propagate(self, *, pulse_type, received_from, **kwargs):
        # update memory for that input
        self.previous_modules[received_from] = pulse_type

        all_high = all(x == "high" for x in self.previous_modules.values())
        if all_high:
            return [
                {
                    "from": self.name,
                    "pulse_type": "low",
                    "to": module,
                }
                for module in self.next_modules
            ]
        else:
            return [{"from": self.name, "pulse_type": "high", "to": module} for module in self.next_modules]


class Broadcast(Module):
    def __init__(self, name="broadcaster", next_modules=None):
        super().__init__(name, next_modules)

    def propagate(self, *, pulse_type, **kwargs):
        signals = []
        for module in self.next_modules:
            signals.append(
                {
                    "from": self.name,
                    "pulse_type": pulse_type,
                    "to": module,
                }
            )
        return signals


class Button(Module):
    def __init__(self, name="button", next_modules=None):
        super().__init__(name, next_modules)

    def propagate(self, pulse_type="low", **kwargs):
        assert len(self.next_modules) == 1
        # self.next_modules[0].propagate(pulse_type=pulse_type)
        return {
            "from": self.name,
            "pulse_type": pulse_type,
            "to": self.next_modules[0],
        }


class TestModule(Module):
    def __init__(self, name):
        super().__init__(name, [])

    def propagate(self, *, pulse_type=None, **kwargs):
        raise Exception("TestModule should not be called")
