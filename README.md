# DocuBot
 AI-Powered Invoice/Receipt Processing and Chatbot Interaction Pipeline
# Document Processing and Chatbot Interaction Pipeline

## Overview

The Document Processing and Chatbot Interaction Pipeline is an innovative project that leverages advanced technologies such as language models, Optical Character Recognition (OCR), and chatbot frameworks to intelligently process documents, extract essential information, and enable user interaction through a chatbot interface. The pipeline is capable of handling various document formats, including PDFs containing both text and image content, and adapts to different information extraction tasks.

## Key Components

- **Language Model (LLM):** Utilizes advanced language models for understanding and processing text data.
- **Optical Character Recognition (OCR):** Employs OCR technology to extract text from images within documents.
- **Langchain:** Framework for language processing and text analytics.
- **Ollama:** Toolkit for information extraction and document analysis.
- **Chatbase:** Chatbot analytics platform for tracking user interactions and improving chatbot performance.

## Features

- **Document Processing:** Analyzes documents, including invoice/receipt type PDFs, to extract essential information such as key-value pairs.
- **OCR Integration:** Handles scenarios where OCR is required to extract text from images within documents.
- **Chatbot Interaction:** Enables user interaction through a chatbot interface for querying extracted information and performing related tasks.
- **Adaptability:** Adapts to different document formats and information extraction tasks, ensuring robust performance across various use cases.

## Installation

To set up the Document Processing and Chatbot Interaction Pipeline, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/document-processing-chatbot-pipeline.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure the environment:

   - Set up the language model, OCR engine, and chatbot framework.
   - Configure API keys and access credentials for external services.

4. Run the application:

   ```bash
   python main.py
   ```

## Usage

1. Start the pipeline application.
   ```bash
   python marker/convert_single.py
   ```
2. Run frontend
   ```bash
   streamlit run frontend.py
   ```  
4. Upload or provide the path to the document you want to process.
   ![Screenshot 2024-06-08 125458](https://github.com/Manu-N-S/DocuBot/assets/98375679/f0e26167-8dc5-40eb-9b16-a16598f21ff0)
5. Ask questions
   ![Screenshot 2024-06-08 125610](https://github.com/Manu-N-S/DocuBot/assets/98375679/28945ae8-660b-4ffe-a12e-324ffd49a231)

##DEMO VIDEO


https://github.com/Manu-N-S/DocuBot/assets/98375679/4d21ba4e-fd06-4405-ba59-77f69cbdbeaa





## Customization

- **Document Types:** Customize the pipeline to handle specific document formats and extraction tasks.
- **Language Model:** Integrate different language models or fine-tune existing ones for improved performance on specific domains.
- **Chatbot Interface:** Customize the chatbot interface to meet user preferences and requirements.

## Contributing

Contributions are welcome! If you'd like to contribute to the Document Processing and Chatbot Interaction Pipeline project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Special thanks to the developers of Langchain, Ollama, OCR technologies, and Chatbase for their valuable contributions and support.
