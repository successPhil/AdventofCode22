def find_marker(filename):
  """This function reads a file by line and slices each line
  to get 4 characters, then compares them to a set of the same characters
  to see if they are distinct
  Return: The amount of characters processed until 4 distinct chars are seen"""
  chars_processed = 0
  with open(filename, 'r') as datastream:
    for line in datastream:
      line = line.strip()
      for i in range(len(line)-4):
        marker = line[i:i+4]
        if len(marker) == len(set(marker)):
          chars_processed += i + 4
          return chars_processed  
        # elif i == len(line)-5:
        #   chars_processed += len(line)
        #Only needed if data is on multiple lines
  


print(find_marker('datastream.txt'))