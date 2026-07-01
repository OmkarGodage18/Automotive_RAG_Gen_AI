# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 23:53:57 2023

@author: admin
"""

from flask import Flask, request, jsonify, render_template

from gen_ai import get_llm


# =========================
# LOAD PDF + CREATE CHATBOT
# =========================

pdf_path = r"Automotive_Sustainability.pdf"

chatbot = get_llm(pdf_path)


# =========================
# CREATE FLASK APP
# =========================

app = Flask(__name__)


# =========================
# HOME PAGE
# =========================

# http://127.0.0.1:5000/

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# CHATBOT API
# =========================

@app.route("/get_answer", methods=["POST"])
def get_answer():

    question = request.form["question"]

    response = chatbot.invoke({
        "query": question
    })

    return jsonify({
        "answer": response["result"]
    })


# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.run(debug=False)