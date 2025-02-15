import subprocess
with open("log.txt","w") as log:
    log.write("")
def run_python_file(filename,n):
    for i in range(n):
        try:
            result = subprocess.run(["python",filename],check=True,text=True,capture_output=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"error occured! : {e.stderr}")

if __name__ == "__main__":
    filename = "search.py"
    iterations = 1000
    run_python_file(filename,iterations)