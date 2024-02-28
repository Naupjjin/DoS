import subprocess

def check_status(url):
    try:
       
        result = subprocess.run(['curl', '--head', '--silent', '--output', '/dev/null', '--write-out', '%{http_code}', url], capture_output=True, text=True, check=True)
        
        status_code = int(result.stdout.strip())

        if status_code == 200:
            print(f"The request to {url} was successful. Status code: {status_code}")

        else:
            print(f"The request to {url} failed. Status code: {status_code}")
    
    except subprocess.CalledProcessError as e:
        print(f"Error executing curl command: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


url_to_check = "https://www.cksh.tp.edu.tw"

check_status(url_to_check)
