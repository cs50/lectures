<?php

    // configuration
    require("../includes/config.php"); 
    
    // get user's cash
    $rows = CS50::query("SELECT cash FROM users WHERE id = ?", $_SESSION["id"]);
    if ($rows === false)
    {
        apologize("Can't find your cash.");
    }
    $cash = $rows[0]["cash"];

    // get user's portfolio
    $rows = CS50::query("SELECT * FROM portfolios WHERE user_id = ?", $_SESSION["id"]);
    if ($rows === false)
    {
        apologize("Can't find your portfolio.");
    }

    // look up stocks' names and prices
    $positions = [];
    foreach ($rows as $row)
    {
        $stock = lookup($row["symbol"]);
        if ($stock !== false)
        {
            $positions[] = [
                "name" => $stock["name"],
                "price" => $stock["price"],
                "shares" => $row["shares"],
                "symbol" => $row["symbol"]
            ];
        }
    }

    // render portfolio
    render("portfolio.php", ["cash" => $cash, "positions" => $positions, "title" => "Portfolio"]);

?>
