#!/usr/bin/env python3
"""Generate publications.qmd body (run manually if needed)."""

def item(title, venue, authors, links=""):
    thumb = '<div class="pub-thumb"></div>'
    links_html = f'<div class="pub-links pub-links--todo">{links}</div>\n' if links else ""
    return f"""<li class="pub-item">
{thumb}
<div class="pub-content">
<div class="pub-title">{title}</div>
<div class="pub-venue">{venue}</div>
<div class="pub-authors">{authors}</div>
{links_html}</div>
</li>"""


def links(*parts):
    sep = '<span class="pub-sep">·</span>'
    return sep.join(f"<span>{p}</span>" for p in parts)


PUBS = {
    "2026": [
        ("Learning Reactive Dexterous Grasping via Hierarchical Task-Space RL Planning and Joint-Space QP Control",
         "Preprint", "Ho Jae Lee, Yonghyeon Lee, Alexander Alexiev, Tzu-Yuan Lin, Se Hwan Jeon, Sangbae Kim", links("arXiv", "Video")),
        ("Point2Pose: Occlusion-Recovering 6D Pose Tracking and 3D Reconstruction for Multiple Unknown Objects Via 2D Point Trackers",
         "Preprint", "Tzu-Yuan Lin, Ho Jae Lee, Kevin Doherty, Yonghyeon Lee, Sangbae Kim", links("arXiv")),
        ("AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models",
         "Preprint", "Hyeongjun Heo, Seungyeon Woo, Sang Min Kim, Junho Kim, Junho Lee, Yonghyeon Lee, Young Min Kim", links("arXiv")),
        ("High-Bandwidth Tactile-Reactive Control for Grasp Adjustment",
         "International Conference on Robotics and Automation (ICRA), 2026", "Yonghyeon Lee*, Tzu-Yuan Lin*, Alexander Alexiev, Sangbae Kim", links("Project page", "arXiv")),
        ("Hierarchical Reactive Grasping via Task-Space Velocity Fields and Joint-Space Quadratic Programming",
         "International Conference on Robotics and Automation (ICRA), 2026", "Yonghyeon Lee*, Tzu-Yuan Lin*, Alexander Alexiev, Sangbae Kim", links("Project page", "arXiv")),
        ("Differentiable Motion Manifold Primitives for Reactive Motion Generation under Kinodynamic Constraints",
         "International Conference on Robotics and Automation (ICRA), 2026", "Yonghyeon Lee", links("Project page", "arXiv")),
        ("Point2Act: Efficient 3D Distillation of Multimodal LLMs for Zero-Shot Context-Aware Grasping",
         "International Conference on Robotics and Automation (ICRA), 2026", "Sang Min Kim, Hyeongjun Heo, Junho Kim, Yonghyeon Lee, Young Min Kim", links("Project page", "arXiv")),
        ("LEGO: Latent-space Exploration for Geometry-aware Optimization of Humanoid Kinematic Design",
         "International Conference on Robotics and Automation (ICRA), 2026", "JiHwan Yoon, Taemoon Jeong, Jeongeun Park, Chanwoo Kim, Jaewoon Kwon, Yonghyeon Lee, Kyungjae Lee, Sungjoon Choi", links("Project page")),
    ],
    "2025": [
        ("Behavior-Controllable Stable Dynamics Models on Riemannian Configuration Manifolds",
         "IEEE Transactions on Robotics (T-RO), 2025", "Byeongho Lee*, Yonghyeon Lee*, Junsu Ha*, Frank C. Park", links("IEEE Xplore")),
        ("ScrewSplat: An End-to-End Method for Articulated Object Recognition",
         "Conference on Robot Learning (CoRL), 2025", "Seungyeon Kim, Junsu Ha, Young Hun Kim, Yonghyeon Lee, Frank C. Park", links("Project page", "Code", "arXiv")),
        ("DreamGrasp: Zero-Shot 3D Multi-Object Reconstruction from Partial-View Images for Robotic Manipulation",
         "arXiv, 2025", "Young Hun Kim, Seungyeon Kim, Yonghyeon Lee, Frank Chongwoo Park", links("arXiv")),
        ("Motion Manifold Flow Primitives for Task-Conditioned Trajectory Generation under Complex Task-Motion Dependencies",
         "IEEE Robotics and Automation Letters (RA-L), 2025", "Yonghyeon Lee, Byeongho Lee, Seungyeon Kim, Frank C. Park", links("IEEE Xplore", "Project page", "arXiv")),
        ("Isometric Regularization for Manifolds of Functional Data",
         "International Conference on Learning Representations (ICLR), 2025", "Hyeongjun Heo, Seonghun Oh, Jae Yong Lee, Young Min Kim, Yonghyeon Lee", links("Project page")),
        ("Diverse Policy Learning via Random Obstacle Deployment for Zero-Shot Adaptation",
         "IEEE Robotics and Automation Letters (RA-L), 2025", "Seokjin Choi*, Yonghyeon Lee*, Seungyeon Kim, Che-Sang Park, Himchan Hwang, Frank C. Park", links("IEEE Xplore", "Project page")),
    ],
    "2024": [
        ("T2SQNet: A Recognition Model for Manipulating Partially Observed Transparent Tableware Objects",
         "Conference on Robot Learning (CoRL), 2024", "Young Hun Kim*, Seungyeon Kim*, Yonghyeon Lee, Frank C. Park", links("Project page", "Code", "Video", "Poster", "OpenReview")),
        ("EquiGraspFlow: SE(3)-Equivariant 6-DoF Grasp Pose Generative Flows",
         "Conference on Robot Learning (CoRL), 2024", "Byeongdo Lim*, Jongmin Kim*, Jihwan Kim, Yonghyeon Lee, Frank C. Park", links("Project page", "Code", "Video", "Poster", "OpenReview")),
        ("MMP++: Motion Manifold Primitives with Parametric Curve Models",
         "IEEE Transactions on Robotics (T-RO), 2024", "Yonghyeon Lee", links("Project page", "Code", "IEEE Xplore")),
        ("Graph Geometry-Preserving Autoencoders",
         "International Conference on Machine Learning (ICML), 2024", "Jungbin Lim*, Jihwan Kim*, Yonghyeon Lee, Cheongjae Jang, Frank C. Park", links("Code", "Video", "Poster", "OpenReview")),
        ("Leveraging Equivariant Representations of 3D Point Clouds for SO(3)-Equivariant 6-DoF Grasp Pose Generation",
         "ICRA 2024 Workshop on 3D Visual Representations for Robot Manipulation", "Byeongdo Lim*, Jongmin Kim*, Jihwan Kim, Yonghyeon Lee, Frank C. Park", links("Poster", "OpenReview")),
        ("Behavior-Controllable Stable Dynamics Models in Riemannian Configuration Manifolds",
         "ICRA 2024 Workshop on Human Modelling in Physical Human-Robot Interaction", "Byeongho Lee*, Yonghyeon Lee*, Junsu Ha*, Frank C. Park", links("Poster")),
    ],
    "2023": [
        ("NFL: Normal Field Learning for 6-DoF Grasping of Transparent Objects",
         "IEEE Robotics and Automation Letters (RA-L), 2023", "Junho Lee, Sang Min Kim, Yonghyeon Lee, Young Min Kim", links("Code", "Video", "Poster")),
        ("A Geometric Perspective on Autoencoders",
         "arXiv, 2023 (summary of Ph.D. thesis)", "Yonghyeon Lee", links("arXiv")),
        ("Equivariant Motion Manifold Primitives",
         "Conference on Robot Learning (CoRL), 2023", "Byeongho Lee*, Yonghyeon Lee*, Seungyeon Kim, Minjun Son, Frank C. Park", links("Project page", "Code", "Video", "Poster", "OpenReview")),
        ("Leveraging 3D Reconstruction for Mechanical Search on Cluttered Shelves",
         "Conference on Robot Learning (CoRL), 2023", "Seungyeon Kim*, Young Hun Kim*, Yonghyeon Lee, Frank C. Park", links("Code", "Video", "Poster", "OpenReview")),
        ("On Explicit Curvature Regularization in Deep Generative Models",
         "TAG-ML Workshop, ICML 2023", "Yonghyeon Lee, Frank C. Park", links("arXiv", "OpenReview", "Poster")),
        ("Geometrically Regularized Autoencoders for Non-Euclidean Data",
         "International Conference on Learning Representations (ICLR), 2023", "Cheongjae Jang, Yonghyeon Lee, Yung-Kyun Noh, Frank C. Park", links("PDF", "Poster", "OpenReview")),
        ("Geometric Methods for Manifold Representation Learning",
         "Ph.D. Thesis, Seoul National University", "Yonghyeon Lee (supervisor: Frank C. Park)", links("PDF", "Abstract", "Slides")),
    ],
    "2022": [
        ("SE(2)-Equivariant Pushing Dynamics Models for Tabletop Object Manipulations",
         "Conference on Robot Learning (CoRL), 2022 (oral, 6.5%)", "Seungyeon Kim, Byeongdo Lim, Yonghyeon Lee, Frank C. Park", links("Proceedings", "Code", "OpenReview")),
        ("Evaluating Out-of-Distribution Detectors Through Adversarial Generation of Outliers",
         "arXiv, 2022", "Sangwoong Yoon, Jinwon Choi, Yonghyeon Lee, Yung-Kyun Noh, Frank C. Park", links("arXiv", "Code")),
        ("DSQNet: A Deformable Model-Based Supervised Learning Algorithm for Grasping Unknown Occluded Objects",
         "IEEE Transactions on Automation Science and Engineering (T-ASE), 2022", "Seungyeon Kim*, Taegyun Ahn*, Yonghyeon Lee, Jihwan Kim, Michael Yu Wang, Frank C. Park", links("Code", "IEEE Xplore")),
        ("A Statistical Manifold Framework for Point Cloud Data",
         "International Conference on Machine Learning (ICML), 2022", "Yonghyeon Lee*, Seungyeon Kim*, Jinwon Choi, Frank C. Park", links("PDF", "Proceedings", "Code", "Video", "Slides", "Poster")),
        ("Regularized Autoencoders for Isometric Representation Learning",
         "International Conference on Learning Representations (ICLR), 2022", "Yonghyeon Lee, Sangwoong Yoon, Minjun Son, Frank C. Park", links("PDF", "Code", "Video", "Slides", "Poster", "OpenReview")),
    ],
    "2021": [
        ("Neighborhood Reconstructing Autoencoders",
         "Conference on Neural Information Processing Systems (NeurIPS), 2021", "Yonghyeon Lee, Hyukjun Kwon, Frank C. Park", links("PDF", "Proceedings", "Code", "Video", "Slides", "Poster", "OpenReview")),
        ("IMAT: The Iterative Medial Axis Transform",
         "Computer Graphics Forum, 2021", "Yonghyeon Lee, Jonghyuk Baek, Youngmin Kim, Frank C. Park", links("PDF", "Article")),
    ],
    "2020": [
        ("Context Awareness and Step Length Estimation by Shape Distance and H-Features",
         "International Journal of Control, Automation, and Systems, 2020", "Daehyun Kim, Yonghyeon Lee, Chan Gook Park", links("Article")),
    ],
}

HEADER = """---
pagetitle: "Publications – RoPhi Lab"
---

Publications from Ro$\\Phi$ Lab and affiliated work. Add a thumbnail per paper under `assets/pubs/` (GIF or PNG) and set the `src` on the `<img>` in each entry's `.pub-thumb` block.

"""

FOOTER = """
---

Replace each link label with `<a href="...">Label</a>`. Thumbnails: add `<img src="assets/pubs/your-file.gif" alt="">` inside `.pub-thumb`. See the [PI publication page](https://www.gabe-yhlee.com/publications) for reference URLs.
"""

def main():
    out = [HEADER]
    for year, entries in PUBS.items():
        out.append(f"## {year}\n\n<ul class=\"pub-list\">\n")
        for e in entries:
            out.append(item(*e) + "\n")
        out.append("</ul>\n\n")
    out.append(FOOTER)
    path = Path(__file__).resolve().parents[1] / "publications.qmd"
    path.write_text("".join(out), encoding="utf-8")
    print(f"Wrote {path}")


if __name__ == "__main__":
    from pathlib import Path
    main()
