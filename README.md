# LoopMonitorAPIs

---

LoopMonitorAPIs is a backend API project designed to offer restaurant owners a comprehensive report on the online status of their stores during business hours. This system operates by polling store data on an hourly basis and processing it to create a detailed report that encompasses store uptime, downtime, and update status.

</hr>

## Project Overview

The primary functionality of this project revolves around two distinct endpoints:

1. **trigger_report Endpoint:** This endpoint serves the purpose of initiating the generation of the detailed report. When triggered, the system processes the most recent store data to provide an up-to-date report.

2. **get_report Endpoint:** This endpoint allows users to retrieve the generated report. The report includes crucial information such as store uptime, downtime, and update status, providing valuable insights to restaurant owners about their online presence during business hours.

## Data Management

The data sources for this API project are stored in a database, ensuring efficient storage and retrieval of information. Regular updates to the database guarantee that the report reflects the most current and accurate status of the stores.

This project is a valuable tool for restaurant owners, offering a convenient and insightful way to monitor and assess the online performance of their stores. By utilizing the LoopMonitorAPIs, owners can make informed decisions based on real-time data, contributing to the overall optimization of their online presence.
