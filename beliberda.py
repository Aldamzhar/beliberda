import re

def is_sensible(text):
    if not text.strip() or text.isdigit() or len(text.split()) == 1 or len(set(text.split())) == 1:
        return False
    return True

# Test cases
print(is_sensible("ыдвшоаыолвтас"))  # False
print(is_sensible("ля ля ля ля ля"))  # False
print(is_sensible("good"))  # False
print(is_sensible("123"))  # False
print(is_sensible("👍"))  # False
print(is_sensible("Все ок"))  # True
print(is_sensible("было челенджево, но суперски. респект"))  # True
print(is_sensible("1. Интересно 2. Креативно 3. всё понятно."))  # True
