st = 0.51 # Similarity threshold for clustering [0, 1]
input_file = 'Users/Adapt/aecid-incremental-clustering/data/in/mainlog' # Path to input log file
output_file = 'Users/Adapt/aecid-incremental-clustering/data/out/clusters(test).txt' # Path to output file
timestamp_length = 19 # Length of time stamp at beginning of log line that will be removed; set to -1 for no timestamp
write_members = True # Set whether output file will only contain cluster representatives or all cluster members [True, False]
