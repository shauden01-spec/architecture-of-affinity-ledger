import os
import shutil
import time

def background_sweeper_daemon():
    root_dir = "C:\\Users\\Admin\\Documents\\architecture-of-affinity"
    routes = {
        ".md": "essays",
        ".yaml": "essays",
        ".csv": "datasets",
        ".png": "datasets",
        ".tmp": "logs"
    }
    
    print("======================================================================")
    print("🛰️ AFFINITY FILE SWEEPER DAEMON ACTIVE: Running background sweep loops")
    print("======================================================================")
    
    try:
        while True:
            for filename in os.listdir(root_dir):
                file_path = os.path.join(root_dir, filename)
                
                # Safeguard executable assets and hidden tracking logs
                if os.path.isdir(file_path) or filename.endswith('.py') or filename.endswith('.bat') or filename.startswith('.'):
                    continue
                    
                _, ext = os.path.splitext(filename)
                if ext.lower() in routes:
                    dest_folder = os.path.join(root_dir, routes[ext.lower()])
                    os.makedirs(dest_folder, exist_ok=True)
                    
                    dest_path = os.path.join(dest_folder, filename)
                    if os.path.exists(dest_path):
                        os.remove(dest_path)
                        
                    shutil.move(file_path, dest_path)
                    print(f"[{time.strftime('%H:%M:%S')}] Daemon automatically swept: {filename} ──> /{routes[ext.lower()]}")
            
            # Wait for 60 seconds before executing the next background file check scan
            time.sleep(60)
            
    except KeyboardInterrupt:
        print("\n🛑 Background sweeper daemon shut down safely by operator.")

if __name__ == "__main__":
    background_sweeper_daemon()
