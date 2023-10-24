import random
from typing import Callable, List, Set, Tuple

Dependency = Tuple[str, str]


def blockers_and_blocked(
    task: str, dependencies: List[Dependency]) -> Tuple[Set[str], Set[str]]:
    """Parameters
    ----------
    task
        The test for which we compute blocking and blocked tasks.
    dependencies
        A list of pairs of tasks, where the first element blocks the
        second.
        
    Returns
    -------
    tuple of blockers and blocked
        A tuple of two sets, where the first set contains all tasks
        that block the given task, and the second set contains all
        tasks that are blocked by the given task.
    """
    # YOUR CODE HERE
    blockers = set()
    blocked = set()
    for s, t in dependencies:
        if t == task or s in blockers:
            blockers.add(s)
        if s == task or s in blockers:
            blocked.add(t)
    return blockers, blocked


def generate_cases(seed: int):
    """Generate tests cases using the given seed."""
    rand = random.Random(seed)

    for _ in range(100):
        num_tasks = rand.randint(0, 100)
        tasks = list(map(str, range(num_tasks)))
        dependencies = []

        rand.shuffle(tasks)

        dependencies = [
            (s, t)
            for i, s in enumerate(tasks)
            for t in tasks[i + 1 :]
            if rand.random() > 0.5
        ]

        yield rand.choice(tasks), dependencies


def checksum(implementation: Callable[[str, List[Dependency]], Tuple[Set[str], Set[str]]], seed: int) -> int:
    """Compute a checksum of an implementation of `blockers_and_blocked` and a random seed."""

    result = 0
    for task, dependencies in generate_cases(seed):
        blockers, blocked = implementation(task, dependencies)

        result = hash((result, tuple(sorted(blockers)), tuple(sorted(blocked))))

    return result


if __name__ == "__main__":
    #
    # To help testing, checksum(blockers_and_blocked, 1) should return 2150572700622488023
    #
    result = checksum(blockers_and_blocked, 1)
    print(result)
    assert result == 2150572700622488023
