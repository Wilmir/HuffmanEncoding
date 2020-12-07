from HuffmanCoding import HuffmanCoding

def main():
    h = HuffmanCoding("sample.txt")
    decompressedFile = h.compress()
    recoveredFile = h.decompress(decompressedFile)
    print(recoveredFile)

if __name__ == "__main__":
    main()