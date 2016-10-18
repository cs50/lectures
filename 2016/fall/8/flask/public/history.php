<?php

    // configuration
    require("../includes/config.php"); 
    
    // get user's history
    $rows = CS50::query("SELECT * FROM history WHERE user_id = ?", $_SESSION["id"]);
    if ($rows === false)
    {
        apologize("Can't find your history.");
    }

    // render history
    render("history.php", ["title" => "Portfolio", "transactions" => $rows]);

?>
