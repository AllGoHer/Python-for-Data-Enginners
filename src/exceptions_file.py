try:
    with open('missing_file.csv','r') as f:
        data = f.read()
except FileNotFoundError:
    with open('MISSING_FILE.csv','r') as f:
        data = f.read()
    print('Filenot Found: Pipeline cannot proceed')
finally:
    print('cleanup complete')