from Backend import app
# from flask_cors import CORS

app = app.App()
# CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == "__main__":
    app.run(debug=True)
