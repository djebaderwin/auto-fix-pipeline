def read_log(file_path):
    try:
        with open(file_path,'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Log File not found: {file_path}")
        return ""
    except Exception as e:
        print(f"Error reading log file: {e}")
        return ""