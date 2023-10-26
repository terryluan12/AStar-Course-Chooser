from run import app
if __name__ == "__main__":
  app.run(port=os.environ.get("PORT", default=os.environ.get("PORT", default=5000)))