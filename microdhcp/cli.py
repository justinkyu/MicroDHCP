import subprocess

def run(cmd):
    try:
        return subprocess.check_output(cmd, text=True, stderr=subprocess.DEVNULL)
    except Exception:
        return None

def main():
    print()
    print("MicroDHCP")
    print("=" * 40)

    route = run(["ip", "route"])

    if route:
        for line in route.splitlines():
            if line.startswith("default"):
                print("Gateway :", line.split()[2])
                break

    dns = run(["cat", "/etc/resolv.conf"])

    if dns:
        print()
        print("DNS Servers")
        print("-" * 20)
        for line in dns.splitlines():
            if line.startswith("nameserver"):
                print(line)

    print()
    print("Done.")
