fname = input("mbox-short.txt")
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
print(count)
