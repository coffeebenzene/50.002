row="""      8b{0:03b}{1:05b}: //test_case {0}, index {1}
        alufn = 6b{2};
        a = {a};
        b = {b};
        out = {out};
        z = bx;
        v = bx;
        n = bx;
""" #.format(test_case, index, alufn, a=a, b=b, o=out)

lines = []

with open("mult.txt") as f:
    for index, line in enumerate(f):
        line = line.strip().split(" ")
        print(line)
        a, b, out = line
        alufn = "000010"
        test_case = 6
        lines.append(row.format(test_case, index, alufn, a=a, b=b, out=out))

with open("ne.txt","w") as f:
    f.write("".join(lines))