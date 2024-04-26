local Players = game:GetService("Players")
local statname = "Coins"

local function leaderstat(player)
    local leaderstats = Instance.new("Folder")
    leaderstats.Name = "leaderstats"
    leaderstats.Parent = player

    local points = Instance.new("IntValue")
    points.Name = statname
    points.Value = 0
    points.Parent = leaderstats
end

Players.PlayerAdded:Connect(onPlayerAdded)
