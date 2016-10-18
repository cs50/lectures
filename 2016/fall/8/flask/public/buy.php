<?php

    // configuration
    require("../includes/config.php"); 

    // if form was submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        // validate submission
        if (empty($_POST["symbol"]))
        {
            apologize("You must specify a stock to buy.");
        }
        else if (empty($_POST["shares"]))
        {
            apologize("You must specify a number of shares.");
        }
        else if (!preg_match("/^\d+$/", $_POST["shares"]))
        {
            apologize("Invalid number of shares.");
        }

        // get stock's price
        $stock = lookup($_POST["symbol"]);
        if ($stock === false)
        {
            apologize("Symbol not found.");
        }

        // get user's cash
        $rows = CS50::query("SELECT cash FROM users WHERE id = ?", $_SESSION["id"]);
        if (count($rows) != 1)
        {
            apologize("Can't find your cash.");
        }
        $cash = $rows[0]["cash"];

        // check whether user can afford
        if ($cash < $_POST["shares"] * $stock["price"])
        {
            apologize("You can't afford that.");
        }

        // update portfolio
        CS50::query("INSERT INTO portfolios (user_id, symbol, shares) VALUES(?, ?, ?) 
            ON DUPLICATE KEY UPDATE shares = shares + VALUES(shares)",
            $_SESSION["id"], $stock["symbol"], $_POST["shares"]);

        // update cash
        CS50::query("UPDATE users SET cash = cash - ? WHERE id = ?", $_POST["shares"] * $stock["price"], $_SESSION["id"]);

        // update history
        CS50::query("INSERT INTO history (user_id, type, symbol, shares, price, datetime)
            VALUES(?, 'BUY', ?, ?, ?, NOW())", $_SESSION["id"], $stock["symbol"],
            $_POST["shares"], $stock["price"]);

        // redirect user
        redirect("/");
    }
    else
    {
        // render form
        render("buy_form.php", ["title" => "Buy"]);
    }

?>
