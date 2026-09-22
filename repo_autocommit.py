import os
import subprocess
import sys

def execute_top_down_repo_commit():
    project_path = r'C:\Users\Admin\Documents\architecture-of-affinity'
    if not os.path.exists(project_path):
        print(f' Error: Repository directory path not found at: {project_path}')
        return
    os.chdir(project_path)
    print(f' Switched workspace context to repository root: {project_path}\n')
    if not os.path.exists(os.path.join(project_path, '.git')):
        print(' Warning: .git folder missing. Initializing fresh repository tracking...')
        subprocess.run(['git', 'init'], check=True)
    try:
        print(' Scanning directory tree and staging tracking file updates...')
        subprocess.run(['git', 'add', '.'], check=True)
        print('\n Current Repository Telemetry Status:')
        subprocess.run(['git', 'status', '-s'], check=True)
        commit_message = 'System Sync: Consolidated all project architecture matrix file corrections'
        print(f'\n Compiling transaction commit payload: "{commit_message}"')
        result = subprocess.run(['git', 'commit', '-m', commit_message], capture_output=True, text=True)
        if 'nothing to commit' in result.stdout.lower() or 'nothing added to commit' in result.stdout.lower():
            print(' Status: No open file changes found. Repository layout already sits at total equilibrium.')
        else:
            print(result.stdout)
            print(' SUCCESS: All tracking file layers securely committed from the top down.')
    except subprocess.CalledProcessError as e:
        print(f' Execution Fault during git operations loop: {e}')
    except FileNotFoundError:
        print(' Error: Git execution tool could not be located in your system environment PATH variables.')

if __name__ == '__main__':
    execute_top_down_repo_commit()
