import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Rules of extensions
EXTENSION_MAP = {
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx', '.md'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Programs': ['.exe', '.msi', '.bat', '.cmd'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Audio_Video': ['.mp3', '.wav', '.mp4', '.avi', '.mkv', '.mov']
}
AI_KEYWORD_MAP = {
    'Finance_And_Work': ['document', 'bill', 'report', 'contract', 'salary', 'salary', 'work'],
    'Education': ['homework', 'learning', 'university', 'school', 'course', 'sporran'],
    'Entertainment_And_Gaming': ['game', 'play', 'steam', 'screenshot', 'move', 'wallpaper', 'team'],
    'Personal_And_Media': ['photo', 'family', 'music', 'travel', 'personal', 'archive']
}

# 1.Fixing the way by r''
target_folder = r'C:\Users\егор4к\OneDrive\Pictures\MSI Wallpaper'

if os.path.exists(target_folder):
    # 2. saving all elements to elements
    elements = os.listdir(target_folder)





    # 3. starting cycle or items
    class Handler(FileSystemEventHandler):
        def on_modified(self, event):
            elements = os.listdir(target_folder)

            for item in elements:
                full_path = os.path.join(target_folder, item)

                if os.path.isfile(full_path):
                    # 1. getting category
                    ai_folder = self.get_ai_category(item)

                    if ai_folder is not None:

                        assigned_category = ai_folder
                    else:

                        file_ext = os.path.splitext(item)[1].lower()

                        assigned_category = "Others"

                        for category, extensions in EXTENSION_MAP.items():
                            if file_ext in extensions:
                                assigned_category = category
                                break

                    # 2. physic deploy
                    category_path = os.path.join(target_folder, assigned_category)
                    if not os.path.exists(category_path):
                        os.makedirs(category_path)

                    shutil.move(full_path, os.path.join(category_path, item))
                    print(f"File: {item} -> Successfully moved to: {assigned_category}")
        def get_ai_category(self, elements):

            pure_name = os.path.splitext(elements)[0]

            # 1. Lowering
            name_low = pure_name.lower()

            # 2. clearing from symbols
            name_clean = name_low.replace('_', ' ').replace('-', ' ')

            # 3. Words by the ' '
            words = name_clean.split()

            # 4. Checking all words
            for word in words:
                for category, keywords in AI_KEYWORD_MAP.items():
                    if word in keywords:
                        return category

            return None



    if os.path.exists(target_folder):
        print(f"Looking for: {target_folder}")

        event_handler = Handler()
        observer = Observer()
        observer.schedule(event_handler, path=target_folder, recursive=False)

        observer.start()

        try:
            while True:
                time.sleep(1)  # delay
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    else:
        print("Error: target folder not found")






else:
    print("Error: target folder not found")



