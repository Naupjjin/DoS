import subprocess

def check_status(url):
    try:
       
        result = subprocess.run(['curl', '--head', '--silent', '--output', '/dev/null', '--write-out', '%{http_code}', url], capture_output=True, text=True, check=True)
        
        status_code = int(result.stdout.strip())
        # 正常狀態status code = 200
        if status_code == 200:
            print(f"The request to {url} was successful. Status code: {status_code}")

        else:
            print(f"The request to {url} failed. Status code: {status_code}")
    
    except subprocess.CalledProcessError as e:
        print(f"Error executing curl command: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# 要檢查的url
url_to_check = ""

check_status(url_to_check)
