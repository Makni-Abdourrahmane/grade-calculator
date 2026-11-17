"""Bug check: a grade of exactly 10/20 must be a pass.

Exit code 0 = good, 1 = bad, so `git bisect run python3 check.py` works.
"""
import sys

try:
    from grades import has_passed
except ImportError:
    print("SKIP: has_passed does not exist yet")
    sys.exit(125)  # tells git bisect to skip this commit

if has_passed(10):
    print("PASS: 10/20 counts as passed")
    sys.exit(0)
print("FAIL: 10/20 is shown as failed")
sys.exit(1)
