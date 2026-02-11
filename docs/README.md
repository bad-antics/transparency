# Transparency Documentation

## Overview

Transparency is a network traffic analysis framework written in Julia. It provides deep packet inspection, flow analysis, and network transparency tools for security auditing.

## Features

- **Deep Packet Inspection** — Protocol-aware traffic analysis
- **Flow Analysis** — Track and visualize network flows
- **Anomaly Detection** — ML-based traffic anomaly identification
- **Protocol Decoding** — Support for 50+ network protocols
- **Real-time Monitoring** — Live traffic dashboard

## Quick Start

```julia
using Transparency

# Capture and analyze traffic
capture = start_capture("eth0", duration=60)
flows = extract_flows(capture)

# Detect anomalies
anomalies = detect_anomalies(flows, model=:isolation_forest)
for a in anomalies
    println("$(a.src_ip) → $(a.dst_ip): $(a.description)")
end
```

## Architecture

The framework uses Julia's multi-dispatch system for protocol handling — each protocol gets its own analysis methods that are selected at runtime based on packet type.

## Part of Baudrillard Suite

Transparency is part of the [Baudrillard Suite](https://github.com/bad-antics/baudrillard-suite) ecosystem.
