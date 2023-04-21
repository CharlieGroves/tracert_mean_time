import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename) as f:
    total = 0
    for line in f:
        row = line.strip()
        times = [float(t[:-3]) for t in row.split() if t.endswith('ms') and t[:-3]]
        if not times and row.split()[-1] == 'ms':
            split_row = row.split()
            times.append(float(split_row[-2]))
            if (split_row[-4] == "ms"):
                continue
            times.append(float(split_row[-4]))
            if (split_row[-6] == "ae0.er02.cwwtf.bbc.co.uk"):
                continue
            times.append(float(split_row[-6]))
            print(times)
        mean_time = sum(times) / len(times) if times else 0
        total+=mean_time
        print(total)
        print(f"{row}\tMean time: {mean_time:.3f} ms")
