import os

# Import the raw data. 
raw_data_path = os.path.join('data', 'TRD_Co.txt')
f_in = open(raw_data_path, 'r', encoding = 'utf-8')

# Clean data output path. 
clean_data_path = os.path.join('data', 'clean_data.csv')
f_out = open(clean_data_path, 'w', encoding = 'utf-8')

# Column headings. 
header = f_in.readline().strip().replace('\t', ',')
f_out.write(header + '\n')

# Process each line. 
for line in f_in:
    line_no_comma = line.replace(',', '')

    # Handle missing data. 
    goodline = line_no_comma.strip().replace('-9999', 'NaN')
    data_pts = goodline.split('\t')
    processed_line = ','.join(data_pts)
    f_out.write(processed_line + '\n')