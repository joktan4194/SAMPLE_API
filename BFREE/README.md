# BFree Test

This is the technical test for BFree. Please implement this on a public github repository and share URL within the next 3days.

## Step 1: API

This section is to verify your competency in writing code.

You will find a [swagger spec](./swagger.yaml) in this zip file defining an API that you must create. It is a simple user system with a single endpoint. Please use the specification and write an API in the language of your choosing. Keep in mind that you will need to store the user information.

## Step 2: Local Setup

This step is to verify your competency in development workflow.

Create a local environment that can be used to verify the code. Please keep in mind that a large number of projects are done with various setups (Unix- and Windows-based), so on any local setup please take into consideration this limitation (i.e. make sure it works across platforms). There is a [CSV](./data.csv) containing data that should be able to be loaded in order to test your setup; please think of a creative way to make loading the data easier.

## Step 3: Containerization and Orchestration

This step is to test your understanding of containerization, automation and orchestration.

Please containerize your application and create the required github action to deploy your application to a sample AWS ECS cluster (We assume you have a personal AWS account before now, if not, create one, you can destroy the resources consumed during this test within the next 7days after submission). Please use best practices when setting this up (treat it as if it were going into production). Part of the process should include the automation of loading the data into the storage that you have chosen.

_NB:_ BFree is a Fintech company, so while we believe in innovation, this should not be at the cost of compromising on security.

