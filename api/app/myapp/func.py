def killer_feature(value):
    try:
        return {"response": value / 0}, 200
    except Exception as e:
        return {"caused_by": "unexpected error: {}".format(str(e))}, 500
