# User Flow

## Features:

1. Demographics Analyzer
 - User uploads dataset(CSV) or selects from preloaded datasets
    - User is directed to chat interface, and can ask questions about the dataset
      - A fully-featured version might look like this:
        - https://www.mage.ai/
      - An AI reads the text, and runs code (using an MCP server?) to answer questions:
        - Example:
          - User: "How many people in the dataset are over 30 years old?"
          - AI: "To answer that question, I will run the following code: `len(df[df['age'] > 30])`"
          - AI: "The answer is 150 people."
      - When necessary, ask the user clarifying questions ("over what time period?" or "for which demographic?"
        - https://www.pecan.ai/product-tour/
        
