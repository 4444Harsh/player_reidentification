# Player Re-Identification: Project Report  

## What We Built  
A system that:  
- Identifies soccer players in video  
- Assigns permanent ID numbers  
- Tracks players even when they disappear from view  

## How It Works  
1. **Player Detection**  
   - Uses YOLOv11 AI model to find players  
   - Processes each video frame (15-20 frames per second)  

2. **Tracking Magic**  
   - Remembers players by their:  
     - Jersey color patterns  
     - Movement direction  
     - Position on field  

3. **Re-Identification**  
   - Matches returning players to their original IDs  
   - Handles temporary disappearances (up to 3 seconds)  

## Challenges We Faced  
 **Problem**: The AI model was too large for GitHub (185MB)  
 **Solution**: Shared via Google Drive instead  

 **Problem**: Slow processing on some computers  
**Solution**: Added progress indicators so users know it's working  


---
