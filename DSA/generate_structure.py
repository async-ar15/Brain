import os
import re

dsa_sheet_path = r"c:\Lab\DSA\DSA_SHEET.md"
base_dir = r"c:\Lab\DSA"

template = """---

# understanding the question 

Pointing out these things:
- i. Draw examples
- ii. Clarify edge cases
- iii. Confirm input/output
- iv. Important key words for the approach 
- v. basic level of understanding of the question & what kinda solution might work for us 

# understanding the constraints

Pointing out these things: 
- i. Time complexity
- ii. Space complexity
- iii. Input space, output space
- iv. What kind of data structure or algorithm can be used here
- v. how constraints help us to find the solution 

# Solution 

## Brute force 

- Intution for the brute force 
- pseudo code for the brute  force 
- draw the dry run for the brute force
- Time complexity and space complexity of the brute force approach 
- solution code 

## better code (if there)

- how  we are optimising from the brute force
- Intution 
- pseudo code for the better approach 
- draw the dry run for the better approach
- Time complexity and space complexity of the better approach 
- solution code 

## optimised code (if there)

- how  we are optimising from the better code
- Intution 
- pseudo code for the optimised approach 
- draw the dry run for the optimised approach
- Time complexity and space complexity of the optimised approach 
- solution code 

# question where I went wrong & what is the correction 
"""

def generate_structure():
    with open(dsa_sheet_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split content by days
    days = re.split(r'## Day \d+:', content)[1:]
    day_names = re.findall(r'## Day (\d+): (.*)', content)

    for i, (day_num, day_topic) in enumerate(day_names):
        # Sanitize topic name
        clean_topic = day_topic.strip().replace('/', '-').replace('\\', '-').replace('?', '').replace(':', '').replace('*', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
        folder_name = f"{int(day_num):02d}-{clean_topic}"
        folder_path = os.path.join(base_dir, folder_name)
        
        # Create directories
        theory_dir = os.path.join(folder_path, "Theory")
        question_dir = os.path.join(folder_path, "Question")
        os.makedirs(theory_dir, exist_ok=True)
        os.makedirs(question_dir, exist_ok=True)
        
        # Create theory files (placeholders)
        for t_file in ["Pre-requisite.md", "revise.md", "Theory.md"]:
            tf_path = os.path.join(theory_dir, t_file)
            if not os.path.exists(tf_path):
                with open(tf_path, "w", encoding="utf-8") as f:
                    f.write(f"# {day_topic} - {t_file.split('.')[0]}\n\n")
                    f.write("> **Note:** In-depth theory for this topic will be generated when you are ready to study this day. Just ask me to 'generate theory for this topic'!\n")
                    
        # Create insight.md
        insight_path = os.path.join(folder_path, "insight.md")
        if not os.path.exists(insight_path):
            with open(insight_path, "w", encoding="utf-8") as f:
                f.write(f"# Insights for {day_topic}\n\n")

        # Parse questions for this day
        day_content = days[i]
        # Regex to capture the index, name, difficulty, and url
        questions = re.findall(r'\|\s*\[(\d+)\.\s*(.+?)\s*#\d+\s*\((.*?)\)\]\((.*?)\)', day_content)
        
        for q_idx, q_name, q_diff, q_url in questions:
            q_name_clean = q_name.strip().replace('/', '-').replace(':', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
            q_filename = f"{int(q_idx):02d} {q_name_clean}.md"
            q_filepath = os.path.join(question_dir, q_filename)
            
            if not os.path.exists(q_filepath):
                with open(q_filepath, "w", encoding="utf-8") as f:
                    f.write(f"# [{q_name}]({q_url})\n\n")
                    f.write(f"**Difficulty:** {q_diff}\n\n")
                    f.write(template)

    print("Structure generated successfully!")

if __name__ == "__main__":
    generate_structure()
