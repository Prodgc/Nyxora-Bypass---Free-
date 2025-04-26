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
