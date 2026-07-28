"""
Security Headers Analyzer Handler

Handles user input validation and connects
the CLI layer with core security header analyzer.
"""

from core.security_headers import analyze_security_headers


def validate_target(target: str) -> bool:
    """
    Validate target input.

    Args:
        target: User provided URL/domain.

    Returns:
        bool: True if valid else False.
    """

    if not target:
        return False

    target = target.strip()

    return len(target) > 3


def security_headers_lookup(target: str) -> dict:
    """
    Execute security headers analysis.

    Args:
        target: Target URL/domain.

    Returns:
        dict: Analysis result.

    Raises:
        ValueError: If target is invalid.
        Exception: For unexpected errors.
    """

    if not validate_target(target):
        raise ValueError("Invalid target provided.")

    try:
        result = analyze_security_headers(target)

        return result

    except Exception as error:
        raise Exception(
            f"Security headers analysis failed: {error}"
        ) from error