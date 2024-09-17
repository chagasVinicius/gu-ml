def test_add_card(test_client) -> None:
    response = test_client.post(
        "/gu-ml/card",
        json={
            "id": 306,
            "name": "Blood Rage",
            "mana": 2,
            "attack": 0,
            "health": 0,
            "type": "spell",
            "god": "war",
        },
    )
    assert response.status_code == 200
    assert "strategy" in response.json()
    assert "early" == response.json()["strategy"]


def test_add_card_invalid_payload(test_client) -> None:
    response = test_client.post("/gu-ml/card", json={"wrong": "foo"})
    assert response.status_code == 422


def test_get_card(test_client) -> None:
    response = test_client.get("/gu-ml/card/306")

    assert response.status_code == 200
    assert "strategy" in response.json()
    assert "early" == response.json()["strategy"]


def test_get_inexistent_card(test_client) -> None:
    response = test_client.get("/gu-ml/card/0")

    assert response.status_code == 404
