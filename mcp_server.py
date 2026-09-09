import sys
import json
from client import BuddyAllocator

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "alloc_and_free":
        alloc = BuddyAllocator(params.get("total", 1024), params.get("min", 32))
        blocks = [alloc.allocate(sz) for sz in params.get("sizes", [])]
        return {"blocks": blocks}
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == '__main__':
    main()
