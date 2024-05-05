class BullyAlgorithm:
    def __init__(self, numNodes):
        self.numNodes = numNodes
        self.nodes = [True] * numNodes  # Set all nodes to True (up)
        self.coordinator = numNodes

    def node_down(self, nodeId):
        print("Node", nodeId, "is down.")
        self.nodes[nodeId - 1] = False  # Set the failed node to False (down)
        initiatingNode = int(input("Enter the node initiating the election: "))
        self.initiate_election(initiatingNode)

    def initiate_election(self, initiatingNode):
        for i in range(initiatingNode, self.numNodes):
            if self.nodes[i]:
                print("Node", initiatingNode, ": Message sent to Node", (i + 1))
                if i != initiatingNode - 1:
                    print("Node", (i + 1), "responds to Node", initiatingNode, ": OK")
        for i in range(initiatingNode, self.numNodes):
            if self.nodes[i]:
                self.initiate_election(i + 1)
                return
        self.new_coordinator(initiatingNode)

    def new_coordinator(self, failedNode):
        print("Node", failedNode, "is the new coordinator.")
        self.coordinator = failedNode
        for i in range(self.numNodes):
            if self.nodes[i] and i != failedNode - 1:
                print("Node", failedNode, "notifies Node", (i + 1), "about being the new coordinator.")

if __name__ == "__main__":
    numNodes = int(input("Enter the number of nodes: "))
    bully_algorithm = BullyAlgorithm(numNodes)

    failedNode = int(input("Enter the node that is down: "))
    bully_algorithm.node_down(failedNode)
