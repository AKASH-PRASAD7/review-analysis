import os
from huggingface_hub import hf_hub_download

def download_model():
    repo_id = "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF"
    filename = "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
    
    # Target directory: backend/models
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_dir = os.path.join(base_dir, "models")
    os.makedirs(models_dir, exist_ok=True)
    
    dest_path = os.path.join(models_dir, "model.gguf")
    
    if os.path.exists(dest_path):
        print(f"Model already exists at {dest_path}")
        return

    print(f"Downloading {filename} from {repo_id}...")
    try:
        model_path = hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            local_dir=models_dir,
            local_dir_use_symlinks=False
        )
        # Rename to model.gguf for simplicity in app
        os.rename(os.path.join(models_dir, filename), dest_path)
        print(f"Model downloaded and saved to {dest_path}")
    except Exception as e:
        print(f"Failed to download model: {e}")

if __name__ == "__main__":
    download_model()
