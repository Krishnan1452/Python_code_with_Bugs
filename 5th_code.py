import threading
import os
class FileReader:
    def __init__(self, directory):
        self.directory = directory
        self.files = []
        self.word_counts = {}
        self.lock = threading.Lock() 

    def find_files(self):
        self.files = [f for f in os.listdir(self.directory) if os.path.isfile(f)]
        
    def read_file(self, file):
        try:
            with open(file, 'r') as f: 
                data = f.read()
                self.process_content(file, data)
        except Exception as e:
            print(f"Error reading file {file}: {e}")

    def process_content(self, file, data):
        words = data.split()
        word_count = len(words)
        self.word_counts[file] = word_count

    def start_processing(self):
        threads = []
        for file in self.files:
            thread = threading.Thread(target=self.read_file, args=(file,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join() 

    def display_results(self):
        for file, count in self.word_counts.items():
            print(f"File: {file}, Word Count: {count}")

# Main function
def main():
    directory = input("Enter the directory path: ")
    file_reader = FileReader(directory)

    # Step 1: Find all files
    file_reader.find_files()

    # Step 2: Start multi-threaded processing
    file_reader.start_processing()

    # Step 3: Display results
    file_reader.display_results()

if __name__ == "__main__":
    main()