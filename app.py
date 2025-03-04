from flask import Flask, render_template, request
import random
import logging

app = Flask(__name__)

# Configure logging to print to console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]  # Ensure logs print to Render logs
)

def calculate_love():
    return random.randint(1, 100)  # Random love percentage

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_name = request.form['user_name']
        crush_name = request.form['crush_name']
        love_percentage = calculate_love()
        
        # Log the data instead of writing to a file
        logging.info(f"{user_name} ❤️ {crush_name} - {love_percentage}% Match!")
        
        return render_template('result.html', user_name=user_name, crush_name=crush_name, love_percentage=love_percentage, fancy_result=f"❤️ {love_percentage}% Match! 💖")
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
