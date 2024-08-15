
# FitAdvisor – Personalized Gym Advice System
**FitAdvisor** is a Streamlit-based web application that provides personalized gym advice and workout recommendations. By inputting details such as weight, height, fitness goals, and body composition, users receive tailored fitness advice generated using the LLaMA 3 model.

## Features

- **User Input Handling:** Interactive sliders and selection boxes to capture user details.
- **Personalized Recommendations:** Uses LLaMA 3 to generate customized gym advice based on user inputs.
- **Real-Time Feedback:** Provides instant advice and recommendations as users interact with the app.
- **User-Friendly Interface:** Designed with Streamlit for an intuitive and engaging user experience.

## Technologies Used

- **Streamlit:** Framework for building interactive web applications.
- **LLaMA 3:** Model for generating personalized fitness recommendations.
- **Python:** Core programming language used for application logic.

## Setup

To run this project locally, follow these steps:

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/FitAdvisor.git
   ```

2. **Navigate to the Project Directory:**

   ```sh
   cd FitAdvisor
   ```

3. **Create a Virtual Environment (Optional but recommended):**

   ```sh
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**

   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

5. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

6. **Run the Streamlit App:**

   ```sh
   streamlit run app.py
   ```

7. **Open your browser and navigate to:**

   ```plaintext
   http://localhost:8501
   ```

## Usage

- **Enter your weight:** Use the slider to specify your weight.
- **Enter your height:** Use the slider to specify your height.
- **Select your fitness goal:** Choose from options like Fat Loss, Muscle Gain, Shredded, or Lean.
- **Select your current body type:** Choose from options like Fat, Skinny, or SkinnyFat.
- **Click "Generate":** Get personalized gym advice based on your inputs.

## Project Structure

- `app.py`: Main Streamlit application file.
- `requirements.txt`: Lists the required Python packages.
- `README.md`: Project documentation.

## Contribution

Feel free to contribute to this project by creating a pull request or opening an issue. Your feedback and suggestions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.