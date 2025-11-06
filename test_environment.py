import subprocess
import sys

def test_installations():
    tools = {
        'Python': ['python', '--version'],
        'Docker': ['docker', '--version'],
        'Terraform': ['terraform', '--version'],
        'Git': ['git', '--version'],
        'AWS CLI': ['aws', '--version']
    }
    
    for tool, command in tools.items():
        try:
            result = subprocess.run(command, capture_output=True, text=True)
            print(f"✅ {tool}: {result.stdout.strip()}")
        except:
            print(f"❌ {tool}: Not installed")

if __name__ == "__main__":
    test_installations()