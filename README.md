# Data_compression
 Considering three methods of Data Compression: Huffman coding, Shannon-fano algorithm and a naive approach, I have proved that the most optimal method for data compression is the Huffman algorithm and for the same, I have tested for three data files.
 
CONCLUSIONS
The compression techniques are run on three types of files, and then the compression ratios are calculated for each
case. A comparison between all the cases leads to the determination of the most efficient method.
A. File 1 – The Adventures of Sherlock Holmes
The original file size was 50638416 bits. The data obtained post-compression is as follows:
1) Naïve Approach – The compressed file size is 49174960 bits and the compression ratio is 2.89.
2) Shannon Fano Approach – The compressed file size is 28818847 bits and the compression ratio is 43.09.
3) Huffman Approach – The compressed file size is 28760793 bits and the compression ratio is 43.2.
B. File 2 – Randomly Generated File containing random letters with very low entropy (unevenness)
The original file size was 8000000 bits. The data obtained post-compression is as follows:
1) Naïve Approach – The compressed file size is 7974520 bits and the compression ratio is 0.3185.
2) Shannon Fano Approach – The compressed file size is 6699396 bits and compression ratio is 16.25755.
3) Huffman Approach – The compressed file size is 6696475 bits and the compression ratio is 16.29406.
C. File 3 – Very Even File containing sequences of ‘A’, ‘B’ and ‘ ‘
The original file size was 8000000 bits. The data obtained post-compression is as follows:
1) Naïve Approach – The compressed file size is 3214296 bits and the compression ratio is 59.8213.
2) Shannon Fano Approach – The compressed file size is 1562500 bits and compression ratio is 80.46875.
3) Huffman Approach – The compressed file size is 1562500 bits and the compression ratio is 80.46875.
The naïve approach is found to work efficiently on a short piece of text, the reason being that only 10 words with
the highest frequencies are encoded. The compression ratios of the Huffman approach and Shannon Fano approach
are very close; however, the Huffman approach has a slight edge in every case.
Thus, the Huffman approach is the most efficient method of lossless data compression. The results are consistent
with the logical deductions.
