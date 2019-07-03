import celery
app = celery.Celery('example')

@app.task
def add(x, y):
    return x + y
