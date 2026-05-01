# API Contract: Dashboard (v1)

## Overview
This contract defines the core API surface of the `dashboard` service, based on the current Bruno collection (`dashboard/bruno/`).

## Endpoints

### 1. Booking
- **GET** `/api/booking/available-days/` - Returns available days for booking.
- **GET** `/api/booking/business-hours/` - Returns configured business hours.
- **GET** `/api/booking/services/` - Returns a list of available services.

## Conventions
- All responses are JSON.
- Standard error handling via `project/handlers.py`.
- Pagination metadata via `project/pagination.py`.
