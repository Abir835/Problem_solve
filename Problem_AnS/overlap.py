def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals based on the starting point
    intervals.sort(key=lambda x: x[0])

    merged = []
    current_interval = intervals[0]

    for next_interval in intervals[1:]:
        if current_interval[1] >= next_interval[0]:  # There is an overlap
            current_interval[1] = max(current_interval[1], next_interval[1])
        else:
            merged.append(current_interval)
            current_interval = next_interval

    merged.append(current_interval)  # Append the last interval
    return merged

# Example usage
intervals = [[1, 6], [3, 8], [2, 6], [15, 18]]
merged_intervals = merge_intervals(intervals)
print(merged_intervals)