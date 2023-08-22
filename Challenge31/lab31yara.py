rule ChromeBrowser {
    meta:
        description = "Detects Google Chrome Browser"
        author = "Raphael Chookagian"
        date = "2023-08-21"

    strings:
        $chrome_sig1 = "Chrome.dll"
        $chrome_sig2 = { 43 68 72 6F 6D 65 }  

    condition:
        any of ($chrome_sig*)
}
