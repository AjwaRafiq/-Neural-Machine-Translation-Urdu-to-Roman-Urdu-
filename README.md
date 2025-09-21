# -Neural-Machine-Translation-Urdu-to-Roman-Urdu-

A BiLSTM encoder-decoder model for translating Urdu text to Roman Urdu transliteration, trained on poetic Ghazal data from Rekhta.

## 🌐 Live Demo

**Try the live application:** [Hugging Face Spaces Demo](https://huggingface.co/spaces/ajwaajwa/NeuralMachineTranslation_Urdu_to_Roman_Urdu)

## 📋 Project Overview

This project implements a sequence-to-sequence neural machine translation model to convert Urdu script text into Roman Urdu (Latin script transliteration). The model uses a bidirectional LSTM encoder and LSTM decoder architecture with custom BPE tokenization.

### Key Features

- **BiLSTM Encoder-Decoder Architecture**
  - 2-layer Bidirectional LSTM Encoder
  - 4-layer LSTM Decoder
  - Attention mechanism for better translation quality

- **Custom Preprocessing Pipeline**
  - Urdu text normalization and cleaning
  - Custom Byte-Pair Encoding (BPE) tokenization
  - Roman Urdu text processing

- **Comprehensive Evaluation**
  - BLEU score metrics (1-gram to 4-gram)
  - Character Error Rate (CER)
  - Perplexity measurements

- **Systematic Experimentation**
  - Multiple hyperparameter configurations tested
  - Performance comparison across different settings
  - Automated experiment tracking

## 📊 Dataset

**Source:** [urdu_ghazals_rekhta](https://github.com/amir9ume/urdu_ghazals_rekhta)

- **Total Pairs:** Extracted from Urdu Ghazal poetry
- **Split Ratio:** 50% Train / 25% Validation / 25% Test
- **Content:** Poetic Urdu text with corresponding Roman Urdu transliterations

## 🏗️ Model Architecture

```
Input: Urdu Text → BiLSTM Encoder (2 layers) → Context Vector → LSTM Decoder (4 layers) → Roman Urdu Output
```

### Architecture Details

- **Embedding Dimension:** 256
- **Encoder Hidden Size:** 512 (bidirectional, 256 each direction)
- **Decoder Hidden Size:** 512
- **Dropout Rate:** 0.3
- **Vocabulary Size:** ~7000 tokens (custom BPE)

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.9+
PyTorch 2.0+
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ajwaajwa/NeuralMachineTranslation_Urdu_to_Roman_Urdu
cd NeuralMachineTranslation_Urdu_to_Roman_Urdu
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download the dataset:
```bash
# Instructions for downloading urdu_ghazals_rekhta dataset
```

## 🧪 Reproduction Steps

1. **Data Preprocessing:**
   - Download urdu_ghazals_rekhta dataset
   - Run preprocessing pipeline
   - Generate train/val/test splits

2. **Model Training:**
   - Train BiLSTM encoder-decoder model
   - Implement teacher forcing
   - Save best model based on validation loss

3. **Evaluation:**
   - Calculate BLEU scores on test set
   - Measure character error rate
     
4. **Deployment:**
   - Create Streamlit interface
   - Deploy on Hugging Face Spaces

## 📊 Technical Implementation

### Key Components

- **Text Normalization:** Unicode handling, character mapping
- **Tokenization:** Custom BPE implementation
- **Model Training:** Adam optimizer, gradient clipping
- **Evaluation:** Comprehensive metrics suite

### Challenges Addressed

- **Low-resource Language:** Limited Urdu-Roman Urdu parallel data
- **Script Differences:** Handling Arabic script to Latin conversion
- **Poetry Domain:** Dealing with poetic language and structure
- **Evaluation:** Developing appropriate metrics for transliteration

## 🔧 Technologies Used

- **Framework:** PyTorch
- **Interface:** Streamlit
- **Data Processing:** Pandas, NumPy
- **Evaluation:** NLTK, SacreBLEU
- **Deployment:** Docker, Hugging Face Spaces

## 📚 References

- Dataset: [urdu_ghazals_rekhta](https://github.com/amir9ume/urdu_ghazals_rekhta)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


## 🙏 Acknowledgments

- Rekhta Foundation for the Urdu poetry dataset
- Course instructor and TAs for guidance
- Open source community for tools and libraries

---

**Note:** This is an academic project demonstrating neural machine translation techniques for Urdu to Roman Urdu conversion. The live demo uses a simplified rule-based approach for demonstration purposes, while the full BiLSTM model implementation is available in the repository.
