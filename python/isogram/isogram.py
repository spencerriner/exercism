def is_isogram(string):
    string = string.replace(" ", "")
    string = string.replace("-", "")
    string = string.lower()
    seen = []
    for char in string:
        if char in seen:
            return False
        seen.append(char)
    return True
