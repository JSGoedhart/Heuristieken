import matplotlib.pyplot as plt

f = plt.figure()
plt.plot(range(10), range(10), "o")

f.savefig("foo.pdf", bbox_inches='tight')