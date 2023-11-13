def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a1=int(s[0])
    a2=int(s[1])
    a3=int(s[2])
    a4=int(s[3])
    a5=int(s[4])
    return a1+a2+a3+a4+a5
print(main("12332"))
print(main("10002"))