import speedtest
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_speedtest_result')
def get_speedtest_result():
    st = speedtest.Speedtest()
    st.get_best_server()
    
    # Use the --secure flag to test the speed over HTTPS
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    isp = st.results.client['isp']
    ip = st.results.client['ip']

    return jsonify({
        "download_speed": download_speed,
        "upload_speed": upload_speed,
        "isp": isp,
        "ip": ip
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
