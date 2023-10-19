## Challenges you ran into during the project.
    I ran into the problem of not knowing anythin about the Vercel platform or how to get python files running on it. I took some time to understand what Vercel was, and why python files would be able to be served via a web interface. I figured out that you intended for us to use the Python runtime with Serverless Functions to publish our code easily via the Vercel platform.
## What I learned during the project.
    I learned how to use the Vercel platform to edge host APIs and websites, along with writing HTTP Request Handler Code
## Overview of the backlog items you created.
    Browser tries to download python file. Figured out I needed to make the code a class extending a specific class.

## Speculate why you see a different IP address when running the code locally vs viewing the Vercel website.
    Because the code is being hosted and ran on a different sever when it is hosted via Vercel.

## URL of the Vercel website you created within part #4.
    https://module-4-silk.vercel.app/

## Identification of the backlog features your team chose to implement.
    #1 App does not use Flask
    #2 App does not have location
## Specific objectives for these selected features.
    #1 App does not use Flask
        a. App needs to be migrated to flask
        b. Flask functionality needs to be tested
    #2 App does not have location
        a. App needs a new endpoint
        b. This endpoint needs to return a users location
## Rationale behind the choice of these features.
    I chose these features because they would be interesting to implement. Each of these features involves something I have not done with this platform yet.
## Showcase the application code with the new features.
    `curl https://module-4-silk.vercel.app/api/ip`
## Demonstrate the changes pushed to GitHub.
    `curl https://module-4-silk.vercel.app/api`
    `curl https://module-4-silk.vercel.app/api/loc`
    There is also a new github actions script that tests both ip and loc endpoints
## Provide details of the test cases utilized.
    Test cases assert if the server is returning valid data. If there is a 404, the assert will fail.
## Explain the functionality of the CI/CD pipeline.
    The CI/CD pipeline that I implemented lints all of the python files for style infractions, and then runs the test case. This all occurs after deployment, so we ensure that the server is up for testing now.
## Reflect on challenges encountered during this activity, how you addressed them, and the lessons learned.
    I wanted to switch the app over to flask, so I can use their render templates and app routing. I discovered that app routing only works when you browse to the correct directory the py file is in, and the @app.route matches the directory string for these serverless functions.