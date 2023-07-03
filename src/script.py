import time

typing_speed = 0.05 # Typing speed (in characters per second)
line_pause = 0.001 # Pause time between each line (in seconds)
file_name = 'file.extension' # Name of file to write

# Ask user if he wants to start writing
response = input("\nBeginning of writing ? (YES/NO) ")

if response.upper() == 'YES':
    start_time = time.time() # Execution start time

    # Open the example.py file
    with open(file_name, 'r') as f:
        code = f.read()

    # Delete the content of example.py
    with open(file_name, 'w') as f:
        f.write('')

    # Write the code progressively in example.py
    with open(file_name, 'a') as f:
        progress_bar = ''
        total_chars = sum(len(line) for line in code.split('\n'))

        for line in code.split('\n'):
            for c in line:
                f.write(c)
                f.flush()

                # Updated progress bar and time remaining
                progress_bar += c
                percent_done = len(progress_bar) / total_chars * 100
                time_remaining = (total_chars - len(progress_bar)) * typing_speed
                time_remaining_str = time.strftime('%H:%M:%S', time.gmtime(time_remaining))
                print(f'\rProgress : [{"=" * int(percent_done / 2):<50}] {percent_done:.1f} % | Time remaining : {time_remaining_str}', end='')

                time.sleep(typing_speed)
            f.write('\n')
            time.sleep(line_pause)

        # Completing the progress bar and displaying the execution time
        end_time = time.time() # Execution end time
        execution_time = end_time - start_time
        execution_time_str = time.strftime('%H:%M:%S', time.gmtime(execution_time))
        print(f'\rProgress : [{"=" * 50}] 100.0 % | Execution time : {execution_time_str}')
        print("Writing finished !")

else:
    print("The writing has been cancelled.")