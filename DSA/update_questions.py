import os
import re
import requests
import markdownify
import json

TERMINOLOGY_DICT = {
    "substring": "A contiguous sequence of characters within a string.",
    "subsequence": "A sequence derived from another sequence by deleting some or no elements without changing the order of the remaining elements.",
    "contiguous": "Sharing a common border; touching. In arrays, it means elements that are next to each other.",
    "monotonic": "A sequence that is entirely non-increasing or non-decreasing.",
    "anagram": "A word, phrase, or name formed by rearranging the letters of another.",
    "palindrome": "A word, phrase, number, or other sequence of characters which reads the same backward as forward.",
    "lexicographical": "Alphabetical order.",
    "binary search tree": "A binary tree in which the left child of a node contains only nodes with keys less than the node's key, and the right child only nodes with keys greater than the node's key.",
    "bipartite": "A graph whose vertices can be divided into two disjoint sets such that every edge connects a vertex in one set to a vertex in the other set.",
    "topological sort": "A linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.",
    "trie": "A type of search tree, a tree data structure used for locating specific keys from within a set. These keys are most often strings, with links between nodes defined not by the entire key, but by individual characters.",
    "prefix sum": "An array whose i-th element is the sum of the first i elements of the original array.",
    "sliding window": "A subset of given array/string that 'slides' over the data to perform some operation over a range.",
    "dynamic programming": "A method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions."
}

def get_leetcode_question(title_slug):
    url = "https://leetcode.com/graphql"
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        content
      }
    }
    """
    variables = {"titleSlug": title_slug}
    try:
        response = requests.post(url, json={"query": query, "variables": variables}, timeout=10)
        data = response.json()
        if 'data' in data and data['data']['question']:
            return data['data']['question']['content']
    except Exception as e:
        print(f"Error fetching {title_slug}: {e}")
    return None

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find Leetcode link
    match = re.search(r'\[.+?\]\((https://leetcode\.com/problems/([^/]+)/?)\)', content)
    if not match:
        return False
    
    title_slug = match.group(2)
    
    # Check if we already injected the problem description
    if "### Terminology" in content or "Example 1:" in content or "<strong>Constraints:</strong>" in content or "Constraints:" in content:
        # It's likely already populated, skip to avoid double injection
        print(f"Skipping {filepath} - already populated.")
        return False

    print(f"Fetching {title_slug} for {filepath}...")
    html_content = get_leetcode_question(title_slug)
    if not html_content:
        print(f"Failed to fetch content for {title_slug}")
        return False
    
    # Convert HTML to Markdown
    md_content = markdownify.markdownify(html_content, heading_style="ATX").strip()
    
    # Add terminology if keywords are found
    found_terms = {}
    lower_md = md_content.lower()
    for term, definition in TERMINOLOGY_DICT.items():
        # Match word boundaries to avoid partial matches
        if re.search(r'\b' + re.escape(term) + r'\b', lower_md):
            found_terms[term] = definition
            
    if found_terms:
        md_content += "\n\n### Terminology\n"
        for term, definition in found_terms.items():
            md_content += f"- **{term.capitalize()}**: {definition}\n"
            
    # Inject into content. We want to place it between **Difficulty:** <diff> and ---
    # Find the insertion point
    diff_match = re.search(r'(\*\*Difficulty:\*\*\s*[^\n]+)\n+(---)', content)
    if not diff_match:
        # Try alternate pattern if spacing is weird
        diff_match = re.search(r'(\*\*Difficulty:\*\*\s*[^\n]+)\n+(# understanding the question)', content)
        if not diff_match:
            print(f"Could not find insertion point in {filepath}")
            return False
        replacement = f"{diff_match.group(1)}\n\n{md_content}\n\n---\n\n{diff_match.group(2)}"
        new_content = content.replace(diff_match.group(0), replacement, 1)
    else:
        replacement = f"{diff_match.group(1)}\n\n{md_content}\n\n{diff_match.group(2)}"
        new_content = content.replace(diff_match.group(0), replacement, 1)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    return True

def main():
    base_dir = r"c:\Brain\DSA"
    updated_count = 0
    for root, dirs, files in os.walk(base_dir):
        if "Question" in os.path.basename(root):
            for file in files:
                if file.endswith(".md"):
                    filepath = os.path.join(root, file)
                    if process_file(filepath):
                        updated_count += 1
                        
    print(f"\nDone! Successfully updated {updated_count} files.")

if __name__ == "__main__":
    main()
