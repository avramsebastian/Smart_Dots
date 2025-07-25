# 🎯 Smart Dots

**Smart Dots** is a machine learning project that uses a **genetic algorithm** to train simple agents (dots) to navigate a 2D environment filled with obstacles. The dots learn over generations to reach a goal more efficiently by evolving their movement strategies.

---

## 🧠 About the Project

Smart Dots is an interactive simulation written in Python using the `pygame` library. Each agent (dot) starts with a random set of movement directions and is evaluated based on how close it gets to the goal, how many obstacles it passes, and whether it reaches the destination. Over generations, the best-performing dots are selected, cloned, and mutated to improve performance.

---

## 🕹️ How to Run

### 1. Clone the Repository

```bash
https://github.com/your-username/smart-dots.git
cd smart-dots
```

### 2. Install Dependencies

Make sure Python 3 is installed, then install `pygame`:

```bash
pip install pygame
```

### 3. Run the Simulation

```bash
python main.py
```

You should see the simulation window appear with dots navigating toward a goal while learning to avoid obstacles.

---

## 🔍 How It Works (Genetic Algorithm)

1. **Initialize Population**: Random movement vectors for each dot.
2. **Simulate Movement**: Dots attempt to reach the goal, navigating obstacles.
3. **Evaluate Fitness**: Based on distance to goal, steps taken, and obstacles passed.
4. **Selection**: Best dot (champion) is selected based on fitness.
5. **Crossover & Mutation**: New generation is created with slight mutations.
6. **Repeat**: Over time, dots learn optimal paths to the goal.

This cycle mimics **natural selection** and demonstrates core principles of **machine learning through evolutionary programming**.

---

## 📌 Notes

- Champion dot can influence how many steps future generations are allowed.
- Agents that fail to pass minimum obstacles after certain generations are eliminated.
- The goal is adaptive learning — no hardcoded paths.

---


## 📚 References & Learning Resources

- [W3Schools Python Tutorial](https://www.w3schools.com/python/)  
  A comprehensive beginner-friendly Python tutorial.

- [Smart Rockets](https://www.youtube.com/watch?v=Wgn_aPH3OEk&list=LL&index=5)  
  Video explaining genetic algorithms with smart rockets, by Daniel Shiffman.

- [Code Bullet](https://www.youtube.com/watch?v=BOZfhUcNiqk&list=LL&index=9)  
  Code Bullet's entertaining and educational take on building a self-learning AI using genetic algorithms.
