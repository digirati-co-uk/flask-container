from main import app as application
import settings

if __name__ == "__main__":
    application.run(debug=settings.DEBUG)
