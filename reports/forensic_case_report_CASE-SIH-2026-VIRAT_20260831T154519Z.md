# FORENSICLENS STANDARDIZED DIGITAL EVIDENCE REPORT
**Case Identifier:** `CASE-SIH-2026-VIRAT`  
**Investigation Title:** ForensicLens Automated Surveillance Case Study  
**Report Generated (UTC):** `2026-08-31T15:44:49.980239Z`  
**Forensic Tool:** ForensicLens Core v2.0 (SIH PS 26150)  
**Evidence Integrity Status:** `MATCH`  

---

## 1. CASE INFORMATION
- **Case ID:** `CASE-SIH-2026-VIRAT`
- **Title:** ForensicLens Automated Surveillance Case Study
- **Evidence Root Path:** `C:\Users\FIZZA ANJUM\OneDrive\Desktop\ForensicLens\dataset\raw`
- **Analysis Timestamp (UTC):** `2026-08-31T15:44:49.980239Z`
- **Total Ingested Files:** 38
- **Total Video Feeds:** 1
- **Total Forensic Review Events:** 16

---

## 2. EVIDENCE INVENTORY
| Evidence ID | Filename | Type | Size (Bytes) | SHA-256 (Pre/Post Status) |
|---|---|---|---|---|
| `ev-785a03f148bb12ce` | `IMG_0003.JPG` | `Image` | 840,101 | `MATCH` |
| `ev-d927bfa9c7a86f18` | `IMG_0007.JPG` | `Image` | 865,313 | `MATCH` |
| `ev-a400f500a6a9b57e` | `IMG_0009.JPG` | `Image` | 840,692 | `MATCH` |
| `ev-92e182ce10f9f767` | `IMG_0011.JPG` | `Image` | 771,052 | `MATCH` |
| `ev-e9602e0a9e5d0ce7` | `IMG_0013.JPG` | `Image` | 842,160 | `MATCH` |
| `ev-3c837350507e57f2` | `IMG_0014.JPG` | `Image` | 873,437 | `MATCH` |
| `ev-6adc90069c28e2da` | `IMG_0016.JPG` | `Image` | 853,839 | `MATCH` |
| `ev-996da4e3f15a1502` | `IMG_0017.JPG` | `Image` | 795,574 | `MATCH` |
| `ev-17fe87b27243edd4` | `IMG_0018.JPG` | `Image` | 784,455 | `MATCH` |
| `ev-35b9fef912b00e6a` | `IMG_0019.JPG` | `Image` | 864,257 | `MATCH` |
| `ev-e0822427ebc97118` | `IMG_0021.JPG` | `Image` | 819,599 | `MATCH` |
| `ev-98adc4980baa675c` | `IMG_0022.JPG` | `Image` | 728,696 | `MATCH` |
| `ev-5508b38c9391e68b` | `IMG_0023.JPG` | `Image` | 858,798 | `MATCH` |
| `ev-5207a01f18af13f3` | `IMG_0024.JPG` | `Image` | 838,434 | `MATCH` |
| `ev-e9df5244acbf929c` | `IMG_0026.JPG` | `Image` | 768,385 | `MATCH` |
| *... and 23 additional files* | | | | |
| `ev-11f452eba4ba48e4` | `VIRAT_S_010000_01_000184_000324.mp4` | `Source Video` | 24,789,774 | `MATCH` |

---

## 3. SOURCE HASHES & CRYPTOGRAPHIC PRESERVATION
Source evidence directories are treated as strictly immutable and read-only.

| Evidence ID | SHA-256 Digest | MD5 Digest | Verification Status |
|---|---|---|---|
| `ev-11f452eba4ba48e4` | `11f452eba4ba48e45301d0d58f971c9edc8e0c41d8b7f214846d1602d4f175fe` | `b95ffcdc6d1935d2c5ef49079228b3c8` | `MATCH (Immutable)` |
| `ev-785a03f148bb12ce` | `785a03f148bb12cec5ef3721e5ee6c38d7a2b40950768ad175dbcc4f2f85a170` | `fde12217846c1e74bb9681b67bebd886` | `MATCH` |
| `ev-d927bfa9c7a86f18` | `d927bfa9c7a86f18f3328ee9200c39bcb128fac1bd1217e02adb4a8e8bbd46f3` | `dbccff636c1af4880fc04b1b0c43968d` | `MATCH` |
| `ev-a400f500a6a9b57e` | `a400f500a6a9b57ec9757eace0c1cc573bbe1f0addc70db5469af8848d6b5cbf` | `82e93a6092da00ea9a4b11dadd724b7f` | `MATCH` |
| `ev-92e182ce10f9f767` | `92e182ce10f9f767241024e39b109cb545998b2c0854bb163585b86f722f3256` | `46ee4abaae3a50eb041945393aa657ff` | `MATCH` |
| `ev-e9602e0a9e5d0ce7` | `e9602e0a9e5d0ce790dbb6aba5178384f8bdd86aaef8bdeeb90f28b9e8c94dba` | `7690b9854abca6cafa9f0ff3fab67a16` | `MATCH` |

---

## 4. DVR / NVR DEVICE & FORMAT FINDINGS
- **Vendor Detection Status:** `Generic / Vendor-Agnostic`
- **Supported Parsers:** Generic_MP4_H264, EXIF_Image
- **Unsupported Proprietary Streams:** 0

---

## 5. VIDEO METADATA & SAMPLING PARAMETERS
### Video: `VIRAT_S_010000_01_000184_000324.mp4` (`ev-11f452eba4ba48e4`)
- **Container Format:** ISO Base Media / MP4
- **Resolution:** 1280x720
- **Frame Rate:** 23.97 FPS
- **Total Frames:** 3,267
- **Duration:** 136.30 seconds
- **Codec FOURCC:** `h264`

---

## 6. NORMALIZED FORENSIC TIMELINE
Unified chronological timeline correlating filesystem timestamps, EXIF metadata, and video-relative events.

| Timestamp | Kind | Event Type | Evidence Reference | Description |
|---|---|---|---|---|
| `2026-08-30T12:41:34.841334Z` | `filesystem_modified_utc` | `file_modified` | `IMG_0003.JPG` | Filesystem modification timestamp recorded. |
| `2026-08-30T12:41:34.873130Z` | `filesystem_modified_utc` | `file_modified` | `IMG_0007.JPG` | Filesystem modification timestamp recorded. |
| `2026-08-30T12:41:34.878307Z` | `filesystem_modified_utc` | `file_modified` | `IMG_0009.JPG` | Filesystem modification timestamp recorded. |
| `2026-08-30T12:41:34.898042Z` | `filesystem_modified_utc` | `file_modified` | `IMG_0011.JPG` | Filesystem modification timestamp recorded. |
| `2026-08-30T12:41:34.924225Z` | `filesystem_modified_utc` | `file_modified` | `IMG_0013.JPG` | Filesystem modification timestamp recorded. |
| `2026-08-30T12:41:34.944829Z` | `filesystem_modified_utc` | `file_modified` | `IMG_0014.JPG` | Filesystem modification timestamp recorded. |
| `2026-08-30T12:41:34.957128Z` | `filesystem_modified_utc` | `file_modified` | `IMG_0016.JPG` | Filesystem modification timestamp recorded. |
| `2026-08-30T12:41:34.972921Z` | `filesystem_modified_utc` | `file_modified` | `IMG_0017.JPG` | Filesystem modification timestamp recorded. |
| `2026-08-30T12:41:34.995870Z` | `filesystem_modified_utc` | `file_modified` | `IMG_0018.JPG` | Filesystem modification timestamp recorded. |
| `2026-08-30T12:41:35.007474Z` | `filesystem_modified_utc` | `file_modified` | `IMG_0019.JPG` | Filesystem modification timestamp recorded. |
| `2026-08-30T12:41:35.024073Z` | `filesystem_modified_utc` | `file_modified` | `IMG_0021.JPG` | Filesystem modification timestamp recorded. |
| `2026-08-30T12:41:35.040810Z` | `filesystem_modified_utc` | `file_modified` | `IMG_0022.JPG` | Filesystem modification timestamp recorded. |
| *... and 732 additional timeline entries* | | | | |

---

## 7. FORENSIC REVIEW EVENTS & TRIAGE SUMMARY
- **Total Review Events:** 16
- **High Priority Findings:** 1
- **Medium Priority Findings:** 4
- **Low Priority Findings:** 11

| Event ID | Timestamp (s) | Event Type | Assertion Type | Review Priority | Anomaly Score | Explanation |
|---|---|---|---|---|---|---|
| `fe-11f452eba4ba48e4-detection_burst-000140-0016` | 5.84 | `detection_burst` | `detected_fact` | **`MEDIUM`** | `0.48` | 11 detections occurred within 5.00s, meeting the burst threshold of 8. |
| `fe-11f452eba4ba48e4-person_entered-000160-0001` | 6.68 | `person_entered` | `inferred_association` | **`LOW`** | `0.24` | Track first appeared near the left frame boundary; this infers visible-frame entry only, not real-world entry. |
| `fe-11f452eba4ba48e4-movement_detected-000160-0002` | 7.93 | `movement_detected` | `detected_fact` | **`MEDIUM`** | `0.39` | Track centroid displacement of 91.18px met the 60.00px threshold. |
| `fe-11f452eba4ba48e4-person_entered-000325-0003` | 13.56 | `person_entered` | `inferred_association` | **`LOW`** | `0.09` | Track first appeared near the left frame boundary; this infers visible-frame entry only, not real-world entry. |
| `fe-11f452eba4ba48e4-multiple_objects_present-000360-0015` | 15.02 | `multiple_objects_present` | `detected_fact` | **`LOW`** | `0.32` | 2 detected objects met the simultaneous-object threshold of 2. |
| `fe-11f452eba4ba48e4-movement_detected-000325-0006` | 28.79 | `movement_detected` | `detected_fact` | **`HIGH`** | `0.67` | Track centroid displacement of 705.11px met the 60.00px threshold. |
| `fe-11f452eba4ba48e4-person_exited-000690-0004` | 28.79 | `person_exited` | `inferred_association` | **`LOW`** | `0.17` | Track last appeared near the bottom frame boundary; this infers visible-frame exit only, not real-world exit. |
| `fe-11f452eba4ba48e4-prolonged_presence-000325-0005` | 28.79 | `prolonged_presence` | `detected_fact` | **`MEDIUM`** | `0.43` | Track was detected for 15.23s, meeting the 10.00s threshold. |
| `fe-11f452eba4ba48e4-movement_detected-000750-0007` | 39.22 | `movement_detected` | `detected_fact` | **`MEDIUM`** | `0.40` | Track centroid displacement of 120.88px met the 60.00px threshold. |
| `fe-11f452eba4ba48e4-person_entered-001350-0008` | 56.32 | `person_entered` | `inferred_association` | **`LOW`** | `0.14` | Track first appeared near the left frame boundary; this infers visible-frame entry only, not real-world entry. |
| `fe-11f452eba4ba48e4-person_exited-001350-0009` | 56.32 | `person_exited` | `inferred_association` | **`LOW`** | `0.21` | Track last appeared near the left frame boundary; this infers visible-frame exit only, not real-world exit. |
| `fe-11f452eba4ba48e4-person_entered-001375-0010` | 57.36 | `person_entered` | `inferred_association` | **`LOW`** | `0.09` | Track first appeared near the left frame boundary; this infers visible-frame entry only, not real-world entry. |
| `fe-11f452eba4ba48e4-person_exited-001375-0011` | 57.36 | `person_exited` | `inferred_association` | **`LOW`** | `0.19` | Track last appeared near the left frame boundary; this infers visible-frame exit only, not real-world exit. |
| `fe-11f452eba4ba48e4-movement_detected-001385-0012` | 59.87 | `movement_detected` | `detected_fact` | **`LOW`** | `0.28` | Track centroid displacement of 86.01px met the 60.00px threshold. |
| `fe-11f452eba4ba48e4-movement_detected-001510-0013` | 65.29 | `movement_detected` | `detected_fact` | **`LOW`** | `0.25` | Track centroid displacement of 73.75px met the 60.00px threshold. |
| `fe-11f452eba4ba48e4-movement_detected-001780-0014` | 79.47 | `movement_detected` | `detected_fact` | **`LOW`** | `0.34` | Track centroid displacement of 93.88px met the 60.00px threshold. |

---

## 8. TRACK SUMMARIES & TRAJECTORIES
Local multi-object tracker trajectories extracted from in-memory frame analysis.

| Track ID | Class | Duration | Displacement | Trajectory Direction | Entry / Exit Boundary | Mean Confidence |
|---|---|---|---|---|---|---|
| `2` | `person` | 1.25s | 91.2px | `east` | `left` / `none` | 0.66 |
| `4` | `person` | 7.09s | 4.9px | `None` | `none` / `none` | 0.34 |
| `7` | `person` | 15.23s | 705.1px | `east` | `left` / `bottom` | 0.59 |
| `26` | `person` | 7.93s | 120.9px | `north-east` | `none` / `none` | 0.46 |
| `46` | `person` | 2.09s | 37.8px | `None` | `none` / `none` | 0.44 |
| `48` | `person` | 0.00s | 0.0px | `None` | `none` / `none` | 0.37 |
| `57` | `person` | 0.21s | 6.2px | `None` | `none` / `none` | 0.52 |
| `58` | `person` | 1.88s | 58.3px | `None` | `none` / `none` | 0.60 |
| `63` | `person` | 0.00s | 0.0px | `None` | `left` / `left` | 0.50 |
| `66` | `person` | 0.00s | 0.0px | `None` | `left` / `left` | 0.60 |
| `67` | `person` | 2.09s | 86.0px | `east` | `none` / `none` | 0.67 |
| `70` | `person` | 2.29s | 73.8px | `west` | `none` / `none` | 0.65 |
| `72` | `person` | 0.00s | 0.0px | `None` | `none` / `none` | 0.55 |
| `73` | `person` | 5.21s | 93.9px | `north-east` | `none` / `none` | 0.49 |
| `77` | `person` | 0.83s | 11.5px | `None` | `none` / `none` | 0.44 |
| `83` | `person` | 0.00s | 0.0px | `None` | `none` / `none` | 0.38 |
| `87` | `person` | 0.00s | 0.0px | `None` | `none` / `none` | 0.57 |

---

## 9. MACHINE LEARNING INTELLIGENCE & ANOMALY ANALYSIS
- **Model Architecture:** `IsolationForest+StandardScaler`
- **Training Mode:** `UNSUPERVISED` (No rule labels leaked)
- **Dataset Source:** `unsupervised_forensic_features_baseline`
- **Calibrated Threshold:** `0.65`
- **Anomaly Rate in Case:** `6.06%`
- **Inference Speed:** `350.88` samples/sec

---

## 10. MULTI-CAMERA & SURVEILLANCE EVENT CORRELATION
Evaluated multi-camera temporal proximity, movement transitions, and track burst sequences.

| Correlation ID | Relationship Type | Score | Source Event -> Target Event | Explanation |
|---|---|---|---|---|
| `corr-000001` | `temporal_proximity` | `0.94` | `fe-11f452eba4ba48e4-detection_burst-000140-0016` -> `fe-11f452eba4ba48e4-person_entered-000160-0001` | Surveillance events 'detection_burst' and 'person_entered' co-occurred in camera feed within 0.83s. |
| `corr-000002` | `temporal_proximity` | `0.86` | `fe-11f452eba4ba48e4-detection_burst-000140-0016` -> `fe-11f452eba4ba48e4-movement_detected-000160-0002` | Surveillance events 'detection_burst' and 'movement_detected' co-occurred in camera feed within 2.09s. |
| `corr-000003` | `temporal_proximity` | `0.49` | `fe-11f452eba4ba48e4-detection_burst-000140-0016` -> `fe-11f452eba4ba48e4-person_entered-000325-0003` | Surveillance events 'detection_burst' and 'person_entered' co-occurred in camera feed within 7.72s. |
| `corr-000004` | `temporal_proximity` | `0.40` | `fe-11f452eba4ba48e4-detection_burst-000140-0016` -> `fe-11f452eba4ba48e4-multiple_objects_present-000360-0015` | Surveillance events 'detection_burst' and 'multiple_objects_present' co-occurred in camera feed within 9.18s. |
| `corr-000005` | `sequential_movement` | `0.96` | `fe-11f452eba4ba48e4-person_entered-000160-0001` -> `fe-11f452eba4ba48e4-movement_detected-000160-0002` | Track 2 progression: 'person_entered' followed by 'movement_detected' over 1.25s. |
| `corr-000006` | `temporal_proximity` | `0.54` | `fe-11f452eba4ba48e4-person_entered-000160-0001` -> `fe-11f452eba4ba48e4-person_entered-000325-0003` | Surveillance events 'person_entered' and 'person_entered' co-occurred in camera feed within 6.88s. |
| `corr-000007` | `temporal_proximity` | `0.44` | `fe-11f452eba4ba48e4-person_entered-000160-0001` -> `fe-11f452eba4ba48e4-multiple_objects_present-000360-0015` | Surveillance events 'person_entered' and 'multiple_objects_present' co-occurred in camera feed within 8.34s. |
| `corr-000008` | `temporal_proximity` | `0.62` | `fe-11f452eba4ba48e4-movement_detected-000160-0002` -> `fe-11f452eba4ba48e4-person_entered-000325-0003` | Surveillance events 'movement_detected' and 'person_entered' co-occurred in camera feed within 5.63s. |
| `corr-000009` | `temporal_proximity` | `0.53` | `fe-11f452eba4ba48e4-movement_detected-000160-0002` -> `fe-11f452eba4ba48e4-multiple_objects_present-000360-0015` | Surveillance events 'movement_detected' and 'multiple_objects_present' co-occurred in camera feed within 7.09s. |
| `corr-000010` | `temporal_proximity` | `0.90` | `fe-11f452eba4ba48e4-person_entered-000325-0003` -> `fe-11f452eba4ba48e4-multiple_objects_present-000360-0015` | Surveillance events 'person_entered' and 'multiple_objects_present' co-occurred in camera feed within 1.46s. |
| `corr-000011` | `temporal_proximity` | `0.40` | `fe-11f452eba4ba48e4-multiple_objects_present-000360-0015` -> `fe-11f452eba4ba48e4-movement_detected-000325-0006` | Surveillance events 'multiple_objects_present' and 'movement_detected' co-occurred in camera feed within 13.77s. |
| `corr-000012` | `temporal_proximity` | `0.40` | `fe-11f452eba4ba48e4-multiple_objects_present-000360-0015` -> `fe-11f452eba4ba48e4-person_exited-000690-0004` | Surveillance events 'multiple_objects_present' and 'person_exited' co-occurred in camera feed within 13.77s. |
| `corr-000013` | `temporal_proximity` | `0.40` | `fe-11f452eba4ba48e4-multiple_objects_present-000360-0015` -> `fe-11f452eba4ba48e4-prolonged_presence-000325-0005` | Surveillance events 'multiple_objects_present' and 'prolonged_presence' co-occurred in camera feed within 13.77s. |
| `corr-000014` | `same_camera_sequence` | `1.00` | `fe-11f452eba4ba48e4-movement_detected-000325-0006` -> `fe-11f452eba4ba48e4-person_exited-000690-0004` | Co-occurring events on Track 7 (movement_detected and person_exited) within 0.00s. |
| `corr-000015` | `same_camera_sequence` | `1.00` | `fe-11f452eba4ba48e4-movement_detected-000325-0006` -> `fe-11f452eba4ba48e4-prolonged_presence-000325-0005` | Co-occurring events on Track 7 (movement_detected and prolonged_presence) within 0.00s. |
| `corr-000016` | `temporal_proximity` | `0.40` | `fe-11f452eba4ba48e4-movement_detected-000325-0006` -> `fe-11f452eba4ba48e4-movement_detected-000750-0007` | Surveillance events 'movement_detected' and 'movement_detected' co-occurred in camera feed within 10.43s. |
| `corr-000017` | `same_camera_sequence` | `1.00` | `fe-11f452eba4ba48e4-person_exited-000690-0004` -> `fe-11f452eba4ba48e4-prolonged_presence-000325-0005` | Co-occurring events on Track 7 (person_exited and prolonged_presence) within 0.00s. |
| `corr-000018` | `temporal_proximity` | `0.40` | `fe-11f452eba4ba48e4-person_exited-000690-0004` -> `fe-11f452eba4ba48e4-movement_detected-000750-0007` | Surveillance events 'person_exited' and 'movement_detected' co-occurred in camera feed within 10.43s. |
| `corr-000019` | `temporal_proximity` | `0.40` | `fe-11f452eba4ba48e4-prolonged_presence-000325-0005` -> `fe-11f452eba4ba48e4-movement_detected-000750-0007` | Surveillance events 'prolonged_presence' and 'movement_detected' co-occurred in camera feed within 10.43s. |
| `corr-000020` | `sequential_movement` | `1.00` | `fe-11f452eba4ba48e4-person_entered-001350-0008` -> `fe-11f452eba4ba48e4-person_exited-001350-0009` | Track 63 progression: 'person_entered' followed by 'person_exited' over 0.00s. |
| `corr-000021` | `temporal_proximity` | `0.93` | `fe-11f452eba4ba48e4-person_entered-001350-0008` -> `fe-11f452eba4ba48e4-person_entered-001375-0010` | Surveillance events 'person_entered' and 'person_entered' co-occurred in camera feed within 1.04s. |
| `corr-000022` | `temporal_proximity` | `0.93` | `fe-11f452eba4ba48e4-person_entered-001350-0008` -> `fe-11f452eba4ba48e4-person_exited-001375-0011` | Surveillance events 'person_entered' and 'person_exited' co-occurred in camera feed within 1.04s. |
| `corr-000023` | `temporal_proximity` | `0.76` | `fe-11f452eba4ba48e4-person_entered-001350-0008` -> `fe-11f452eba4ba48e4-movement_detected-001385-0012` | Surveillance events 'person_entered' and 'movement_detected' co-occurred in camera feed within 3.55s. |
| `corr-000024` | `temporal_proximity` | `0.40` | `fe-11f452eba4ba48e4-person_entered-001350-0008` -> `fe-11f452eba4ba48e4-movement_detected-001510-0013` | Surveillance events 'person_entered' and 'movement_detected' co-occurred in camera feed within 8.97s. |
| `corr-000025` | `temporal_proximity` | `0.93` | `fe-11f452eba4ba48e4-person_exited-001350-0009` -> `fe-11f452eba4ba48e4-person_entered-001375-0010` | Surveillance events 'person_exited' and 'person_entered' co-occurred in camera feed within 1.04s. |
| `corr-000026` | `temporal_proximity` | `0.93` | `fe-11f452eba4ba48e4-person_exited-001350-0009` -> `fe-11f452eba4ba48e4-person_exited-001375-0011` | Surveillance events 'person_exited' and 'person_exited' co-occurred in camera feed within 1.04s. |
| `corr-000027` | `temporal_proximity` | `0.76` | `fe-11f452eba4ba48e4-person_exited-001350-0009` -> `fe-11f452eba4ba48e4-movement_detected-001385-0012` | Surveillance events 'person_exited' and 'movement_detected' co-occurred in camera feed within 3.55s. |
| `corr-000028` | `temporal_proximity` | `0.40` | `fe-11f452eba4ba48e4-person_exited-001350-0009` -> `fe-11f452eba4ba48e4-movement_detected-001510-0013` | Surveillance events 'person_exited' and 'movement_detected' co-occurred in camera feed within 8.97s. |
| `corr-000029` | `sequential_movement` | `1.00` | `fe-11f452eba4ba48e4-person_entered-001375-0010` -> `fe-11f452eba4ba48e4-person_exited-001375-0011` | Track 66 progression: 'person_entered' followed by 'person_exited' over 0.00s. |
| `corr-000030` | `temporal_proximity` | `0.83` | `fe-11f452eba4ba48e4-person_entered-001375-0010` -> `fe-11f452eba4ba48e4-movement_detected-001385-0012` | Surveillance events 'person_entered' and 'movement_detected' co-occurred in camera feed within 2.50s. |
| `corr-000031` | `temporal_proximity` | `0.47` | `fe-11f452eba4ba48e4-person_entered-001375-0010` -> `fe-11f452eba4ba48e4-movement_detected-001510-0013` | Surveillance events 'person_entered' and 'movement_detected' co-occurred in camera feed within 7.93s. |
| `corr-000032` | `temporal_proximity` | `0.83` | `fe-11f452eba4ba48e4-person_exited-001375-0011` -> `fe-11f452eba4ba48e4-movement_detected-001385-0012` | Surveillance events 'person_exited' and 'movement_detected' co-occurred in camera feed within 2.50s. |
| `corr-000033` | `temporal_proximity` | `0.47` | `fe-11f452eba4ba48e4-person_exited-001375-0011` -> `fe-11f452eba4ba48e4-movement_detected-001510-0013` | Surveillance events 'person_exited' and 'movement_detected' co-occurred in camera feed within 7.93s. |
| `corr-000034` | `temporal_proximity` | `0.64` | `fe-11f452eba4ba48e4-movement_detected-001385-0012` -> `fe-11f452eba4ba48e4-movement_detected-001510-0013` | Surveillance events 'movement_detected' and 'movement_detected' co-occurred in camera feed within 5.42s. |
| `corr-000035` | `temporal_proximity` | `0.40` | `fe-11f452eba4ba48e4-movement_detected-001510-0013` -> `fe-11f452eba4ba48e4-movement_detected-001780-0014` | Surveillance events 'movement_detected' and 'movement_detected' co-occurred in camera feed within 14.18s. |

---

## 11. EVIDENCE RELATIONSHIP GRAPH SUMMARY
- **Total Graph Nodes:** 107
- **Total Graph Edges:** 143
- **Detected Facts (Direct):** 49
- **Inferred Associations (Track/ML/Corr):** 94

---

## 12. CHAIN OF CUSTODY
- **Chain Status:** `CHAIN_VALID`
- **Total Custody Entries:** 154

| Entry ID | Timestamp (UTC) | Evidence ID | Operation | Actor / Source | Current Entry Hash |
|---|---|---|---|---|---|
| `coc-000001` | `2026-08-31T15:44:49.980239Z` | `ev-11f452eba4ba48e4` | `evidence_registered` | `source_evidence` | `f99ff915e09c1062...` |
| `coc-000002` | `2026-08-31T15:44:49.980239Z` | `ev-11f452eba4ba48e4` | `evidence_hashed` | `source_evidence` | `26b1d2f0e294ccd4...` |
| `coc-000003` | `2026-08-31T15:44:49.980239Z` | `ev-11f452eba4ba48e4` | `evidence_analyzed` | `source_evidence` | `e5661d59fbc0cc07...` |
| `coc-000004` | `2026-08-31T15:44:49.980239Z` | `ev-11f452eba4ba48e4` | `evidence_verified` | `source_evidence` | `cc76aec5f586429e...` |
| `coc-000005` | `2026-08-31T15:44:49.980239Z` | `ev-785a03f148bb12ce` | `evidence_registered` | `source_evidence` | `47d88a81141a8ae6...` |
| `coc-000006` | `2026-08-31T15:44:49.980239Z` | `ev-785a03f148bb12ce` | `evidence_hashed` | `source_evidence` | `030967d5450339f1...` |
| `coc-000007` | `2026-08-31T15:44:49.980239Z` | `ev-785a03f148bb12ce` | `evidence_verified` | `source_evidence` | `aca2df966d1bf39d...` |
| `coc-000008` | `2026-08-31T15:44:49.980239Z` | `ev-d927bfa9c7a86f18` | `evidence_registered` | `source_evidence` | `42181cc55eb76ffe...` |
| `coc-000009` | `2026-08-31T15:44:49.980239Z` | `ev-d927bfa9c7a86f18` | `evidence_hashed` | `source_evidence` | `9433a5137c73c6d9...` |
| `coc-000010` | `2026-08-31T15:44:49.980239Z` | `ev-d927bfa9c7a86f18` | `evidence_verified` | `source_evidence` | `518eeb798a66daa5...` |
| *... and 144 additional verified custody entries* | | | | | |

---

## 13. PRIVATE EVIDENCE LEDGER VERIFICATION
- **Ledger Type:** `local_private_hash_linked`
- **Public Blockchain:** `False` (Compliant: zero evidence data sent to public networks)
- **Block Count:** 154
- **Ledger Verification Status:** `CHAIN_VALID`

---

## 14. TAMPER VERIFICATION
- **Overall Tamper Status:** `MATCH`
- **Source Evidence Count:** 37
- **Derived Artifacts Verified:** 21

---

## 15. SECURE ERASURE CERTIFICATES (TEST-ONLY COPIES)
*No safe test copies were submitted for sanitization in this run. Source evidence remained untouched.*

---

## 16. SCOPE & FORENSIC LIMITATIONS
- The hash-linked ledger is local/private and does not claim public-blockchain immutability or legal admissibility.
- Unsupported proprietary DVR/NVR formats remain unsupported.
- Track IDs are local to one video analysis.
- Video-relative timestamps are not wall-clock UTC.
- Inferred tracker, boundary, and correlation relationships remain strictly labeled as inferred.
- File-level sanitization applies solely to safe test copies; it does not replace physical drive degaussing.

---

## 17. REPRODUCIBILITY CONFIGURATION
```json
{
  "video_intelligence": {
    "model_name": "yolov8n.pt",
    "confidence_threshold": 0.25,
    "sampling_stride_frames": 5,
    "frame_change_threshold": 0.12,
    "tracker": "bytetrack.yaml"
  },
  "forensic_event_aggregation": {
    "prolonged_presence_seconds": 10.0,
    "movement_displacement_pixels": 60.0,
    "boundary_margin_ratio": 0.05,
    "multiple_object_count": 2,
    "event_window_seconds": 5.0,
    "detection_burst_count": 8
  },
  "forensic_event_aggregation_version": "1.0"
}
```

---

## 18. TOOL & MODEL RUNTIME VERSIONS
- **Python Version:** `3.11.9`
- **OpenCV Version:** `4.12.0`
- **Torch Version:** `2.11.0+cpu`
- **Ultralytics Version:** `8.4.136`
- **Scikit-Learn Version:** `1.8.0`

**[END OF FORENSIC CASE REPORT]**