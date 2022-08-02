from website import create_app
import os

app = create_app()
port = int(os.getenv('PORT'))

if __name__ == '__main__':
    app.run(port=port, debug=True)