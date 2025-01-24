def accept():
    """
    Accept user input for the reference string and page frame size.
    Returns:
        a (list): The reference string as a list of single-character strings.
        m (int) : The page frame size.
    """
    n = int(input("Enter the size of the reference string: "))
    a = []
    for i in range(n):
        # Instead of converting to int, we take the input as a string (character).
        val = input(f" Enter element [{i+1}]: ")
        # If you want to strictly enforce a single character, you could do:
        # val = val[0]  # Force single-character usage
        a.append(val)
    m = int(input("\nEnter the page frame size: "))
    return a, m


def fifo(a, m):
    """
    First In First Out (FIFO) Page Replacement Algorithm.
    Prints page faults and returns the total count.
    """
    page_faults = 0
    frames = ['-'] * m  # Use '-' to denote an empty frame

    front = 0  # Index of the next frame to replace

    for ref in a:
        if ref not in frames:
            frames[front] = ref
            front = (front + 1) % m
            page_faults += 1
            print(f"\n{ref} ->", ' '.join(frames))
        else:
            print(f"\n{ref} -> No Page Fault")

    print(f"\nTotal page faults: {page_faults}")
    return page_faults


def lru(a, m):
    """
    Least Recently Used (LRU) Page Replacement Algorithm.
    Prints page faults and returns the total count.
    """
    page_faults = 0
    frames = ['-'] * m

    for i, ref in enumerate(a):
        if ref not in frames:
            # If all frames are occupied, find the least recently used
            if '-' not in frames:
                lru_index = None
                min_back_index = float('inf')

                for f_idx in range(m):
                    # Look backwards for the last usage of frames[f_idx]
                    used_index = None
                    for back_pos in range(i - 1, -1, -1):
                        if a[back_pos] == frames[f_idx]:
                            used_index = back_pos
                            break

                    # If never used before (or not found in the past), replace immediately
                    if used_index is None:
                        lru_index = f_idx
                        break

                    if used_index < min_back_index:
                        min_back_index = used_index
                        lru_index = f_idx

                frames[lru_index] = ref
            else:
                # There's an empty slot
                empty_slot = frames.index('-')
                frames[empty_slot] = ref

            page_faults += 1
            print(f"\n{ref} ->", ' '.join(frames))
        else:
            print(f"\n{ref} -> No Page Fault")

    print(f"\nTotal page faults: {page_faults}")
    return page_faults


def optimal(a, m):
    """
    Optimal Page Replacement Algorithm.
    Prints page faults and returns the total count.
    """
    page_faults = 0
    frames = ['-'] * m

    for i, ref in enumerate(a):
        if ref not in frames:
            if '-' in frames:
                # Fill an empty slot
                empty_idx = frames.index('-')
                frames[empty_idx] = ref
            else:
                # Find the page to replace (farthest future usage)
                farthest_future = -1
                replace_idx = -1

                for f_idx in range(m):
                    if frames[f_idx] not in a[i+1:]:
                        # If this page isn't used again, replace it immediately
                        replace_idx = f_idx
                        break
                    else:
                        next_use = a[i+1:].index(frames[f_idx]) + (i+1)
                        if next_use > farthest_future:
                            farthest_future = next_use
                            replace_idx = f_idx

                frames[replace_idx] = ref

            page_faults += 1
            print(f"\n{ref} ->", ' '.join(frames))
        else:
            print(f"\n{ref} -> No Page Fault")

    print(f"\nTotal page faults: {page_faults}")
    return page_faults


def main():
    # Default reference string is a list of characters.
    reference_string = list("ABCBDAFBGBAHAGFA")
    # You can customize the default frame size here.
    m = 3

    while True:
        print("\nSIMULATION OF PAGE REPLACEMENT ALGORITHMS")
        print("Menu:")
        print("0. Accept new reference string and frame size")
        print("1. FIFO")
        print("2. LRU")
        print("3. Optimal")
        print("4. Exit")

        try:
            choice = int(input("Select: "))
        except ValueError:
            print("Invalid choice. Try again.")
            continue

        if choice == 0:
            reference_string, m = accept()
        elif choice == 1:
            fifo(reference_string, m)
        elif choice == 2:
            lru(reference_string, m)
        elif choice == 3:
            optimal(reference_string, m)
        elif choice == 4:
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
