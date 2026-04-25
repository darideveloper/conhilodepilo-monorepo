# Create Categories API

## Summary
Implements a new public API endpoint `GET /api/services/` to retrieve all available service categories (`EventType` models) and their associated nested services (`Event` models). This API is required for the frontend discovery phase to display what services are offered.

## Context
The booking system utilizes a two-step selection process: selecting a category, then selecting a service within that category. The current documentation outlines a `GET /services/` endpoint to handle this. The system already has the `EventType` and `Event` models defined with the necessary data. We need to expose this data, including all relevant texts, images, and configuration flags, but strictly excluding availability data as per requirements.

## Problem Statement
The frontend needs to present a catalog of services grouped by categories to the user. Currently, there is no API endpoint to provide this structured data.

## Proposed Solution
We will implement a Django REST Framework (DRF) `ListAPIView` for `GET /api/services/`.
The endpoint will return a list of `EventType` objects. Each object will contain its own details (id, name, description, image) and a nested list of related `Event` objects (`services`). Each nested service will include its id, title (name), description, price, duration, and image. Availability configurations will be explicitly omitted from this endpoint.

We will also provide unit tests and update the Bruno API collection to ensure the endpoint is synchronized.

## Alternatives Considered
- Returning categories and services in separate flat lists: Rejected because the two-step frontend UI heavily relies on the nested relationship. Returning them nested minimizes client-side data massaging.
- Including availability directly in the category response: Rejected per explicit requirements, as it would cause the payload size to balloon and make caching less effective (since availability changes frequently, while catalog data changes rarely).
