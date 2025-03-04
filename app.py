from flask import Flask, render_template, request
import random

app = Flask(__name__)

def calculate_love():
    return random.randint(1, 100)  # Random love percentage

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_name = request.form['user_name']
        crush_name = request.form['crush_name']
        love_percentage = calculate_love()
        
        # Log data instead of writing to a file
        app.logger.info(f"{user_name} loves {crush_name}: {love_percentage}%")
        
        return render_template('result.html', user_name=user_name, crush_name=crush_name, love_percentage=love_percentage, fancy_result=f"❤️ {love_percentage}% Match! 💖")
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
