<?php

    // configuration
    require("../includes/config.php"); 

    // if form was submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        // validate submission
        if (empty($_POST["symbol"]))
        {
            apologize("You must provide a symbol.");
        }

        // look up quote
        $stock = lookup($_POST["symbol"]);
        if ($stock === false)
        {
            apologize("Symbol not found.");
        }

        // render quote
        render("quote.php", ["stock" => $stock, "title" => "Quote"]);
    }
    else
    {
        // else render form
        render("quote_form.php", ["title" => "Get Quote"]);
    }

?>
