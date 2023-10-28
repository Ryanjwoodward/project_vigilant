#!/bin/bash

# Function to get network throughput
get_network_throughput() {
    net_counters1=$(cat /proc/net/dev | grep "eth0" | awk '{print $10, $2}')
    sleep 1
    net_counters2=$(cat /proc/net/dev | grep "eth0" | awk '{print $10, $2}')

    sent_bytes1=$(echo "$net_counters1" | awk '{print $1}')
    received_bytes1=$(echo "$net_counters1" | awk '{print $2}')
    sent_bytes2=$(echo "$net_counters2" | awk '{print $1}')
    received_bytes2=$(echo "$net_counters2" | awk '{print $2}')

    sent_bytes_per_sec=$((sent_bytes2 - sent_bytes1))
    received_bytes_per_sec=$((received_bytes2 - received_bytes1))

    echo "Sent bytes per second: $sent_bytes_per_sec"
    echo "Received bytes per second: $received_bytes_per_sec"
}

# Function to get network latency
get_network_latency() {
    host="$1"
    count="${2:-4}" # Default to 4 packets

    ping_result=$(ping -c "$count" "$host")
    latency=$(echo "$ping_result" | grep "round-trip" | awk -F'/' '{print $5}')

    echo "Latency to $host: $latency ms"
}

# Function to check internet connectivity
is_internet_connected() {
    url="https://www.google.com"
    status_code=$(curl -o /dev/null -s -w "%{http_code}" "$url")

    if [ "$status_code" -eq 200 ]; then
        echo "Connected to the internet."
    else
        echo "Not connected to the internet."
    fi
}

# Main script
echo "Network Throughput:"
get_network_throughput

echo -e "\nNetwork Latency:"
get_network_latency "example.com"  # Replace "example.com" with the desired host

echo -e "\nInternet Connectivity Check:"
is_internet_connected
