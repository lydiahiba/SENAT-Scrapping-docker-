from flask import Flask, request, jsonify, render_template
from scrapping import ScrappingSena
import config

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/scrapper',methods=["POST"])
def scrapper():
    link_field = request.form['link_field']
    SENA = ScrappingSena(link_field,config)
    df = SENA.get_press_release_links_by_page()
    SENA.to_es(request.form['es_url'],request.form['index_name'],request.form['username'],request.form['password'],request.form['who'])
    return render_template('results.html',  tables=[df.to_html(classes='table')], titles=df.columns.values)        

if __name__ == '__main__':
    # app.run(port=8888, host='0.0.0.0', debug=True)
    app.run(port=5000,debug=True,host='0.0.0.0')