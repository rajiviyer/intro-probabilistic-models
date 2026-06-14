def conditional_probability(
    joint_probability: float,
    given_probability: float,
) -> float:
    """
    Compute P(A | B) = P(A and B) / P(B)
    """

    if given_probability == 0:
        raise ValueError("given_probability cannot be zero.")

    return joint_probability / given_probability


def conditional_probability_from_counts(
    joint_count: int,
    given_count: int,
) -> float:
    """
    Compute conditional probability using counts.

    P(A | B) = count(A and B) / count(B)
    """

    if given_count == 0:
        raise ValueError("given_count cannot be zero.")

    return joint_count / given_count


def are_independent(
    probability_a: float,
    probability_a_given_b: float,
    tolerance: float = 1e-9,
) -> bool:
    """
    Check independence using:

    P(A | B) = P(A)
    """

    return abs(probability_a - probability_a_given_b) <= tolerance