# Yabatech SmartBot

This project is a smart chatbot for Yaba College of Technology (Yabatech) students and staff. It is designed to provide quick answers to frequently asked questions, facilitate data filtering, and offer a seamless user experience.

## Features

- **FAQ Answering:** Provides instant answers to common questions.
- **Data Filtering:** Allows users to filter and view student and staff information.
- **Chat History:** Stores conversation history for users.
- **Sentiment Analysis:** Analyzes user feedback to improve the chatbot.
- **Web Integration:** Can be embedded as a floating widget on the Yabatech website.

## Project Structure

The project is organized into the following directories:

- `src/`: Core application logic.
- `interface/`: User interface components.
- `analytics/`: Scripts for usage statistics and sentiment analysis.
- `data/`: Sample and real data files (CSV).
- `model/`: Machine learning models and related scripts.
- `test/`: Test scripts for the application.
- `assets/`: UI assets like logos and mockups.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python src/main.py
   ```
   or if using FastAPI:
   ```bash
   uvicorn src.main:app --reload
   ```

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.
