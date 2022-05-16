import mysql.connector
text_blob = []

connection = mysql.connector.connect(
            host="localhost",
            user="",
            passwd="",
            database=""
)
cursor = connection.cursor()
#border: 1px groove black;s
form = """\n<br>\n<footer style="height; 100%;background-color: black;color: White;padding: 0;vertical-align: middle;line-height: normal;margin: 0;position: fixed;bottom: -2px;width: 100%;"><h3>
    <form action="{{ url_for('main') }}" method="post">
    <input type="text" name="msg">
    <input type="submit" value="send">
</form>\n</h3>\n</footer>\n\n</body></html>"""
from werkzeug.serving import WSGIRequestHandler
#html_bd = "<html>\n<head><title>Insert_here</title><link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css\" rel=\"stylesheet\"></head><body>\n<h1 style=\"text-align:center;color: white;background-color: black\">Title</h1>"<meta http-equiv=\"Refresh\" content=\"10\">
html_bd = "<html>\n<head><title>Insert_here</title></head><body style=\"background-color: black;\">\n<h1 style=\"text-align:center;color: white;background-color: black\">Title</h1>"
msg_html = "<br>\n<p>"
iframe = "<iframe style=\"border-style: hidden;\" height=\"84%\" width=\"100%\" src=\"/messages\"></iframe>"
text_style = "<p style=\"border: 2px solid black;background-color: black;border-radius: 5px;padding: 10px;margin: 10px 0;color: white;\">"
#text_style = "<p style=\"border: 2px solid #dedede;background-color: #f1f1f1;border-radius: 5px;padding: 10px;margin: 10px 0;\">"
