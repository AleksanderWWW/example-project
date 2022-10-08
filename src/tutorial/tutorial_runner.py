from dataclasses import dataclass


@dataclass
class Runner:
    id: str
    name: str

    def run_tutorial(self, tutorial: "Tutorial") -> int:
        if not isinstance(tutorial, Tutorial):
            raise TypeError(f"Expected tutorial type to be 'Tutorial." f"Got {type(tutorial)} instead")

        print(f"{self} running {tutorial}")
        status = tutorial.run()
        print(f"{self} finished running {tutorial}")
        return status


@dataclass
class Tutorial:
    id: str
    name: str

    def run(self) -> int:
        print(f"{self} doing some tasks...")
        status_code = 0
        return status_code
