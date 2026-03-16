
def chunk_text(filename, chunk_size=250, overlap=50):
    with open(filename, 'r') as f:
        lines = f.readlines()

    chunks = []
    step = chunk_size - overlap
    for i in range(0, len(lines), step):
        chunk = lines[i:i + chunk_size]
        if not chunk:
            break
        chunks.append(chunk)

    for i, chunk in enumerate(chunks):
        with open(f'chunk_{i}.txt', 'w') as f:
            f.writelines(chunk)
    
    print(f"Created {len(chunks)} chunks.")

if __name__ == "__main__":
    chunk_text('speech_full.txt')
