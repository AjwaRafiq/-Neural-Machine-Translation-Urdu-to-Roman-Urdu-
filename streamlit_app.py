import streamlit as st
import pandas as pd
import numpy as np
import re
import unicodedata
from typing import Dict, List

# Set page config
st.set_page_config(
    page_title="Urdu to Roman Urdu Translator",
    page_icon="🌙",
    layout="wide"
)

# Simple transliteration mapping (rule-based approach as fallback)
URDU_TO_ROMAN_MAPPING = {
    # Vowels
    'ا': 'a', 'آ': 'aa', 'ع': 'a', 'ای': 'ai', 'اے': 'e',
    'ی': 'i', 'ے': 'e', 'او': 'au', 'و': 'o',
    
    # Consonants
    'ب': 'b', 'پ': 'p', 'ت': 't', 'ٹ': 't', 'ث': 's',
    'ج': 'j', 'چ': 'ch', 'ح': 'h', 'خ': 'kh', 'د': 'd',
    'ڈ': 'd', 'ذ': 'z', 'ر': 'r', 'ڑ': 'r', 'ز': 'z',
    'ژ': 'zh', 'س': 's', 'ش': 'sh', 'ص': 's', 'ض': 'z',
    'ط': 't', 'ظ': 'z', 'غ': 'gh', 'ف': 'f', 'ق': 'q',
    'ک': 'k', 'گ': 'g', 'ل': 'l', 'م': 'm', 'ن': 'n',
    'ں': 'n', 'ه': 'h', 'ھ': 'h', 'ء': '', 'ؤ': 'o',
    
    # Common words
    'اور': 'aur', 'کی': 'ki', 'کے': 'ke', 'کا': 'ka',
    'میں': 'mein', 'سے': 'se', 'کو': 'ko', 'نے': 'ne',
    'ہے': 'hai', 'ہیں': 'hain', 'تھا': 'tha', 'تھی': 'thi',
    'کہ': 'keh', 'یہ': 'yeh', 'وہ': 'woh', 'جو': 'jo'
}

class SimpleUrduTranslator:
    def __init__(self):
        self.mapping = URDU_TO_ROMAN_MAPPING
        
    def normalize_urdu(self, text: str) -> str:
        """Basic Urdu text normalization"""
        if not text:
            return ""
        
        # Unicode normalization
        text = unicodedata.normalize('NFKC', text)
        
        # Remove extra spaces
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def simple_translate(self, urdu_text: str) -> str:
        """Simple rule-based translation"""
        if not urdu_text:
            return ""
        
        urdu_text = self.normalize_urdu(urdu_text)
        words = urdu_text.split()
        translated_words = []
        
        for word in words:
            # Remove punctuation for processing
            clean_word = re.sub(r'[۔،؟!]', '', word)
            
            # Check if entire word exists in mapping
            if clean_word in self.mapping:
                translated_words.append(self.mapping[clean_word])
            else:
                # Character-by-character transliteration
                translated_chars = []
                for char in clean_word:
                    if char in self.mapping:
                        translated_chars.append(self.mapping[char])
                    elif char.isspace():
                        translated_chars.append(' ')
                    else:
                        translated_chars.append(char)  # Keep unknown characters
                
                if translated_chars:
                    translated_words.append(''.join(translated_chars))
                else:
                    translated_words.append(word)
        
        return ' '.join(translated_words)

def load_sample_examples() -> Dict[str, str]:
    """Sample Urdu texts for demonstration"""
    return {
        "Greeting": "آپ کیسے ہیں",
        "Poetry": "چاند رات میں چمکتا ہے",
        "Simple": "یہ میرا گھر ہے",
        "Question": "آپ کا نام کیا ہے؟",
        "Nature": "پھول خوبصورت ہیں"
    }

def main():
    # Header
    st.title("🌙 Urdu to Roman Urdu Translator")
    st.markdown("### Simple Rule-Based Translation Demo")
    st.markdown("---")
    
    # Initialize translator
    if 'translator' not in st.session_state:
        st.session_state.translator = SimpleUrduTranslator()
    
    # Create two columns
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📝 Input Urdu Text")
        
       # Remove sample examples dropdown
        st.subheader("Enter Your Urdu Text")
        sample_text = ""  # no preloaded examples

        
        # Text input
        urdu_input = st.text_area(
            "Enter Urdu text:",
            value=sample_text,
            height=150,
            help="Enter the Urdu text you want to transliterate to Roman Urdu",
            placeholder="یہاں اردو ٹیکسٹ لکھیں..."
        )
        
        # Options
        st.subheader("Options")
        show_mapping = st.checkbox("Show character mapping", value=False)
        
        # Translate button
        translate_button = st.button("🔄 Translate", type="primary")
    
    with col2:
        st.header("🔤 Roman Urdu Output")
        
        if translate_button and urdu_input.strip():
            with st.spinner("Translating..."):
                translation = st.session_state.translator.simple_translate(urdu_input.strip())
            
            st.success("Translation completed!")
            
            # Show translation
            st.text_area(
                "Translation:",
                value=translation,
                height=150,
                disabled=True
            )
            
            # Statistics
            input_chars = len(urdu_input.strip())
            output_chars = len(translation)
            input_words = len(urdu_input.strip().split())
            output_words = len(translation.split())
            
            col2a, col2b = st.columns(2)
            with col2a:
                st.metric("Input", f"{input_words} words", f"{input_chars} chars")
            with col2b:
                st.metric("Output", f"{output_words} words", f"{output_chars} chars")
            
            # Show character mapping if requested
            if show_mapping and urdu_input.strip():
                st.subheader("Character Mapping")
                mapping_data = []
                
                for char in set(urdu_input):
                    if char in st.session_state.translator.mapping:
                        mapping_data.append({
                            "Urdu": char,
                            "Roman": st.session_state.translator.mapping[char]
                        })
                
                if mapping_data:
                    df = pd.DataFrame(mapping_data)
                    st.dataframe(df, use_container_width=True)
        
        elif translate_button:
            st.warning("Please enter some Urdu text to translate.")
    
    # Information sections
    st.markdown("---")
    
    # Method explanation
    with st.expander("ℹ️ Translation Method"):
        st.markdown("""
        **Current Method:** Rule-Based Transliteration
        
        This demo uses a simple character-to-character mapping approach:
        - Direct word mapping for common Urdu words
        - Character-level transliteration for unknown words
        - Basic text normalization and cleanup
        
        **Note:** This is a simplified version. For production use, the neural 
        BiLSTM encoder-decoder model would provide much better accuracy.
        
        **Model Architecture (Full Version):**
        - BiLSTM Encoder: 2 layers
        - LSTM Decoder: 4 layers  
        - Custom BPE tokenization
        - Trained on Urdu Ghazals dataset
        """)
    
    # Statistics
    with st.expander("📊 Demo Statistics"):
        st.markdown(f"""
        **Available Mappings:**
        - Character mappings: {len([k for k in URDU_TO_ROMAN_MAPPING.keys() if len(k) == 1])}
        - Word mappings: {len([k for k in URDU_TO_ROMAN_MAPPING.keys() if len(k) > 1])}
        - Total mappings: {len(URDU_TO_ROMAN_MAPPING)}
        
        **Coverage:** Basic Urdu characters and common words
        """)
        
        # Show some mappings as examples
        sample_mappings = dict(list(URDU_TO_ROMAN_MAPPING.items())[:10])
        df_sample = pd.DataFrame([
            {"Urdu": k, "Roman": v} for k, v in sample_mappings.items()
        ])
        st.dataframe(df_sample)
    
    # Usage instructions
    with st.expander("📋 How to Use"):
        st.markdown("""
        1. **Select Sample**: Choose from predefined examples or enter custom text
        2. **Enter Text**: Type or paste Urdu text in the input area
        3. **Options**: Enable character mapping display if desired
        4. **Translate**: Click the translate button to see Roman Urdu output
        5. **Review**: Check the translation and character mappings
        
        **Tips:**
        - Try the sample examples first to see how it works
        - Common words are translated more accurately
        - Character mapping shows the conversion rules used
        """)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>"
        "<p>Built with Streamlit | Neural Machine Translation Project Demo</p>"
        "<p>Full BiLSTM model implementation available in complete version</p>"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()