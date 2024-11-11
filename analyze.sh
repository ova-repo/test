#!/bin/bash

print_size() {
    local item=$1
    du -sh "$item" 2>/dev/null
}

analyze_directory() {
    local dir="."
    local items=()

    for item in "$dir"/*; do
        if [ -e "$item" ]; then
            items+=("$(print_size "$item")")
        fi
    done

    printf "%s\n" "${items[@]}" | sort -hr
}

analyze_directory
