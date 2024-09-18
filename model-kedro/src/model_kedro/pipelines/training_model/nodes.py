def generate_model(train_df):
    import pandas as pd
    import lightgbm as lgb
    from sklearn.model_selection import train_test_split

    train_df["mana_group"] = pd.cut(train_df["mana"], 5, labels=[0, 1, 2, 3, 4])
    train_df["attack_group"] = pd.cut(train_df["attack"], 5, labels=[0, 1, 2, 3, 4])
    train_df["health_group"] = pd.cut(train_df["attack"], 5, labels=[0, 1, 2, 3, 4])
    gods_c = {
        "neutral": 0,
        "light": 1,
        "nature": 2,
        "deception": 3,
        "death": 4,
        "war": 5,
        "magic": 6,
    }
    train_df["god_categories"] = train_df["god"].map(lambda x: gods_c.get(x, 7))
    type_c = {"creature": 0, "spell": 1, "weapon": 2, "god power": 3}
    train_df["type_categories"] = train_df["type"].map(lambda x: type_c.get(x, 4))
    train_df["strategy_categories"] = train_df["strategy"].map(
        lambda x: 0 if x == "early" else 1
    )
    X = train_df[
        [
            "type_categories",
            "god_categories",
            "mana_group",
            "attack_group",
            "health_group",
            "mana",
            "health",
            "attack",
        ]
    ]
    y = train_df["strategy_categories"]
    X_train, X_valid, y_train, y_valid = train_test_split(
        X[
            [
                "type_categories",
                "god_categories",
                "mana_group",
                "attack_group",
                "health_group",
            ]
        ],
        y,
        test_size=0.2,
        random_state=42,
    )
    train_data = lgb.Dataset(
        X_train,
        label=y_train,
        categorical_feature=[
            "type_categories",
            "god_categories",
            "mana_group",
            "health_group",
            "attack_group",
        ],
    )
    valid_data = lgb.Dataset(X_valid, label=y_valid, reference=train_data)
    params = {
        "objective": "binary",
        "metric": "binary_logloss",
        "boosting_type": "gbdt",
        "num_leaves": 11,
        "learning_rate": 0.05,
    }
    num_round = 100
    lgb_model = lgb.train(
        params, train_data, num_round, valid_sets=[train_data, valid_data]
    )
    return lgb_model
