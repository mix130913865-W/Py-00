def evaluate_expression(expression: str) -> str:  # 計算表達式並回傳結果

    try:
        result = str(eval(expression))  # 使用 eval 計算表達式
        # 將結果轉成字串，並將除號和乘號替換
        return result  # 回傳計算結果字串
    except Exception:
        return "Error"  # 計算錯誤時回傳錯誤訊息
