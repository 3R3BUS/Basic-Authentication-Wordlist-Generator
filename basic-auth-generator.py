import base64
import argparse
import os

def process_wordlist(prefix, input_file, output_file):
    # Open the input wordlist file and output file
    try:
        with open(input_file, 'r', encoding='latin-1') as infile, open(output_file, 'w') as outfile:
            # Initialize a counter to track the number of lines processed
            counter = 0
            
            for line in infile:
                if counter >= 25000:
                    break  # Stop after processing 25,000 lines
                
                line = line.strip()  # Remove any leading/trailing whitespace
                
                if line:
                    # Create the string prefix + line
                    new_line = f"{prefix}:{line}"
                    
                    # Base64 encode the new string (using bytes)
                    encoded = base64.b64encode(new_line.encode('utf-8')).decode('utf-8')
                    
                    # Remove '==' postfix (if any)
                    encoded = encoded.rstrip("=")
                    
                    # Write the modified line to the output file
                    outfile.write(f"{encoded}\n")
                
                counter += 1
        
        print(f"Process complete! The updated file is '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The input file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Generate a base64-encoded wordlist with a prefix.")
    
    # Add arguments for prefix, input wordlist, and optional output file
    parser.add_argument('prefix', type=str, help="The prefix to add to each word (e.g., 'admin').")
    parser.add_argument('input', type=str, help="Path to the input wordlist (e.g., 'rockyou.txt').")
    parser.add_argument('-o', '--output', type=str, default='updated-rock.txt', help="Optional output filename (default: 'updated-rock.txt').")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Call the function to process the wordlist
    process_wordlist(args.prefix, args.input, args.output)

if __name__ == "__main__":
    main()