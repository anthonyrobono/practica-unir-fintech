import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <file> <yes/no>")
        sys.exit(1)

    filename = sys.argv[1]
    choice = sys.argv[2].lower()

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            print(f"File {filename} has {len(lines)} lines.")
            if choice == 'yes':
                for line in lines:
                    print(line.strip())
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")

if __name__ == "__main__":
    main()
