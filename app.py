import logging

# Enable logging
logging.basicConfig(level=logging.INFO)

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
