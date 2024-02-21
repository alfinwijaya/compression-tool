## <h1>Compression Tool</h1>

This repository contains the implementation of a Huffman coding tool in Python for both compression and decompression of text files.

**<h2>Features:</h2>**

* Implements lossless data compression using Huffman coding algorithm.
* Supports compression and decompression of text files.
* Allows specifying input and output filenames.
* Includes comprehensive unit tests for core functionalities.

**<h2>Requirements:</h2>**

* Python

**<h2>Installation:</h2>**

1. **Clone this repository:**

   ```bash
   git clone https://github.com/your-username/huffman-coding.git
   ```

2. **Create a virtual environment (recommended):**

   This helps isolate project dependencies and avoids conflicts with system-wide packages. Here's how to do it:

   **Create `venv`:**

   ```bash
   python3 -m venv venv
   ```

   **Using `venv`:**

   ```bash
   .\venv\Scripts\activate
   ```

3. **Install dependencies:**

   Activate your virtual environment (if you created one) and install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation:**

   After installation, try running the script with the `--help` flag to check if it works:

   ```bash
   python main.py --help
   ```

   This should display the usage information and available options.

**<h2>Usage:</h2>**

```
python main.py <input_file> <mode> <output_file>

where:
* <input_file>: Path to the text file to be compressed/decompressed.
* <output_file>: Path to the compressed/decompressed file.
* <mode>: either "-d" for decompress or "-e" compress
```

**Example:**

To compress the file "input.txt" and save the compressed data to "output.dat", use:

```
python main.py input.txt -e output.dat
```

To decompress the file "output.dat" and save the decompressed text to "decompressed.txt", use:

```
python huffman_coding.py output.dat -d decompressed.txt
```
**<h2>Testing:</h2>**

This project utilizes unit tests to ensure the correctness and reliability of its functionalities. The tests are located in the `tests` directory and can be run using the following commands:

```bash
python -m unittest tests/test.py
```

**Test Coverage:**

The tests aim to cover all critical logic within the codebase, focusing on core functions like:

* Frequency counting accuracy for various characters and text samples.
* Huffman tree construction based on frequencies.
* Prefix code table generation from the tree.
* Bit packing and unpacking for compression and decompression.
* Successful compression and decompression of text files, verifying identical content restoration.

**<h2>Further Information:</h2>**

* Explanation of Huffman coding: [https://opendsa-server.cs.vt.edu/ODSA/Books/CS3/html/Huffman.html](https://opendsa-server.cs.vt.edu/ODSA/Books/CS3/html/Huffman.html)
