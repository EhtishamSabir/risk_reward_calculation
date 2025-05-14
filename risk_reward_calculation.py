def calculate_risk_reward(entry_price, tp_price, sl_price, position_type):
    """
    Calculate Risk-to-Reward ratio and determine if trade should be exited.

    Parameters:
    - entry_price (float): Price at which trade is entered
    - tp_price (float): Take-profit price
    - sl_price (float): Stop-loss price
    - position_type (str): "Long" or "Short"

    Returns:
    - tuple: (rr_ratio, exit)
        - rr_ratio (float): Risk-to-Reward ratio
        - exit (bool): True if R:R < 2, False otherwise
    """
    # Initialize variables
    risk = 0.0
    reward = 0.0
    rr_ratio = 0.0

    # Calculate risk and reward based on position type
    if position_type == "Long":
        risk = entry_price - sl_price
        reward = tp_price - entry_price
    elif position_type == "Short":
        risk = sl_price - entry_price
        reward = entry_price - tp_price
    else:
        raise ValueError("position_type must be 'Long' or 'Short'")

    # Avoid division by zero
    if risk == 0:
        raise ValueError("Risk cannot be zero (entry_price equals sl_price)")

    # Calculate R:R ratio
    rr_ratio = reward / risk

    # Determine if trade should be exited (R:R < 2)
    exit_trade = rr_ratio < 2

    return rr_ratio, exit_trade


# Example usage for SOLUSDT for testing purpose
if __name__ == "__main__":
    entry_price = 180.0
    tp_price = 186.0
    sl_price = 178.0
    position_type = "Long"

    rr_ratio, exit_trade = calculate_risk_reward(entry_price, tp_price, sl_price, position_type)
    print(f"Risk-to-Reward Ratio: {rr_ratio:.2f}")
    print(f"Exit Trade: {exit_trade}")