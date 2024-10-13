# ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# ("~   Spectrum Event Config Analyzer   ~")
# ("~        Michael Lee / emdotel       ~")
# ("~            October 2024            ~")
# ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Please view the README.md file for further information
# https://github.com/emdotel/spectrum-event-config-analyzer

import csv
import sys

# Function to convert the EventCode HEX to Integers and vice versa
def hex_to_int(hex_str):
    return int(hex_str, 16)
def int_to_hex(integer):
    return '0x{:08X}'.format(integer)

# Function to check for Gaps within the list of events, taking user's input as the minimum gap required and assuming custom event codes only
def find_free_space(event_codes, free_space, min_hex_value):
    gaps = []
    for i in range(len(event_codes) - 1):
        current_event_code = event_codes[i]
        next_event_code = event_codes[i + 1]

        if current_event_code < min_hex_value:
            continue

        gap = next_event_code - current_event_code - 1
        if gap >= free_space:
            gaps.append((int_to_hex(current_event_code + 1), gap))

    return gaps

# Main function - with a little error-checking to ensure there's a valid Event Configuration CSV input
# Calls the Find Free Space function
# Prints gaps matching the input Integer variable
# Finally, prints the remaining space after the last-used Event code
def main(input_csv, free_space):
    try:
        with open(input_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            event_codes = []

            if 'Event Code' not in reader.fieldnames:
                print("Error: 'Event Code' column not found in input CSV file")
                return

            # extract the "Event Code" column and convert Hex to int
            # if the CSV had been modified, make sure only the Hex is present
            for row in reader:
                event_code = row['Event Code'].strip()
                event_codes.append(hex_to_int(event_code))
        event_codes = sorted(event_codes)

        min_usable_hex = hex_to_int('0xfff00000')
        max_usable_hex = hex_to_int('0xffffffff')

        free_space_required = int(free_space)
        gaps = find_free_space(event_codes, free_space_required, min_usable_hex)

        # Now printing the results
        if gaps:
            print(f"Found gaps that can fit {free_space} Events:")
            for gap_start, gap_size in gaps:
                print(f"Gap starts at {gap_start} with available space of {gap_size} Events.")
        else:
            print(f"No gaps found that can fit the free space of {free_space} Events.")

        # Finally, priting results after the last-used event code / end of file
        last_event_code = event_codes[-1]
        if last_event_code >= min_usable_hex:
            remaining_space = max_usable_hex - last_event_code
            print(
                f"All space from {int_to_hex(last_event_code + 1)} onwards is free. Available space: {remaining_space} Events.")

    except Exception as e:
        print(f"Error processing the file: {e}")


# Launching the script based on the provided Input Variables
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: spectrum-event-config-analyzer.py <input_csv> <FreeSpace>")
    else:
        input_csv = sys.argv[1]
        free_space = sys.argv[2]
        main(input_csv, free_space)