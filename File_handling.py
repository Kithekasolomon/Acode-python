

# Prompt user for input filename
try:
    input_filename = input("Enter the input filename (e.g., input.txt): ")

    # Attempt to read the input file
    with open(input_filename, 'r') as input_file:
        content = input_file.read()

    # Modify content (convert to uppercase as an example)
    modified_content = content.upper()

    # Write modified content to a new file
    output_filename = 'output_modified.txt'
    with open(output_filename, 'w') as output_file:
        output_file.write(modified_content)

    print(f"Success! Modified content written to {output_filename}")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied when accessing '{input_filename}' or writing to output file.")
except IOError as e:
    print(f"Error: An I/O error occurred: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")