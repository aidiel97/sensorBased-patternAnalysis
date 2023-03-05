"""Dimentional Reduction on Botnet Data"""
"""Writen By: M. Aidiel Rachman Putra"""
"""Organization: Net-Centic Computing Laboratory | Institut Teknologi Sepuluh Nopember"""

import warnings

warnings.simplefilter(action='ignore')

# import utilities.helpers.menuManagement as menu
import utilities.repositories.dataLoader as load
from utilities.helpers.common import *

if __name__ == "__main__":
  load.pcap(ctuPcap['scenario1'])
  # menu.mainMenu()

# from flask import Flask, request, redirect

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def upload_file():
#     if request.method == "POST":
#         file = request.files["file"]
#         if file:
#             contents = file.read()
#             # Do something with the contents of the file
#             return redirect("/")
#     return '''
#     <form action="/" method="post" enctype="multipart/form-data">
#         <input type="file" name="file">
#         <input type="submit" value="Upload">
#     </form>
#     '''

# if __name__ == "__main__":
#     app.run(debug=True)