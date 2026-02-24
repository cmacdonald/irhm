"""Top-level package for IRHM."""

__version__ = '0.1.4'

__all__ = [
  'assert_versions_ex2'
]

def _assert_version(pkg, min_version=None, max_version=None):
    from importlib.metadata import version, PackageNotFoundError
    from packaging.version import parse
    try:
        installed = parse(version(pkg))
    except PackageNotFoundError:
        raise AssertionError(f"{pkg} is not installed")

    if min_version and installed < parse(min_version):
        raise AssertionError(f"{pkg} {installed} is below required {min_version}")

    if max_version and installed > parse(max_version):
        raise AssertionError(f"{pkg} {installed} must be < {max_version}")

    print(f"{pkg} {installed} ✓")

def assert_versions_ex2():
    _assert_version("pyterrier", min_version="1.0.4")
    _assert_version("pyterrier-caching", min_version="0.5.6")
    _assert_version("lightgbm", max_version="2.2.3")
    _assert_version("scikit-learn", max_version="1.7.2")
