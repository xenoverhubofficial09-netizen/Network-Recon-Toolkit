def merge_results(*sources):
    """
    Merge multiple subdomain sources.

    Example:

    merge_results(
        source1,
        source2,
        source3
    )
    """

    merged = set()

    for source in sources:

        if not source:
            continue

        merged.update(source)

    return sorted(merged)