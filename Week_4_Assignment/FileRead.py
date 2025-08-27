# This program reads from a file, modifies the text,
# and writes it into a new file.

def read_and_modify(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, "r") as infile:
            content = infile.read()

        # Modify the content (example: make it uppercase)
        modified_content = content.upper()

        # Write the modified content into the new file
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Modified content written to '{output_file}' successfully!")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You don't have permission to read/write this file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


# Error Handling Lab 🧪
# Ask the user for a filename and handle errors properly.

filename = input("Enter the filename you want to read: ")
output_file = "modified_" + filename

read_and_modify(filename, output_file)
