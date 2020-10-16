from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook
from bokeh.resources import CDN
from bokeh.embed import file_html, components
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/customplot')
def custom_plot():
    stock = request.args.get('ticker')
    start = "2017-01-01"
    end = "2020-08-30"

    data = pd.DataFrame(yf.download(stock, start=start, end=end).reset_index())

    p1 = figure(x_axis_type="datetime", title="Stock Closing Prices")
    p1.grid.grid_line_alpha=0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Price'

    p1.line(data['Date'], data['Close'], color='green')
    #show(p1)
    script, div = components(p1)
    
    return render_template('plot2.html', script=script, div=div)

if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
    app.run()

