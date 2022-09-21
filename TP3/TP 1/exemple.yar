rule ExampleRule1
{
    strings:
        $my_text_string = "Test_ESGI"
        $my_hex_string = { 544553542045534749 }

    condition:
        $my_text_string or $my_hex_string

}