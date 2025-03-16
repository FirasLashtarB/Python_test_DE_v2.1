from src.data_loader import load_data
from src.data_cleaner import clean_data
from src.data_processor import process_data
from src.output_generator import save_output

def main():
    data = load_data()
    cleaned_data = clean_data(data)  # Correction du nom de variable
    processed_data = process_data(cleaned_data)
    save_output(processed_data)

if __name__ == "__main__":
    main()