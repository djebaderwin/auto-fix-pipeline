import sys
from .fixer import apply_local_fix,run_fix
from .parser import read_log
import argparse

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Autoheal Agent for CI/CD pipelines.")
    parser.add_argument('log_file', type=str, help='Path to the log file to be processed')
    parser.add_argument('--mode',choices=["apply","suggest"], type=str, default="suggest", help='Fix mode (default: suggest)')
    args = parser.parse_args()

    log_file = sys.argv[1]
    print(f"Reading log file: {args.log_file}")
    try:
        log_data = read_log(args.log_file)
    except FileNotFoundError:
        print(f"Log file '{args.log_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading log file: {e}")
        return
    print("Log read successfully.")

    
    matched, fix = apply_local_fix(log_data)

    if matched:
        if args.mode == "suggest":
            print("Local fix found.")
            print(f"Fix details: {fix}")
        else:
            print("Mode is 'apply'. Applying local fix.")
            run_fix(fix)
    else:
        print("No local fix applied. Skipping to remote fix.")

if __name__ == "__main__":
    print("🔥 Starting the agent...")
    main()
    print("✅ Agent finished execution.")
    sys.exit(0)

print("🏁 Finished script")


