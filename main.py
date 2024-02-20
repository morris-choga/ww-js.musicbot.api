from songmetadata import get_song_metadata
from download_song import download,tagger
from downloadsong_api import download_song
from flask import request
import os
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    requested_song = request.get_json()
    song_metadata = get_song_metadata(f"{requested_song['key']}")


    song = download_song(song_metadata["video_id"])
    # song = download(song_metadata["title"],song_metadata["video_id"],os.path.join("/","songs"))
    tagger(song_metadata["title"],song_metadata["artist"],song_metadata["album_name"],song_metadata["url"],song)


    return type(song)


@app.route('/get_status', methods=['GET'])
def get_status():
    return {'status': 200}, 200

if __name__ =="__main__":
    # app.run(debug=True,use_reloader=False)
    # app.run(debug=True,use_reloader=False,host='0.0.0.0')
    app.run(debug=True,use_reloader=True,host='0.0.0.0')



# build -t bot .
# docker run -v /songs:/usr/src/app/songs --name bot -p 5000:5000 bot