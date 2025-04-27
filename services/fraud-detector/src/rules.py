from collections import defaultdict, deque

VELOCITY_LIMIT = 5
VELOCITY_WINDOW = 60

_user_windows: dict[str, deque] = defaultdict(deque)

def check_velocity(user_id: str, timestamp: float) -> bool:
    """Returns True if transaction looks suspicious."""
    window = _user_windows[user_id]
    now = timestamp


    while window and now - window[0] > VELOCITY_WINDOW:
        window.popleft()

    window.append(now)
    return len(window) > VELOCITY_LIMIT