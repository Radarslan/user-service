def assert_unique_violation(response_body: dict, nonunique_value: str) -> None:
    assert (
        response_body.get("detail", None)
        == f"(number)=({nonunique_value}) already exists"
    )
