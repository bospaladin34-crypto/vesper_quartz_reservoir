import os

filepath = os.path.join(os.environ['HOME'], "vesper_git_repo", "logic", "vesper_tensor_network.py")
with open(filepath, 'r') as f:
    content = f.read()

# Target the exact load command we injected previously
target_string = "weights_only=True)"
collapse_math = "weights_only=True).mean(dim=1) # 8D -> 1D Projection"

if target_string in content and collapse_math not in content:
    content = content.replace(target_string, collapse_math)
    with open(filepath, 'w') as f:
        f.write(content)
    print("[+] DIMENSIONAL FRACTURE SEALED. 8D GEOMETRY PROJECTED TO 1D ACTIVATIONS.")
else:
    print("[!] PATCH ALREADY APPLIED OR TARGET NOT FOUND.")
