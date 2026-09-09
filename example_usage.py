from client import BuddyAllocator

def main():
    print("=== Testing Buddy System Memory Allocator ===")
    alloc = BuddyAllocator(total_size=512, min_block=32)
    b1 = alloc.allocate(60)
    print("Allocated 60B at block offset:", b1)
    assert b1 is not None

    b2 = alloc.allocate(100)
    print("Allocated 100B at block offset:", b2)
    assert b2 is not None

    assert alloc.free(b1) is True
    assert alloc.free(b2) is True
    print("Buddy Memory Allocator verified successfully!")

if __name__ == '__main__':
    main()
