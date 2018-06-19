def m(a):
    import os
    for root, i, files in os.walk(a):
        for f in files:
            if f.endswith('.mp3'):
                print(os.path.join(root, f))
