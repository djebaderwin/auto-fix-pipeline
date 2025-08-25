import yaml
import subprocess

def load_rules(rule_path=r"agent\rules\build_failures.yaml"):
    try:
        with open(rule_path, 'r') as f:
            return yaml.safe_load(f)['rules']
    except FileNotFoundError:
        print(f"Rule file not found: {rule_path}")
        return None
    
def apply_local_fix(log_data):
    rules = load_rules()
    if not rules:
        print("No rules loaded, skipping local fix.")
        return False, None
    
    for rule in rules:
        if rule['match'] in log_data:
            return True, rule['fix']
    return False, None

def run_fix(fix_cmd):
    try:
        # Ensure the command is a string and properly formatted
        if not isinstance(fix_cmd, str):
            raise ValueError("Fix command must be a string.")
        # Check if the command is empty
        if not fix_cmd.strip():
            raise ValueError("Fix command cannot be empty.")\
        # Execute the fix command
        print(f"Running fix command: {fix_cmd}")
        subprocess.run(fix_cmd, shell=True, check=True,capture_output=True,text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running fix command: {e}")
        print(f"Command output: {e.output}")
    except Exception as e:
        print(f"Unexpected error running fix command: {e}")
    

