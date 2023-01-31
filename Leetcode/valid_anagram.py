def is_anagram(s,t):
    n_ = "".join(sorted(s))
    t_ = "".join(sorted(t))
    if n_ == t_:
        return True
    else:
        return False


print(is_anagram('anagram', 'naagram'))
