from typing import Tuple


# %%
def gcd_basic(a: int, b: int) -> int:
    """
    Compute the Greatest Common Divisor (GCD) of two integers using the
    Euclidean algorithm. Works for positive, negative, and zero values.

    The GCD is always returned as a non-negative integer.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        The greatest common divisor of a and b.

    Examples:
        >>> gcd(54, 24)
        6
        >>> gcd(-54, 24)
        6
        >>> gcd(0, 5)
        5
        >>> gcd(0, 0)
        0
    """
    # Normalize to non-negative, as gcd is defined non-negative.
    a, b = abs(a), abs(b)

    # Euclidean algorithm: repeatedly replace (a, b) with (b, a % b)
    # until b becomes 0; then a is the GCD.
    while b != 0:
        a, b = b, a % b

    return a


# %%
def gcd_extended(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean algorithm.
    Returns (g, x, y) such that g = gcd(a, b) and a*x + b*y = g.

    Useful if you need Bézout coefficients.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        A tuple (g, x, y) where g is gcd(a, b), and x, y are Bézout coefficients.

    Examples:
        >>> gcd_extended(54, 24)
        (6, 1, -2)
        >>> gcd_extended(0, 5)
        (5, 0, 1)
        >>> gcd_extended(0, 0)
        (0, 0, 0)
    """
    old_r, r = abs(a), abs(b)
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    # Adjust signs to reflect original a, b
    # If a or b were negative, Bézout coefficients should match original signs.
    x = old_s if a >= 0 else -old_s
    y = old_t if b >= 0 else -old_t

    return old_r, x, y


# %%
def main() -> None:
    """Simple test cases for gcd and gcd_extended functions."""
    test_cases = [
        (54, 24),
        (-54, 24),
        (0, 5),
        (0, 0),
        (101, 10),
        (270, 192),
    ]

    for a, b in test_cases:
        g = gcd_basic(a, b)
        g_ext, x, y = gcd_extended(a, b)
        print(f"gcd({a}, {b}) = {g}")
        print(f"gcd_extended({a}, {b}) = (g: {g_ext}, x: {x}, y: {y})")
        assert g == g_ext, "GCD values do not match!"
        assert a * x + b * y == g_ext, "Bézout identity does not hold!"
        print("-" * 40)


# %%
