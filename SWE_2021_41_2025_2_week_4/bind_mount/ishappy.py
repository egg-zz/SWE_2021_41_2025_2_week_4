import os

def isHappy(n):
    def next_val(x):
        sum = 0
        while x > 0:
            sum += (x%10)**2
            x //= 10
        return sum

    happy = set()
    while n != 1:
        if n in happy:
            return False
        happy.add(n)
        n = next_val(n)
    return True

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")

    print("Results saved to /app/bind_mount/output.txt")