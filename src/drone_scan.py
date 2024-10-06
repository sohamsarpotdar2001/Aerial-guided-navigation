#!/usr/bin/env python3

import asyncio
from math import *
from mavsdk import System
from mavsdk.offboard import (OffboardError, PositionNedYaw)
import csv

async def run():

    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break

    print("-- Arming")
    await drone.action.arm()

    print("-- Setting initial setpoint")
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, 0.0, 0.0))

    print("-- Starting offboard")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard mode failed \
                with error code: {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return
    
    await drone.offboard.set_position_ned(
        PositionNedYaw(0,0,-3,0))
    await asyncio.sleep(10)
    
    await drone.offboard.set_position_ned(
        PositionNedYaw(4,5,-3,0))
    await asyncio.sleep(30)

    y = 5
    x = 4
    while y >= 0:    
        x -= 1
        if x == 0:
            y -= 1
            x = 4
        await drone.offboard.set_position_ned(
            PositionNedYaw(x,y,-3.0,0))
        await asyncio.sleep(10)


    print("-- Stopping offboard")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        print(f"Stopping offboard mode failed \
                with error code: {error._result.result}")


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())