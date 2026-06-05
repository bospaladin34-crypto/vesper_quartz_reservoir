import os

filepath = os.path.join(os.environ['HOME'], "vesper_git_repo", "logic", "vesper_tensor_network.py")
with open(filepath, 'r') as f:
    content = f.read()

# Add OS import if missing
if "import os" not in content:
    content = content.replace("import time", "import time\nimport os")

old_line = "self.tensors[self.layers['E8_Roots'][0]:self.layers['E8_Roots'][1]] = 1.0 # Placeholder for 240 root vectors"
new_line = "self.tensors[self.layers['E8_Roots'][0]:self.layers['E8_Roots'][1]] = torch.load(os.path.join(os.environ['HOME'], 'vesper_git_repo', 'weights', 'e8_latent_space.pt'), weights_only=True)"

if old_line in content:
    content = content.replace(old_line, new_line)
    with open(filepath, 'w') as f:
        f.write(content)
    print("[+] LATTICE BRIDGE PATCHED: E8 PARAMETERS INJECTED INTO ACTIVE TENSOR NETWORK.")
else:
    print("[!] PLACEHOLDER NOT FOUND. ALREADY PATCHED?")
