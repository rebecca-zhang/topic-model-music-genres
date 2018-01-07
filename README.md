# Analyzing Musical Genres and Trends with Topic Models

This repo contains our final project for Princeton's COS424 course on machine learning, Spring 2014. It includes raw data, code, and a copy of our writeup.

To run from the lda-c-dist directory:
```
python RunLDA.py [number of topics] [path to chords directory] [output directory]
```
## Abstract
Using an LDA topic model and document influence model, we analyzed 856 pieces of music from three distinct genres and nine subgenres. We found that nine topics, defined by their most common three-chord sequences, were able to distinguish the subgenres, identify the most influential pieces, and track the changes in frequency of chord progressions over musical history.

## Data and Methods
The data comes from the Prosemus project, from the Universitat Pompeu Fabra and the Universidad de Alicante, containing an academic repository of 856 pieces that have hand-labelled roman numeral chords.

For genre analysis, we utilized Latent Dirichlet Allocation (LDA). For trend analysis, we utilized an extension to LDA, the Dynamic Influence Model (DIM). 