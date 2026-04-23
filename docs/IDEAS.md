# Implementation Ideas

## Notes:
- implement caching
    - can use cache control headers

- For visualization, we can use:
    - cluvio:
        - [cluvio](https://dashboards.cluvio.com/dashboards/qxny-9e5q-k65v/shared?filters=%7B%22platform_filter%22%3A%5B%5D%2C%22political_content%22%3A%5B%5D%2C%22political_lean%22%3A%5B%5D%7D&sharingToken=78eb1196-5766-429d-acf8-edcfd96b7067&timerange=1759622400~1762300799)
    - [datawrapper](https://www.datawrapper.de/)
    - [flourish](https://flourish.studio/)
    - d3js, plotly, chartjs
- for AI analysis, either make our own, or use:
    - automl solutions?
        - [autoML list](https://github.com/askery/automl-list)
            - [google's vertex ai](https://cloud.google.com/vertex-ai)
            - [microsoft's NNI - now archived](https://github.com/microsoft/nni)


## Features

### Big
- Add basic analysis of uploaded files, regardless of dataset/columns
    - need to find a way to analyze data from different populations (example: population data vs likelihood of voting vs most used platform) and determine the appropriate type/level of analysis
    - then, have AI generate text summary (and visuals, possibly?) explaining any insights
        - try to clean data (remove nulls/zeroes), but also note if the data needs to be cleaned by a human first before returning results
    - to simplify, can have the AI just return prettified data first, and then answer specific questions from the user

- Add panel that makes a call to backend (not built yet) to check sentiment on recent US news on major social media platforms

- Add quick chatgpt/grok/gemini wrapper to the "platform tips" page so users can see how their message will be summarized by popular AI models

### Small
- Save text inputted to textarea on "AI Platform Guides" panel to localstorage
- Add another mockup panel with upcoming deadlines or voting events
    - used to decide when to text voters
- once I fully transfer to backend, change "AI platform guides" and "georgia developments" to fetch data from the backend, instead of using hardcoded info

