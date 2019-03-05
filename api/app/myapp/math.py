import numpy as np


def random(size):
    try:
        if isinstance(size, int) and size > 0:
            return {"result": np.random.randint(100, size=size).tolist()}, 200
        else:
            return {"caused_by": "invalid size type"}, 400
    except Exception as e:
        return {"caused_by": "unexpected error: {}".format(str(e))}, 500
