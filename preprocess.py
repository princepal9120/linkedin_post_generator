import json


def process_posts(raw_file_path, processed_file_path):
    enrichecd_posts = []
    with open(raw_file_path, encoding="utf-8") as file:  
        posts=json.load(file)
        # print(posts[0])
        for post in posts:
            metadata = extract_metadata(post['text'])
            post_with_metadata= post | metadata
            enrichecd_posts.append(post_with_metadata)

    for epost in enrichecd_posts:
        print(epost)        

def extract_metadata(text):
    return {
        'line_count': text.count('\n'),
        'language': "English", 
        'tags': ['Recruitement','AI'],
    }

if __name__ == "__main__":
    process_posts("data/raw_post.json", "data/pre_post.json")