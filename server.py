from flask import Flask, render_template, redirect, url_for
from helper import dynamic_type

app = Flask(__name__)

# Define a route that renders a template
@app.route('/')
def index():
    # Pass some data to the template
    return render_template('index.html')

    
essay_dates = [
    '2024-02-01', '2024-02-02',
    '2024-02-03'
]
@app.route('/<dynamic>')
def dynamic(dynamic):
    type = dynamic_type(dynamic)

    if type == 'date':
        if dynamic in essay_dates:
            return render_template(f'Essays/{dynamic}.html')
        else:
            return redirect(url_for('index'))
    
    # elif type == 
        
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=9090)
