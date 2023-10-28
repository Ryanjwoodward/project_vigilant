--[[
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗██╗ ██████╗ ██╗██╗      █████╗ ███╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██║██╔════╝ ██║██║     ██╔══██╗████╗  ██║╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║██║██║  ███╗██║██║     ███████║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██║██║   ██║██║██║     ██╔══██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ██║╚██████╔╝██║███████╗██║  ██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                            
                 _        _                         _                      _      _             
  _ __ ___   ___| |_ _ __(_) ___ ___     _ __   ___| |___      _____  _ __| | __ | |_   _  __ _ 
 | '_ ` _ \ / _ \ __| '__| |/ __/ __|   | '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ / | | | | |/ _` |
 | | | | | |  __/ |_| |  | | (__\__ \   | | | |  __/ |_ \ V  V / (_) | |  |   < _| | |_| | (_| |
 |_| |_| |_|\___|\__|_|  |_|\___|___/___|_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_(_)_|\__,_|\__,_|
                                   |_____|                                                                                    
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#   AUTHOR          |       Ryan Woodward
#   ORGANIZATION    |       Grand Canyon University
#   CLASS           |       SWE452 - SDLC II
#   DATE            |       October 28, 2023
#   PROJECT         |       Project Vigilant - A Comprehensive Linux Server Monitoring System
#   FILE            |       metrics_network.lua
#-------------------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION     |       This file contains all the data collection functions for metrics pertaining to Network
#                   |       (i.e Throughput). This file meant to accessed, only, by the data collection script.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
]]



-- -----------------------------------------------------------------------------------------
--                                        IMPORTS
-- -----------------------------------------------------------------------------------------

local subprocess = require("subprocess")
local psutil = require("psutil")
local socket = require("socket.http")


-- -----------------------------------------------------------------------------------------
--                                       FUNCTIONS
-- -----------------------------------------------------------------------------------------

-- Define the get_network_throughput function
function get_network_throughput()
    -- Initialize network counters
    local net_counters1 = psutil.net_io_counters()
    
    -- Wait for a moment (e.g., 1 second)
    socket.sleep(1)
    
    -- Get network counters again
    local net_counters2 = psutil.net_io_counters()
    
    -- Calculate network throughput in bytes per second
    local sent_bytes_per_sec = net_counters2.bytes_sent - net_counters1.bytes_sent
    local received_bytes_per_sec = net_counters2.bytes_recv - net_counters1.bytes_recv
    
    return {
        sent_bytes_per_sec = sent_bytes_per_sec,
        received_bytes_per_sec = received_bytes_per_sec
    }
end

-- Define the get_network_latency function
function get_network_latency(host, count)
    count = count or 4 -- Default to 4 packets
    
    local ping_command = "ping -c " .. count .. " " .. host
    local handle = io.popen(ping_command)
    local result = handle:read("*a")
    handle:close()
    
    local latency = 0
    
    for line in result:gmatch("[^\r\n]+") do
        local _, _, round_trip_time = line:find("time=(%d+%.%d+) ms")
        if round_trip_time then
            latency = tonumber(round_trip_time)
        end
    end
    
    return latency
end

-- Define the is_internet_connected function
function is_internet_connected()
    local url = "https://www.google.com"
    local response, status = socket.request(url)
    
    if status == 200 then
        return true
    else
        return false
    end
end
