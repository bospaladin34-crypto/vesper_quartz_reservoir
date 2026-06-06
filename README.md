# Vesper Genesis Integration
Existing AI Studio project has:
- CRT Terminal Interface (keep)
- Native JNI Bridge libbraidc.so (replace with nephilim_ops)
- On-Device AI Acceleration via NNAPI (use our phason_npu.tflite)
- Distributed Compute Node (Omega Uplink to 192.168.1.100:8000)

Integration steps:
1. Copy nephilim_ops.cc into Vesper's cpp/ folder, rename libbraidc.so -> libnephilim.so
2. Replace [IGNITE LAMINAR CORE] button to call braid(a,b,c) instead of igniteSilicon()
3. Add NPU status monitor showing phason_hz=15.965
4. Point ESTABLISH OMEGA UPLINK to FastAPI /status endpoint
