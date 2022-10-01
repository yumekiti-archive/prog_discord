import attendance
import asyncio

async def main():
  await attendance.delete()

if __name__ == '__main__':
  asyncio.run(main())