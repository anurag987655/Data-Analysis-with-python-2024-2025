import re

def file_listing(filename="src/listing.txt"):
    
    pattern = r'\S+\s+\S+\s+\S+\s+\S+\s+(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s+(.+)'

    result = []
    
    with open(filename, 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                size = int(match.group(1))
                month = match.group(2)
                day = int(match.group(3))
                hour = int(match.group(4))
                minute = int(match.group(5))
                filename = match.group(6)
            
                result.append((size, month, day, hour, minute, filename))
    
    return result


if __name__ == "__main__":
    listing = file_listing()
    for entry in listing:
        print(entry)