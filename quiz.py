from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABb4eAJkBs74-EYVGqxYaICeM-bVWykVidgZbF-YjIodX-_' \
          b'wZJQuO0oC3IdmzVmUQc0bzCxMW10JCLJwyzsp1Ou7I1C4_3md1N7kEGq7m6gKGoga70UJ3eoU-jmxlZNcf91sfEqzB00m73VZEg_' \
          b'6HWmos5KDVBbPipuwMjtGXh2ZXI6DpKjzEGQ-MEM3BvNLh50tHPc'


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
