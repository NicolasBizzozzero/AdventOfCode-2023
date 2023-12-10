from itertools import pairwise


def mirage_maintenance(report):
    predictions = []
    predictions_reversed = []
    for history in report:
        predictions.append(predict_value(history=history))
        predictions_reversed.append(predict_value(history=list(reversed(history))))
    return sum(predictions), sum(predictions_reversed)


def predict_value(history: list[int]) -> int:
    if not history:
        return 0

    # Compute differences (with one less value, because pairwise)
    differences = [b - a for a, b in pairwise(history)]
    return history[-1] + predict_value(differences)
