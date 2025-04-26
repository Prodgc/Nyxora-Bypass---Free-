-- NOT WORKS 1.
local httpc = false -- DONT TOUCH
pcall(function()
    if not script or not script.Source then
        httpc = true
    end
end)

if httpsc then
    print("http request") -- loadstring(game:HttpGet(" URL "))()
else
    print("source")
end




--second
local function detectExecutionMethod()
    local info = debug.getinfo(2)
    if info and info.what == "Lua" then
        print("source")
    else
        print("http")
    end
end

detectExecutionMethod()
