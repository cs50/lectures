<?php

    // configuration
    require("../includes/config.php"); 

    // if form was submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        // validate submission
        if (empty($_POST["symbol"]))
        {
            apologize("You must select a stock to sell.");
        }

        // get user's number of shares
        $rows = CS50::query("SELECT shares FROM portfolios WHERE user_id = ? AND symbol = ?", $_SESSION["id"], $_POST["symbol"]);
        if (count($rows) != 1)
        {
            apologize("You don't own that stock.");
        }
        $shares = $rows[0]["shares"];

        // sell shares
        $stock = lookup($_POST["symbol"]);
        if ($stock !== false)
        {
            // update portfolio
            CS50::query("DELETE FROM portfolios WHERE user_id = ? AND symbol = ?", $_SESSION["id"], $_POST["symbol"]);

            // update cash
            CS50::query("UPDATE users SET cash = cash + ? WHERE id = ?", $shares * $stock["price"], $_SESSION["id"]);

            // update history
            CS50::query("INSERT INTO history (user_id, type, symbol, shares, price, datetime)
                VALUES(?, 'SELL', ?, ?, ?, NOW())", $_SESSION["id"], $stock["symbol"],
                $shares, $stock["price"]);

            // redirect user
            redirect("/");
        }
    }
    else
    {
        // get user's portfolio
        $symbols = [];
        $rows = CS50::query("SELECT symbol FROM portfolios WHERE user_id = ? ORDER BY symbol", $_SESSION["id"]);
        if ($rows === false)
        {
            apologize("Could not find your portfolio.");
        }

        // get symbols in portfolio
        foreach ($rows as $row)
        {
            $symbols[] = $row["symbol"];
        }

        // render form
        if (count($symbols) > 0)
        {
            render("sell_form.php", ["symbols" => $symbols, "title" => "Sell"]);
        }
        else
        {
            apologize("Nothing to sell.");
        }
    }

?>
