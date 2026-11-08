from __future__ import annotations
from collections import deque
from typing import Literal


class Room:
    def __init__(self, name: str):
        self.name: str = name
        self.left: Room | None = None
        self.right: Room | None = None
        self.parent: Room | None = None
        self.connections: set[Room] = set()

    def set_left_branch(self, left: Room) -> Room:
        return self._set_branch(left, "left")

    def set_right_branch(self, right: Room) -> Room:
        return self._set_branch(right, "right")

    def _set_branch(self, room: Room, side: Literal["left", "right"]) -> Room:
        if not isinstance(room, Room):
            raise ValueError(f"{side.capitalize()} branch should be a Room")

        if room.parent is not None:
            raise ValueError(f"{side.capitalize()} branch already has a parent")

        if getattr(self, side) is not None:
            raise ValueError(f"{side.capitalize()} branch is already set")

        # Check the parent chain to prevent a cycle.
        ancestor = self
        while ancestor is not None:
            if ancestor is room:
                raise ValueError("Adding this room would create a cycle")
            ancestor = ancestor.parent

        room.parent = self
        match side:
            case "left":
                self.left = room
            case "right":
                self.right = room

        # Store the branch connection in both directions.
        self.connections.add(room)
        room.connections.add(self)

        return self

    def add_portal(room_a: Room, room_b: Room) -> Room:
        if not isinstance(room_b, Room):
            raise ValueError("The destination must be a Room instance.")

        if room_a is room_b:
            raise ValueError("A room cannot create a portal to itself.")

        # A portal connects the two rooms in both directions.
        room_a.connections.add(room_b)
        room_b.connections.add(room_a)

        return room_a

    # Traverse the binary tree recursively
    def dfs_recursive(self, level: int = 0):
        print(f"[DFS] Level: {level}, Room Name: {self.name}")

        if self.left is not None:
            self.left.dfs_recursive(level + 1)

        if self.right is not None:
            self.right.dfs_recursive(level + 1)

    # Traverse the binary tree iteratively using a stack.
    def dfs(self):
        stack = [(self, 0)]

        # Use a stack to explore one branch at a time.
        while len(stack) > 0:
            node, level = stack.pop()
            print(f"[DFS] Level: {level}, Room Name: {node.name}")

            # Push right first so the left branch is searched first.
            if node.right is not None:
                stack.append((node.right, level + 1))
            if node.left is not None:
                stack.append((node.left, level + 1))

    # Find the shortest path to the exit using BFS.
    def find_shortest_exit(current_room: Room, exit_room: Room) -> list[Room] | None:
        if not isinstance(exit_room, Room):
            raise ValueError("Exit room must be a Room instance")

        queue: deque[Room] = deque([current_room])
        # The previous room map also tracks which rooms have been visited.
        previous: dict[Room, Room | None] = {current_room: None}

        # Continue until the queue is empty
        while queue:
            current_room = queue.popleft()
            if current_room is exit_room:
                return_path = []
                room: Room | None = current_room

                # Follow previous rooms back to the start, then reverse the path.
                while room is not None:
                    return_path.append(room)
                    room = previous[room]

                return return_path[::-1]

            for neighbor in current_room.connections:
                if neighbor not in previous:
                    # Save how we reached this room and add it to the queue.
                    previous[neighbor] = current_room
                    queue.append(neighbor)

        return None
