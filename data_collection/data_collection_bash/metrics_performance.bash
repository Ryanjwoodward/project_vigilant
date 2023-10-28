#!/bin/bash

# Function to get system load averages
get_load_average() {
    loadavg=$(cat /proc/loadavg)
    IFS=' ' read -ra load_array <<< "$loadavg"
    echo "1-minute: ${load_array[0]}"
    echo "5-minute: ${load_array[1]}"
    echo "15-minute: ${load_array[2]}"
}

# Function to get system uptime
get_uptime() {
    uptime
}

# Function to measure response time of a web request
get_response_time() {
    url="$1"
    start_time=$(date +%s.%N)
    status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    end_time=$(date +%s.%N)

    if [ "$status_code" -eq 200 ]; then
        response_time_ms=$(echo "scale=3; ($end_time - $start_time) * 1000" | bc)
        echo "Response time: $response_time_ms ms"
    else
        echo "HTTP request failed with status code $status_code"
    fi
}

# Main script
echo "System Load Averages:"
get_load_average

echo -e "\nSystem Uptime:"
get_uptime

echo -e "\nResponse Time for https://www.google.com:"
get_response_time "https://www.google.com"
