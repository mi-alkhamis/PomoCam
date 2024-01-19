def s2ms(seconds):
    """
    Convert seconds to minutes and seconds.

    Parameters:
    seconds (int): The number of seconds.

    Returns:
    tuple: A tuple containing minutes and remaining seconds.
    """
    if seconds < 0:
        raise ValueError("Seconds must be non-negative.")

    minutes = seconds // 60
    seconds %= 60
    return minutes, seconds
