import os
def get_file(file):
# Open the file in read-only mode
    file_descriptor = os.open(file, os.O_RDONLY)

# Read the contents of the file
    file_contents = os.read(file_descriptor, os.path.getsize(file))

# Print the contents (decode from bytes to string)
    print(file_contents.decode())
    output=file_contents.decode()
# Close the file
    os.close(file_descriptor)