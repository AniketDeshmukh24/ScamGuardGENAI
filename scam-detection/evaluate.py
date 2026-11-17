from collections.abc import Sequence


def evaluate_model(
    actual_labels: Sequence[str],
    predicted_labels: Sequence[str],
) -> dict[str, int | float | str]:
    """Compare actual and predicted labels and return the UI's summary metrics."""
    if len(actual_labels) != len(predicted_labels):
        raise ValueError("actual_labels and predicted_labels must have the same length")
    if not actual_labels:
        raise ValueError("At least one label is required to calculate evaluation metrics")

    normalized_actual = []
    normalized_predicted = []
    for index, (actual, predicted) in enumerate(zip(actual_labels, predicted_labels), start=1):
        if not isinstance(actual, str) or not actual.strip():
            raise ValueError(f"Actual label at row {index} must be a non-empty string")
        if not isinstance(predicted, str) or not predicted.strip():
            raise ValueError(f"Predicted label at row {index} must be a non-empty string")
        normalized_actual.append(actual.strip().casefold())
        normalized_predicted.append(predicted.strip().casefold())

    total_predictions = len(normalized_actual)
    correct_predictions = sum(
        actual == predicted
        for actual, predicted in zip(normalized_actual, normalized_predicted)
    )
    overall_accuracy = round(correct_predictions / total_predictions * 100, 2)

    return {
        "overall_accuracy": overall_accuracy,
        "total_predictions": total_predictions,
        "correct_predictions": correct_predictions,
        "summary": (
            f"{correct_predictions} of {total_predictions} predictions were correct "
            f"({overall_accuracy:.2f}%)."
        ),
    }