from huggingface_hub import model_info

def check_availability():
    try:
        info=model_info('google/magenta-realtime',token='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')
        print(f"doc: {info.__doc__}")
        print(f"Pipeline tag: {info.pipeline_tag}")
        print(f"Library: {info.library_name}")
    except Exception as e:
        print(f"Error: {e}")
    
def clear_cache():
    from huggingface_hub import scan_cache_dir
    try:
        cache_info = scan_cache_dir()
            
        # Convert frozenset to list to access repos
        repos_list = list(cache_info.repos)
            
        if repos_list:
            # Delete all revisions from the first repo
            repo = repos_list[0]
            if repo.revisions:
                cache_info.delete_revisions(*repo.revisions).execute()
                print(f"Cache cleared for repo: {repo.repo_id}")
            else:
                print("No revisions to delete")
        else:
            print("No repos found in cache")
                
    except Exception as e:
        print(f"Error clearing cache: {e}")
    
def main():
    clear_cache()
    
if __name__=="__main__":
    main()