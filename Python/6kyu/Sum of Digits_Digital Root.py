def digital_root(n):
    final = 0
    for a in range(len(str(n))):
        final += int(str(n)[a])
    if len(str(final)) > 1:
        return digital_root(final)
    else:
        return final