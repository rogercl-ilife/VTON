# VTON

## To-do list
- [x] Preprocessing database
  - [x] Preprocessing cloth size
  - [x] Preprocessing person image - apply densepose 
- [ ] Cloth wrapping
  - [x] Run C-VTON's cloth warp
    - [x] Train 
    - [ ] ~~Test : Generate all test results~~
    - [ ] Run tensorboard to check result
      - [ ]  ~~sudo docker run -it --gpus all -v  /home/rogercl/covis:/covis -p 6006:6006 --name tensorboard  cuda-11.2:v1~~
  - [ ] Run KGI
    - [x] Generate KG results
    - [ ] Generate PG results
    - [ ] Generate warp(TPS) results
    - [ ] Generate inpainting results
  - [ ] Run PFAFN's cloth warp 
  - [ ] Work on my own cloth warp 
- [ ] Evaluation 
- [ ] Segmentation generation
- [ ] Diffusion
