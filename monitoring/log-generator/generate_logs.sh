#!/bin/bash

generate_log() {
  local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
  local user_id=$((RANDOM % 1000 + 1))
  local product_id=$((RANDOM % 100 + 1))
  local quantity=$((RANDOM % 10 + 1))
  local price=$(awk -v min=10 -v max=100 'BEGIN{srand(); print int(min+rand()*(max-min+1))}')
  local total=$(awk "BEGIN {print $quantity * $price}")

  echo "$timestamp, user_id: $user_id, product_id: $product_id, quantity: $quantity, price: $price, total: $total"
}

while true; do
  generate_log
  sleep 1
done