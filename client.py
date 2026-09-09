class BuddyAllocator:
    """Binary Buddy System Memory Allocator."""
    def __init__(self, total_size=1024, min_block=32):
        self.total_size = total_size
        self.min_block = min_block
        self.max_order = 0
        sz = min_block
        while sz < total_size:
            sz *= 2
            self.max_order += 1
        self.free_lists = {i: [] for i in range(self.max_order + 1)}
        self.free_lists[self.max_order].append(0)
        self.allocated = {}

    def allocate(self, size):
        req_order = 0
        sz = self.min_block
        while sz < size and req_order < self.max_order:
            sz *= 2
            req_order += 1

        for order in range(req_order, self.max_order + 1):
            if self.free_lists[order]:
                block = self.free_lists[order].pop(0)
                while order > req_order:
                    order -= 1
                    buddy = block + (self.min_block * (2 ** order))
                    self.free_lists[order].append(buddy)
                self.allocated[block] = req_order
                return block
        return None

    def free(self, block):
        if block not in self.allocated:
            return False
        order = self.allocated.pop(block)
        while order < self.max_order:
            block_size = self.min_block * (2 ** order)
            buddy = block ^ block_size
            if buddy in self.free_lists[order]:
                self.free_lists[order].remove(buddy)
                block = min(block, buddy)
                order += 1
            else:
                break
        self.free_lists[order].append(block)
        return True
