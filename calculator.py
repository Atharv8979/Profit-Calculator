def calculate(cp, sp):
    if sp > cp:
        profit = sp - cp
        profit_percent = (profit / cp) * 100
        msg = f"Profit: ₹{profit:.2f}\nProfit Percentage: {profit_percent:.2f}%"
        return msg, "Profit", profit, profit_percent

    elif cp > sp:
        loss = cp - sp
        loss_percent = (loss / cp) * 100
        msg = f"Loss: ₹{loss:.2f}\nLoss Percentage: {loss_percent:.2f}%"
        return msg, "Loss", loss, loss_percent

    else:
        msg = "Neither Profit nor Loss."
        return msg, "None", 0, 0
