local players = game.Players

local changeColor = game.ReplicatedStorage.Admin
local spawnLocation = game.Workspace.SpawnLocation
local adminPanel = game.ServerStorage.AdminPanel
local consoleBtn = game.ServerStorage.Console

local Buy = game.ReplicatedStorage.Buy
local sword = game.ServerStorage.Sword


local admin = "Player1"

local Attack = game.ReplicatedStorage.Attack

local hitbox = game.ServerStorage.Hitbox

local s1 = game.SoundService.s1
local s2 = game.SoundService.s2

local hitVfx = game.ServerStorage.VFX_Attachment.Circle2



-- plr join
players.PlayerAdded:Connect(function(plr)
	local leaderstats = Instance.new("Folder", plr)
	leaderstats.Name = "leaderstats"
	
	local coins = Instance.new("IntValue", leaderstats)
	coins.Name = "Coins"
	coins.Value = 100
	
	if plr.Name == admin then
		adminPanel.Parent = plr.PlayerGui
		consoleBtn.Parent = plr.PlayerGui:WaitForChild("Main")
	end
end)

-- admin commands
changeColor.OnServerEvent:Connect(function(plr, color)
	if plr.Name == admin then
		spawnLocation.Color = color
	else
		-- anticheat 
		plr:Kick("NICE TRY BUDDY, FIND BETTER GAME EXPLOIT")
	end
end)


-- buy item
Buy.OnServerInvoke = function(plr)
	if plr.leaderstats.Coins.Value >= 50 then
		plr.leaderstats.Coins.Value -= 50
		local newSword = sword:Clone()
		newSword.Parent = plr.Backpack
		return true
	end
	return false
end

-- sword combat
Attack.OnServerInvoke = function(plr)

	if plr:FindFirstChild("Attacking") then
		return
	end

	local attacking = Instance.new("Folder")
	attacking.Name = "Attacking"
	attacking.Parent = plr

	if not plr:FindFirstChild("attackingCombo") then
		local attackingCombo = Instance.new('IntValue')
		attackingCombo.Name = "attackingCombo"
		attackingCombo.Value = 0
		attackingCombo.Parent = plr
	end

	game.Debris:AddItem(attacking, 0.3)

	local hitboxClone = hitbox:Clone()
	hitboxClone.CFrame = plr.Character.HumanoidRootPart.CFrame * CFrame.new(0, 0, -3)

	local comboNumber = plr:FindFirstChild("attackingCombo").Value

	if comboNumber % 2 == 0 then
		local s1Clone = s1:Clone()
		s1Clone.Parent = 	plr.Character.HumanoidRootPart
		s1Clone:Play()
	else
		local s2Clone = s2:Clone()
		s2Clone.Parent = plr.Character.HumanoidRootPart
		s2Clone:Play()
	end

	plr:FindFirstChild("attackingCombo").Value += 1

	local params = OverlapParams.new()
	params.FilterType = Enum.RaycastFilterType.Exclude
	params.FilterDescendantsInstances = {plr.Character}

	local touched = game.Workspace:GetPartsInPart(hitboxClone, params)
	hitboxClone.Parent = game.Workspace
	game.Debris:AddItem(hitboxClone, 0.3)

	for _, item in pairs(touched) do
		local humanoid = item.Parent:FindFirstChild("Humanoid")
		local vfxClone = hitVfx:Clone()

		if humanoid then
			vfxClone.Parent = item.Parent.HumanoidRootPart.RootAttachment
			game.Debris:AddItem(vfxClone, 0.85)
			humanoid.Health -= 20
			return true
		end
	end

	return false
end