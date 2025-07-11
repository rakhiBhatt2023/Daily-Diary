# Autility class where we will have file I/O operations
# IO -> Input meeans reading data from file
#       output means writing data into file


import os       # This is for headers add only one time 

# CONTROLLER using OOPS
class Filehelper:
      def __init__(self):
            
            # this constructor will make headers in csv file
            visitor_file_path = 'visitor-log.csv'
            if os.path.exists(visitor_file_path):
                print('FileHelper Initialized')
            else:
                file = open('visitor-log.csv', 'a')
                headers = 'serial_no,date_time_stamp,name,phone,address,whome_to_meet,purpose\n'
                file.write(headers)
                print('FileHelper Initialized for the First Time')

            def write_in_file(self, content):
                file = open('visitor-log.csv', 'a')
                file.write(content)
                print('Content:', content, 'Saved in File')
        
            def read_file(self):
                file = open('visitor-log.csv', 'r')
                lines = file.readlines()
                print('Reading Data From File. Total Lines:', len(lines))
                for line in lines:
                    print(line)
        
            def file_size(self):
                file = open('visitor-log.csv', 'r')
                data = file.read()
                return len(data)
            
            def lines_in_file(self):
                file = open('visitor-log.csv', 'r')
                lines = file.readlines()
                return len(lines)