class Process:
    def __init__(self, id):
        self.id = id
        self.active = True

class CoordinatorElection:
    def __init__(self, num_processes):
        self.num_processes = num_processes
        self.processes = []

    def initialize_processes(self):
        print(f"Number of processes: {self.num_processes}")
        self.processes = [Process(i) for i in range(1, self.num_processes + 1)]

    def election(self):
        print(f"Process {self.processes[self.get_maximum()].id} fails")
        self.processes[self.get_maximum()].active = False
        print("Election initiated by Process 2")
        initiator = 2

        current = initiator
        next_process = (current + 1) % self.num_processes

        while True:
            if self.processes[next_process].active:
                print(f"Process {self.processes[current].id} passes election message to Process {self.processes[next_process].id}")
                current = next_process
            next_process = (next_process + 1) % self.num_processes
            if next_process == initiator:
                break

        coordinator_id = self.get_maximum()
        print(f"Process {self.processes[coordinator_id].id} becomes coordinator")

        current = coordinator_id
        next_process = (current + 1) % self.num_processes

        while True:
            if self.processes[next_process].active:
                print(f"Process {self.processes[current].id} passes coordinator message to Process {self.processes[next_process].id}")
                current = next_process
            next_process = (next_process + 1) % self.num_processes
            if next_process == coordinator_id:
                print("End of Election")
                break

    def get_maximum(self):
        max_id = float('-inf')
        max_index = 0
        for i in range(self.num_processes):
            if self.processes[i].active and self.processes[i].id > max_id:
                max_id = self.processes[i].id
                max_index = i
        return max_index

def main():
    num_processes = 5
    coordinator_election = CoordinatorElection(num_processes)
    coordinator_election.initialize_processes()
    coordinator_election.election()

if __name__ == "__main__":
    main()
