-- Importing services
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")

-- varaible declaration
local buildingTool = script.Parent
local wall = game.ReplicatedStorage.Wall


local plr = game.Players.LocalPlayer
local mouse = plr:GetMouse()

local PlaceRemote = game.ReplicatedStorage.Place

local holdingR = false

UserInputService.InputBegan:Connect(function(inputObject)
	if inputObject.KeyCode == Enum.KeyCode.R then
		holdingR = true
	end
end)

UserInputService.InputEnded:Connect(function(inputObject)
	if inputObject.KeyCode == Enum.KeyCode.R then
		holdingR = false
	end
end)

local rotationAngle = 0

-- buiilding logic
buildingTool.Equipped:Connect(function()
	local wallClone = wall:Clone()
	wallClone.CanCollide = false
	wallClone.Transparency = 0.5
	
	mouse.TargetFilter = wallClone
	
	local height = wallClone.Size.Y / 2
	
	RunService.Heartbeat:Connect(function(dt)
		if holdingR then
			rotationAngle += dt * 100
		end
		
		wallClone.Position = mouse.Hit.Position + Vector3.new(0, height, 0)
		wallClone.Orientation = Vector3.new(0, rotationAngle, 0)
	end)
	
	wallClone.Parent = workspace
	
	buildingTool.Activated:Connect(function()
		PlaceRemote:FireServer(wallClone.Position, rotationAngle)
	end)
	
	buildingTool.Unequipped:Connect(function()
		wallClone:Destroy()
	end)
end)