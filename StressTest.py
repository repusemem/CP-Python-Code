import time, subprocess, sys
from random import randint

NTEST = 30
TIMELIMIT = 1
NAME = "task"
BFNAME = "task_trau"
inp = NAME + ".inp"
out = NAME + ".out"
ans = NAME + ".ans"
endl = "\n"

def check(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        return f1.read().strip() == f2.read().strip()

def runscript(script_name, timeout):
	try:
		begin = time.time()
		subprocess.run(["python", script_name], timeout=timeout)
		end = time.time()
		return True, end-begin  # Successfully ran within timeout
	except subprocess.TimeoutExpired:
		return False, None  # Timed out

for i in range(1, NTEST + 1):
	# Generate test input
    with open(inp, 'w') as f:
        n = randint(1,30)
        m = randint(1,30)
        f.write(str(n) + ' '+ str(m))


    temp, t = runscript(NAME+".py", TIMELIMIT)
    if not temp:
        print(f"Case #{i} TLE\n---------------\n")
        continue
    runscript(BFNAME+".py",None)

    # Check outputs
    if check(out, ans):
        print(f"Case #{i}\n AC in [{(t):.4f} s]\n---------------\n")
    else:
        print(f"Case #{i} WA\n---------------\n")
        break
