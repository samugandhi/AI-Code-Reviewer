
# AI Code Advisor 💡

Analyze your Python code effortlessly with **AI Code Advisor**. This tool provides error detection, performance optimization tips, and best practices for writing clean and efficient code. Built using Streamlit and powered by Google's Generative AI.

## Features

- **🔍 Error Detection**: Identify issues in your Python code.
- **📈 Optimization Tips**: Improve code performance with actionable suggestions.
- **💡 Best Practices**: Enhance your coding standards for cleaner, more efficient development.

## Installation

### Prerequisites

1. Python 3.7 or later installed on your system.
2. Google Generative AI API key.

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/AI-Code-Advisor.git
   cd AI-Code-Advisor
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your API key:
   - Replace `"Your API file Path here"` in the script with the path to your Google Generative AI API key file.

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run Codereview.py
   ```
2. Open the app in your web browser (default: [http://localhost:8501](http://localhost:8501)).
3. Paste your Python code into the input area, click "Run Analysis," and receive insights on your code.

## Project Structure

- **`Codereview.py`**: Main Streamlit app script.
- **`requirements.txt`**: Python dependencies required for the project.

## Customization

- Modify the CSS in `Codereview.py` to adjust the app's styling.
- Update the sidebar markdown for additional tools or descriptions.

## Contributing

Contributions are welcome! Fork the repository, create a feature branch, and submit a pull request.

## Acknowledgements

- **Streamlit**: For the intuitive app framework.
- **Google Generative AI**: For enabling intelligent code analysis.

## License

This project is licensed under the [MIT License](LICENSE).
