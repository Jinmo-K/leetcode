# Store changes only to prevent going over memory limit 
class SnapshotArray:

    def __init__(self, length: int):
      self.curr_id = 0
      self.changes = {}
      self.snapshots = []

    def set(self, index: int, val: int) -> None:
      self.changes[index] = val

    def snap(self) -> int:
      self.snapshots.append(self.changes.copy())
      self.curr_id += 1
      return self.curr_id - 1

    def get(self, index: int, snap_id: int) -> int:
      if index in self.snapshots[snap_id]:
        return self.snapshots[snap_id][index]
      else:
        return 0