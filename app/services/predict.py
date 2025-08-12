from app.models.model_loader import model


def make_prediction(feature_vector, return_score=False):
    prediction = model.predict(feature_vector)
    is_inlier = int(prediction[0])

    response_data = {"is_inlier": is_inlier}

    if return_score:
        scores = model.score_samples(feature_vector)
        response_data["anomaly_score"] = float(scores[0])
    return response_data
