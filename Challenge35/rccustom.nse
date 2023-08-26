description = [[
Retrieves the title of the web page using HTTP.
]]

categories = {"discovery", "safe"}

portrule = function(host, port)
    return port.number == 80 and port.protocol == "tcp" and port.state == "open"
end

action = function(host, port)
    local http = require("http")
    local result = {}

    local response = http.get(host, port, "/")
    if response.status == 200 then
        local title = string.match(response.body, "<title>(.-)</title>")
        if title then
            result.title = title
            return result
        end
    end
end
