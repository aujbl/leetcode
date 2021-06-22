class ThroneInheritance:

    def __init__(self, kingName: str):
        self.order = [kingName]

    def birth(self, parentName: str, childName: str) -> None:
        self.order.insert(self.order.index(parentName)+1, childName)

    def death(self, name: str) -> None:
        self.order.pop(self.order.index(name))

    def getInheritanceOrder(self) -> List[str]:
        return self.order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()