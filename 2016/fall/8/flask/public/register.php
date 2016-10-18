<?php

    // configuration
    require("../includes/config.php"); 

    // if form was submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        // validate inputs
        if (empty($_POST["username"]))
        {
            apologize("You must provide a username.");
        }
        else if (empty($_POST["password"]))
        {
            apologize("You must provide a password.");
        }
        else if (empty($_POST["confirmation"]) || $_POST["password"] != $_POST["confirmation"])
        {
            apologize("Those passwords did not match.");
        }

        // try to register user
        $rows = CS50::query("INSERT IGNORE INTO users (username, hash, cash) VALUES(?, ?, 10000.0000)",
            $_POST["username"], password_hash($_POST["password"], PASSWORD_DEFAULT)
        );
        if ($rows !== 1)
        {
            apologize("That username appears to be taken.");
        }

        // get new user's ID
        $rows = CS50::query("SELECT LAST_INSERT_ID() AS id");
        if (count($rows) !== 1)
        {
            apologize("Can't find your ID.");
        }
        $id = $rows[0]["id"];

        // log user in
        $_SESSION["id"] = $id;

        // redirect to portfolio
        redirect("/");
    }
    else
    {
        // else render form
        render("register_form.php", ["title" => "Register"]);
    }

?>
