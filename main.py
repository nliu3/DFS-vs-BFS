from room import Room


def print_path(path):
    if path is None:
        print("No path found.")
    else:
        print(" -> ".join(room.name for room in path))
        print(f"Total steps: {len(path) - 1}")


def main():
    # Create dungeon rooms
    entrance = Room("Entrance")

    collapsed_gallery = Room("Collapsed Gallery")
    iron_watch = Room("Iron Watch")

    moss_library = Room("Moss Library")
    flooded_crossing = Room("Flooded Crossing")
    whisper_archive = Room("Whisper Archive")
    clockwork_study = Room("Clockwork Study")
    broken_observatory = Room("Broken Observatory")
    sunken_chapel = Room("Sunken Chapel")
    echo_well = Room("Echo Well")
    rusted_gate = Room("Rusted Gate")
    forgotten_armory = Room("Forgotten Armory")
    smuggler_den = Room("Smuggler Den")
    narrow_passage = Room("Narrow Passage")
    exit_chamber = Room("Exit Chamber")

    guard_barracks = Room("Guard Barracks")
    supply_cache = Room("Supply Cache")
    abandoned_kitchen = Room("Abandoned Kitchen")
    ashen_furnace = Room("Ashen Furnace")
    deep_shaft = Room("Deep Shaft")
    crystal_cavern = Room("Crystal Cavern")
    ancient_lift = Room("Ancient Lift")
    sealed_vault = Room("Sealed Vault")
    warden_keep = Room("Warden Keep")
    prison_cells = Room("Prison Cells")
    hidden_tunnel = Room("Hidden Tunnel")
    alchemy_lab = Room("Alchemy Lab")

    hidden_treasury = Room("Hidden Treasury")

    # Build the original binary tree
    entrance.set_left_branch(collapsed_gallery)
    entrance.set_right_branch(iron_watch)

    collapsed_gallery.set_left_branch(moss_library)
    collapsed_gallery.set_right_branch(flooded_crossing)

    moss_library.set_right_branch(whisper_archive)
    whisper_archive.set_left_branch(clockwork_study)
    whisper_archive.set_right_branch(broken_observatory)

    flooded_crossing.set_left_branch(sunken_chapel)
    flooded_crossing.set_right_branch(rusted_gate)
    sunken_chapel.set_right_branch(echo_well)

    rusted_gate.set_left_branch(forgotten_armory)
    rusted_gate.set_right_branch(narrow_passage)
    forgotten_armory.set_right_branch(smuggler_den)
    narrow_passage.set_left_branch(exit_chamber)

    iron_watch.set_left_branch(guard_barracks)
    iron_watch.set_right_branch(deep_shaft)

    guard_barracks.set_left_branch(supply_cache)
    guard_barracks.set_right_branch(abandoned_kitchen)
    abandoned_kitchen.set_left_branch(ashen_furnace)

    deep_shaft.set_right_branch(crystal_cavern)
    crystal_cavern.set_left_branch(ancient_lift)
    crystal_cavern.set_right_branch(warden_keep)
    ancient_lift.set_right_branch(sealed_vault)

    warden_keep.set_left_branch(prison_cells)
    warden_keep.set_right_branch(alchemy_lab)
    prison_cells.set_right_branch(hidden_tunnel)

    # Part 1: DFS traversal
    print("\n=== Recursive DFS ===")
    entrance.dfs_recursive()

    print("\n=== Iterative DFS ===")
    entrance.dfs()

    # Part 2: Before unlocking portals
    print("\n=== Original Exit Route ===")
    print_path(entrance.find_shortest_exit(exit_chamber))

    print("\n=== Hidden Treasury Before Portal ===")
    print_path(entrance.find_shortest_exit(hidden_treasury))

    # Part 3: Unlock secret portals
    print("\n=== Unlocking Secret Portals ===")
    guard_barracks.add_portal(exit_chamber)
    whisper_archive.add_portal(warden_keep)
    echo_well.add_portal(hidden_treasury)

    # Part 4: BFS after unlocking portals
    print("\n=== New Shortest Exit Route ===")
    print_path(entrance.find_shortest_exit(exit_chamber))

    print("\n=== Hidden Treasury After Portal ===")
    print_path(entrance.find_shortest_exit(hidden_treasury))


if __name__ == "__main__":
    main()
