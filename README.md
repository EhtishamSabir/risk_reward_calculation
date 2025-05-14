# Risk-to-Reward Ratio Calculator

This repository contains two scripts to calculate the **Risk-to-Reward (R:R)** ratio for trading, specifically designed for a **SOLUSDT** trade example. The scripts help traders evaluate trade setups by computing the R:R ratio and determining if a trade should be exited based on an R:R threshold of **2**.

## Overview

The scripts are built for a trading scenario with the following parameters (example for SOLUSDT):

- **Entry Price:** $180.0  
- **Take Profit (TP) Price:** $186.0  
- **Stop Loss (SL) Price:** $178.0  
- **Position Type:** Long

### Functionality

#### R:R Calculation

- **Long positions:**  
  `Risk = Entry - SL`  
  `Reward = TP - Entry`  
  `R:R = Reward / Risk`

- **Short positions:**  
  `Risk = SL - Entry`  
  `Reward = Entry - TP`  
  `R:R = Reward / Risk`

**Example for SOLUSDT:**  
`Risk = $180 - $178 = $2`  
`Reward = $186 - $180 = $6`  
`R:R = $6 / $2 = 3.0`

#### Exit Decision

If `R:R < 2`, the trade is considered **unfavorable** (`exit = True`). Otherwise, `exit = False`.  
For SOLUSDT, `R:R = 3.0 ≥ 2`, so `exit = False`.

---

## Scripts

### 1. Pine Script (`risk_reward_SOLUSDT.pine`)

**Purpose:**  
Displays the R:R ratio on the latest candle of a TradingView chart for SOLUSDT, along with entry, TP, and SL lines.

**Features:**

- Draws horizontal lines for:
  - Entry ($180.0, **blue**)
  - TP ($186.0, **green dashed**)
  - SL ($178.0, **red dashed**)
- Shows a label on the latest candle with the R:R ratio (e.g., `"R:R = 3.00"`).
- Displays a **red warning label** if `R:R < 2` (not applicable here).
- Outputs R:R to the TradingView data window.

**Usage:**

1. Open TradingView’s Pine Editor.
2. Copy and paste the script from `risk_reward_SOLUSDT.pine`.
3. Add it to the SOLUSDT chart.
4. The script will display lines and a label on the latest candle.

**Notes:**

- Inputs are **hardcoded** for SOLUSDT (can be updated with `input.float()`).
- Uses floating-point precision for calculations.

---

### 2. Python Script (`risk_reward.py`)

**Purpose:**  
Programmatically calculates the R:R ratio and determines if the trade should be exited (`R:R < 2`).

**Features:**

- Takes parameters: `entry_price`, `tp_price`, `sl_price`, `position_type`.
- Returns a tuple: `(rr_ratio, exit_trade)`  
  where `exit_trade` is `True` if `R:R < 2`, otherwise `False`.

**Example Output for SOLUSDT:**

```bash
Risk-to-Reward Ratio: 3.00  
Exit Trade: False
