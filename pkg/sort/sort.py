def sort(individuals, low, high, partition):
    if low < high:
        i = partition(individuals, low, high)
        sort(individuals, low, i, partition)
        sort(individuals, i + 1, high, partition)


def default_partition(getter):
    def partition(individuals, low, high):
        i = low - 1
        pivot = getter(individuals[high])
        for j in range(low, high):
            if getter(individuals[j]) < pivot:
                i += 1
                individuals[high], individuals[j] = individuals[j], individuals[high]
        i += 1
        individuals[high], individuals[i] = individuals[i], individuals[high]
        return i

    return partition
