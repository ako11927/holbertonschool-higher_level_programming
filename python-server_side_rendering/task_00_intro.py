import os

def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and a list of attendees.
    
    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries containing attendee data
    
    Returns:
        None: Creates output files or logs error messages
    """
    
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list.")
        return
    
    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Verify each attendee is a dictionary
    for i, attendee in enumerate(attendees, 1):
        if not isinstance(attendee, dict):
            print(f"Error: Attendee at index {i-1} is not a dictionary.")
            return
    
    # Process each attendee
    for i, attendee in enumerate(attendees, 1):
        try:
            # Start with the template
            processed_text = template
            
            # Define the placeholders to replace
            placeholders = ['name', 'event_title', 'event_date', 'event_location']
            
            # Replace each placeholder with the value from attendee or "N/A"
            for placeholder in placeholders:
                # Get the value from attendee, use "N/A" if missing or None
                value = attendee.get(placeholder)
                if value is None or value == "":
                    value = "N/A"
                
                # Replace the placeholder in the template
                processed_text = processed_text.replace(f"{{{placeholder}}}", str(value))
            
            # Generate output filename
            output_filename = f"output_{i}.txt"
            
            # Write to file
            with open(output_filename, 'w') as file:
                file.write(processed_text)
            
            print(f"Created {output_filename}")
            
        except Exception as e:
            print(f"Error processing attendee {i}: {e}")
