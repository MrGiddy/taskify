"""The entry point to the api application"""
from api.v1 import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
