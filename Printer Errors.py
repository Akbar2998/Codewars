def printer_error(s):
    a = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    errors = 0
    for i in range(len(s)):
        if s[i] not in a:
            errors += 1
    return (f"{errors}/{len(s)}")
